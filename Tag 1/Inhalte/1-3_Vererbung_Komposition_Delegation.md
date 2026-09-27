# 1-3 · Vererbung, Komposition & Delegation

Vererbung und Komposition ermöglichen beide Wiederverwendung, modellieren aber **unterschiedliche Beziehungen**. Die Entscheidung sollte deshalb nicht danach fallen, womit sich Code am schnellsten wiederverwenden lässt.

- **Vererbung** – Eine Unterklasse spezialisiert einen Typ und übernimmt dessen Vertrag. Sie ist sinnvoll, wenn tatsächlich eine stabile „ist-ein“-Beziehung besteht.
- **Polymorphismus** – Unterschiedliche Implementierungen können über denselben erwarteten Vertrag verwendet werden. Vererbung ist eine Möglichkeit, diesen Vertrag auszudrücken – in Python aber nicht die einzige.
- **Risiko der Vererbung** – Unterklassen hängen von Verhalten und Annahmen ihrer Basisklasse ab. Tiefe Hierarchien verteilen Wissen über mehrere Ebenen und erschweren Änderungen.
- **Komposition** – Ein Objekt verwendet andere Objekte, um seine Aufgabe zu erfüllen. Verantwortlichkeiten bleiben getrennt und können unabhängig verändert werden.
- **Delegation** – Ein Objekt nimmt einen Aufruf entgegen und überträgt die konkrete Arbeit an einen geeigneten Kollaborateur. Dadurch kann die äußere API stabil bleiben.
- **Austauschbarkeit** – Komponierte Abhängigkeiten lassen sich häufig zur Laufzeit auswählen oder für Tests ersetzen.
- **Wiederverwendung ist kein Selbstzweck** – Gemeinsamer Code allein rechtfertigt keine Vererbung. Die semantische Beziehung und die zukünftigen Änderungsrichtungen sind entscheidend.
- **Testautomatisierung** – Basisklassen für alle Tests oder alle Screens wirken zunächst bequem, entwickeln sich aber leicht zu Sammelstellen. Komposition kann Logging, Navigation, Synchronisation oder andere Fähigkeiten gezielter bereitstellen.

## Entscheidungsfrage

**Ist das neue Objekt wirklich eine Spezialisierung des Basistyps – oder benötigt es lediglich einen Teil seines Verhaltens?**

Im zweiten Fall ist Komposition meist die passendere Ausgangshypothese.

> **Merksatz:** Vererbung modelliert eine echte Beziehung; Komposition kombiniert Verhalten.
