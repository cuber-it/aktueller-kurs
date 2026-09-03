# 2-2 · Entity und Value Object

Zwei Arten von Dingen im Modell, unterschieden durch **eine** Frage: Hat es eine Identität, die über die Zeit bestehen bleibt — oder ist es durch seine Werte bestimmt?

Die Antwort entscheidet, wie verglichen, gespeichert und geändert wird. Sie ist eine **fachliche** Frage, keine technische: Dasselbe Ding kann in einem Kontext Entity sein und im anderen Value Object.

- **Entity** – Etwas, das dieselbe Sache bleibt, auch wenn sich alle Merkmale ändern. Ein Fahrzeug mit neuem Kennzeichen und neuem Halter ist dasselbe Fahrzeug.
- **Identität** – Was eine Entity über die Zeit zusammenhält; fachlich vergeben (Fahrgestellnummer) oder technisch (laufende Nummer).
- **Value Object** – Etwas, das vollständig durch seine Werte bestimmt ist. Zwei Beträge von 50 Euro sind austauschbar.
- **Unveränderlich** – Value Objects werden nicht geändert, sondern ersetzt. Wer aus 50 Euro 60 macht, hat einen anderen Betrag, nicht denselben mit neuem Wert.
- **Die Prüffrage** – Interessiert es, ob es **dasselbe** ist, oder nur, ob es **gleich** ist?
- **Kontextabhängig** – Ein Geldschein ist für die Kasse ein Betrag (Value Object), für die Zentralbank ein Einzelstück mit Seriennummer (Entity).
- **Value Objects tragen Regeln** – Ein Zeitraum weiß, dass sein Ende nach seinem Beginn liegt. Solche Regeln gehören zum Wert, nicht in den Aufrufer.
- **Warum das lohnt** – Value Objects sind einfacher: kein Lebenszyklus, keine Identitätsverwaltung, gefahrlos kopierbar und vergleichbar.
- **Häufiger Fehler** – Alles zur Entity machen. Anschrift, Zeitraum, Betrag, Kennzeichen sind meist Werte, keine Dinge mit Geschichte.
- **Zweiter Fehler** – Werte als bloße Zahlen oder Zeichenketten führen. Ein „Betrag" ohne Währung und ohne Rundungsregel ist eine Zahl, kein Wert.
- **Erkennungszeichen für eine Entity** – Man kann sie suchen, verfolgen, ihre Geschichte erzählen. Bei einem Wert wäre das sinnlos.
