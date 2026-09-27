# Pro und Contra · Kollaborateure statt Basisklasse, Vererbung nur für Ergebnistypen

Bewertet wird der Vorschlag aus dem Lösungspapier: Tests erhalten `DeviceSession`, `ScreenWaiter` und `Reporter` als Kollaborateure, die Protokollierung kommt über einen delegierenden `RecordingDriver`, die Ergebnisklassen bleiben eine Vererbungshierarchie mit `RetriedResult` unter `PassedResult`.

---

## Pro

**Jeder Test zeigt, was er benutzt**
Am Konstruktor von `AlarmTest` stehen Session, Warteobjekt und Bericht. Wer wissen will, ob eine Änderung am Warten einen Test betrifft, muss nicht 1.120 Zeilen Basisklasse lesen.

**Eine Änderung trifft nur die Tests, die den Kollaborateur erhalten**
Alarmtests bekommen einen `ScreenWaiter` mit 5 Sekunden, Section-Control-Tests einen mit 10. Eine Änderung des Timeouts für Alarmtests trifft die Section-Control-Tests nicht mehr, und die 61 einzeln gesetzten Timeouts entfallen.

**Tests ohne Gerät belegen kein Gerät**
Die 23 Exporttests erhalten keine `DeviceSession`. Die 46 Minuten Rackbelegung pro Nacht werden frei.

**Der Runner braucht keine Sonderfälle**
Der Reset der Gerätedatenbank ist kein Teil des Runners mehr. `ServiceMenuTest` muss nichts verweigern, die `isinstance`-Prüfung entfällt.

**Die Protokollierung kommt ohne Eingriff in Tests oder Treiber**
`RecordingDriver` legt sich um jeden Treiber, auch um einen späteren Simulator. Eine neue Treibermethode ohne Protokoll fällt durch einen `AttributeError` sofort auf.

**Vererbung bleibt dort, wo sie etwas aussagt**
Die Ergebnisklassen sind eine Typfamilie. Der Bericht zählt über `is_success()` und muss die einzelnen Typen nicht kennen.

---

## Contra

**212 Tests müssen zusammengesetzt werden**
Vorher genügte `class X(BaseTest)`. Jetzt braucht jeder Test eine Stelle, die seine Kollaborateure erzeugt. Ohne eine gemeinsame Fixture oder Fabrik entsteht an vielen Stellen derselbe Aufbaucode.

**Die Werkzeuge sind schwerer zu finden**
Mit der Basisklasse zeigte `self.` in der IDE alle verfügbaren Fähigkeiten. Wer jetzt eine Fähigkeit sucht, muss wissen, welches Objekt sie anbietet.

**Leere Methoden für den Runner**
`ReportExportTest` enthält ein leeres `setup()` und ein leeres `teardown()`. Sie zeigen, dass der Test keinen Lebenszyklus hat, sind aber Code, der nur für den Runner existiert.

**Der Wrapper muss gepflegt werden**
Jede neue Methode am Treiber braucht eine Entsprechung im `RecordingDriver`. Der `AttributeError` macht das sichtbar, aber er tritt im Nachtlauf auf, wenn niemand vorher daran gedacht hat.

**Zwei Welten während der Umstellung**
Die 212 Klassen können nicht in einem Schritt umgestellt werden. Über Monate existieren Tests mit Basisklasse und Tests mit Kollaborateuren nebeneinander, mit zwei Arten, dasselbe zu tun.

**`RetriedResult` unter `PassedResult` ist eine fachliche Festlegung**
Ein Test, der erst im zweiten Versuch besteht, gilt jetzt als bestanden. In einer Umgebung für die Konformitätsprüfung kann genau das umstritten sein.

---

## Bewertung

Der Fall trägt die Trennung, weil **die Testklassen keine Spezialisierungen von `BaseTest` sind**: Sie nutzen im Mittel 7 von 46 Methoden, eine Klasse verweigert geerbtes Verhalten, und der Runner braucht eine Typprüfung.

Gegenprobe – *`BaseTest` wird in mehrere kleinere Basisklassen aufgeteilt, bleiben Nachteile?* Ja: Fähigkeiten wie Screenshots werden von Geräte- und Exporttests gebraucht und passen auf keine einzelne Ebene. Die Diskussion aus dem Fallbeispiel entsteht wieder, und Defaults in einer Zwischenklasse wirken weiter auf alle darunter.

**Die Grenzen:**

1. **Die Zusammensetzung ist ungelöst.** Der Vorschlag zeigt sie für zwei Tests von Hand. Für 212 Tests braucht es eine gemeinsame Stelle, etwa Fixtures. Das ist eigener Aufwand und Thema der Einheit 1-5.

2. **Die Umstellung dauert.** Ein Übergang, bei dem `BaseTest` intern dieselben Kollaborateure verwendet, hält das Verhalten beider Welten gleich, verlängert aber die Zeit, in der zwei Stile nebeneinander bestehen.

3. **Die Bedeutung von „wiederholt bestanden" ist nicht geklärt.** Der Vorschlag ordnet `RetriedResult` unter `PassedResult` ein. Ob das für Konformitätsnachweise gelten darf, muss fachlich entschieden werden.

---

## Diskussionsfragen

1. Wie würden Sie die 212 Tests umstellen: nach Team, nach Fähigkeit oder erst bei der nächsten Änderung eines Tests?
2. Wo entsteht in Ihrer Suite die Zusammensetzung der Kollaborateure, und wer ist dafür zuständig?
3. Ist ein leeres `setup()` ein Zeichen für einen zu großen Runner-Vertrag?
4. Soll ein wiederholt bestandener Test im Bericht als bestanden zählen?
5. Welche Basisklassen in Ihrem Testcode modellieren eine Typfamilie, welche sind Werkzeugkisten?
