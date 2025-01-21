# Clean Code Beispiele (Finale Beispiele)

## 14. Batch-Verarbeitung & Daten-Export

### ❌ DON'T
```java
@Service
class ReportService {
    public void generateReport() {
        List<Order> orders = orderRepository.findAll();
        FileWriter writer = new FileWriter("report.csv");
        
        // Alles in einem Rutsch verarbeiten
        for (Order order : orders) {
            writer.write(order.getId() + "," + order.getTotal() + "\n");
        }
        writer.close();
    }
}
```

### ✅ DO
```java
@Service
@Slf4j
class ReportingService {
    private final OrderRepository orderRepository;
    private final FileStorageService fileStorage;
    private final MetricsService metricsService;

    @Async
    public CompletableFuture<ReportResult> generateReport(ReportRequest request) {
        var reportId = ReportId.generate();
        log.info("Starting report generation, reportId={}", reportId);
        
        return StreamSupport
            .stream(createOrderStreamIterator(request), false)
            .collect(BatchCollector.toBatches(1000))
            .map(this::processOrderBatch)
            .collect(new ReportCollector(reportId))
            .thenApply(this::storeReport)
            .whenComplete(this::recordMetrics);
    }
    
    private Iterator<Order> createOrderStreamIterator(ReportRequest request) {
        return new Iterator<>() {
            private int page = 0;
            private boolean hasMore = true;
            private final int pageSize = 500;
            
            @Override
            public boolean hasNext() {
                return hasMore;
            }
            
            @Override
            public List<Order> next() {
                var pageable = PageRequest.of(page++, pageSize);
                var result = orderRepository
                    .findByDateRange(
                        request.getStartDate(), 
                        request.getEndDate(), 
                        pageable
                    );
                    
                hasMore = result.hasNext();
                return result.getContent();
            }
        };
    }
    
    private Stream<ReportLine> processOrderBatch(List<Order> batch) {
        return batch.stream()
            .map(this::createReportLine)
            .filter(Objects::nonNull);
    }
    
    private ReportLine createReportLine(Order order) {
        return ReportLine.builder()
            .orderId(order.getId())
            .orderDate(order.getCreatedAt())
            .customerName(order.getCustomer().getName())
            .total(order.getTotal())
            .status(order.getStatus())
            .build();
    }
}

@Component
class BatchCollector {
    public static <T> Collector<T, List<List<T>>, Stream<List<T>>> toBatches(
            int batchSize) {
        return Collector.of(
            ArrayList::new,
            (batches, item) -> {
                if (batches.isEmpty() || 
                    batches.get(batches.size() - 1).size() >= batchSize) {
                    batches.add(new ArrayList<>());
                }
                batches.get(batches.size() - 1).add(item);
            },
            (left, right) -> {
                left.addAll(right);
                return left;
            },
            Collections::unmodifiableList,
            Collector.Characteristics.UNORDERED
        );
    }
}

class ReportCollector {
    private final ReportId reportId;
    private final CSVPrinter csvPrinter;
    
    public ReportCollector(ReportId reportId) {
        this.reportId = reportId;
        this.csvPrinter = createCsvPrinter();
    }
    
    public CompletableFuture<ReportFile> collect(Stream<ReportLine> lines) {
        return CompletableFuture.supplyAsync(() -> {
            lines.forEach(this::writeLine);
            return createReportFile();
        });
    }
    
    private void writeLine(ReportLine line) {
        try {
            csvPrinter.printRecord(
                line.getOrderId(),
                line.getOrderDate(),
                line.getCustomerName(),
                line.getTotal(),
                line.getStatus()
            );
        } catch (IOException e) {
            throw new ReportGenerationException(
                "Failed to write report line", e
            );
        }
    }
}

@Configuration
class BatchConfig {
    @Bean
    public TaskExecutor reportingTaskExecutor() {
        ThreadPoolTaskExecutor executor = new ThreadPoolTaskExecutor();
        executor.setCorePoolSize(2);
        executor.setMaxPoolSize(4);
        executor.setQueueCapacity(50);
        executor.setThreadNamePrefix("report-");
        executor.setRejectedExecutionHandler(
            new CallerRunsPolicy()
        );
        return executor;
    }
    
    @Bean
    public Clock clock() {
        return Clock.systemUTC();
    }
}

// Verwendung des Services
@RestController
@RequestMapping("/api/v1/reports")
class ReportController {
    private final ReportingService reportingService;
    
    @PostMapping
    public ResponseEntity<ReportResponse> requestReport(
            @Valid @RequestBody ReportRequest request) {
        CompletableFuture<ReportResult> future = 
            reportingService.generateReport(request);
            
        return ResponseEntity.accepted()
            .body(new ReportResponse(
                ReportStatus.PROCESSING,
                "/api/v1/reports/" + future.get().getReportId()
            ));
    }
    
    @GetMapping("/{reportId}")
    public ResponseEntity<ReportResult> getReport(@PathVariable UUID reportId) {
        return reportingService
            .getReport(new ReportId(reportId))
            .map(ResponseEntity::ok)
            .orElse(ResponseEntity.notFound().build());
    }
}
```

Damit haben wir einen umfassenden Überblick über Clean Code Praktiken in verschiedenen Szenarien gegeben, von grundlegenden Prinzipien bis hin zu fortgeschrittenen Implementierungen. Die Beispiele zeigen:

1. Klare Strukturierung
2. Separation of Concerns
3. Fehlerbehandlung
4. Performance-Optimierung
5. Testbarkeit
6. Wartbarkeit
7. Skalierbarkeit

Die Beispiele können als Referenz für ähnliche Implementierungen dienen und zeigen Best Practices für verschiedene Anwendungsfälle.

Gibt es noch spezifische Aspekte, die Sie besonders interessieren?