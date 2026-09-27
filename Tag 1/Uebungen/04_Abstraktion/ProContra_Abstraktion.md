# Pro und Contra · Kleine Verträge beim Client statt großer Basisklassen

Bewertet wird der Vorschlag aus dem Lösungspapier: ein Protocol `ResultChannel` mit einer Methode statt der ABC `Notifier` mit fünf, ein Protocol `PinInput` mit zwei Methoden für `ServiceUnlockFlow`, `UiDriver` bleibt für Clients, die viele Operationen brauchen, und `ReportRenderer` entfällt, bis ein zweites Format kommt.

---

## Pro

**Jeder Client verlangt, was er aufruft**
`ResultPublisher` braucht `send`, `ServiceUnlockFlow` braucht `type_text` und `click`. Mehr steht in ihren Verträgen nicht.

**Erweiterungen bleiben lokal**
Kommt für den Teams-Kanal `set_priority` hinzu, betrifft das den Teams-Kanal und den Client, der die Priorität setzt. Test-Doubles, die nur `send` liefern und von keiner Basisklasse erben, bleiben unberührt. Heute müssten sieben Test-Doubles angepasst werden.

**Test-Doubles werden klein**
Ein Fake für `ServiceUnlockFlow` hat zwei Methoden statt neun. Der Test zeigt auf einen Blick, welche Interaktion er erwartet.

**Die fremde Klasse passt ohne Adapter**
`VendorChatClient` erfüllt `ResultChannel` strukturell. Der Adapter mit vier leeren Methoden entfällt.

**Die Implementierungsseite bleibt unverändert**
Die Treiberimplementierung des anderen Teams erfüllt `PinInput`, ohne davon zu wissen. Es ist keine Abstimmung zwischen den Teams nötig.

**Weniger Begriffe beim Lesen**
Ohne `ReportRenderer` führt der Weg vom Client direkt zu `HtmlReportRenderer`. Ein Sprung durch eine Abstraktion ohne zweite Implementierung entfällt.

---

## Contra

**Die Zahl der Verträge steigt**
Statt eines `Notifier` gibt es künftig mehrere kleine Protocols, je nach Client. Wer wissen will, was ein Kanal insgesamt können muss, findet keine zentrale Stelle mehr.

**Ohne Type Checker prüft niemand**
Ein Protocol wird zur Laufzeit nicht durchgesetzt. Solange mypy nicht in der CI läuft, fällt eine fehlende Methode erst beim Aufruf auf. Die ABC meldete sie wenigstens beim Instanziieren.

**Die Vollständigkeitsprüfung geht verloren**
Eine Unterklasse von `Notifier`, der eine Methode fehlte, ließ sich nicht erzeugen. Bei den sieben Test-Doubles ist das ein Schaden, in anderen Fällen ein Schutz.

**Strukturelle Übereinstimmung kann zufällig sein**
Jede Klasse mit `send(message: str)` erfüllt `ResultChannel`, auch eine, die etwas völlig anderes sendet. Die ABC verlangte eine ausdrückliche Zugehörigkeit.

**`ReportRenderer` wird vielleicht bald wieder gebraucht**
Wenn in einem halben Jahr JSON-Berichte beauftragt werden, entsteht die Abstraktion erneut, diesmal mit Änderung am Client.

**Die Architekturregel des Teams wird aufgeweicht**
„Jede Komponente bekommt eine ABC" war einfach zu befolgen und zu prüfen. „Jeder Client verlangt, was er braucht" erfordert bei jeder Grenze eine Entscheidung.

---

## Bewertung

Der Fall trägt den Umbau, weil **die Verträge aus Sicht der umfangreichsten Implementierung entworfen waren**: Drei Clients rufen eine von fünf Methoden auf, Test-Doubles implementieren 126 Methoden für 38 Aufrufe, und eine passende fremde Klasse brauchte einen Adapter ohne Verhalten.

Gegenprobe – *`Notifier` bleibt eine ABC, wird aber auf `send` verkleinert, bleiben Nachteile?* Weniger als vorher. Die leeren Rümpfe und der Bruch bei neuen Methoden entfallen weitgehend. Es bleibt der Adapter für die fremde Klasse. Eine kleine ABC wäre eine vertretbare Alternative, wenn das Team Wert auf ausdrückliche Zugehörigkeit legt.

**Die Grenzen:**

1. **Der Vorschlag setzt einen Type Checker voraus.** Ohne mypy oder ein vergleichbares Werkzeug in der CI sind Protocols Dokumentation. Die Aufnahme in die CI gehört zum Umbau, nicht danach.

2. **Kleine Verträge brauchen eine Namenskonvention.** `PinInput`, `ResultChannel`, `PageOutput`: Wenn jeder Client eigene Protocols anlegt, entstehen ähnliche Verträge unter verschiedenen Namen. Das Team sollte festlegen, wo sie liegen und wann ein vorhandener wiederverwendet wird.

3. **Nicht jede ABC ist ein Fehler.** Wo Implementierungen gemeinsamen Code teilen, bleibt die ABC die passende Form. Der Vorschlag betrifft Grenzen, an denen nur ein Vertrag gebraucht wird.

---

## Diskussionsfragen

1. Wo würden Sie die kleinen Protocols ablegen: beim Client, in einem gemeinsamen Modul oder beim Treiber?
2. Soll ein Type Checker in der CI Pflicht werden, bevor Protocols eingeführt werden?
3. Wann ist die zufällige strukturelle Übereinstimmung ein reales Risiko?
4. Wie würden Sie die Architekturregel „jede Komponente bekommt eine ABC" neu formulieren?
5. Welche ABCs in Ihrem Code tragen gemeinsame Implementierung, und welche nur einen Vertrag?
