### 2. Tests implementieren (Fortsetzung)
```java
public interface PaymentGateway {
    PaymentResult charge(CreditCard card, Money amount);
}

public interface EmailService {
    void sendReceipt(EmailAddress to, Payment payment);
}

public class PaymentProcessor {
    private final PaymentGateway paymentGateway;
    private final PaymentRepository repository;
    private final EmailService emailService;

    public PaymentProcessor(
            PaymentGateway paymentGateway,
            PaymentRepository repository,
            EmailService emailService) {
        this.paymentGateway = paymentGateway;
        this.repository = repository;
        this.emailService = emailService;
    }

    public PaymentResult processPayment(CreditCard card, Money amount) {
        PaymentResult result = paymentGateway.charge(card, amount);
        
        if (result.isSuccessful()) {
            Payment payment = new Payment(amount, LocalDateTime.now());
            repository.save(payment);
            emailService.sendReceipt(card.getEmailAddress(), payment);
        }
        
        return result;
    }
}

class PaymentProcessorTest {
    @Test
    void successfulPaymentShouldSaveAndSendReceipt() {
        // Arrange
        PaymentGateway mockGateway = mock(PaymentGateway.class);
        PaymentRepository mockRepo = mock(PaymentRepository.class);
        EmailService mockEmail = mock(EmailService.class);
        
        when(mockGateway.charge(any(), any()))
            .thenReturn(PaymentResult.successful());
        
        PaymentProcessor processor = new PaymentProcessor(
            mockGateway, mockRepo, mockEmail);
        
        // Act
        CreditCard card = new CreditCard("4111111111111111");
        Money amount = Money.of(100, "USD");
        PaymentResult result = processor.processPayment(card, amount);
        
        // Assert
        assertTrue(result.isSuccessful());
        verify(mockRepo).save(any(Payment.class));
        verify(mockEmail).sendReceipt(any(), any());
    }
}
```

### 3. Testfälle erweitern (30 Minuten)

```java
class PaymentProcessorTest {
    private PaymentGateway mockGateway;
    private PaymentRepository mockRepo;
    private EmailService mockEmail;
    private PaymentProcessor processor;
    
    @BeforeEach
    void setUp() {
        mockGateway = mock(PaymentGateway.class);
        mockRepo = mock(PaymentRepository.class);
        mockEmail = mock(EmailService.class);
        processor = new PaymentProcessor(mockGateway, mockRepo, mockEmail);
    }
    
    @Test
    void failedPaymentShouldNotSaveOrSendReceipt() {
        when(mockGateway.charge(any(), any()))
            .thenReturn(PaymentResult.failed("Insufficient funds"));
            
        CreditCard card = new CreditCard("4111111111111111");
        Money amount = Money.of(100, "USD");
        
        PaymentResult result = processor.processPayment(card, amount);
        
        assertFalse(result.isSuccessful());
        verifyNoInteractions(mockRepo);
        verifyNoInteractions(mockEmail);
    }
    
    @Test
    void shouldHandleExceptionFromGateway() {
        when(mockGateway.charge(any(), any()))
            .thenThrow(new GatewayException("Network error"));
            
        CreditCard card = new CreditCard("4111111111111111");
        Money amount = Money.of(100, "USD");
        
        assertThrows(PaymentProcessingException.class, () -> 
            processor.processPayment(card, amount));
    }
}
```

### 4. Integration Tests (30 Minuten)

```java
@SpringBootTest
class PaymentProcessorIntegrationTest {
    @Autowired
    private PaymentProcessor processor;
    
    @Autowired
    private PaymentRepository repository;
    
    @MockBean
    private PaymentGateway gateway;
    
    @MockBean
    private EmailService emailService;
    
    @Test
    void shouldProcessPaymentEndToEnd() {
        // Test-Setup
        when(gateway.charge(any(), any()))
            .thenReturn(PaymentResult.successful());
            
        // Test durchführen
        CreditCard card = new CreditCard("4111111111111111");
        Money amount = Money.of(100, "USD");
        
        PaymentResult result = processor.processPayment(card, amount);
        
        // Verifikation
        assertTrue(result.isSuccessful());
        assertNotNull(repository.findLatestPaymentForCard(card));
        verify(emailService).sendReceipt(any(), any());
    }
}
```

## Zusatzaufgaben

### 1. Test Data Builder
```java
public class TestCreditCard {
    public static CreditCard valid() {
        return new CreditCard("4111111111111111")
            .withExpiryDate(LocalDate.now().plusYears(1))
            .withCvv("123");
    }
    
    public static CreditCard expired() {
        return new CreditCard("4111111111111111")
            .withExpiryDate(LocalDate.now().minusMonths(1))
            .withCvv("123");
    }
}
```

### 2. Property-Based Testing
```java
@Property
void allSuccessfulPaymentsShouldBeSaved(
    @ForAll @ValidCreditCard String cardNumber,
    @ForAll @Positive int amount) {
    
    CreditCard card = new CreditCard(cardNumber);
    Money payment = Money.of(amount, "USD");
    
    PaymentResult result = processor.processPayment(card, payment);
    
    if (result.isSuccessful()) {
        verify(mockRepo).save(any(Payment.class));
    }
}
```

## Bewertungskriterien
- [ ] Tests sind lesbar und wartbar
- [ ] Mocks werden sinnvoll eingesetzt
- [ ] Edge Cases sind abgedeckt
- [ ] Tests sind unabhängig voneinander
- [ ] Testdaten sind sauber verwaltet

[Neue Übung folgt...]

Soll ich mit der nächsten Übung fortfahren?