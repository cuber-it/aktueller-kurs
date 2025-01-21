# Übung 3: Code Review

## Ziel
Durchführung eines strukturierten Code Reviews unter Berücksichtigung aller bisher gelernten Clean Code Prinzipien.

## Ausgangscode
```java
public class OrderSystem {
    private static OrderSystem instance;
    private ArrayList<HashMap<String, Object>> orders = new ArrayList();
    private ArrayList<HashMap<String, Object>> customers = new ArrayList();
    private boolean DEBUG = true;

    private OrderSystem() {
        // private constructor
    }

    public static OrderSystem getInstance() {
        if (instance == null) {
            instance = new OrderSystem();
        }
        return instance;
    }

    public boolean add_new_order(String customer_id, ArrayList<String> items, double total_price) {
        // validate customer
        boolean found = false;
        HashMap<String, Object> customer = null;
        for(HashMap<String, Object> c : customers) {
            if(c.get("id").equals(customer_id)) {
                found = true;
                customer = c;
                break;
            }
        }
        if(!found) return false;

        // check credit
        if((Double)customer.get("credit") < total_price) {
            if(DEBUG) System.out.println("Insufficient credit for customer " + customer_id);
            return false;
        }

        // create order
        HashMap<String, Object> order = new HashMap();
        order.put("customer", customer_id);
        order.put("items", items);
        order.put("total", total_price);
        order.put("status", "new");
        order.put("date", new Date());

        // update customer credit
        customer.put("credit", (Double)customer.get("credit") - total_price);

        // save order
        orders.add(order);
        
        return true;
    }

    public void p_orders() {
        for(HashMap<String, Object> o : orders) {
            System.out.println("Order: " + o.toString());
        }
    }
}
```

## Aufgaben

### 1. Code Smells identifizieren (20 Minuten)
- Markieren Sie alle Code Smells
- Kategorisieren Sie die gefundenen Probleme
- Priorisieren Sie die Verbesserungen

### 2. Refactoring-Plan erstellen (15 Minuten)
- Erstellen Sie einen schrittweisen Plan zur Verbesserung
- Definieren Sie die notwendigen Klassen/Interfaces
- Skizzieren Sie die neue Struktur

### 3. Implementierung (40 Minuten)
- Führen Sie das Refactoring schrittweise durch
- Schreiben Sie Tests für die neue Implementierung
- Dokumentieren Sie Ihre Entscheidungen

### 4. Peer Review (15 Minuten)
- Präsentieren Sie Ihre Lösung einem anderen Team
- Geben und empfangen Sie Feedback
- Diskutieren Sie alternative Ansätze

## Bewertungskriterien
- [ ] Singleton Pattern korrekt ersetzt
- [ ] Primitive Obsession beseitigt
- [ ] Namensgebung verbessert
- [ ] Fehlerbehandlung implementiert
- [ ] Klassen extrahiert
- [ ] Tests geschrieben

## Beispiellösung (Auszug)
```java
public class Order {
    private final Customer customer;
    private final List<OrderItem> items;
    private final Money totalPrice;
    private OrderStatus status;
    private final LocalDateTime orderDate;

    public Order(Customer customer, List<OrderItem> items, Money totalPrice) {
        this.customer = Objects.requireNonNull(customer);
        this.items = new ArrayList<>(items);
        this.totalPrice = totalPrice;
        this.status = OrderStatus.NEW;
        this.orderDate = LocalDateTime.now();
    }

    public boolean canBePlaced() {
        return customer.hasSufficientCredit(totalPrice);
    }

    public void place() {
        if (!canBePlaced()) {
            throw new InsufficientCreditException(customer, totalPrice);
        }
        customer.deductCredit(totalPrice);
        status = OrderStatus.PLACED;
    }
}
```

## Hinweise für den Trainer
- Auf häufige Anti-Patterns achten
- Verschiedene Lösungsansätze zulassen
- Diskussion über Trade-offs anregen
- Auf realistische Zeitbegrenzung achten
