# TA-224 · GNSS-Tests für das Review durch die Applikationstechnik lesbar machen

**Typ:** Story
**Komponente:** Testfälle Maschineneinstellungen
**Priorität:** Mittel

---

## Story

**Als** Verantwortliche der Applikationstechnik
**möchte ich** aus einem GNSS-Test erkennen, welche Einstellung er vornimmt und was er prüft,
**damit** ich beurteilen kann, ob die Tests die fachlichen Anforderungen abdecken.

---

## Description

Die GNSS-Tests sollen einmal im Quartal von der Applikationstechnik geprüft werden. Das erste Review wurde nach zwei Stunden abgebrochen.

**Bestand:**

| Was | Anzahl |
|---|---|
| GNSS-Testfälle | 14 |
| davon mit direktem Zugriff auf `masetth.submenu_gnss_source.<quelle>_btn` | 11 |
| Zurück-Navigation mit Objekt des Zielmenüs im Test | 14 |
| Aufrufe `test_wrapper(None, False)` mit Positionsargumenten | 9 |

**Befund:** Welche GNSS-Quelle ein Test wählt, ist nur am Attributnamen erkennbar (`masetth.submenu_gnss_source.sae_j1939_btn`). Für ein Review durch die Applikationstechnik, die Python nicht fließend liest, sind die Tests damit kaum auswertbar.

**Befund zur Entstehung:** Fachliche Helper gibt es für Wege (`open_gnss_source_submenu`) und Prüfungen (`assert_gnss_diagnostics_values`), aber nicht für die Einstellung selbst.

**Nicht Gegenstand:** Die Screen Objects und Controls (TA-212, TA-218).

## Randbedingungen

- Die Tests laufen weiter in Squish und verwenden die vorhandenen Screen Objects.
- Die Applikationstechnik liest Python nicht fließend, aber Begriffe wie „GNSS-Quelle“ und „SAE J1939“.
- Fehlermeldungen müssen weiterhin zeigen, welches Control betroffen ist.

## Akzeptanzkriterien

- **AK1** – Ein GNSS-Test nennt die gewählte Quelle als `GnssSource`-Wert.
- **AK2** – Testfälle enthalten keine Controls und keine Menüwege mehr.
- **AK3** – Prüfungen bleiben im Testfall sichtbar.
- **AK4** – Aufrufe von `test_wrapper` verwenden Schlüsselwortargumente.
- **AK5** – Eine Fehlermeldung aus einer fachlichen Operation nennt das betroffene Control.

## Hinweise

Einen Helper `run_gnss_test(source)` zu schreiben, der alles enthält, erfüllt AK3 nicht.

AK5 wird unbequem: Je mehr die Operation verbirgt, desto mehr muss ihre Meldung zeigen.

---

## Für den Kurs

Dieses Ticket nennt keine Lösung. Arbeiten Sie entlang der Frage:

**Welche Information verschwindet, und ist genau diese für den Test wichtig?**

---
---

# Addendum · Woran man die Ebenen eines Tests erkennt

## Ebenen

| Ebene | Beispiel |
|---|---|
| fachliche Absicht | GNSS-Quelle SAE J1939 wählen |
| Navigation | Statusleiste → Einstellungen → Maschine → Traktor → GNSS-Quelle |
| UI-Bedienung | `sae_j1939_btn.set(True)` |
| Infrastruktur | Simulation starten, Datensatz |
| Prüfung | Diagnosewerte mit Referenz vergleichen |

## Was eine fachliche Operation verbergen darf

| gute Kandidaten | Vorsicht bei |
|---|---|
| Menüwege | Assertions |
| Real Names, Controls | Recovery, Wiederholungen |
| Wartezeiten mit fachlichem Grund | Seiteneffekten, die der Test kennen muss |

## Facade, Domain API, Fluent Interface

| Form | kennzeichnend |
|---|---|
| Facade | eine Funktion vereinfacht mehrere Komponenten |
| Domain API | Namen und Parameter in Begriffen der Fachlichkeit |
| Fluent Interface | Aufrufe als Kette; lesbar, aber Zustand und Fehlerort schwerer zu verfolgen |
