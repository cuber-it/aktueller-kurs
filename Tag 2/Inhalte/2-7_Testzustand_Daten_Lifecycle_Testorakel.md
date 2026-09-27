# 2-7 · Testzustand, Daten, Lifecycle & Testorakel

Eine belastbare Testarchitektur muss nicht nur UI-Aktionen organisieren. Sie kontrolliert auch **Vorbedingungen, Daten, Lebenszyklus, Beobachtung und Bewertung**.

- **Ausgangszustand und Isolation** – Tests benötigen bekannte Vorbedingungen und sollten nicht unbeabsichtigt vom Zustand vorheriger Tests abhängen.
- **Setup und Cleanup** – Initialisierung und Aufräumen gehören zur Architektur und müssen auch für Fehlerpfade funktionieren.
- **Test-Wrapper** – Gemeinsame Lifecycle-, Fehler- und Diagnosemechanismen können zentral um Tests gelegt werden.
- **Testdaten** – Konfiguration, Datenobjekte, Enums, Builder oder externe Datenquellen sind unterschiedliche Möglichkeiten, Daten kontrolliert bereitzustellen.
- **Zustandsaufbau** – Setup über die UI ist nicht immer erforderlich; der gewählte Weg darf jedoch die Aussage des Tests nicht verändern.
- **Target-Abstraktion** – Ermöglicht Beobachtung oder Interaktion mit unterschiedlichen Zielsystemen über eine gemeinsame Schnittstelle.
- **Testorakel** – Bewertet anhand beobachtbarer Informationen, ob das erwartete Verhalten eingetreten ist.
- **Verifikationsobjekte** – Können wiederkehrende Prüfarten vereinheitlichen und Diagnose verbessern.
- **Fehlerdiagnose** – Testfehler, Umgebungsprobleme und AUT-Fehler sollten möglichst unterscheidbar bleiben.

## Leitgedanke

Aktion, Beobachtung und Bewertung sind unterschiedliche Verantwortungen, auch wenn sie nicht zwangsläufig in getrennten Klassen implementiert werden.

> **Merksatz:** Testarchitektur organisiert nicht nur Aktionen – sie kontrolliert Zustand, Daten, Beobachtung und Diagnose.
