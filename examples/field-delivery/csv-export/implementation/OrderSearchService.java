import java.time.LocalDate;
import java.time.format.DateTimeParseException;
import java.util.ArrayList;
import java.util.Comparator;
import java.util.List;
import java.util.Objects;

/** Read-only, in-memory search. Pass another order list to test different cases. */
public final class OrderSearchService {
    public enum Status { NEW, SHIPPED, CANCELLED }

    public static final class Order {
        private final String id;
        private final LocalDate date;
        private final Status status;

        public Order(String id, LocalDate date, Status status) {
            if (id == null || id.isBlank() || date == null || status == null) {
                throw new IllegalArgumentException("Order id, date and status are required");
            }
            this.id = id;
            this.date = date;
            this.status = status;
        }

        public String id() { return id; }
        public LocalDate date() { return date; }
        public Status status() { return status; }

        @Override
        public boolean equals(Object other) {
            if (this == other) return true;
            if (!(other instanceof Order order)) return false;
            return id.equals(order.id) && date.equals(order.date) && status == order.status;
        }

        @Override
        public int hashCode() {
            return Objects.hash(id, date, status);
        }
    }

    private static final Comparator<Order> DISPLAY_ORDER =
            Comparator.comparing(Order::date).reversed().thenComparing(Order::id);
    private final List<Order> orders;

    public OrderSearchService(List<Order> orders) {
        this.orders = List.copyOf(Objects.requireNonNull(orders, "orders"));
    }

    /** Blank or null filters mean unspecified. Invalid filters throw IllegalArgumentException. */
    public List<Order> search(String statusText, String fromText, String toText) {
        Status status = parseStatus(statusText);
        LocalDate from = parseDate(fromText, "from");
        LocalDate to = parseDate(toText, "to");
        if (from != null && to != null && from.isAfter(to)) {
            throw new IllegalArgumentException("開始日は終了日以前にしてください");
        }
        List<Order> matches = new ArrayList<>();
        for (Order order : orders) {
            if ((status == null || order.status() == status)
                    && (from == null || !order.date().isBefore(from))
                    && (to == null || !order.date().isAfter(to))) {
                matches.add(order);
            }
        }
        matches.sort(DISPLAY_ORDER);
        return List.copyOf(matches);
    }

    public List<Order> sourceSnapshot() {
        return orders;
    }

    private static Status parseStatus(String value) {
        if (value == null || value.isEmpty()) return null;
        try {
            return Status.valueOf(value);
        } catch (IllegalArgumentException ex) {
            throw new IllegalArgumentException("未定義の状況です: " + value);
        }
    }

    private static LocalDate parseDate(String value, String label) {
        if (value == null || value.isEmpty()) return null;
        if (!value.matches("[0-9]{4}-[0-9]{2}-[0-9]{2}")) {
            throw new IllegalArgumentException(label + " はYYYY-MM-DDで指定してください");
        }
        try {
            return LocalDate.parse(value);
        } catch (DateTimeParseException ex) {
            throw new IllegalArgumentException(label + " は実在する日付で指定してください");
        }
    }

    public static OrderSearchService sample() {
        return new OrderSearchService(List.of(
                new Order("O-101", LocalDate.of(2026, 10, 1), Status.NEW),
                new Order("O-102", LocalDate.of(2026, 10, 2), Status.SHIPPED),
                new Order("O-103", LocalDate.of(2026, 10, 3), Status.NEW),
                new Order("O-104", LocalDate.of(2026, 10, 3), Status.CANCELLED),
                new Order("O-105", LocalDate.of(2026, 10, 4), Status.NEW)));
    }
}
