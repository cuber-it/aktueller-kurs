# Übung: Legacy Code Refactoring

## Ausgangssituation: Inventarsystem einer Bibliothek
```java
public class Library {
    private static Library instance;
    private ArrayList<HashMap<String, Object>> books = new ArrayList<>();
    private ArrayList<HashMap<String, Object>> users = new ArrayList<>();
    private ArrayList<HashMap<String, Object>> loans = new ArrayList<>();
    
    public static Library getInstance() {
        if(instance == null) instance = new Library();
        return instance;
    }
    
    public boolean addBook(String isbn, String title, String author, int year, 
                         String publisher, int copies) {
        for(HashMap<String, Object> book : books) {
            if(book.get("isbn").equals(isbn)) {
                int curr_copies = (int)book.get("copies");
                book.put("copies", curr_copies + copies);
                System.out.println("Updated copies for book: " + title);
                return true;
            }
        }
        
        HashMap<String, Object> book = new HashMap<>();
        book.put("isbn", isbn);
        book.put("title", title);
        book.put("author", author);
        book.put("year", year);
        book.put("publisher", publisher);
        book.put("copies", copies);
        book.put("available", copies);
        books.add(book);
        System.out.println("Added new book: " + title);
        return true;
    }
    
    public boolean lendBook(String isbn, String userId) {
        HashMap<String, Object> user = null;
        for(HashMap<String, Object> u : users) {
            if(u.get("id").equals(userId)) {
                user = u;
                break;
            }
        }
        if(user == null) {
            System.out.println("User not found!");
            return false;
        }
        
        HashMap<String, Object> book = null;
        for(HashMap<String, Object> b : books) {
            if(b.get("isbn").equals(isbn)) {
                book = b;
                break;
            }
        }
        if(book == null) {
            System.out.println("Book not found!");
            return false;
        }
        
        int available = (int)book.get("available");
        if(available <= 0) {
            System.out.println("No copies available!");
            return false;
        }
        
        ArrayList<HashMap<String, Object>> userLoans = new ArrayList<>();
        for(HashMap<String, Object> loan : loans) {
            if(loan.get("userId").equals(userId) && loan.get("returned") == null) {
                userLoans.add(loan);
            }
        }
        if(userLoans.size() >= 3) {
            System.out.println("User has too many books!");
            return false;
        }
        
        HashMap<String, Object> loan = new HashMap<>();
        loan.put("isbn", isbn);
        loan.put("userId", userId);
        loan.put("loanDate", new Date());
        loan.put("dueDate", new Date(System.currentTimeMillis() + 14 * 24 * 60 * 60 * 1000));
        loans.add(loan);
        
        book.put("available", available - 1);
        System.out.println("Book lent successfully!");
        return true;
    }
    
    // ... weitere Methoden für returnBook, addUser, etc.
}
```

## Aufgaben

### 1. Analyse und Planung (30 Minuten)
- Code Smells identifizieren
- Abhängigkeiten aufzeichnen
- Refactoring-Strategie entwickeln

### 2. Domain Model erstellen (45 Minuten)
```java
public class Book {
    private final ISBN isbn;
    private final String title;
    private final Author author;
    private final Year publishYear;
    private final Publisher publisher;
    private int totalCopies;
    private int availableCopies;
    
    // Constructor, Getters, Domain Methods
}

public class Loan {
    private final Book book;
    private final User user;
    private final LocalDateTime loanDate;
    private final LocalDateTime dueDate;
    private LocalDateTime returnDate;
    
    // Constructor, Methods
}

public class User {
    private final UserId id;
    private final String name;
    private final List<Loan> activeLoans;
    
    public boolean canBorrowBooks() {
        return activeLoans.size() < 3;
    }
}
```

### 3. Services implementieren (45 Minuten)
```java
@Service
public class LibraryService {
    private final BookRepository bookRepository;
    private final UserRepository userRepository;
    private final LoanRepository loanRepository;
    
    public LoanResult lendBook(ISBN isbn, UserId userId) {
        User user = userRepository.findById(userId)
            .orElseThrow(() -> new UserNotFoundException(userId));
            
        Book book = bookRepository.findByIsbn(isbn)
            .orElseThrow(() -> new BookNotFoundException(isbn));
            
        if (!user.canBorrowBooks()) {
            return LoanResult.failure("Too many active loans");
        }
        
        if (!book.isAvailable()) {
            return LoanResult.failure("Book not available");
        }
        
        Loan loan = book.lendTo(user);
        loanRepository.save(loan);
        bookRepository.save(book);
        
        return LoanResult.success(loan);
    }
}
```

### 4. Tests schreiben (30 Minuten)
```java
class LibraryServiceTest {
    private LibraryService service;
    private BookRepository mockBookRepo;
    private UserRepository mockUserRepo;
    private LoanRepository mockLoanRepo;
    
    @BeforeEach
    void setUp() {
        mockBookRepo = mock(BookRepository.class);
        mockUserRepo = mock(UserRepository.class);
        mockLoanRepo = mock(LoanRepository.class);
        service = new LibraryService(mockBookRepo, mockUserRepo, mockLoanRepo);
    }
    
    @Test
    void shouldLendAvailableBookToEligibleUser() {
        // Arrange
        User user = new User(UserId.random(), "John Doe");
        Book book = new Book(ISBN.of("123-456"), "Clean Code", Author.of("Uncle Bob"));
        
        when(mockUserRepo.findById(any())).thenReturn(Optional.of(user));
        when(mockBookRepo.findByIsbn(any())).thenReturn(Optional.of(book));
        
        // Act
        LoanResult result = service.lendBook(book.getIsbn(), user.getId());
        
        // Assert
        assertTrue(result.isSuccess());
        verify(mockLoanRepo).save(any(Loan.class));
        verify(mockBookRepo).save(any(Book.class));
    }
}
```

### 5. Bonus: Exception Handling (30 Minuten)
```java
public class LibraryException extends RuntimeException {
    private final ErrorCode code;
    
    public LibraryException(ErrorCode code, String message) {
        super(message);
        this.code = code;
    }
}

@ControllerAdvice
public class LibraryExceptionHandler {
    @ExceptionHandler(LibraryException.class)
    public ResponseEntity<ErrorResponse> handleLibraryException(LibraryException ex) {
        ErrorResponse response = new ErrorResponse(ex.getCode(), ex.getMessage());
        return ResponseEntity.status(ex.getCode().getHttpStatus()).body(response);
    }
}
```

## Bewertungskriterien
- [ ] Saubere Domänenmodelle
- [ ] Klare Verantwortlichkeiten
- [ ] Fehlerbehandlung
- [ ] Testabdeckung
- [ ] Wartbarkeit
- [ ] Performance-Berücksichtigung

[Fortsetzung mit der nächsten Übung...]

Soll ich mit der letzten Übung des Workshops fortfahren?