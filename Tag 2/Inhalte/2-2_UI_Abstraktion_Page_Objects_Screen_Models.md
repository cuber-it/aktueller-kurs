# 2-2 · UI-Abstraktion: Page Objects, Screen Models & bestehende Lösung

Page Objects und Screen Models dienen als **Referenzkonzepte** für die vorhandene UI-Abstraktion. Es geht nicht darum, sie nachträglich als Zielarchitektur einzuführen.

- **UI-Abstraktion** – Bündelt Wissen über einen UI-Bereich hinter einer für Tests nutzbaren Schnittstelle.
- **Page / Screen Object** – Konzentriert Aktionen, Zustände und technische UI-Details, die zu einer sinnvollen Verantwortung gehören.
- **Object Map und Objektidentifikation** – Wissen darüber, wie UI-Objekte gefunden werden, ist technische Kopplung und sollte nicht unnötig über Tests verteilt sein.
- **Grenzen** – Visuelle Seiten, Fenster und technische AUT-Grenzen sind nicht zwangsläufig identisch.
- **Aktion, Zustand und Verifikation** – Welche dieser Aufgaben eine UI-Abstraktion übernimmt, ist eine bewusste Architekturentscheidung.
- **Größe** – Große UI-Objekte können wie jede andere Klasse zu viele Verantwortlichkeiten ansammeln.
- **Vergleich** – Interessant ist, welche POM-Ideen die vorhandene Lösung bereits enthält und wo sie bewusst anders geschnitten ist.

## Leitgedanke

Pattern-Namen helfen beim Vergleich, entscheiden aber nicht über die Qualität einer vorhandenen UI-Abstraktion.

> **Merksatz:** Entscheidend ist nicht, ob etwas „Page Object“ heißt, sondern ob seine Verantwortung und Grenze sinnvoll gewählt sind.
