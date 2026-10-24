import java.time.LocalDate;
import java.util.ArrayList;
import java.util.List;
public final class AlternateCsvHarness {
    public static void main(String[] args) throws Exception {
        List<OrderSearchService.Order> orders = new ArrayList<>();
        for (String id : List.of("comma,only", "quote\"only", "cr\ronly", "lf\nonly", "日本語のみ")) {
            orders.add(new OrderSearchService.Order(id, LocalDate.of(2026, 10, 6), OrderSearchService.Status.NEW));
        }
        System.out.write(OrderCsv.format(orders));
    }
}
