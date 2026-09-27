# Fallbeispiel · Eine Basisklasse für alle Tests

**Situationstyp:** Gemeinsamer Code wird über eine Basisklasse verteilt. Jede Erweiterung erreicht alle Unterklassen, auch die, die sie nicht brauchen.

---

## Ausgangslage

Tests für die Bediensoftware von Terminals laufen nachts auf einem Testrack mit vier Geräten. Drei Teams schreiben Tests: Alarmierung, Section Control, Service. 2016 entstand `BaseTest` mit sechs Methoden: verbinden, trennen, anmelden, auf einen Bildschirm warten, protokollieren, Bericht schreiben.

## Wie es gewachsen ist

Neue Fähigkeiten kamen in `BaseTest`, damit alle sie nutzen können: Screenshots, Testdaten für Anbaugeräte, Zurücksetzen der Gerätedatenbank, ein Exportprüfer für TaskData. Teile wanderten in Mixins, die weiter auf Attribute von `BaseTest` zugreifen. Heute: 46 Methoden, 1.120 Zeilen, 212 Testklassen erben davon und verwenden im Mittel 7 der 46 Methoden.

## Was auffällt

**Ein Default gilt für alle, ohne dass es sichtbar ist.** `wait_for_screen()` hat einen Default-Timeout von 10 s. Alarmbildschirme erscheinen nach 2 s, Section-Control-Wechsel dauern bis zu 8 s. Die Section-Control-Tests setzen den Timeout nie selbst. Wer ihn für die Alarmtests senkt, trifft sie.

**Ein Test legt geerbtes Verhalten still.** `ServiceMenuTest` überschreibt `reset_device_database()` mit `NotImplementedError`. Der Nachtlauf braucht deshalb eine Sonderbehandlung für genau diese Klasse.

**23 Tests belegen Geräte, ohne sie zu brauchen.** Die Exporttests prüfen Dateien, verbinden sich über `setup()` aber mit einem Gerät: etwa 46 Minuten Rackzeit pro Nacht.

**Die Mixins haben unsichtbare Voraussetzungen.** Das Screenshot-Mixin braucht `self.driver` und `self.report_dir`. Vor `setup()` benutzt, bricht es mit `'NoneType' object has no attribute 'save_screenshot'` ab.

## Naheliegende Ansätze

**Den Timeout an jeder Aufrufstelle setzen.** Funktioniert, bedeutet aber 61 Stellen mit demselben Wert.

**`BaseTest` in `DeviceTest`, `ExportTest`, `ServiceTest` aufteilen.** Offen bleibt, auf welche Ebene die Screenshots gehören, weil Geräte- und Exporttests sie brauchen.

## Diskussionsfragen

1. Die Basisklasse war 2016 eine gute Idee. Ab wann war sie keine mehr?
2. Warum wissen die Section-Control-Tests nicht, dass sie den Default-Timeout benutzen?
3. Was sagt die Sonderbehandlung im Nachtlauf über die Beziehung zwischen `ServiceMenuTest` und `BaseTest`?
4. Warum führt die Aufteilung in mehrere Basisklassen zu einer Diskussion über Ebenen?
5. Wo haben Sie so etwas?
