import java.util.ArrayList;
import java.util.List;
import java.util.concurrent.*;

/** Independent acceptance cases derived from the agreed conditions, not service internals. */
public final class AcceptanceTest {
    private static void check(boolean value, String reason) {
        if (!value) throw new AssertionError(reason);
    }
    public static void main(String[] args) throws Exception {
        OrderService service = new OrderService();
        OrderService.Result first = service.submit("C-A", "K-1", "P-1", 2);
        check(first.getStatusCode() == 201, "first creation");
        check(service.submit("C-A", "K-1", "P-1", 2).getOrderId().equals(first.getOrderId()), "retry identity");
        check(service.submit("C-A", "K-1", "P-2", 2).getStatusCode() == 409, "changed item");
        check(service.submit("C-A", "K-1", "P-1", 3).getStatusCode() == 409, "changed quantity");
        check(service.submit("C-A", "K-1", "P-1", 2).getStatusCode() == 200, "conflict preserves first");
        check(!service.submit("C-B", "K-1", "P-1", 2).getOrderId().equals(first.getOrderId()), "customer isolation");
        check(!service.submit("C-A", "K-2", "P-1", 2).getOrderId().equals(first.getOrderId()), "new request");
        System.out.println("PASS acceptance identity, conflict, isolation (7 assertions)");

        String[][] invalid = {{null,"K","P"},{"","K","P"},{"C",null,"P"},{"C","","P"},{"C","K",null},{"C","K",""}};
        for (String[] fields : invalid) check(service.submit(fields[0],fields[1],fields[2],1).getStatusCode()==400,"invalid identifier");
        check(service.submit("C","bad","P",0).getStatusCode()==400,"zero");
        check(service.submit("C","bad","P",-1).getStatusCode()==400,"negative");
        check(service.submit("C","bad","P",1).getStatusCode()==201,"invalid request must not reserve key");
        System.out.println("PASS acceptance rejected input leaves key usable (9 assertions)");

        ExecutorService pool = Executors.newFixedThreadPool(12);
        try {
            OrderService concurrent = new OrderService();
            List<Callable<OrderService.Result>> work = new ArrayList<>();
            for(int i=0;i<120;i++) work.add(() -> concurrent.submit("parallel","once","P",1));
            int creations=0; String id=null;
            for(Future<OrderService.Result> f:pool.invokeAll(work)) {
                OrderService.Result result=f.get();
                if(result.getStatusCode()==201) creations++;
                else check(result.getStatusCode()==200,"retry code");
                if(id==null) id=result.getOrderId();
                check(id.equals(result.getOrderId()),"parallel identity");
            }
            check(creations==1,"one creation across 120 calls");
            System.out.println("PASS acceptance 120 concurrent calls, one creation");
        } finally { pool.shutdownNow(); }

        // Deliberately different caller behavior, not a defect seeded into the service.
        OrderService faultyCaller = new OrderService();
        String before = faultyCaller.submit("C", "attempt-1", "P", 1).getOrderId();
        String after = faultyCaller.submit("C", "attempt-2", "P", 1).getOrderId();
        check(!before.equals(after),"different request keys produce two orders");
        System.out.println("REPRODUCED caller failure: fresh key on retry creates two orders");
        OrderService correctedCaller = new OrderService();
        String retainedKey = "user-action-1";
        String original = correctedCaller.submit("C",retainedKey,"P",1).getOrderId();
        check(correctedCaller.submit("C",retainedKey,"P",1).getOrderId().equals(original),"reuse caller key");
        System.out.println("PASS caller retest: retain key for one user action, same order");

        OrderService replacement = new OrderService();
        check(replacement.submit("C",retainedKey,"P",1).getStatusCode()==201,"memory does not survive restart");
        System.out.println("OBSERVED limitation: new service instance accepts same request as new");
        System.out.println("PASS all independent acceptance groups; production readiness NOT established");
    }
}
