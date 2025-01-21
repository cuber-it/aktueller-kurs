# Clean Code Beispiele (Teil 3)

## 6. Validation & Error Handling

### ❌ DON'T
```java
@RestController
class UserController {
    @PostMapping("/users")
    public ResponseEntity<String> createUser(@RequestBody Map<String, String> data) {
        // Inline Validierung
        if (data.get("email") == null || !data.get("email").contains("@")) {
            return ResponseEntity.badRequest().body("Invalid email");
        }
        
        if (data.get("password") == null || data.get("password").length() < 8) {
            return ResponseEntity.badRequest().body("Password too short");
        }
        
        try {
            User user = new User(data.get("email"), data.get("password"));
            userRepository.save(user);
            return ResponseEntity.ok("User created");
        } catch (Exception e) {
            return ResponseEntity.status(500).body("Error: " + e.getMessage());
        }
    }
}
```

### ✅ DO
```java
@Validated
@RestController
@RequestMapping("/api/v1/users")
class UserController {
    private final UserService userService;
    
    @PostMapping
    public ResponseEntity<UserResponse> createUser(
            @Valid @RequestBody UserCreationRequest request) {
        return ResponseEntity
            .status(HttpStatus.CREATED)
            .body(userService.createUser(request));
    }
}

record UserCreationRequest(
    @NotBlank(message = "Email is required")
    @Email(message = "Invalid email format")
    String email,

    @NotBlank(message = "Password is required")
    @ValidPassword
    String password,

    @NotBlank(message = "Name is required")
    @Size(min = 2, max = 100, message = "Name must be between 2 and 100 characters")
    String name
) {}

@ControllerAdvice
class GlobalExceptionHandler extends ResponseEntityExceptionHandler {
    
    @ExceptionHandler(ConstraintViolationException.class)
    public ResponseEntity<ErrorResponse> handleValidationErrors(
            ConstraintViolationException ex) {
        List<String> errors = ex.getConstraintViolations()
            .stream()
            .map(violation -> String.format("%s: %s",
                violation.getPropertyPath(),
                violation.getMessage()))
            .toList();
            
        return ResponseEntity
            .badRequest()
            .body(new ErrorResponse(
                "VALIDATION_ERROR",
                "Validation failed",
                errors
            ));
    }
    
    @ExceptionHandler(BusinessException.class)
    public ResponseEntity<ErrorResponse> handleBusinessException(
            BusinessException ex) {
        return ResponseEntity
            .status(ex.getStatus())
            .body(new ErrorResponse(
                ex.getCode(),
                ex.getMessage()
            ));
    }
}

// Custom Validator
@Constraint(validatedBy = PasswordValidator.class)
@Target({ElementType.FIELD})
@Retention(RetentionPolicy.RUNTIME)
@interface ValidPassword {
    String message() default "Invalid password";
    Class<?>[] groups() default {};
    Class<? extends Payload>[] payload() default {};
}

class PasswordValidator implements ConstraintValidator<ValidPassword, String> {
    private static final Pattern PASSWORD_PATTERN = 
        Pattern.compile("^(?=.*[A-Za-z])(?=.*\\d)[A-Za-z\\d]{8,}$");
    
    @Override
    public boolean isValid(String password, ConstraintValidatorContext context) {
        if (password == null) {
            return false;
        }
        return PASSWORD_PATTERN.matcher(password).matches();
    }
}

// Domain Validation
@Value
class Email {
    String value;
    
    public Email(String value) {
        if (!isValid(value)) {
            throw new InvalidEmailException(value);
        }
        this.value = value;
    }
    
    private boolean isValid(String email) {
        return email != null &&
               email.contains("@") &&
               email.length() >= 5 &&
               email.length() <= 255;
    }
}
```

## 7. Security & Authorization

### ❌ DON'T
```java
@Service
class UserService {
    public void deleteUser(String userId, String currentUser) {
        // Inline Security Checks
        if (!currentUser.equals("admin")) {
            throw new RuntimeException("Not authorized");
        }
        
        if (userRepository.findById(userId).getRole().equals("ADMIN")) {
            throw new RuntimeException("Cannot delete admin");
        }
        
        userRepository.deleteById(userId);
    }
}
```

### ✅ DO
```java
@Service
class UserService {
    private final AuthorizationService authService;
    
    @PreAuthorize("hasRole('ADMIN')")
    @Transactional
    public void deleteUser(@NonNull UserId userId) {
        User user = userRepository.findById(userId)
            .orElseThrow(() -> new UserNotFoundException(userId));
            
        authService.validateUserDeletion(user);
        
        userRepository.deleteById(userId);
        eventPublisher.publishEvent(new UserDeleted(userId));
    }
}

@Service
class AuthorizationService {
    private final SecurityContext securityContext;
    
    public void validateUserDeletion(User targetUser) {
        User currentUser = getCurrentUser();
        
        if (targetUser.hasRole(Role.ADMIN) && 
            !currentUser.hasRole(Role.SUPER_ADMIN)) {
            throw new NotAuthorizedException(
                "Only super admins can delete admin users"
            );
        }
        
        if (targetUser.getId().equals(currentUser.getId())) {
            throw new NotAuthorizedException(
                "Users cannot delete themselves"
            );
        }
    }
    
    private User getCurrentUser() {
        return securityContext.getCurrentUser()
            .orElseThrow(() -> new NotAuthenticatedException());
    }
}

@Configuration
@EnableWebSecurity
class SecurityConfig {
    @Bean
    public SecurityFilterChain filterChain(HttpSecurity http) {
        return http
            .authorizeHttpRequests(auth -> auth
                .requestMatchers("/api/v1/public/**").permitAll()
                .requestMatchers("/api/v1/admin/**").hasRole("ADMIN")
                .anyRequest().authenticated()
            )
            .csrf(csrf -> csrf.disable())
            .sessionManagement(session -> session
                .sessionCreationPolicy(SessionCreationPolicy.STATELESS)
            )
            .oauth2ResourceServer(oauth2 -> oauth2
                .jwt(jwt -> jwt
                    .jwtAuthenticationConverter(jwtAuthConverter())
                )
            )
            .build();
    }
    
    @Bean
    public JwtAuthenticationConverter jwtAuthConverter() {
        JwtGrantedAuthoritiesConverter authoritiesConverter = 
            new JwtGrantedAuthoritiesConverter();
        authoritiesConverter.setAuthoritiesClaimName("roles");
        authoritiesConverter.setAuthorityPrefix("ROLE_");
        
        JwtAuthenticationConverter converter = new JwtAuthenticationConverter();
        converter.setJwtGrantedAuthoritiesConverter(authoritiesConverter);
        return converter;
    }
}
```

## 8. Transaktionsmanagement & Consistency

### ❌ DON'T
```java
@Service
class OrderService {
    public void processOrder(Order order) {
        // Manuelle Transaktionshandhabung
        Connection conn = dataSource.getConnection();
        try {
            conn.setAutoCommit(false);
            
            orderDao.save(order);
            inventoryDao.updateStock(order.getItems());
            paymentDao.process(order.getPayment());
            
            conn.commit();
        } catch (Exception e) {
            conn.rollback();
            throw new RuntimeException("Order processing failed", e);
        } finally {
            conn.close();
        }
    }
}
```

### ✅ DO
```java
@Service
class OrderService {
    private final OrderRepository orderRepository;
    private final InventoryService inventoryService;
    private final PaymentService paymentService;
    
    @Transactional
    public Order processOrder(ProcessOrderCommand command) {
        // Validierung
        Order order = orderRepository.findById(command.orderId())
            .orElseThrow(() -> new OrderNotFoundException(command.orderId()));
            
        // Geschäftsregeln prüfen
        order.validate();
        
        // Bestand prüfen und reservieren
        inventoryService.reserveItems(order.getItems());
        
        try {
            // Zahlung verarbeiten
            PaymentResult paymentResult = paymentService.process(
                order.getPayment()
            );
            
            if (paymentResult.isSuccessful()) {
                order.markAsPaid(paymentResult.getTransactionId());
                return orderRepository.save(order);
            } else {
                throw new PaymentFailedException(
                    paymentResult.getErrorMessage()
                );
            }
        } catch (Exception e) {
            // Bei Fehler Bestand wieder freigeben
            inventoryService.releaseItems(order.getItems());
            throw e;
        }
    }
}

@Service
class InventoryService {
    private final InventoryRepository repository;
    private final LockManager lockManager;
    
    @Transactional(propagation = Propagation.REQUIRED)
    public void reserveItems(List<OrderItem> items) {
        items.forEach(item -> {
            Lock lock = lockManager.acquireLock(item.getProductId());
            try {
                InventoryItem inventory = repository
                    .findByProductId(item.getProductId())
                    .orElseThrow(() -> new ProductNotFoundException(
                        item.getProductId()
                    ));
                    
                inventory.reserve(item.getQuantity());
                repository.save(inventory);
            } finally {
                lockManager.releaseLock(lock);
            }
        });
    }
}

@Component
class LockManager {
    private final RedisTemplate<String, String> redisTemplate;
    
    public Lock acquireLock(ProductId productId) {
        String lockKey = "lock:product:" + productId.getValue();
        boolean acquired = redisTemplate.opsForValue()
            .setIfAbsent(lockKey, "locked", Duration.ofSeconds(10));
            
        if (!acquired) {
            throw new ConcurrentModificationException(
                "Could not acquire lock for product " + productId
            );
        }
        
        return new Lock(lockKey);
    }
    
    public void releaseLock(Lock lock) {
        redisTemplate.delete(lock.getKey());
    }
}
```

[Fortsetzung folgt...]

Soll ich mit weiteren spezifischen Beispielen fortfahren, z.B. für Logging, Monitoring oder Testing?