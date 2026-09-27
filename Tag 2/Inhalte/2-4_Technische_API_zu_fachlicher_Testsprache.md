# 2-4 · Von technischer Test-API zu fachlicher Testsprache

Eine technische Test-API kapselt Squish-Details. Eine zusätzliche fachlichere API kann darüber die **Absicht des Tests** ausdrücken – aber nur, wenn sie tatsächlich Klarheit schafft oder technische Komplexität verbirgt.

- **Technische Test-API** – Beschreibt UI-nahe Operationen wie klicken, auswählen, eingeben oder warten.
- **Fachliche Test-API** – Beschreibt eine relevante Testabsicht statt der einzelnen Bedienungsschritte.
- **Facade / Domain API** – Kann mehrere Controls oder UI-Abstraktionen hinter einer fachnäheren Operation koordinieren.
- **Fluent Interface** – Kann Tests lesbarer machen, erzeugt aber zusätzliche API- und Wartungskosten.
- **Kapselung** – Object Map, Squish-Interaktion und Synchronisation können verborgen werden, wenn der Aufrufer diese Details nicht benötigt.
- **Beobachtbarkeit** – Wesentliche Ergebnisse, Assertions und Fehler dürfen durch die Abstraktion nicht unsichtbar werden.
- **Direkter Zugriff** – Direkte Squish- oder Control-Nutzung bleibt sinnvoll, wenn die Operation klar und lokal ist.
- **YAGNI** – Eine weitere API-Schicht braucht ein konkretes Problem, das sie löst.

## Leitgedanke

Abstraktion verbessert Tests nur, wenn sie die richtige Information verbirgt und die relevante Testabsicht deutlicher macht.

> **Merksatz:** Eine zusätzliche API-Schicht lohnt sich nur, wenn sie relevante Testabsicht klarer ausdrückt oder echte technische Komplexität kapselt.
