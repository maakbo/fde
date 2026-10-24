import com.sun.net.httpserver.HttpServer;
import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;
import java.time.LocalDate;
import java.util.List;

public final class OrderSearchTest {
    private static int checks;

    private static void equal(Object expected, Object actual, String label) {
        checks++;
        if (!expected.equals(actual)) throw new AssertionError(label + " expected=" + expected + " actual=" + actual);
    }

    private static void invalid(Runnable operation, String label) {
        checks++;
        try {
            operation.run();
            throw new AssertionError(label + " should reject input");
        } catch (IllegalArgumentException expected) {
            // Rejected without changing source data.
        }
    }

    private static String ids(List<OrderSearchService.Order> orders) {
        return orders.stream().map(OrderSearchService.Order::id).toList().toString();
    }

    private static HttpResponse<String> request(HttpClient client, int port, String path, String method) throws Exception {
        HttpRequest request = HttpRequest.newBuilder(URI.create("http://127.0.0.1:" + port + path))
                .method(method, HttpRequest.BodyPublishers.noBody()).build();
        return client.send(request, HttpResponse.BodyHandlers.ofString());
    }

    public static void main(String[] args) throws Exception {
        OrderSearchService service = OrderSearchService.sample();
        List<OrderSearchService.Order> before = List.of(
                new OrderSearchService.Order("O-101", LocalDate.of(2026, 10, 1), OrderSearchService.Status.NEW),
                new OrderSearchService.Order("O-102", LocalDate.of(2026, 10, 2), OrderSearchService.Status.SHIPPED),
                new OrderSearchService.Order("O-103", LocalDate.of(2026, 10, 3), OrderSearchService.Status.NEW),
                new OrderSearchService.Order("O-104", LocalDate.of(2026, 10, 3), OrderSearchService.Status.CANCELLED),
                new OrderSearchService.Order("O-105", LocalDate.of(2026, 10, 4), OrderSearchService.Status.NEW));
        equal("[O-105, O-103, O-104, O-102, O-101]", ids(service.search("", "", "")), "all and sort");
        equal("[O-105, O-103]", ids(service.search("NEW", "2026-10-02", "2026-10-04")), "AND and inclusive dates");
        equal("[O-103, O-104]", ids(service.search(null, "2026-10-03", "2026-10-03")), "same day and id sort");
        equal("[O-105, O-103, O-101]", ids(service.search("NEW", null, null)), "status only");
        equal("[O-101]", ids(service.search(null, null, "2026-10-01")), "to only");
        equal("[O-105]", ids(service.search(null, "2026-10-04", null)), "from only");
        equal("[]", ids(service.search("CANCELLED", "2026-10-04", null)), "zero is normal");
        invalid(() -> service.search("UNKNOWN", null, null), "unknown status");
        invalid(() -> service.search("new", null, null), "case mismatch");
        invalid(() -> service.search(null, "2026-02-30", null), "invalid calendar date");
        invalid(() -> service.search(null, "2026-1-01", null), "invalid format");
        invalid(() -> service.search(null, "2026-10-04", "2026-10-03"), "reversed interval");
        equal(before, service.sourceSnapshot(), "source is unchanged");

        OrderSearchService custom = new OrderSearchService(List.of(
                new OrderSearchService.Order("B", LocalDate.of(2026, 10, 3), OrderSearchService.Status.NEW),
                new OrderSearchService.Order("A", LocalDate.of(2026, 10, 3), OrderSearchService.Status.NEW),
                new OrderSearchService.Order("Z", LocalDate.of(2026, 10, 4), OrderSearchService.Status.SHIPPED)));
        equal("[A, B]", ids(custom.search("NEW", null, null)), "custom dataset / tie-break");
        checks++;
        try {
            custom.sourceSnapshot().clear();
            throw new AssertionError("source snapshot should be unmodifiable");
        } catch (UnsupportedOperationException expected) {
            // The search service does not expose a mutable source list.
        }

        HttpServer server = new OrderSearchServer(service).start(0);
        try {
            int port = server.getAddress().getPort();
            HttpClient client = HttpClient.newHttpClient();
            HttpResponse<String> page = request(client, port, "/", "GET");
            equal(200, page.statusCode(), "page status");
            checks++;
            if (!page.body().contains("受注検索") || !page.body().contains("fetch('/orders?'")
                    || !page.body().contains("該当する受注はありません")) {
                throw new AssertionError("page controls or result handling missing");
            }
            HttpResponse<String> found = request(client, port,
                    "/orders?status=NEW&from=2026-10-02&to=2026-10-04", "GET");
            equal(200, found.statusCode(), "search HTTP status");
            equal("{\"count\":2,\"orders\":[{\"id\":\"O-105\",\"date\":\"2026-10-04\",\"status\":\"NEW\"},{\"id\":\"O-103\",\"date\":\"2026-10-03\",\"status\":\"NEW\"}]}",
                    found.body(), "search JSON");
            equal("{\"count\":0,\"orders\":[]}", request(client, port,
                    "/orders?status=CANCELLED&from=2026-10-04", "GET").body(), "zero JSON");
            equal(400, request(client, port, "/orders?status=BAD", "GET").statusCode(), "invalid status HTTP");
            equal(400, request(client, port, "/orders?from=2026-10-04&to=2026-10-03", "GET").statusCode(), "interval HTTP");
            equal(400, request(client, port, "/orders?status=NEW&status=SHIPPED", "GET").statusCode(), "duplicate HTTP");
            equal(405, request(client, port, "/orders", "POST").statusCode(), "non-GET HTTP");
            equal(404, request(client, port, "/missing", "GET").statusCode(), "missing route");
            System.out.println("HTTP sample: " + found.statusCode() + " " + found.body());
        } finally {
            server.stop(0);
        }
        System.out.println("PASS " + checks + " checks");
    }
}
