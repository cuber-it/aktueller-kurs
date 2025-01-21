# Übung: Funktionen reinigen

## Ausgangscode
```java
public class ReportGenerator {
    private Database db;
    private Logger logger;
    
    public void generateAndSendReport(String reportType, String format, 
                                    String recipient, boolean includeGraphics,
                                    boolean sendEmail, String ccRecipient,
                                    boolean urgent, String subject) {
        try {
            // Get data
            List<Map<String, Object>> data = db.query("SELECT * FROM sales");
            
            // Process data
            double total = 0;
            List<Map<String, Object>> processedData = new ArrayList<>();
            for(Map<String, Object> row : data) {
                if(reportType.equals("DAILY")) {
                    if(isToday(row.get("date"))) {
                        processRow(row, processedData, total);
                    }
                } else if(reportType.equals("WEEKLY")) {
                    if(isThisWeek(row.get("date"))) {
                        processRow(row, processedData, total);
                    }
                } else if(reportType.equals("MONTHLY")) {
                    if(isThisMonth(row.get("date"))) {
                        processRow(row, processedData, total);
                    }
                }
            }
            
            // Generate report
            String report = "";
            if(format.equals("PDF")) {
                report = generatePDFReport(processedData, includeGraphics);
            } else if(format.equals("HTML")) {
                report = generateHTMLReport(processedData, includeGraphics);
            } else if(format.equals("CSV")) {
                report = generateCSVReport(processedData);
            }
            
            // Send report
            if(sendEmail) {
                EmailService emailService = new EmailService();
                if(urgent) {
                    subject = "URGENT: " + subject;
                }
                emailService.sendEmail(recipient, ccRecipient, subject, report);
            }
            
            logger.log("Report generated and sent successfully");
        } catch(Exception e) {
            logger.error("Error generating report: " + e.getMessage());
            throw e;
        }
    }
    
    private void processRow(Map<String, Object> row, 
                          List<Map<String, Object>> processedData,
                          double total) {
        // Complex processing logic here
    }
    
    // Weitere Hilfsmethoden...
}
```

## Aufgaben

### 1. Analyse (15 Minuten)
- Identifizieren Sie Verstöße gegen Clean Code Prinzipien
- Markieren Sie zu lange Methoden
- Finden Sie versteckte Abhängigkeiten

### 2. Refactoring (45 Minuten)
1. Extrahieren Sie Methoden
2. Erstellen Sie Value Objects
3. Implementieren Sie Strategy Pattern für Report-Typen
4. Verwenden Sie Builder Pattern für Report-Konfiguration

### 3. Implementierung (45 Minuten)
Beispiel für eine verbesserte Struktur:

```java
public class ReportGenerator {
    private final ReportDataProvider dataProvider;
    private final ReportFormatter formatter;
    private final ReportSender sender;
    
    public Report generateReport(ReportConfiguration config) {
        ReportData data = dataProvider.getData(config.getTimeFrame());
        Report report = formatter.format(data, config.getFormatting());
        
        if (config.shouldSend()) {
            sender.send(report, config.getDeliveryOptions());
        }
        
        return report;
    }
}

public class ReportConfiguration {
    private final TimeFrame timeFrame;
    private final FormattingOptions formatting;
    private final DeliveryOptions delivery;
    
    // Builder Pattern implementieren
}
```

[Fortsetzung folgt...]

Soll ich mit der nächsten Übung fortfahren?