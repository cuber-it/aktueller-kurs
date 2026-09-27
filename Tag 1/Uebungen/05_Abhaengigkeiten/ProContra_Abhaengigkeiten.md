# Pro und Contra · Konstruktorparameter statt selbst beschaffter Kollaborateure

Bewertet wird der Vorschlag aus dem Lösungspapier: Terminal, Dienst für Aufwandmengen und Reporter über den Konstruktor, das Datum als Default-Parameter, die Mengenregel als eigene Funktion mit Werten als Eingabe, Zusammensetzen in `build_application_workflow`.

---

## Pro

**Die Mengenregel ist in Sekunden prüfbar**
Fünf Tests mit Zahlenpaaren, ohne Terminal, Backend und Freigabe. Fehler in der Regel, etwa ein falscher Vergleichswert oder eine falsche Rundung, fallen vor dem Commit auf, nicht im Nachtlauf.

**Was der Workflow braucht, steht in seiner Signatur**
`ApplicationWorkflow(form, rates, reporter)` sagt, womit er zusammenarbeitet. Wer ihn verwendet, muss `execute` nicht lesen.

**Tests brauchen keine Modulpfade**
Die Doubles werden übergeben, nicht per `mock.patch` untergeschoben. Das Verschieben von `environment` in ein Paket berührt keinen Test.

**Kein geteilter Zustand zwischen Tests**
Das Singleton entfällt. Jeder Test erzeugt seine eigenen Objekte, niemand muss etwas zurücksetzen.

**Die Konfiguration hat einen Ort**
`CONFIG` wird nur in `build_application_workflow` gelesen. Kommt ein zweiter Prüfstand mit anderer Konfiguration, ändert sich eine Funktion.

**Der Workflow hängt nur von drei Operationen des Terminals ab**
Der Vertrag `TaskForm` ist schmal. Ändert sich am Terminal-Client etwas, das der Workflow nicht verwendet, betrifft es ihn nicht.

**Kein Framework**
Konstruktorparameter und ein `Protocol` aus der Standardbibliothek genügen. AK7 ist ohne Aufwand erfüllt.

---

## Contra

**Jede Stelle, die einen Workflow braucht, muss ihn zusammensetzen**
Bisher genügte `ApplicationWorkflow()`. Jetzt braucht es `build_application_workflow()` oder drei Argumente. Bei 74 Tests, die den Workflow verwenden, ist das eine sichtbare Umstellung.

**Die Protocols sind zusätzliche Konzepte**
`TaskForm`, `RateSource` und `ResultReporter` sind drei neue Namen. Ohne Typprüfung im Build dokumentieren sie nur, sie erzwingen nichts.

**Der Default für das Datum ist eine Ausnahme von der eigenen Regel**
Für den Reporter wird ein Default abgelehnt, für das Datum akzeptiert. Die Unterscheidung „harmloser Standard" ist nachvollziehbar, muss aber im Team erklärt und durchgehalten werden.

**Stubs können vom echten Verhalten abweichen**
`StubTaskForm` liefert eine Menge als `Decimal`. Liefert der echte Terminal-Client einen String wie `"196,00 l"`, ist der Test grün und der Prüfstand rot. Die Doubles prüfen den Workflow, nicht den Vertrag zum Terminal.

**Die Umstellung trifft nur einen von vielen Workflows**
Freischaltung, Anbaugerät und Feldgrenzen-Import folgen weiterhin dem alten Muster. Zwei Stile nebeneinander sind eine eigene Last.

**`build_application_workflow` ist neuer Code ohne Test**
Die Stelle, an der zusammengesetzt wird, läuft nur auf dem Prüfstand. Ein Fehler dort fällt wieder erst im Nachtlauf auf, allerdings sofort und für alle 74 Tests gleichzeitig.

---

## Bewertung

Der Fall trägt den Umbau, weil **eine fachliche Regel in einem Ablauf mit drei externen Ressourcen gefangen war**. Das Herauslösen der Regel allein hätte AK1 erfüllt. Die Konstruktorparameter erfüllen zusätzlich AK2 bis AK5 und machen den Workflow selbst prüfbar.

Gegenprobe – *nur die Regel herauslösen, den Workflow lassen, bleiben Nachteile?* Ja: Die Regel wäre prüfbar, das Zusammenspiel von Anzeige, Vergleich und Meldung weiterhin nur auf dem Prüfstand. Das Singleton und die Kopplung an `CONFIG` blieben.

**Die Grenzen:**

1. **Der Vertrag zum Terminal ist nicht geprüft.** Ob `TerminalClient.read_volume` ein `Decimal` liefert, zeigen die Stubs nicht. Dafür braucht es mindestens einen Test auf dem Prüfstand.

2. **Der Mengensprung an der Schwelle ist ungeklärt.** Bei 9,99 ha und 20 l/ha erwartet die Regel 199,80 l, bei 10 ha 196,00 l. Die Tests halten das fest, entscheiden muss die Applikationstechnik.

3. **Nur ein Workflow ist umgestellt.** Ob die übrigen demselben Muster folgen sollen, ist eine Teamentscheidung.

---

## Diskussionsfragen

1. Würden Sie alle Workflows umstellen oder nur die, deren Regeln sich ändern?
2. Wer testet `build_application_workflow`, und wie?
3. Sollen die Protocols per Typprüfung im Build erzwungen werden?
4. Wann ist ein Default-Parameter für Sie vertretbar? Formulieren Sie eine Regel.
5. Welche Abhängigkeiten in Ihrer Testsuite sollen bewusst konkret bleiben?
