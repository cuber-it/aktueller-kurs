# Folie 1: Titelfolie
```
Clean Code Workshop
Tag 1: Grundlagen und Prinzipien
[Datum]
[Trainer Name]
```

# Folie 2: Agenda Tag 1
```
Vormittag (9:00 - 12:00)
• Einführung in Clean Code
• Code Smells verstehen
• Namensgebung & Standards

Nachmittag (13:00 - 17:00)
• Kommentare & Dokumentation
• Praktische Übungen
• Code Reviews
```

# Folie 3: Was ist Clean Code?
```
Clean Code Definition:

• Lesbar und verständlich auf den ersten Blick
• Einfach zu warten und zu erweitern
• Gut getestet
• Keine Überraschungen
• Ein Code ist clean, wenn er besser ist als zuvor
  ("Boy Scout Rule")

Zitat (Robert C. Martin):
"Any fool can write code that a computer can understand. 
Good programmers write code that humans can understand."
```

# Folie 4: Warum Clean Code?
```
Wirtschaftliche Gründe:
• 80% der Kosten entstehen in der Wartung
• Neue Teammitglieder schneller produktiv
• Weniger Bugs durch bessere Lesbarkeit

Technische Gründe:
• Einfachere Fehlerbehebung
• Bessere Testbarkeit
• Leichtere Erweiterbarkeit

Persönliche Gründe:
• Höhere Entwicklerzufriedenheit
• Bessere Teamzusammenarbeit
• Professionelle Entwicklung
```

# Folie 5: Code Smells - Einführung
```
Was sind Code Smells?
• Warnsignale im Code
• Hinweise auf mögliche Probleme
• Nicht zwingend Fehler
• Zeigen Verbesserungspotenzial

Häufige Kategorien:
1. Bloaters (aufgeblähter Code)
2. Object-Orientation Abusers
3. Change Preventers
4. Dispensables (Überflüssiges)
5. Couplers (Kopplungsprobleme)
```

# Folie 6: Wichtige Code Smells
```
1. Long Method
   • Methode > 20 Zeilen
   • Viele Abstraktionsebenen
   • Lösung: Extract Method

2. Large Class
   • Klasse > 200 Zeilen
   • Zu viele Verantwortlichkeiten
   • Lösung: Extract Class/Interface

3. Duplicate Code
   • Copy & Paste Code
   • Ähnliche Strukturen
   • Lösung: Extract Method/Superclass

4. Long Parameter List
   • > 3 Parameter
   • Lösung: Parameter Object
```

# Folie 7: Namen - Grundregeln
```
Grundprinzipien guter Namen:
• Aussagekräftig und präzise
• Entsprechend der Verwendungsdauer
• Aussprechbar
• Suchbar
• Keine Codierungen

Beispiele:
❌ Schlecht         ✅ Gut
d                  daysSinceStart
proc               processOrder
calcTax            calculateTaxForOrder
hp                 highPriorityCount
```

# Folie 8: Namenskonventionen
```
Klassen:
• Nomen oder Nominalphrasen
• Konkrete Bedeutung
Beispiel: Customer, OrderProcessor

Methoden:
• Verben oder Verbphrasen
• Aktion beschreiben
Beispiel: processOrder(), validateInput()

Variablen:
• Präzise Bedeutung
• Kontext beachten
Beispiel: firstName, orderTotal

Konstanten:
• Großbuchstaben mit Unterstrichen
Beispiel: MAX_RETRY_COUNT
```

[Fortsetzung folgt...]

Soll ich mit den weiteren Folien für Tag 1 fortfahren?