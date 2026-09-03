# Lösungsvorschlag · Bounded Context Canvas

**Vorbemerkung:** Ein Vorschlag. Bei mehreren strittigen Aufgaben sind zwei Zuordnungen vertretbar — bewertet wird die Begründung und ihre Konsistenz mit dem Zwecksatz.

---

## 1 · Der Zwecksatz

> **Die Anmietung verantwortet den Mietvorgang von der Reservierung bis zum Abschluss.**

**Warum dieser Satz trägt:**

| Prüfung | |
|---|---|
| Nennt ein fachliches Ergebnis | ja — der abgeschlossene Mietvorgang |
| Ohne Aufzählung | ja |
| Ohne Ortsangabe | ja — „Station" kommt nicht vor, damit ist die Webseite eingeschlossen |
| Grenze erkennbar | ja — vor der Reservierung und nach dem Abschluss endet die Zuständigkeit |

**Was der Satz ausschließt:** alles, was vor der Reservierung liegt (Konditionen vereinbaren) und alles danach (abrechnen, reparieren).

**Verworfene Formulierungen:**

| Vorschlag | Warum nicht |
|---|---|
| „Alles, was am Tresen passiert" | Ort statt Fachlichkeit; schließt die Webseite fälschlich aus |
| „Fahrzeuge ausgeben und zurücknehmen" | zu eng, lässt Reservierung und Verlängerung weg |
| „Die Kundenbeziehung während der Miete" | zu weit, überschneidet mit Vertragsverwaltung |
| „Vorgänge verwalten und Fahrzeuge disponieren" | „und" — zwei Klammern statt einer |

---

## 2 · Die acht unstrittigen Aufgaben

| # | Aufgabe | Passt zum Zweck |
|---|---|---|
| 1 | Reservierung entgegennehmen | ja — Beginn des Vorgangs |
| 2 | Ausgeben, Mietvertrag erstellen | ja |
| 3 | Zurücknehmen, Vorgang abschließen | ja — Ende des Vorgangs |
| 4 | Verlängerung | ja — Änderung am laufenden Vorgang |
| 7 | Zusatzleistungen buchen | ja — Bestandteil des Vorgangs |
| 12 | Buchungen aus dem Partnernetzwerk | ja — eine Reservierung, andere Herkunft |
| 13 | Firmenkonditionen anwenden | ja — Anwendung, nicht Festlegung |
| 14 | Vorgangshistorie bereithalten | ja |

**Alle acht passen.** Bei 13 ist die Formulierung wichtig: *anwenden*, nicht *festlegen*. Das Festlegen gehört in die Vertragsverwaltung.

---

## 3 · Die sechs strittigen Aufgaben

### 5 · Fahrerlaubnis prüfen

**Prüffrage:** Würde eine Änderung daran die übrigen Aufgaben betreffen?

Nein. Ob der Prüfdienst wechselt oder die Prüfregeln sich ändern, berührt Reservierung, Ausgabe und Rückgabe nicht — außer dass ein Ergebnis gebraucht wird.

**Zusätzlicher Befund:** Die Vertragsverwaltung nutzt denselben Dienst für die Jahresprüfung.

**Entscheidung:** Gehört **nicht** in die Anmietung. Die Prüfung ist eine eigenständige Fähigkeit, die zwei Kontexte nutzen.

**Wohin:** Ein eigener kleiner Kontext **Fahrerprüfung** — oder, falls das übertrieben erscheint, ein gemeinsam genutzter Dienst mit eigener Grenze. Die Anmietung fragt an und bekommt ein Ergebnis.

### 6 · Kaution sperren und freigeben

**Prüffrage:** Änderung betrifft übrige Aufgaben?

Ja. Die Sperrung ist Teil der Ausgabe, die Freigabe Teil der Rückgabe. Ohne sie ist der Vorgang unvollständig.

**Abgrenzung:** Die *buchhalterische* Behandlung — durchlaufender Posten, Verrechnung — liegt bei der Fakturierung. Das ist eine andere Frage als die Sperrung auf der Karte.

**Entscheidung:** Bleibt. Mit ausdrücklicher Abgrenzung im Canvas.

### 8 · Preis für Zusatzleistungen berechnen

**Prüffrage:** Nein. Eine Preisänderung berührt den Vorgangsablauf nicht.

**Befund:** Preise stehen im Rahmenvertrag oder in einer Preisliste, die der Vertrieb pflegt.

**Entscheidung:** Gehört **nicht** in die Anmietung. Die Anmietung *bucht* Zusatzleistungen und *wendet* Preise an, sie *legt sie nicht fest*.

**Wohin:** Vertragsverwaltung — dieselbe Klammer wie die Firmenkonditionen.

**Konsistenz:** Dieselbe Begründung wie bei Aufgabe 13. Anwenden ja, festlegen nein.

### 9 · Schaden bei Rückgabe aufnehmen

**Prüffrage:** Ja. Die Aufnahme geschieht im Rahmen der Rückgabe und hält den Vorgang offen, bis geklärt ist.

**Entscheidung:** Bleibt — begrenzt auf die **Aufnahme**. Was der Schaden kostet und wer ihn zahlt, entscheidet die Fakturierung nach Beurteilung durch die Werkstatt.

### 10 · Schadensfotos speichern und weiterleiten

**Prüffrage:** Das Speichern ja — es gehört zur Aufnahme. Das **Weiterleiten** an Werkstatt und Schadensplattform: nein.

**Entscheidung:** Aufteilen.

| Teil | Wohin |
|---|---|
| Fotos aufnehmen und speichern | Anmietung — Teil der Schadensaufnahme |
| Weiterleitung an die Werkstatt | Flotte und Instandhaltung holt sie sich |
| Weiterleitung an die Schadensplattform | Fakturierung — sie führt die Regulierung |

**Begründung:** Ein Kontext, der Empfänger kennt, hängt von ihnen ab. Die Anmietung soll melden, dass ein Schaden aufgenommen wurde — wer das braucht, holt es sich.

### 11 · Verfügbarkeitsanzeige für die Webseite

**Prüffrage:** Teilweise. Sie braucht Reservierungen (Anmietung) und Fahrzeugbestand (Flotte).

Das ist der schwierigste Fall. Zwei vertretbare Antworten:

| Antwort | Begründung |
|---|---|
| **Bleibt in der Anmietung** | Buchbarkeit ist eine Aussage über Reservierbarkeit. Der Bestand kommt von der Flotte |
| **Eigener Kontext Verfügbarkeit** | Sie dient dem Vertriebskanal, nicht dem Vorgang. Sie hat eigene Anforderungen (Antwortzeit, Zwischenspeicherung, Lastspitzen) |

**Vorschlag:** Bleibt vorerst, aber **ausdrücklich als offen ausgewiesen**. Kriterium für die spätere Entscheidung: Wenn die Webseite eigene Anforderungen an Antwortzeit oder Vorschau stellt, die den Vorgangsablauf nicht betreffen, wird sie ein eigener Kontext.

---

## 4 · Das ausgefüllte Canvas

| Feld | Inhalt |
|---|---|
| **Name** | Anmietung |
| **Zweck** | Verantwortet den Mietvorgang von der Reservierung bis zum Abschluss |
| **Strategische Einordnung** | **Core Domain.** Hier findet das Kerngeschäft statt; die Qualität des Vorgangs ist unterscheidungsrelevant gegenüber Wettbewerbern |
| **Fachliche Entscheidungen** | Ist ein Fahrzeug reservierbar? · Darf ausgegeben werden? · Ist der Vorgang abgeschlossen oder bleibt er offen? · Wurde ein Schaden festgestellt? |
| **Ubiquitous Language** | Vorgang, Mietvertrag, Verlängerung, Mieter, Firmenkonditionen, Fahrzeug, Rückläufer, Reserviert, Kaution → Glossar Anmietung |
| **Eingehende Nachrichten** | Konditionen (Vertragsverwaltung) · Fahrzeugbestand (Flotte) · Buchungen (Partnernetzwerk) · Prüfergebnis Fahrerlaubnis (Fahrerprüfung) · Preise für Zusatzleistungen (Vertragsverwaltung) |
| **Ausgehende Nachrichten** | Abgeschlossener Vorgang (Fakturierung) · Ausgabe und Rückgabe (Flotte) · Schaden aufgenommen (Flotte, Fakturierung) |
| **Nicht zuständig für** | Konditionen und Preise **festlegen** → Vertragsverwaltung · Buchhalterische Behandlung der Kaution → Fakturierung · Schadensbewertung und Kostenzuweisung → Werkstatt, Fakturierung · Fahrerlaubnisprüfung → Fahrerprüfung · Fahrzeuglebenszyklus → Flotte |

---

## 5 · Aufgaben 9 und 10 unterschiedlich entschieden

**Kein Problem — sondern das erwartbare Ergebnis.**

„Schaden aufnehmen" und „Fotos weiterleiten" sehen zusammengehörig aus, sind es aber nicht:

| | Aufnehmen | Weiterleiten |
|---|---|---|
| Gehört zu | dem Vorgang | den Empfängern |
| Ändert sich, wenn | die Aufnahme sich ändert | ein Empfänger sich ändert |

Dass zwei Aufgaben in einem Ticket standen, sagt nichts über ihre Zusammengehörigkeit. Genau solche Bündel sind die Ursache dafür, dass Kontexte wachsen.

**Die Regel dahinter:** Ein Kontext meldet, dass etwas geschehen ist. Wer es braucht, holt es sich. Ein Kontext, der seine Empfänger kennt, muss bei jedem neuen Empfänger geändert werden.

---

## 6 · Umfang nach der Entscheidung

| | vorher | nachher |
|---|---|---|
| Aufgaben | 14 | **11** |
| davon offen ausgewiesen | 0 | 1 (Verfügbarkeitsanzeige) |
| abgegeben | | 3 (Fahrerprüfung, Preisfestlegung, Weiterleitung) |

**Ist er damit ausgewogen?** Noch nicht. Elf Aufgaben sind weiterhin mehr als in den übrigen Kontexten, und der Anteil an den offenen Tickets wird sich nicht auf ein Viertel reduzieren.

**Aber:** Der Zweck ist jetzt formuliert, und die Grenze ist begründet. Weitere Anforderungen lassen sich prüfen, statt im Zweifel hier zu landen. Das war das eigentliche Problem.

**Wenn der Kontext weiter wächst,** ist der nächste Schnitt vorgezeichnet: Reservierung (vor der Ausgabe) und Durchführung (Ausgabe bis Abschluss) sind zwei unterscheidbare Phasen mit unterschiedlicher Sprache.

---

## 7 · Die Frage des neuen Entwicklers

> „Gehört die Auswertung, welche Zusatzleistungen sich lohnen, in diesen Kontext?"

**Antwort anhand des Canvas:**

Der Zweck lautet: Verantwortung für den Mietvorgang von der Reservierung bis zum Abschluss.

Eine Auswertung über die Rentabilität von Zusatzleistungen betrifft keinen einzelnen Vorgang. Sie dient der Entscheidung, welche Zusatzleistungen angeboten und wie sie bepreist werden — das ist Vertragsverwaltung, konsistent mit der Entscheidung zu Aufgabe 8.

**Bemerkenswert:** Diese Frage war eine der drei, die bei der Quartalsplanung nicht zugeordnet werden konnten. Mit dem Canvas ist sie in zwei Sätzen beantwortet.

**Das ist der Test aus AK9** — und er ist bestanden.

---

## Diskussionsanschluss

Der Vorschlag schafft einen neuen Kontext „Fahrerprüfung" für eine einzige Aufgabe. Ist das gerechtfertigt, oder ist ein Kontext mit einer Aufgabe ein Zeichen dafür, dass man zu fein schneidet?
