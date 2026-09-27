# Pro und Contra · Attribute, Properties und Protokollmethoden statt Getter und Hilfsklassen

Bewertet wird der Vorschlag aus dem Lösungspapier: öffentliche Attribute, eine Property für den Timeout, `__repr__`, `__eq__` und `__hash__` für `TestCase`, Funktionen auf Modulebene statt `StringUtils` und `TimestampFormatter`.

---

## Pro

**Die Regel steht dort, wo der Wert gesetzt wird**
Ein Timeout von 0 wird beim Setzen abgewiesen, auch im Konstruktor. Ein Timeout von 0 fällt beim ersten Testlauf auf, nicht im Nachtlauf.

**Spätere Regeln berühren keine Aufrufer**
Kommt für `retries` eine Obergrenze dazu, wird aus dem Attribut eine Property. Die 214 Aufrufstellen bleiben, wie sie sind.

**Keine Vorleistung für Fälle, die nicht eintreten**
Von 37 Getter/Setter-Paaren hatten 29 nie eine Logik. Mit Attributen entsteht Struktur erst, wenn es eine Regel gibt.

**Python-Werkzeuge verstehen die Objekte**
`print()`, Logging, das Squish-Testprotokoll und Sets verwenden `__repr__`, `__eq__` und `__hash__`. Die Duplikaterkennung funktioniert, das Protokoll ist lesbar.

**Der Umweg über umbenannte Namen entfällt**
Tests setzen einen kurzen Timeout über `TestConfiguration(timeout=5)`. Die elf Zugriffe auf `_TestConfiguration__…` haben keinen Grund mehr.

**Der Code entspricht dem, was Python-Entwickler erwarten**
Neue Kollegen mit Python-Hintergrund müssen keine zweite Konvention lernen.

---

## Contra

**Die Umstellung betrifft 214 Aufrufstellen**
Der Wechsel von `getTimeout()` zu `timeout` ist mechanisch, aber er berührt fast jede Testdatei. Das erzeugt große Diffs und Konflikte mit laufender Arbeit.

**Öffentliche Attribute laden zu direkten Zuweisungen ein**
`config.can_interface = ""` ist jetzt ohne Hürde möglich. Bei einem Setter hätte es wenigstens einen Methodenaufruf gegeben, den man im Review sieht.

**Properties verbergen Logik**
`config.timeout = 0` sieht aus wie eine Zuweisung und wirft eine Exception. Wer Properties nicht kennt, erwartet das nicht.

**Gleichheit ist jetzt eine fachliche Festlegung**
`TestCase` mit gleichem Namen und verschiedenen Tags gilt als gleich. Das war auch vorher so gemeint, hat aber nie gewirkt. Jetzt wirkt es, und Tests, die sich bisher auf zwei Einträge im Set verlassen haben, verhalten sich anders.

**Ein Teil des Teams denkt in Java**
Drei von fünf Entwicklern haben Java-Hintergrund. Für sie wirken Getter vertraut und Properties ungewohnt. Die Umstellung braucht Erklärung, nicht nur einen Commit.

**Modulfunktionen verlieren den Klassennamen als Anker**
`StringUtils.normalize` war in der IDE leicht zu finden. `normalize` allein kann mit anderen Funktionen gleichen Namens kollidieren, wenn nicht über das Modul importiert wird.

---

## Bewertung

Der Fall trägt den Umbau, weil **die übernommene Struktur ihren Zweck in Python nicht erfüllt**: Die Setter prüften nichts, die doppelten Unterstriche schützten nichts, `toString()` und `equals()` wurden nie aufgerufen.

Gegenprobe – *die Getter bleiben, nur mit Validierung ergänzt, bleiben Nachteile?* Ja: `toString()` und `equals()` erreichen Python weiterhin nicht, und jede weitere Regel erfordert, dass man sich an den Setter erinnert. Die elf Tests mit Umweg bleiben ebenfalls bestehen.

**Die Grenzen:**

1. **Die Aufrufstellen sind ein echter Aufwand.** Der Umbau lohnt sich über die Laufzeit der Testsuite, nicht in der Woche der Umstellung. Ein schrittweiser Übergang, bei dem Getter vorübergehend auf Properties verweisen, ist möglich.

2. **Die Gleichheit von `TestCase` ist nicht geklärt.** Der Vorschlag übernimmt „gleicher Name heißt gleich". Ob Tags dazugehören, ist eine fachliche Entscheidung, die das Team treffen sollte.

3. **Properties brauchen eine Teamregel.** Wann eine Property, wann eine Methode, sollte einmal festgelegt werden. Sonst entstehen Properties mit Datei- oder Netzwerkzugriff.

---

## Diskussionsfragen

1. Würden Sie die 214 Aufrufstellen in einem Schritt umstellen oder schrittweise? Was spricht jeweils dafür?
2. Wie verhindern Sie `config.can_interface = ""`, ohne wieder Setter einzuführen – oder müssen Sie das gar nicht?
3. Wer entscheidet, wann zwei Testfälle gleich sind?
4. Welche Regel zu Properties und Methoden würden Sie in den Teamstandard aufnehmen?
5. Gibt es Klassen in Ihrem Code, die nur `@staticmethod` enthalten und trotzdem Klassen bleiben sollten?
