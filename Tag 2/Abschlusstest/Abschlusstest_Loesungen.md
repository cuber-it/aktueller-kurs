# Abschlusstest · Lösungen

**40 Fragen · je 1 Punkt**

| Punkte | Bewertung |
|---|---|
| 36–40 | sehr sicher |
| 30–35 | sicher |
| 24–29 | Grundlagen sitzen |
| unter 24 | Wiederholung empfohlen |

---

## Teil A · Grundlagen und Modell

**1.** Richtig: **c)** Was das Unternehmen fachlich tut

*Einheit 1-1.* Der Problemraum beschreibt, was das Unternehmen fachlich tut. Der Lösungsraum beschreibt, wie die Software geschnitten ist.

**2.** Richtig: **c)** DDD trifft keine Aussage über Verteilung

*Einheit 1-1.* DDD trifft keine Aussage über Verteilung. Bounded Contexts können in einem Monolithen liegen; das Buch von 2003 kennt keine Microservices.

**3.** Richtig: **d)** Es ist eine Auswahl für einen bestimmten Zweck

*Einheit 1-2.* Ein Modell ist eine Auswahl für einen Zweck. Was weggelassen wird, gehört zur Modellentscheidung.

**4.** Richtig: **c)** Er erhebt Daten statt Entscheidungen

*Einheit 1-2.* Wer nach Daten fragt, bekommt Formulare und Listen. Daraus entsteht ein Datenbestand, kein Modell. Zu fragen wäre nach Entscheidungen.

**5.** Richtig: **a)** Welche Entscheidungen treffen Sie?

*Einheit 1-2.* Die drei Fragen lauten: Welche Entscheidungen treffen Sie? Woran machen Sie sie fest? Was passiert, wenn Sie falsch entscheiden?

**6.** Richtig: **b)** Das Modell bedient mehrere Zwecke zugleich

*Einheit 1-2.* Viele Merkmale, wenige gefüllt — jedes Merkmal gehört einem anderen Zweck. Das Modell bedient mehrere Zwecke und wird für jeden schlechter.

---

## Teil B · Sprache und Grenzen

**7.** Richtig: **b)** Innerhalb eines Bounded Context

*Einheit 1-3.* Die Ubiquitous Language gilt innerhalb eines Bounded Context. Über Grenzen hinweg gibt es keine gemeinsame Sprache.

**8.** Richtig: **c)** Es fällt niemandem auf

*Einheit 1-3.* Zwei Wörter für eine Sache fallen beim Lesen auf. Ein Wort für zwei Sachen nicht — beide Seiten glauben sich verstanden zu haben. Der Fehler zeigt sich erst beim Zusammenführen.

**9.** Richtig: **a)** Dieselbe Sache, zwei Sichten

*Einheit 1-3.* Unterschiedliche Detailtiefe ergibt eine Vereinigungsmenge, keinen Widerspruch. Das ist dieselbe Sache in zwei Sichten und rechtfertigt keine Grenze.

**10.** Richtig: **c)** Ein Widerspruch — Kontextgrenze

*Einheit 1-3.* 1 gegen 340 ist ein Widerspruch — dieselbe Frage hat zwei unvereinbare Antworten. Das ist der Prüfstein für eine Kontextgrenze.

**11.** Richtig: **b)** Die Bedeutungen folgen aus der Arbeit

*Einheit 1-3.* Die Bedeutungen folgen aus der Arbeit und sind nicht verhandelbar. Ein Kompromiss zwingt mindestens zwei Bereiche zu einem Hilfsbegriff, der dann nicht verwendet wird.

**12.** Richtig: **d)** Er dokumentiert die Mehrdeutigkeit

*Einheit 1-4.* Ein Eintrag mit „je nach Kontext" dokumentiert die Mehrdeutigkeit, statt sie auszuschließen. Eindeutigkeit ist nur innerhalb eines Kontextes möglich.

**13.** Richtig: **a)** Die Abgrenzung zu Verwandtem

*Einheit 1-4.* Die Abgrenzung — „nicht zu verwechseln mit …" — verhindert mehr Fehler als jede sorgfältige Definition.

**14.** Richtig: **d)** Es liegt nicht am Ort der Arbeit

*Einheit 1-4.* Elf Zugriffe in acht Monaten sind ein Ortsproblem, kein Inhaltsproblem. Ein Glossar gehört dorthin, wo gearbeitet wird.

**15.** Richtig: **d)** Verantwortet den Mietvorgang bis zum Abschluss

*Einheit 1-5.* Ein Zwecksatz nennt ein fachliches Ergebnis, hat kein „und" und keine Ortsangabe. Vor allem muss er etwas ausschließen können.

**16.** Richtig: **a)** Ändert sie sich mit dem Übrigen?

*Einheit 1-5.* Die Prüffrage lautet: Würde eine Änderung an dieser Aufgabe auch die übrigen Aufgaben betreffen? Ort, Empfänger und Historie sind schwache oder gar keine Kriterien.

**17.** Richtig: **d)** Die Abgrenzung

*Einheit 1-5.* Das Feld „nicht zuständig für" begrenzt das Wachstum. Ohne Abgrenzung ist im Zweifel der Kontext zuständig.

---

## Teil C · Subdomains und Beziehungen

**18.** Richtig: **a)** Wettbewerber können sie nicht

*Einheit 1-6.* Core Domain heißt: Ein Wettbewerber könnte es nicht einfach nachmachen. Datenmenge, Nutzerzahl und Kompliziertheit sind keine Kriterien.

**19.** Richtig: **c)** Der Aufwand liegt am falschen Ort

*Einheit 1-6.* Die Core Domain wurde zugekauft, eine Generic Subdomain selbst gebaut. Genau verkehrt herum investiert.

**20.** Richtig: **a)** Es verarbeitet den gesamten Umsatz

*Einheit 1-6.* Umsatzanteil ist kein Kriterium — die Buchhaltung verarbeitet den gesamten Umsatz und unterscheidet niemanden.

**21.** Richtig: **d)** Der Sonderfall wurde nicht abgetrennt

*Einheit 1-6.* Ein Sonderfall zog einen ganzen Generic-Bereich in die Eigenentwicklung. Richtig wäre, den Sonderfall abzutrennen und den Rest als Standard zu nehmen.

**22.** Richtig: **a)** Standard nehmen und nicht anpassen

*Einheit 1-6.* Standard nehmen und nicht anpassen. Ein stark angepasstes Standardprodukt hat Lizenzkosten und Entwicklungsaufwand.

**23.** Richtig: **b)** wer nachziehen muss

*Einheit 1-7.* Eine Context Map zeigt die Abhängigkeitsrichtung — wer nachziehen muss. Diese kann der Datenrichtung entgegengesetzt sein.

**24.** Richtig: **d)** Conformist

*Einheit 1-7.* Kein Einfluss und keine Übersetzung: Conformist. Mit Übersetzung an der Grenze wäre es ein Anticorruption Layer.

**25.** Richtig: **b)** Gekoppelte Releases und Abstimmung

*Einheit 1-7.* Shared Kernel bedeutet Abstimmung bei jeder Änderung und gekoppelte Releases. Der langsamere Kontext bestimmt das Tempo für beide.

**26.** Richtig: **c)** Eine Übersetzung an der Grenze

*Einheit 1-7.* Das Fremdformat ist über die Anbindung hinaus gewandert. Ein Anticorruption Layer hätte die Auswirkung auf eine Stelle begrenzt.

---

## Teil D · Bausteine

**27.** Richtig: **b)** Entity

*Einheit 2-2.* Etwas, das dieselbe Sache bleibt, obwohl sich alle Merkmale ändern, hat Identität über die Zeit — eine Entity.

**28.** Richtig: **a)** Muss es dasselbe sein?

*Einheit 2-2.* Die Prüffrage: Interessiert es, ob es dasselbe ist, oder nur, ob es gleich ist? Speicherbedarf und Wichtigkeit entscheiden nichts.

**29.** Richtig: **d)** Die Zuordnung trägt die Geschichte

*Einheit 2-2.* Wenn ein Wert eine Geschichte zu brauchen scheint, trägt meist die Zuordnung die Geschichte: nicht „die Anschrift gilt bis", sondern „der Kunde verwendet sie bis".

**30.** Richtig: **b)** Eine Regel muss sofort gelten

*Einheit 2-3.* Ohne Invariante kein Aggregate. Sachliche Zusammengehörigkeit, gemeinsame Anzeige und gemeinsame Ablage sind keine Regeln.

**31.** Richtig: **c)** Vorgänge behindern sich gegenseitig

*Einheit 2-3.* Eine große Klammer wird bei jeder Änderung als Ganzes behandelt. Vorgänge, die nichts miteinander zu tun haben, warten aufeinander.

**32.** Richtig: **a)** Was passiert bei kurzer Abweichung?

*Einheit 2-3.* Die Frage gehört dem Fachbereich gestellt: Was passiert, wenn das kurz nicht zusammenpasst? Die Antwort lautet öfter „nichts", als Entwickler erwarten.

**33.** Richtig: **b)** Falsch geschnitten oder Ereignis fehlt

*Einheit 2-3.* Die Faustregel lautet: eine Änderung, eine Klammer. Wer mehrere ändert, hat falsch geschnitten oder braucht ein Ereignis zum Nachziehen.

**34.** Richtig: **c)** Vorgang wurde abgeschlossen

*Einheit 2-4.* Ein Ereignis ist in der Vergangenheit formuliert und fachlich. „Rechnung erstellen" ist ein Command, „Datensatz gespeichert" ist technisch.

**35.** Richtig: **a)** Weil er sonst ständig geändert wird

*Einheit 2-4.* Kennt der Sender seine Empfänger, muss er bei jedem neuen geändert werden — obwohl sich an ihm nichts ändert.

**36.** Richtig: **c)** Zwingend

*Einheit 2-4.* Zwingend heißt: muss ankommen. Sofort heißt: unverzüglich. Die Rechnung ist zwingend, aber nicht sofort.

---

## Teil E · Umsetzung und Ablösung

**37.** Richtig: **b)** Eine fachliche Regel prüfen

*Einheit 2-6.* Ein Application Service steuert den Ablauf: holen, rufen, speichern, melden. Fachliche Regeln gehören ins Modell.

**38.** Richtig: **d)** Die Regel steckt in technischem Ablauf

*Einheit 2-6.* Die Regel steckt zwischen technischen Schritten. Attrappen verkürzen die Vorbereitung, ändern aber nichts daran.

**39.** Richtig: **d)** Nach 30 Tagen ohne Rückfall

*Einheit 2-7.* Ein Kriterium ist überprüfbar, hat einen Zeitpunkt und ist unabhängig von Meinung. Termine und Zufriedenheit erfüllen das nicht.

**40.** Richtig: **b)** in beide Richtungen

*Einheit 2-7.* Solange beide Systeme laufen, muss auch das Neue dem Alten liefern. Die Rückrichtung wird regelmäßig vergessen.

---

## Lösungsfolge zum schnellen Abgleich

`c c d c a b b c a c b d a d d a d a c a d a b d b c b a d b c a b c a c b d d b`

---

## Verteilung

| Antwort | Häufigkeit |
|---|---|
| a | 10 |
| b | 10 |
| c | 10 |
| d | 10 |

Gleichverteilt, keine drei gleichen Antworten hintereinander, keine Längenverzerrung.