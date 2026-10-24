import com.sun.net.httpserver.HttpExchange;
import com.sun.net.httpserver.HttpServer;
import java.io.IOException;
import java.net.InetAddress;
import java.net.InetSocketAddress;
import java.net.URLDecoder;
import java.nio.charset.StandardCharsets;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/** Small localhost-only demonstration server. No authentication or persistent data. */
public final class OrderSearchServer {
    private final OrderSearchService service;

    public OrderSearchServer(OrderSearchService service) {
        this.service = service;
    }

    public HttpServer start(int port) throws IOException {
        if (port < 0 || port > 65535) throw new IllegalArgumentException("port must be 0..65535");
        HttpServer server = HttpServer.create(new InetSocketAddress(
                InetAddress.getByName("127.0.0.1"), port), 0);
        server.createContext("/", this::handle);
        server.start();
        return server;
    }

    private void handle(HttpExchange exchange) throws IOException {
        try {
            if (!"GET".equals(exchange.getRequestMethod())) {
                exchange.getResponseHeaders().set("Allow", "GET");
                send(exchange, 405, "application/json", "{\"error\":\"GETのみ利用できます\"}");
                return;
            }
            String path = exchange.getRequestURI().getPath();
            if ("/".equals(path)) {
                send(exchange, 200, "text/html", HTML);
            } else if ("/orders".equals(path) || "/orders.csv".equals(path)) {
                try {
                    Map<String, String> query = parseQuery(exchange.getRequestURI().getRawQuery());
                    List<OrderSearchService.Order> orders = service.search(
                            query.get("status"), query.get("from"), query.get("to"));
                    if ("/orders.csv".equals(path)) {
                        byte[] csv = OrderCsv.format(orders);
                        exchange.getResponseHeaders().set("Content-Type", "text/csv;charset=utf-8");
                        exchange.getResponseHeaders().set("Content-Disposition", "attachment; filename=\"orders.csv\"");
                        exchange.getResponseHeaders().set("Cache-Control", "no-store");
                        sendBytes(exchange, 200, csv);
                    } else {
                        send(exchange, 200, "application/json", ordersJson(orders));
                    }
                } catch (IllegalArgumentException ex) {
                    send(exchange, 400, "application/json", "{\"error\":" + jsonString(ex.getMessage()) + "}");
                }
            } else {
                send(exchange, 404, "application/json", "{\"error\":\"見つかりません\"}");
            }
        } finally {
            exchange.close();
        }
    }

    private static Map<String, String> parseQuery(String raw) {
        Map<String, String> result = new HashMap<>();
        if (raw == null || raw.isEmpty()) return result;
        for (String part : raw.split("&", -1)) {
            if (part.isEmpty()) throw new IllegalArgumentException("検索条件が不正です");
            String[] pair = part.split("=", 2);
            String key = decode(pair[0]);
            if (!key.equals("status") && !key.equals("from") && !key.equals("to")) {
                throw new IllegalArgumentException("未定義の検索条件です: " + key);
            }
            if (result.putIfAbsent(key, pair.length == 2 ? decode(pair[1]) : "") != null) {
                throw new IllegalArgumentException("検索条件が重複しています: " + key);
            }
        }
        return result;
    }

    private static String decode(String value) {
        try {
            return URLDecoder.decode(value, StandardCharsets.UTF_8);
        } catch (IllegalArgumentException ex) {
            throw new IllegalArgumentException("検索条件の文字コードが不正です");
        }
    }

    private static String ordersJson(List<OrderSearchService.Order> orders) {
        StringBuilder json = new StringBuilder("{\"count\":").append(orders.size()).append(",\"orders\":[");
        for (int i = 0; i < orders.size(); i++) {
            if (i > 0) json.append(',');
            OrderSearchService.Order order = orders.get(i);
            json.append("{\"id\":").append(jsonString(order.id()))
                    .append(",\"date\":").append(jsonString(order.date().toString()))
                    .append(",\"status\":").append(jsonString(order.status().name())).append('}');
        }
        return json.append("]}").toString();
    }

    private static String jsonString(String value) {
        StringBuilder json = new StringBuilder("\"");
        for (int i = 0; i < value.length(); i++) {
            char ch = value.charAt(i);
            switch (ch) {
                case '"' -> json.append("\\\"");
                case '\\' -> json.append("\\\\");
                case '\n' -> json.append("\\n");
                case '\r' -> json.append("\\r");
                case '\t' -> json.append("\\t");
                default -> {
                    if (ch < 0x20) json.append(String.format("\\u%04x", (int) ch));
                    else json.append(ch);
                }
            }
        }
        return json.append('"').toString();
    }

    private static void send(HttpExchange exchange, int status, String mime, String body) throws IOException {
        byte[] bytes = body.getBytes(StandardCharsets.UTF_8);
        exchange.getResponseHeaders().set("Content-Type", mime + "; charset=UTF-8");
        exchange.getResponseHeaders().set("Cache-Control", "no-store");
        if ("HEAD".equals(exchange.getRequestMethod())) {
            exchange.sendResponseHeaders(status, -1);
            return;
        }
        exchange.sendResponseHeaders(status, bytes.length);
        try (var out = exchange.getResponseBody()) {
            out.write(bytes);
        }
    }

    private static void sendBytes(HttpExchange exchange, int status, byte[] bytes) throws IOException {
        exchange.sendResponseHeaders(status, bytes.length);
        try (var out = exchange.getResponseBody()) {
            out.write(bytes);
        }
    }

    public static void main(String[] args) throws Exception {
        if (args.length != 1) throw new IllegalArgumentException("Usage: java OrderSearchServer <port>");
        int port = Integer.parseInt(args[0]);
        HttpServer server = new OrderSearchServer(OrderSearchService.sample()).start(port);
        System.out.println("PORT=" + server.getAddress().getPort());
        System.out.flush();
    }

    private static final String HTML = """
            <!doctype html>
            <html lang="ja">
            <head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1">
            <title>受注検索</title>
            <style>
              body{font-family:system-ui,sans-serif;max-width:680px;margin:2rem auto;padding:0 1rem;line-height:1.6}
              form{display:flex;flex-wrap:wrap;gap:1rem;align-items:end} label{display:grid;gap:.3rem}
              input,select,button{font:inherit;padding:.4rem} table{border-collapse:collapse;width:100%;margin-top:1rem}
              th,td{border-bottom:1px solid #ddd;text-align:left;padding:.5rem} #message{margin-top:1rem}
            </style></head>
            <body><h1>受注検索</h1><p>出荷状況と受注日で絞り込めます。開始日と終了日を含みます。</p>
            <form id="search-form">
              <label>状況<select name="status"><option value="">すべて</option><option value="NEW">未出荷</option><option value="SHIPPED">出荷済み</option><option value="CANCELLED">取消済み</option></select></label>
              <label>開始日<input type="date" name="from"></label>
              <label>終了日<input type="date" name="to"></label>
              <button type="submit">検索</button>
              <button type="button" id="csv-download">現在の入力条件でCSV出力</button>
            </form>
            <p id="message" role="status" aria-live="polite"></p>
            <p id="csv-message" role="status" aria-live="polite"></p>
            <table><thead><tr><th>受注ID</th><th>受注日</th><th>状況</th></tr></thead><tbody id="results"></tbody></table>
            <script>
              const form = document.querySelector('#search-form');
              const message = document.querySelector('#message');
              const results = document.querySelector('#results');
              const csvMessage = document.querySelector('#csv-message');
              const labels = {NEW:'未出荷',SHIPPED:'出荷済み',CANCELLED:'取消済み'};
              form.addEventListener('submit', async event => {
                event.preventDefault(); results.replaceChildren(); message.textContent = '検索中…';
                const query = new URLSearchParams(new FormData(form));
                try {
                  const response = await fetch('/orders?' + query.toString());
                  const data = await response.json();
                  if (!response.ok) { message.textContent = '入力エラー: ' + (data.error || '条件を確認してください'); return; }
                  message.textContent = data.count === 0 ? '0件：該当する受注はありません' : data.count + '件の受注が見つかりました';
                  for (const order of data.orders) {
                    const row = document.createElement('tr');
                    for (const value of [order.id, order.date, labels[order.status] || order.status]) {
                      const cell = document.createElement('td'); cell.textContent = value; row.append(cell);
                    }
                    results.append(row);
                  }
                } catch (_) { message.textContent = '通信エラー：検索できませんでした'; }
              });
              document.querySelector('#csv-download').addEventListener('click', async () => {
                csvMessage.textContent = 'CSVを準備中…';
                const query = new URLSearchParams(new FormData(form));
                try {
                  const response = await fetch('/orders.csv?' + query.toString());
                  if (!response.ok) {
                    const data = await response.json();
                    csvMessage.textContent = '入力エラー: ' + (data.error || '条件を確認してください');
                    return;
                  }
                  const blob = await response.blob();
                  const url = URL.createObjectURL(blob);
                  const link = document.createElement('a');
                  link.href = url; link.download = 'orders.csv';
                  document.body.append(link);
                  link.click();
                  link.remove();
                  setTimeout(() => URL.revokeObjectURL(url), 1000);
                  csvMessage.textContent = 'CSVをダウンロードしました';
                } catch (_) { csvMessage.textContent = '通信エラー：CSVを取得できませんでした'; }
              });
            </script></body></html>
            """;
}
