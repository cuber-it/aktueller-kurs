# 2-5 · Wiederverwendbare Abläufe: Tasks, Workflows & Helper

Vorhandene Helper reichen von kleinen technischen Hilfen bis zu vollständigen Abläufen. Für die Architektur ist deshalb nicht ihr Name entscheidend, sondern ihre **tatsächliche Verantwortung**.

- **Technischer Helper** – Kapselt eine wiederverwendbare technische Fähigkeit nahe an Squish oder Infrastruktur.
- **Task** – Beschreibt eine zusammenhängende Testhandlung und kann mehrere UI-Bereiche koordinieren.
- **Workflow** – Modelliert einen wiederkehrenden Ablauf mit mehreren Schritten und gegebenenfalls eigenem Zustand oder Lifecycle.
- **Service Layer** – Kann übergeordnete Abläufe kapseln, benötigt dafür aber eine eigene Verantwortung statt bloßer Weiterleitung.
- **Komposition** – Tasks und Workflows verwenden vorhandene Controls und UI-Abstraktionen, statt deren Verantwortlichkeiten zu duplizieren.
- **Versteckte Testlogik** – Wiederverwendung wird problematisch, wenn wesentliche Aktionen oder Prüfungen im Testfall nicht mehr erkennbar sind.
- **Wiederverwendung** – Gleicher Code ist ein Hinweis auf mögliche Gemeinsamkeit, aber noch keine Begründung für eine neue Schicht.
- **Lifecycle** – Längere Abläufe müssen Zustand, AUT-Kontext und Fehlerpfade berücksichtigen.

## Leitgedanke

Eine neue Schicht entsteht nicht durch Umbenennen oder Verschieben vorhandener Helper, sondern durch eine eigenständige und erkennbare Verantwortung.

> **Merksatz:** Wiederverwendung allein rechtfertigt keine neue Schicht – ein Workflow braucht eine eigene, erkennbare Verantwortung.
