# 1-6 · Zustand, Lifecycle & Ressourcen

Objekte können Zustände besitzen, Ressourcen verwalten und während ihrer Lebensdauer unterschiedliche Bedingungen erfüllen müssen. Diese Aspekte gehören zum **Design des Objekts** und nicht nur zur Fehlerbehandlung.

- **Zustand** – Der aktuelle Zustand eines Objekts beeinflusst, welche Operationen sinnvoll oder zulässig sind.
- **Invarianten** – Bedingungen, die für ein gültiges Objekt stets gelten sollen, sollten durch die API und Initialisierung geschützt werden.
- **Initialisierung** – Nach erfolgreicher Konstruktion sollte ein Objekt möglichst verwendbar sein. Halb initialisierte Objekte erhöhen die Zahl möglicher Fehlerzustände.
- **Lifecycle** – Manche Objekte müssen explizit gestartet, beendet, verbunden oder geschlossen werden. Diese Übergänge sollten in der Schnittstelle erkennbar sein.
- **Ressourcen** – Dateien, Verbindungen, Prozesse oder Testumgebungen benötigen verlässliches Cleanup – auch bei Exceptions.
- **Context Manager** – `with` und das Context-Manager-Protokoll modellieren einen klar begrenzten Lebenszyklus und garantieren einen definierten Ausstiegspfad.
- **Exceptions** – Fehler sollten dort behandelt werden, wo sinnvoll entschieden werden kann, wie es weitergeht. Zu frühes Verschlucken von Exceptions erschwert Diagnose und Wiederherstellung.
- **Cleanup in Testsystemen** – Setup und Teardown sind besonders kritisch: Ein fehlgeschlagener Test darf die Umgebung möglichst nicht in einem undefinierten Zustand für den nächsten Test hinterlassen.

## Designfrage

Ein Objekt, das eine Ressource öffnet oder einen Zustand aktiviert, braucht eine klare Antwort auf:

**Wer beendet diesen Zustand – und was passiert, wenn zwischen Start und Ende ein Fehler auftritt?**

> **Merksatz:** Zustand, Fehlerbehandlung und Cleanup sind Teil des Objektdesigns.
