# Übung · Pythonisch oder übertragen?

Sie untersuchen Code aus einem Testframework, das aus einer Java-Codebasis nach Python übertragen wurde. Der Code funktioniert. Die Frage ist, welche seiner Strukturen in Python etwas ausdrücken und welche nur mitgebracht wurden.

**Es werden keine Squish-Kenntnisse benötigt.** Der Code ist so reduziert, dass nur die Objektstruktur zählt.

---

## Material A · Die Konfigurationsklasse

```python
class TestConfiguration:
    def __init__(self):
        self.__timeout = 20
        self.__can_interface = "can0"
        self.__retries = 0

    def getTimeout(self):
        return self.__timeout

    def setTimeout(self, timeout):
        self.__timeout = timeout

    def getCanInterface(self):
        return self.__can_interface

    def setCanInterface(self, can_interface):
        self.__can_interface = can_interface

    def getRetries(self):
        return self.__retries

    def setRetries(self, retries):
        self.__retries = retries
```

---

## Material B · Weitere Klassen aus demselben Modul

```python
class TestCase:
    def __init__(self, name, tags):
        self.__name = name
        self.__tags = tags

    def getName(self):
        return self.__name

    def getTags(self):
        return self.__tags

    def toString(self):
        return "TestCase[" + self.__name + "]"

    def equals(self, other):
        return self.__name == other.getName()


class StringUtils:
    @staticmethod
    def normalize(text):
        return " ".join(text.split()).lower()

    @staticmethod
    def is_blank(text):
        return text is None or text.strip() == ""


class TimestampFormatter:
    def format(self, moment):
        return moment.strftime("%Y-%m-%d %H:%M:%S")
```

---

## Material C · So wird der Code verwendet

```python
from datetime import datetime

config = TestConfiguration()
config.setTimeout(config.getTimeout() * 2)

first = TestCase("select_implement", ["smoke"])
second = TestCase("select_implement", ["regression"])

print(first.toString())
if first.equals(second):
    print("duplicate test case")

label = StringUtils.normalize("  Select   Implement ")
stamp = TimestampFormatter().format(datetime.now())


# aus einem Test für den Nachtlauf
def test_short_timeout_for_smoke_run():
    config = TestConfiguration()
    config._TestConfiguration__timeout = 5
    assert config.getTimeout() == 5
```

---

## Material D · Eine neue Anforderung und eine Aussage aus dem Team

Neue Anforderung: **Der Timeout muss zwischen 1 und 300 Sekunden liegen.** Ungültige Werte sollen beim Setzen sofort auffallen.

Aus dem Team, Entwickler mit Java-Hintergrund:

> „Die Getter und Setter haben wir damals eingeführt, damit wir später Validierung einbauen können, ohne alle Aufrufer zu ändern. Und die doppelten Unterstriche machen die Felder privat. Das ist sauberes OO."

---

## Aufgabe

### Teil 1 · Lesen und einordnen

**1.** Legen Sie eine Tabelle an: Welche Konstrukte in Material A und B stammen aus Java- oder C#-Gewohnheiten? Nennen Sie für jedes Konstrukt, welche Absicht dahintersteht.

**2.** Der Test in Material C greift auf `config._TestConfiguration__timeout` zu. Erklären Sie, warum das funktioniert. Was sagt das über die Aussage „die doppelten Unterstriche machen die Felder privat"?

**3.** `StringUtils` und `TimestampFormatter` sind Klassen. Besitzen sie Zustand? Welche Rolle spielt die Klasse jeweils?

### Teil 2 · Pythonisch umbauen

**4.** Schreiben Sie `TestConfiguration` so um, dass die Anforderung aus Material D erfüllt ist. Der Zugriff soll wie ein Attributzugriff aussehen. Welche der drei Einstellungen braucht dafür eine Property, welche nicht?

**5.** Ersetzen Sie `toString()` und `equals()` durch die passenden Python-Protokollmethoden. Was ändert sich dadurch für `print()`, für `==` und für die Verwendung von `TestCase` in einem `set`?

**6.** Bauen Sie `StringUtils` und `TimestampFormatter` so um, wie Sie es in Python schreiben würden. Wie sehen die Aufrufstellen danach aus?

### Teil 3 · Abwägen

**7.** Das Team sagt, die Getter seien eingeführt worden, „damit wir später Validierung einbauen können, ohne alle Aufrufer zu ändern". Prüfen Sie die Aussage an Ihrer Lösung aus Aufgabe 4: Welche Aufrufer hätten sich bei der Property-Variante ändern müssen, als die Validierung dazukam?

**8.** Gibt es Fälle, in denen Sie in Python bewusst eine Methode wie `load_timeout()` statt einer Property schreiben würden? Nennen Sie mindestens zwei Kriterien.

**9.** Ein Scheduler im Framework erwartet „etwas, das man aufrufen kann". In der Java-Fassung gab es dafür ein Interface `Runnable` mit einer Methode `run()`. Wie übergeben Sie in Python die Methode `smoke_suite.run` eines vorhandenen Objekts, ohne ein Interface einzuführen? Was wird dabei übergeben?

---

## Hinweise zur Bearbeitung

- Der Code muss nicht ausgeführt werden. Er sollte aber so geschrieben sein, dass er lauffähig wäre.
- Ändern Sie nur, was sich aus der Aufgabe begründen lässt. Ziel ist nicht der kürzeste Code.
- Wenn Sie unsicher sind, ob eine Struktur bleiben sollte, fragen Sie: **Welches Problem löst sie in Python?**
- Für die Aufgaben 1 bis 3 genügen Stichpunkte.
