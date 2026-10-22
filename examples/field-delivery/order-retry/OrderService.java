import java.util.HashMap;
import java.util.Map;
import java.util.Objects;

/**
 * A minimal, in-memory order intake service for one local Java process.
 * No customer records, secrets, database, HTTP endpoint, or external service are used.
 */
public final class OrderService {
    private final Map<RequestIdentity, SavedOrder> orders = new HashMap<>();
    private long nextOrderNumber = 1;

    /**
     * Registers one order or returns the first order for an identical retry.
     * Synchronization covers the lookup and creation together so local threads cannot
     * both create an order for the same customer ID and request key.
     */
    public synchronized Result submit(
            String customerId, String requestKey, String item, int quantity) {
        if (isMissing(customerId) || isMissing(requestKey) || isMissing(item)
                || quantity <= 0) {
            return new Result(400, null);
        }

        RequestIdentity identity = new RequestIdentity(customerId, requestKey);
        SavedOrder first = orders.get(identity);
        if (first != null) {
            if (first.item.equals(item) && first.quantity == quantity) {
                return new Result(200, first.orderId);
            }
            // The first accepted content owns this identity; a conflict never changes it.
            return new Result(409, null);
        }

        String orderId = "ORD-" + nextOrderNumber++;
        orders.put(identity, new SavedOrder(orderId, item, quantity));
        return new Result(201, orderId);
    }

    private static boolean isMissing(String value) {
        // Whitespace normalization is deliberately unspecified by the requirements.
        return value == null || value.isEmpty();
    }

    public static final class Result {
        private final int statusCode;
        private final String orderId;

        private Result(int statusCode, String orderId) {
            this.statusCode = statusCode;
            this.orderId = orderId;
        }

        public int getStatusCode() {
            return statusCode;
        }

        public String getOrderId() {
            return orderId;
        }
    }

    private static final class RequestIdentity {
        private final String customerId;
        private final String requestKey;

        private RequestIdentity(String customerId, String requestKey) {
            this.customerId = customerId;
            this.requestKey = requestKey;
        }

        @Override
        public boolean equals(Object other) {
            if (this == other) {
                return true;
            }
            if (!(other instanceof RequestIdentity)) {
                return false;
            }
            RequestIdentity that = (RequestIdentity) other;
            return customerId.equals(that.customerId) && requestKey.equals(that.requestKey);
        }

        @Override
        public int hashCode() {
            return Objects.hash(customerId, requestKey);
        }
    }

    private static final class SavedOrder {
        private final String orderId;
        private final String item;
        private final int quantity;

        private SavedOrder(String orderId, String item, int quantity) {
            this.orderId = orderId;
            this.item = item;
            this.quantity = quantity;
        }
    }
}
