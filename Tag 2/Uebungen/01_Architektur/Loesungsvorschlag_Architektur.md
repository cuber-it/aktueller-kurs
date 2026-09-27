# Lösungsvorschlag · Wo landet diese Änderung?

**Vorbemerkung:** Ein Vorschlag, keine Musterlösung. Die Grenzen zwischen Schichten lassen sich unterschiedlich ziehen. Bewertet wird, ob jede Schicht **eine benennbare Verantwortung** hat und ob jede Änderung **einem Ort** zugeordnet ist.

---

## 1 · Schichten

| Schicht | Datei / Klasse | Verantwortung |
|---|---|---|
| Testfall | `tst_…/test.py`, `main()` | was geprüft wird und in welcher Reihenfolge |
| Lifecycle | `test_wrapper` | Datensatz, AUT-Verbindung und Aufräumen um jeden Test |
| Helper (Task) | `open_gnss_source_submenu` | ein wiederkehrender Weg durch mehrere Menüs |
| Screen Object | `SubMenuGNSSSource` | welche Controls ein Menü hat und wie sie gefunden werden |
| Control | `Control`, `CheckDelegate` | wie mit Squish gewartet, geklickt und gelesen wird |
| Target | `test_exec_helper.target.helper` | Gerät, Anwendungskontexte, Dateien |
| Verifikation | `UIElementTest` | Wert lesen, vergleichen, Abweichung melden |
| Simulation | `Simulation_Helper` | GPS-Fahrt und Simulations-Docker |

---

## 2 · Wissen im Testfall, das nicht zur Testaussage gehört

- dass nach der GNSS-Quelle das Menü Zugfahrzeug kommt (`traction_unit_title_txt`)
- dass die Diagnose 8 s braucht (`snooze_time=8`)
- wie man die Diagnose verlässt (`back_btn.click_while_exists()`)
- dass `test_wrapper` den Datensatz nicht ersetzen soll (`False` an zweiter Position)

---

## 3 · Was `Control.wait()` außer Warten tut

- wechselt den Application Context auf die Anwendung des Controls
- verbindet die Anwendung neu, wenn Squish ein Null-Objekt liefert
- protokolliert bei Timeout einen FAIL und gibt `None` zurück, statt abzubrechen

Ein Testfall sieht davon nichts. Er sieht nur `click()` oder `get()`.

---

## 4 · Änderungen

| Änderung | betroffen | Schichten |
|---|---|---|
| D1 Real Name | `SubMenuGNSSSource.sae_j1939_btn` | Screen Object |
| D2 Menüstruktur | `open_gnss_source_submenu`, Screen Objects, Testfall (Navigation zurück) | Helper, Screen Object, Testfall |
| D3 Anwendungsname | `ApplicationName`, `MACHINESETTINGS_APP_NAME`, Target-Helper | Konfiguration, Target |
| D4 zweites Target | Target-Helper, Bildvergleiche (Displaygröße) | Target |
| D5 Wartebedingung | `open_gnss_diagnostics_submenu`, Aufrufer mit `snooze_time` | Helper, Testfall |

D1, D3 und D4 bleiben in einer Schicht. D2 und D5 ziehen bis in den Testfall, weil der Testfall Wissen über Navigation und Wartezeit enthält.

---

## 5 · Wer kennt den Real Name?

Im Bestand steht jeder Real Name einmal, im UI-Modul. Prüfbar mit einer Suche nach `itemGnssSourceJ1939` über alle Python-Dateien: eine Fundstelle.

---

## 6 · Wer kennt die Wartezeit?

Heute der Helper (Standard 7 s) und jeder Testfall, der `snooze_time` übergibt. Die neue Bedingung „Satelliten sichtbar“ müsste das Screen Object der Diagnose kennen, weil dort die Anzeige beschrieben ist. Der Helper würde darauf warten, der Testfall nichts mehr davon wissen.

---

## 7 · Kopplung

| Kopplung | Einordnung |
|---|---|
| Control → Squish | notwendig, an einem Ort |
| Screen Object → Real Names | notwendig, an einem Ort |
| Helper → Screen Objects | notwendig, der Weg kennt die Menüs |
| Testfall → Zielmenü beim Zurückgehen | könnte im Screen Object liegen (2-2) |
| Testfall → Wartezeit | könnte im Screen Object oder Helper liegen (2-3) |
| Control → Target-Helper über globales `test_exec_helper` | notwendig in der Sache, versteckt in der Form (Tag 1, 1-5) |

---

## 8 · Beibehalten

- **Kein direkter Squish-Zugriff in Testfällen.** Kein Testfall im aktiven Bestand (983) weicht ab. Eine Änderung am Squish-Verhalten trifft die Control-Schicht, nicht tausend Tests.
- **Real Names an einer Stelle.** D1 ist eine Zeile.

---

## Diskussionsanschluss

Die Übersicht aus diesem Ticket soll an Tag 3 auch Claude Code dienen. Was müsste sie zusätzlich enthalten, damit ein Werkzeug eine Änderung an der richtigen Stelle vornimmt?
