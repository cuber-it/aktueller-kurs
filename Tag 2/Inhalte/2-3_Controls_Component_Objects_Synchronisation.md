# 2-3 · Controls, Component Objects & Synchronisation

Controls und Component Objects kapseln wiederkehrende UI-Interaktion. Entscheidend ist, **welches Verhalten auf dieser Ebene sinnvoll aufgehoben ist und wie sichtbar es für Test und Diagnose bleibt**.

- **Control** – Kapselt elementare Squish-Interaktionen und kann wiederkehrendes technisches Verhalten vereinheitlichen.
- **Component Object** – Modelliert eine zusammengesetzte oder wiederverwendbare UI-Komponente wie Dialog, Tabelle, Tree oder Toolbar.
- **Komposition** – Größere UI-Bereiche können aus kleineren Controls und Components aufgebaut werden.
- **Thin vs. Smart Control** – Mehr gekapseltes Verhalten reduziert Duplikation, erhöht aber Verantwortung und mögliche Nebenwirkungen.
- **Interaction + Wait** – Aktion und Synchronisation können zusammengehören, wenn der erwartete Folgezustand stabil Teil der Interaktion ist.
- **Zustandsorientiertes Warten** – Auf relevante Bedingungen zu warten ist robuster als pauschale Sleeps.
- **Application Context** – AUT-Wechsel und Restarts können Teil der Interaktions- und Synchronisationsarchitektur sein.
- **Diagnose** – Kapselung darf relevante Informationen über Objekt, Zustand und Fehlerursache nicht verbergen.

## Leitgedanke

Synchronisation ist Teil der Interaktionsarchitektur und gehört auf die Ebene, die den erwarteten Zustand zuverlässig kennt.

> **Merksatz:** Synchronisation gehört dorthin, wo der relevante Zustand verstanden wird – aber sie darf Verhalten nicht unsichtbar machen.
