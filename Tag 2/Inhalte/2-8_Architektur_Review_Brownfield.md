# 2-8 · Architektur-Review am bestehenden Squish-Projekt

Die Konzepte des Tages dienen als **Analysewerkzeuge für die vorhandene Testautomatisierung**. Ziel ist nicht, möglichst viele Patterns einzuführen, sondern bestehende Entscheidungen zu verstehen und mögliche Änderungen an konkreten Problemen zu messen.

- **Brownfield** – Die vorhandene Architektur ist unter realen Anforderungen und Randbedingungen entstanden und wird nicht allein an Pattern-Namen bewertet.
- **Verantwortung** – Controls, UI-Modelle, Helper, Workflows, Verifikationsobjekte und Tests werden nach ihrer tatsächlichen Aufgabe betrachtet.
- **Änderungsursachen** – Relevant ist, welche Teile bei Änderungen an UI, Squish-Integration, Ablauf, Target oder Testdaten betroffen sind.
- **Kopplung** – Notwendige technische Kopplung wird von unnötig verteiltem Wissen unterschieden.
- **Synchronisation und Verifikation** – Ihre Position wird danach bewertet, welche Ebene Zustand und Testaussage tatsächlich versteht.
- **Wiederverwendung** – Gemeinsamer Code rechtfertigt nur dann weitere Abstraktion, wenn auch Verantwortung und Änderungsursachen zusammengehören.
- **Alternativen und Kosten** – Ein anderes Pattern ist eine Option, deren Nutzen gegen Indirektion, Migration und Lernaufwand abgewogen wird.
- **Entscheidung** – Ein Review kann zu *beibehalten, vereinfachen, ergänzen, gezielt umbauen, bewusst nicht übernehmen* oder *offenlassen* führen.
- **Teamregel** – Lokale Entscheidungen werden erst dann zum Standard, wenn sie verallgemeinerbar und begründbar sind.

## Leitgedanke

Brownfield-Architekturarbeit bedeutet, vorhandene Strukturen zu verstehen und Änderungen nur dort vorzunehmen, wo sie einen nachvollziehbaren Vorteil bringen.

> **Merksatz:** Gute Architekturarbeit beginnt im Brownfield mit Verstehen und begründeten Entscheidungen – nicht mit dem Austausch funktionierender Strukturen.
