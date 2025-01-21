# Spezifische Clean Code Beispiele

## 1. Repository Pattern & Datenbankzugriff

### ❌ DON'T
```java
class UserManager {
    private Connection getConnection() {
        return DriverManager.getConnection("jdbc:mysql://localhost/db", "user", "pass");
    }
    
    public User findUser(String id) {
        try (Connection conn = getConnection()) {
            PreparedStatement stmt = conn.prepareStatement(
                "SELECT * FROM users WHERE id = ?"
            );
            stmt.setString(1, id);
            ResultSet rs = stmt.executeQuery();
            
            if (rs.next()) {
                User user = new User();
                user.setId(rs.getString("id"));
                user.setName(rs.getString("name"));
                user.setEmail(rs.getString("email"));
                return user;
            }
            return null;
        } catch (SQLException e) {
            System.out.println("Database error: " + e.getMessage());
            return null;
        }
    }
    
    public void saveUser(User user) {
        try (Connection conn = getConnection()) {
            PreparedStatement stmt = conn.prepareStatement(
                "INSERT INTO users (id, name, email) VALUES (?, ?, ?)"
            );
            stmt.setString(1, user.getId());
            stmt.setString(2, user.getName());
            stmt.setString(3, user.getEmail());
            stmt.executeUpdate();
        } catch (SQLException e) {
            System.out.println("Error saving user: " + e.getMessage());
        }
    }
}
```

### ✅ DO
```java
interface UserRepository {
    Optional<User> findById(UserId id);
    User save(User user);
    boolean exists(EmailAddress email);
}

@Repository
class JpaUserRepository implements UserRepository {
    private final JpaTemplate jpa;
    private final UserMapper mapper;
    
    @Inject
    JpaUserRepository(JpaTemplate jpa, UserMapper mapper) {
        this.jpa = requireNonNull(jpa);
        this.mapper = requireNonNull(mapper);
    }
    
    @Override
    public Optional<User> findById(UserId id) {
        try {
            UserEntity entity = jpa.findById(UserEntity.class, id.getValue());
            return Optional.ofNullable(entity).map(mapper::toDomain);
        } catch (PersistenceException e) {
            throw new RepositoryException("Error fetching user", e);
        }
    }
    
    @Override
    public User save(User user) {
        try {
            UserEntity entity = mapper.toEntity(user);
            UserEntity savedEntity = jpa.save(entity);
            return mapper.toDomain(savedEntity);
        } catch (PersistenceException e) {
            throw new RepositoryException("Error saving user", e);
        }
    }
    
    @Override
    public boolean exists(EmailAddress email) {
        try {
            return jpa.createQuery(
                "SELECT COUNT(u) FROM UserEntity u WHERE u.email = :email",
                Long.class
            )
            .setParameter("email", email.getValue())
            .getSingleResult() > 0;
        } catch (PersistenceException e) {
            throw new RepositoryException("Error checking user existence", e);
        }
    }
}

@Service
class UserService {
    private final UserRepository userRepository;
    private final PasswordHasher passwordHasher;
    private final UserValidator validator;
    
    public User createUser(UserCreationRequest request) {
        validator.validate(request);
        
        if (userRepository.exists(request.getEmail())) {
            throw new UserAlreadyExistsException(request.getEmail());
        }
        
        User user = new User(
            UserId.generate(),
            request.getUsername(),
            request.getEmail(),
            passwordHasher.hash(request.getPassword())
        );
        
        return userRepository.save(user);
    }
}
```

## 2. API Design & Controller Pattern

### ❌ DON'T
```java
@RestController
class UserController {
    @Autowired
    private UserRepository repo;
    
    @PostMapping("/users")
    public ResponseEntity<?> createUser(@RequestBody Map<String, Object> data) {
        try {
            // Direktes Mapping von Request-Daten
            User user = new User();
            user.setName((String) data.get("name"));
            user.setEmail((String) data.get("email"));
            
            // Direkte Validierung im Controller
            if (user.getEmail() == null || !user.getEmail().contains("@")) {
                return ResponseEntity.badRequest().body("Invalid email");
            }
            
            repo.save(user);
            return ResponseEntity.ok(user);
        } catch (Exception e) {
            return ResponseEntity.status(500).body("Error: " + e.getMessage());
        }
    }
    
    @GetMapping("/users/{id}")
    public ResponseEntity<?> getUser(@PathVariable String id) {
        User user = repo.findById(id).orElse(null);
        if (user == null) {
            return ResponseEntity.notFound().build();
        }
        return ResponseEntity.ok(user);
    }
}
```

### ✅ DO
```java
@RestController
@RequestMapping("/api/v1/users")
class UserController {
    private final UserFacade userFacade;
    private final UserDtoMapper mapper;
    
    @Inject
    UserController(UserFacade userFacade, UserDtoMapper mapper) {
        this.userFacade = requireNonNull(userFacade);
        this.mapper = requireNonNull(mapper);
    }
    
    @PostMapping
    public ResponseEntity<UserResponse> createUser(
            @Valid @RequestBody UserCreationRequest request) {
        User user = userFacade.createUser(request);
        return ResponseEntity
            .status(HttpStatus.CREATED)
            .body(mapper.toResponse(user));
    }
    
    @GetMapping("/{id}")
    public ResponseEntity<UserResponse> getUser(@PathVariable UUID id) {
        return userFacade.findUser(new UserId(id))
            .map(mapper::toResponse)
            .map(ResponseEntity::ok)
            .orElseThrow(() -> new UserNotFoundException(id));
    }
    
    @ExceptionHandler(UserNotFoundException.class)
    public ResponseEntity<ErrorResponse> handleUserNotFound(UserNotFoundException ex) {
        return ResponseEntity
            .status(HttpStatus.NOT_FOUND)
            .body(new ErrorResponse(
                "USER_NOT_FOUND",
                String.format("User with ID %s not found", ex.getUserId())
            ));
    }
    
    @ExceptionHandler(UserValidationException.class)
    public ResponseEntity<ErrorResponse> handleValidationError(
            UserValidationException ex) {
        return ResponseEntity
            .status(HttpStatus.BAD_REQUEST)
            .body(new ErrorResponse(
                "VALIDATION_ERROR",
                "Invalid user data",
                ex.getViolations()
            ));
    }
}

@Value
class UserCreationRequest {
    @NotBlank(message = "Username is required")
    @Size(min = 3, max = 50, message = "Username must be between 3 and 50 characters")
    String username;
    
    @NotBlank(message = "Email is required")
    @Email(message = "Invalid email format")
    String email;
    
    @NotBlank(message = "Password is required")
    @Pattern(
        regexp = "^(?=.*[A-Za-z])(?=.*\\d)[A-Za-z\\d]{8,}$",
        message = "Password must be at least 8 characters and contain letters and numbers"
    )
    String password;
}

@Value
class UserResponse {
    UUID id;
    String username;
    String email;
    LocalDateTime createdAt;
    UserStatus status;
}
```

[Fortsetzung folgt...]

Soll ich mit weiteren spezifischen Beispielen fortfahren, z.B. für Event Handling, Caching oder Async-Operationen?