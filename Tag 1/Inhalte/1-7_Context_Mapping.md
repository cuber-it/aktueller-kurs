# 1-7 · Context Mapping: Beziehungen zwischen Kontexten

Eine Context Map zeigt, **wie Bounded Contexts zueinander stehen** — nicht welche Daten fließen, sondern wer nachziehen muss, wenn sich beim anderen etwas ändert.

Die bestimmende Frage lautet: **Wer zieht nach, und wie viel Einfluss hat er darauf?** Aus der Antwort folgt das Beziehungsmuster.

- **Context Map** – Übersicht der Kontexte und ihrer Beziehungen; beantwortet vor einer Änderung die Frage, wen es trifft.
- **Abhängigkeitsrichtung** – Wer bei einer Änderung nachziehen muss; kann der Datenrichtung entgegengesetzt sein.
- **Customer / Supplier** – Der Abnehmer kann Anforderungen stellen, es gibt Absprache und Vorlauf; der Lieferant berücksichtigt sie.
- **Conformist** – Der Abnehmer übernimmt das fremde Modell unverändert, weil er keinen Einfluss hat. Legitim bei stabilem Format und geringer Bedeutung — aber als Entscheidung, nicht als Zustand.
- **Anticorruption Layer** – Der Abnehmer übersetzt das fremde Modell an der Grenze in sein eigenes; schützt davor, dass Fremdformate in mehrere Kontexte durchsickern.
- **Open Host Service** – Der Lieferant bietet eine veröffentlichte Schnittstelle für viele Abnehmer, statt jeden einzeln zu bedienen.
- **Published Language** – Ein gemeinsames Austauschformat, auf das sich mehrere geeinigt haben; oft mit Open Host Service zusammen.
- **Shared Kernel** – Zwei Kontexte teilen sich einen Modellausschnitt; jede Änderung muss abgestimmt werden, Releases sind gekoppelt. Das teuerste Muster im Katalog.
- **Partnership** – Zwei Teams stehen und fallen gemeinsam; koordinierte Planung und gemeinsame Auslieferung.
- **Separate Ways** – Keine Verbindung. Eine Entscheidung, keine Lücke, und gehört in die Map.
- **Conformist ohne Grenze** – Der teure Fall: Das Fremdformat wandert über die Anbindung hinaus in andere Kontexte. Eine Formatänderung trifft dann alles.
- **Umfang der Map** – Auf eine Seite. Eine Darstellung über mehrere Seiten wird vor einer Änderung nicht gelesen.
- **Aktualität** – Durch Anlass, nicht durch Turnus: Bei jeder neuen Anbindung ergänzen, bevor entwickelt wird.
