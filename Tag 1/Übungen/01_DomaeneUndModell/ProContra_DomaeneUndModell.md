# Pro und Contra · Das fachliche Modell (Modell 2)

Bewertet wird Modell 2 aus der Übung: `Mietvorgang` mit Verhalten, benannten Zuständen und Regeln im Modell.

---

## Pro

**Die fachlichen Vorgänge haben einen Ort**
`ausgeben()`, `verlaengernBis()`, `abschliessen()` — jeder Vorgang ist eine Methode. Die Frage „wo findet eine Verlängerung statt" ist in Sekunden beantwortet statt in elf Tagen.

**Die Regeln stehen dort, wo sie gelten**
„Verlängern nur einmal" steht in `verlaengernBis()`. Es gibt keinen zweiten Ort, an dem sie anders lauten könnte — genau das war die Ursache der drei abweichenden Verlängerungswege.

**Ungültige Zustände sind nicht konstruierbar**
Ein abgeschlossener Vorgang mit unerledigtem Schaden existiert nicht, weil `abschliessen()` ihn verweigert. Das ist eine Zusicherung, keine Absprache.

**Der Fachbereich kann das Modell prüfen**
Alle Begriffe stammen aus dem Gespräch mit der Stationsleiterin. Sie kann sagen „stimmt" oder „bei Firmenkunden geht das zweimal" — ohne Übersetzung.

**Benannte Zustände statt Zahlencodes**
`Laufend` trägt seine Bedeutung mit sich, `statusCode = 2` nicht. Beim Lesen entfällt der Blick in die Dokumentation.

**Es gibt keine Setter für den Zustand**
Der Übergang von `Reserviert` zu `Laufend` ist nur über `ausgeben()` erreichbar. Jeder Weg ins Modell führt durch die Prüfung.

**Die Zahl der mitverantwortlichen Stellen sinkt auf eine**
In Modell 1 muss jeder Aufrufer die Regeln kennen. Hier kennt sie das Modell.

---

## Contra

**Auswertungen werden schwierig**
„Alle Verlängerungen im März nach Station" ist in Modell 1 eine Abfrage. Hier liegen die Daten hinter Methoden. Man braucht ein eigenes Lesemodell — zusätzlicher Aufwand und eine zweite Struktur, die konsistent bleiben muss.

**Berechtigte Korrekturen werden verweigert**
Wenn ein Vorgang fälschlich abgeschlossen wurde, lässt er sich in Modell 1 richtigstellen. Modell 2 verweigert den Zustand — auch wenn die Korrektur richtig ist. Es braucht einen eigenen Weg dafür, der leicht zur Hintertür wird.

**Datenmigration und Import passen nicht**
Altdaten erfüllen die heutigen Regeln oft nicht. Ein Modell, das sich wehrt, lehnt sie ab. Für den Import braucht es eine Umgehung — und damit eine Stelle, an der die Regeln nicht gelten.

**Die Historie fehlt**
Modell 1 hat `FahrzeugStatusHistorie` und `PreisHistorie`. Modell 2 kennt nur den aktuellen Zustand. Wer den Verlauf braucht, muss ihn ergänzen.

**Der Umbau ist erheblich**
61 Klassen, fünfzehn Jahre Datenbestand. Der Weg vom einen zum anderen Modell ist kein Refactoring, sondern ein Projekt. Der Nutzen zeigt sich erst danach.

**Es ist mehr Code**
Methoden statt Getter, Prüfungen statt Vertrauen. Für ein System, das selten geändert wird, ist das Aufwand ohne Gegenwert.

**Nicht jede Klasse braucht Verhalten**
Wo keine Regeln gelten, ist eine Datenklasse angemessen. Wer das Prinzip überall durchzieht, baut Methoden für nichts.

---

## Bewertung

Der Fall trägt das fachliche Modell, weil **Regeln gelten, die verletzt wurden** — drei Verlängerungswege mit drei Auslegungen, ein Fehler, der vier Monate unbemerkt blieb. Der Schaden ist eingetreten, und die Ursache liegt darin, dass die Regeln keinen Ort hatten.

Gegenprobe — *bei Modell 1 bleiben, bleiben Nachteile?* Ja: Jede neue Zugriffsstelle ist eine neue Gelegenheit, eine Regel anders auszulegen.

**Die Grenzen:**

1. **Das Lesemodell gehört mitgeplant.** Ein fachliches Modell ohne Antwort auf die Auswertungsfrage ist eine halbe Lösung. Die übliche Antwort ist eine getrennte Lesestruktur — das gehört entschieden, bevor umgebaut wird.

2. **Korrektur und Migration brauchen einen benannten Weg.** Wenn es keinen gibt, entsteht eine Umgehung — und die hebelt das Modell aus. Besser ein ausdrücklicher, geprüfter Korrekturweg als eine Hintertür.

3. **Der Umbau ist nicht Gegenstand des Vorschlags.** 61 Klassen umzustellen ist ein Projekt. Realistisch ist ein schrittweiser Weg, bei dem beide Modelle eine Zeit lang nebeneinander bestehen — mit allem, was das an Doppelpflege bedeutet.

---

## Diskussionsfragen

1. Wie beantworten Sie Auswertungsfragen, ohne das Modell aufzuweichen?
2. Wie sieht ein Korrekturweg aus, der kein Schlupfloch ist?
3. Welche Klassen brauchen kein Verhalten — und woran erkennen Sie das?
4. Wie migrieren Sie 61 Klassen, ohne den Betrieb anzuhalten?
5. Wann ist Modell 1 die richtige Wahl?
