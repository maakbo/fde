import java.nio.charset.StandardCharsets;
import java.time.LocalDate;
import java.util.List;

/** Implementation self-test; independent acceptance is a separate handoff. */
public final class OrderCsvTest {
    private static int checks;

    private static void equal(String expected, String actual, String label) {
        checks++;
        if (!expected.equals(actual)) throw new AssertionError(label + " expected=" + expected + " actual=" + actual);
    }

    private static String body(byte[] bytes) {
        checks++;
        if (bytes.length < 3 || (bytes[0] & 0xff) != 0xef
                || (bytes[1] & 0xff) != 0xbb || (bytes[2] & 0xff) != 0xbf) {
            throw new AssertionError("UTF-8 BOM missing");
        }
        return new String(bytes, 3, bytes.length - 3, StandardCharsets.UTF_8);
    }

    public static void main(String[] args) {
        equal("受注ID,受注日,状況\r\n", body(OrderCsv.format(List.of())), "header only");
        List<OrderSearchService.Order> orders = List.of(
                new OrderSearchService.Order("あ,\"B\"\r\nC", LocalDate.of(2026, 10, 3), OrderSearchService.Status.NEW),
                new OrderSearchService.Order("日本語", LocalDate.of(2026, 10, 2), OrderSearchService.Status.SHIPPED));
        equal("受注ID,受注日,状況\r\n\"あ,\"\"B\"\"\r\nC\",2026-10-03,NEW\r\n日本語,2026-10-02,SHIPPED\r\n",
                body(OrderCsv.format(orders)), "quoted content and row endings");
        equal("あ,\"B\"\r\nC", orders.get(0).id(), "input unchanged");
        System.out.println("PASS CSV formatter " + checks + " checks");
    }
}
