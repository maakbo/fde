import java.util.ArrayList;
import java.util.List;
import java.util.concurrent.Callable;
import java.util.concurrent.CountDownLatch;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.Future;
import java.util.concurrent.TimeUnit;

/** Executable tests using only the Java 16 standard library. */
public final class OrderServiceTest {
    public static void main(String[] args) throws Exception {
        testFirstRetryConflict();
        testIdentityScope();
        testInvalidInputsDoNotReserveIdentity();
        testConcurrentIdenticalRetries();
        testConcurrentDifferentContent();
        System.out.println("PASS all 5 test groups");
    }

    private static void testFirstRetryConflict() {
        OrderService service = new OrderService();
        OrderService.Result first = service.submit("C1", "K1", "widget", 2);
        check(first, 201, "ORD-1", "first submission");
        check(service.submit("C1", "K1", "widget", 2), 200, "ORD-1", "retry");
        check(service.submit("C1", "K1", "widget", 3), 409, null, "quantity conflict");
        check(service.submit("C1", "K1", "other", 2), 409, null, "item conflict");
        check(service.submit("C1", "K1", "widget", 2), 200, "ORD-1", "first content retained");
        System.out.println("PASS first=201, retry=200/same ID, conflicting content=409/unchanged");
    }

    private static void testIdentityScope() {
        OrderService service = new OrderService();
        check(service.submit("C1", "K1", "widget", 1), 201, "ORD-1", "first identity");
        check(service.submit("C2", "K1", "widget", 1), 201, "ORD-2", "same key/new customer");
        check(service.submit("C1", "K2", "widget", 1), 201, "ORD-3", "same customer/new key");
        System.out.println("PASS identity scope=(customer ID, request key)");
    }

    private static void testInvalidInputsDoNotReserveIdentity() {
        OrderService service = new OrderService();
        String[][] missing = {
                {null, "K", "widget"}, {"", "K", "widget"},
                {"C", null, "widget"}, {"C", "", "widget"},
                {"C", "K", null}, {"C", "K", ""}
        };
        for (String[] input : missing) {
            check(service.submit(input[0], input[1], input[2], 1), 400, null, "missing string");
        }
        check(service.submit("C", "K", "widget", 0), 400, null, "zero quantity");
        check(service.submit("C", "K", "widget", -1), 400, null, "negative quantity");
        check(service.submit("C", "K", "widget", Integer.MAX_VALUE), 201, "ORD-1",
                "no invented upper bound");
        check(service.submit("C", "K", "widget", Integer.MAX_VALUE), 200, "ORD-1",
                "retry after invalid inputs");
        System.out.println("PASS null/empty/quantity<=0=400, no reservation or invented maximum");
    }

    private static void testConcurrentIdenticalRetries() throws Exception {
        OrderService service = new OrderService();
        int calls = 64;
        ExecutorService pool = Executors.newFixedThreadPool(16);
        CountDownLatch start = new CountDownLatch(1);
        List<Future<OrderService.Result>> futures = new ArrayList<>();
        try {
            for (int i = 0; i < calls; i++) {
                futures.add(pool.submit(() -> {
                    start.await();
                    return service.submit("C", "K", "widget", 7);
                }));
            }
            start.countDown();
            int created = 0;
            int repeated = 0;
            for (Future<OrderService.Result> future : futures) {
                OrderService.Result result = future.get(10, TimeUnit.SECONDS);
                require("ORD-1".equals(result.getOrderId()), "parallel calls returned different IDs");
                if (result.getStatusCode() == 201) {
                    created++;
                } else if (result.getStatusCode() == 200) {
                    repeated++;
                } else {
                    throw new AssertionError("unexpected parallel status " + result.getStatusCode());
                }
            }
            require(created == 1 && repeated == calls - 1, "parallel duplicate creation");
            System.out.println("PASS concurrent identical calls: 1 x 201, 63 x 200, one ID");
        } finally {
            pool.shutdownNow();
        }
    }

    private static void testConcurrentDifferentContent() throws Exception {
        OrderService service = new OrderService();
        ExecutorService pool = Executors.newFixedThreadPool(2);
        CountDownLatch start = new CountDownLatch(1);
        try {
            Callable<OrderService.Result> firstCall = () -> {
                start.await();
                return service.submit("C", "K", "widget", 1);
            };
            Callable<OrderService.Result> secondCall = () -> {
                start.await();
                return service.submit("C", "K", "widget", 2);
            };
            Future<OrderService.Result> one = pool.submit(firstCall);
            Future<OrderService.Result> two = pool.submit(secondCall);
            start.countDown();
            OrderService.Result r1 = one.get(10, TimeUnit.SECONDS);
            OrderService.Result r2 = two.get(10, TimeUnit.SECONDS);
            require((r1.getStatusCode() == 201 && r2.getStatusCode() == 409)
                    || (r1.getStatusCode() == 409 && r2.getStatusCode() == 201),
                    "parallel conflicting calls did not resolve to one create and one conflict");
            int winningQuantity = r1.getStatusCode() == 201 ? 1 : 2;
            int losingQuantity = winningQuantity == 1 ? 2 : 1;
            check(service.submit("C", "K", "widget", winningQuantity), 200, "ORD-1",
                    "winning content retained");
            check(service.submit("C", "K", "widget", losingQuantity), 409, null,
                    "losing content not saved");
            System.out.println("PASS concurrent conflicting calls: 1 x 201, 1 x 409, first content retained");
        } finally {
            pool.shutdownNow();
        }
    }

    private static void check(OrderService.Result result, int status, String id, String label) {
        require(result.getStatusCode() == status, label + ": expected status " + status
                + " but got " + result.getStatusCode());
        require(id == null ? result.getOrderId() == null : id.equals(result.getOrderId()),
                label + ": unexpected order ID " + result.getOrderId());
    }

    private static void require(boolean condition, String message) {
        if (!condition) {
            throw new AssertionError(message);
        }
    }
}
