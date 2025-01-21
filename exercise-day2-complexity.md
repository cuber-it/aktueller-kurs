# Übung: Komplexität reduzieren

## Ausgangscode: Versicherungsberechnung
```java
public class InsuranceCalculator {
    public double calculatePremium(Person person, Policy policy) {
        double premium = 0;
        if (person != null && policy != null) {
            if (person.getAge() >= 18 && person.getAge() <= 70) {
                if (policy.getType().equals("LIFE")) {
                    if (person.isSmoker()) {
                        if (person.getAge() < 35) {
                            premium = policy.getBaseAmount() * 1.5;
                        } else if (person.getAge() < 50) {
                            premium = policy.getBaseAmount() * 2.0;
                        } else {
                            premium = policy.getBaseAmount() * 2.5;
                        }
                        if (person.hasDangerousOccupation()) {
                            premium *= 1.3;
                        }
                    } else {
                        if (person.getAge() < 35) {
                            premium = policy.getBaseAmount() * 1.0;
                        } else if (person.getAge() < 50) {
                            premium = policy.getBaseAmount() * 1.3;
                        } else {
                            premium = policy.getBaseAmount() * 1.5;
                        }
                        if (person.hasDangerousOccupation()) {
                            premium *= 1.2;
                        }
                    }
                } else if (policy.getType().equals("HEALTH")) {
                    if (person.hasPreExistingConditions()) {
                        premium = policy.getBaseAmount() * 2.5;
                        if (person.getAge() >= 50) {
                            premium *= 1.5;
                        }
                    } else {
                        premium = policy.getBaseAmount() * 1.5;
                        if (person.getAge() >= 50) {
                            premium *= 1.2;
                        }
                    }
                }
            }
        }
        return premium;
    }
}
```

## Aufgaben

### 1. Komplexität analysieren (15 Minuten)
- Zyklomatische Komplexität berechnen
- Abhängigkeiten identifizieren
- Geschäftsregeln extrahieren

### 2. Refactoring durchführen (45 Minuten)

#### Schritt 1: Grundlegende Validierung extrahieren
```java
public class InsuranceCalculator {
    public double calculatePremium(Person person, Policy policy) {
        validateInputs(person, policy);
        if (!isEligible(person)) {
            return 0.0;
        }
        return calculatePremiumByPolicyType(person, policy);
    }

    private void validateInputs(Person person, Policy policy) {
        Objects.requireNonNull(person, "Person must not be null");
        Objects.requireNonNull(policy, "Policy must not be null");
    }
}
```

#### Schritt 2: Strategy Pattern für Policen
```java
public interface PremiumCalculationStrategy {
    double calculatePremium(Person person, Policy policy);
}

public class LifeInsuranceCalculator implements PremiumCalculationStrategy {
    @Override
    public double calculatePremium(Person person, Policy policy) {
        double basePremium = calculateBasePremium(person, policy);
        return applyOccupationMultiplier(person, basePremium);
    }
}
```

### 3. Tests implementieren (30 Minuten)
```java
class InsuranceCalculatorTest {
    @Test
    void shouldCalculateLifePremiumForYoungNonSmoker() {
        Person person = new Person(25, false, false, false);
        Policy policy = new Policy("LIFE", 1000.0);
        InsuranceCalculator calculator = new InsuranceCalculator();
        
        double premium = calculator.calculatePremium(person, policy);
        
        assertEquals(1000.0, premium);
    }
}
```

### 4. Bonus: Regelengine implementieren (30 Minuten)
```java
public class PremiumRule {
    private final Predicate<Person> condition;
    private final DoubleUnaryOperator adjustment;

    public PremiumRule(Predicate<Person> condition, DoubleUnaryOperator adjustment) {
        this.condition = condition;
        this.adjustment = adjustment;
    }

    public double apply(Person person, double currentPremium) {
        return condition.test(person) ? adjustment.applyAsDouble(currentPremium) : currentPremium;
    }
}
```

## Bewertungskriterien
- [ ] Reduzierte Verschachtelungstiefe
- [ ] Keine magischen Zahlen
- [ ] Separierte Geschäftslogik
- [ ] Testabdeckung
- [ ] Erweiterbarkeit

## Hinweise für Trainer
- Code-Coverage-Tools zeigen
- Refactoring schrittweise durchführen
- Alternative Lösungsansätze diskutieren
