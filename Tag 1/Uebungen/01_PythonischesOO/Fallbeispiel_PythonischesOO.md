# Fallbeispiel · Getter und Setter aus Java

**Situationstyp:** Konventionen einer anderen Sprache wurden übernommen. Sie versprechen einen Schutz, den sie in Python nicht liefern.

---

## Ausgangslage

Ein Testframework für die Oberfläche von Terminals für Landmaschinen entstand ab 2012 in Java und wurde 2019 nach Python übertragen, weil das GUI-Testwerkzeug Python als Skriptsprache anbietet. Die Übertragung erfolgte Klasse für Klasse mit denselben Methoden und derselben Struktur.

## Wie es gewachsen ist

Aus `private int timeout` mit `getTimeout()` und `setTimeout()` wurde `self.__timeout` mit denselben Methoden. Aus `StringUtils` mit statischen Methoden wurde eine Klasse mit `@staticmethod`, aus `toString()` und `equals()` Methoden mit denselben Namen. Neuer Code übernahm den Stil. Das Konfigurationsmodul enthält heute 37 Getter/Setter-Paare, 29 davon ohne eigene Logik.

## Was auffällt

**Die Setter prüfen nichts.** Sie wurden eingeführt, „damit später Validierung eingebaut werden kann“. Bei keinem der 29 logikfreien Paare ist das geschehen. Ein Timeout von 0 wird ohne Einwand übernommen.

**Die doppelten Unterstriche schützen nichts.** Elf Tests greifen über `config._TestConfiguration__timeout` direkt auf Felder zu, um Werte zu setzen, die kein Setter vorsieht.

**`toString()` wird nie aufgerufen.** Python verwendet für `print()`, Logging und Fehlermeldungen `__str__` und `__repr__`. Im Protokoll erscheinen Testfälle als `<configuration.TestCase object at 0x7f3a…>`.

**`equals()` wird von `==` nicht verwendet.** Eine Duplikaterkennung mit `==` findet keine Duplikate. Drei Tests sind doppelt registriert.

## Naheliegende Ansätze

**Eine Review-Regel „keine direkten Zugriffe auf Felder“.** Die elf Tests bleiben, weil es für ihren Zweck keinen anderen Weg gibt.

**Validierung im Setter nachrüsten.** Tests, die den umbenannten Namen verwenden, umgehen die Prüfung.

## Diskussionsfragen

1. Die Getter sollten spätere Validierung ermöglichen. Warum wurde sie nie ergänzt?
2. Würde `config.timeout = 0` im Review mehr Aufmerksamkeit bekommen als `setTimeout(0)`?
3. Warum fällt nicht auf, dass `equals()` nie aufgerufen wird?
4. Wo haben Sie so etwas?
