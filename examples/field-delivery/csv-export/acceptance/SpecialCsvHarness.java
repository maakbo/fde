import java.lang.reflect.Constructor;
import java.lang.reflect.Method;
import java.time.LocalDate;
import java.util.List;

/** Emits formatter bytes for the predeclared synthetic D-P08 fixture. */
public final class SpecialCsvHarness {
    private SpecialCsvHarness() {}

    public static void main(String[] args) throws Exception {
        String id = "和文,\"引用\",末尾\r\n次行";
        Class<?> orderClass = Class.forName("OrderSearchService$Order");
        Constructor<?> constructor = null;
        for (Constructor<?> candidate : orderClass.getDeclaredConstructors()) {
            Class<?>[] types = candidate.getParameterTypes();
            if (types.length == 3 && types[0] == String.class
                    && types[1] == LocalDate.class && types[2].isEnum()) {
                constructor = candidate;
                break;
            }
        }
        if (constructor == null) {
            throw new IllegalStateException("Order(String, LocalDate, Status) seam unavailable");
        }
        constructor.setAccessible(true);
        Object status = null;
        for (Object value : constructor.getParameterTypes()[2].getEnumConstants()) {
            if (((Enum<?>) value).name().equals("NEW")) {
                status = value;
                break;
            }
        }
        if (status == null) {
            throw new IllegalStateException("NEW status unavailable");
        }
        Object order = constructor.newInstance(id, LocalDate.of(2026, 10, 5), status);
        Class<?> formatter = Class.forName("OrderCsv");
        Method format = formatter.getDeclaredMethod("format", List.class);
        format.setAccessible(true);
        byte[] bytes = (byte[]) format.invoke(null, List.of(order));
        System.out.write(bytes);
        System.out.flush();
    }
}
