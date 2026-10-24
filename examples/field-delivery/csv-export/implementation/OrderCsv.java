import java.nio.charset.StandardCharsets;
import java.util.List;

/** Pure CSV formatting for an already searched, ordered list of orders. */
public final class OrderCsv {
    private OrderCsv() {}

    public static byte[] format(List<OrderSearchService.Order> orders) {
        StringBuilder csv = new StringBuilder("受注ID,受注日,状況\r\n");
        for (OrderSearchService.Order order : orders) {
            csv.append(cell(order.id())).append(',')
                    .append(cell(order.date().toString())).append(',')
                    .append(cell(order.status().name())).append("\r\n");
        }
        byte[] content = csv.toString().getBytes(StandardCharsets.UTF_8);
        byte[] output = new byte[content.length + 3];
        output[0] = (byte) 0xef;
        output[1] = (byte) 0xbb;
        output[2] = (byte) 0xbf;
        System.arraycopy(content, 0, output, 3, content.length);
        return output;
    }

    private static String cell(String value) {
        if (value.indexOf(',') < 0 && value.indexOf('"') < 0
                && value.indexOf('\r') < 0 && value.indexOf('\n') < 0) {
            return value;
        }
        return '"' + value.replace("\"", "\"\"") + '"';
    }
}
