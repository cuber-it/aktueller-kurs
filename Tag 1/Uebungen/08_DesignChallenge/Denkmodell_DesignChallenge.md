# Denkmodell · Gewachsenen Testcode begründet umbauen

Vier Stufen: **Signale → Erkenntnisse → Optionen → Entscheidung.**

---

## Stufe 1 · Signale

### Im Code

| Signal | Beispiel |
|---|---|
| Konfiguration, die sich beim Erzeugen global einträgt | `global test_config` in `__post_init__` |
| Konfiguration, die beim Erzeugen Testdaten liest | `self.test_sets = [...]` in `__post_init__` |
| Aufräumen als Kette in einem `finally` | Sichern, Target-Cleanup, Simulation stoppen nacheinander |
| Veränderliche Vorgabewerte in Datenklassen | `turn_radius: NumValueDTO = NumValueDTO(...)` |
| Konstruktorwerte, die überschrieben werden | `self.data_set = "with_sc_boundary"` |
| Grenzen als Daten, geprüft an anderer Stelle | `NumValueDTO(0, "m", 0, 100)` ohne Prüfung |
| Schalter-Parameter ohne Verwendung | `get_data_value(..., is_bool=False, cast_type=None)` |

### Bei Änderungen

| Signal | Konkret |
|---|---|
| Ein Wert taucht in einem fremden Testsatz auf | `narrow` fährt mit dem Wenderadius von `wide` |
| Ein Fehler erzeugt Folgefehler | 1 echter Fehlschlag, 38 weitere durch eine laufende Simulation |
| Abhängigkeiten, die an keiner Signatur stehen | 64 Aufrufe von `get_test_config()` |
| Ein Umbauversuch wird zurückgenommen, weil ihn niemand überblickt | 19 Klassen, 7 Protocols |

---

## Stufe 2 · Erkenntnisse

**1. Kopplung zeigt sich an Änderungen, nicht am Diagramm.**
Welche Stellen ein Change Request trifft, sagt mehr über einen Entwurf als die Zahl seiner Klassen.

**2. Jede Abstraktion hat einen Preis.**
Sie fügt ein Konzept hinzu, das gelesen, verstanden und gepflegt werden muss. Sie lohnt sich, wenn sie eine konkrete Änderung leichter macht oder einen Fehler verhindert.

**3. Es gibt mehr als einen tragfähigen Entwurf.**
Entwürfe unterscheiden sich in den Annahmen, die sie über die Zukunft machen. Der Vergleich macht diese Annahmen sichtbar.

**4. Aus einer Entscheidung wird erst durch Wiederholung eine Regel.**
Was in einem Entwurf richtig war, ist noch kein Teamstandard. Eine Regel sollte für den ganzen Testcode gelten und begründbar sein.

**Was gesucht wird:** der kleinste Umbau, der die erwarteten Änderungen trägt und die beobachteten Fehler verhindert.

---

## Stufe 3 · Optionen

| Maßnahme | Käme in Frage, wenn |
|---|---|
| **Verantwortung aufteilen** | eine Klasse mehrere unabhängige Änderungsgründe hat |
| **Komposition statt Basisklasse** | die Unterklasse nur Werkzeuge nutzt, keine Typbeziehung besteht |
| **Abhängigkeit übergeben** | ein Kollaborateur im Test ersetzt oder je Umgebung ausgetauscht werden muss |
| **Protocol oder ABC einführen** | mehrere Implementierungen existieren und ein Client den Vertrag benennen soll |
| **Context Manager** | etwas gestartet wird, das auch im Fehlerfall beendet werden muss |
| **Technische Details hinter einer absichtsnahen API bündeln** | technische Namen im Testablauf stehen und sich ändern können |
| **Exception weiterreichen oder übersetzen** | Fehler verschluckt werden oder ihre Ursache verloren geht |
| **Nichts ändern** | kein Change Request und kein beobachteter Fehler die Stelle betrifft |

---

## Stufe 4 · Entscheidung

### Frage 1 — Welche Änderungsursache löse ich gerade?

- **Ein Change Request oder ein beobachteter Fehler ist benennbar** → weiter.
- **Keiner** → nicht umbauen. Umbau ohne Anlass verteilt Code, ohne eine Änderung leichter zu machen.

### Frage 2 — Wo liegt der Hotspot?

Für jeden Change Request die betroffenen Stellen notieren. Stellen, die mehrfach auftauchen, sind die Hotspots.

- **Ein Hotspot** → dort ansetzen.
- **Viele verstreute Stellen, kein Hotspot** → Hinweis auf fehlende Bündelung, etwa technische Namen an vielen Orten.

### Frage 3 — Was ist die kleinste Maßnahme, die den Hotspot auflöst?

Aus Stufe 3 die einfachste Option wählen, die den Change Request trägt. Eine Funktion vor einer Klasse, eine Klasse vor einem Protocol, ein Protocol vor einer Hierarchie.

### Frage 4 — Was wäre schlechter, wenn ich die Abstraktion wieder entferne?

- **Ein Change Request würde schwerer, ein Fehler wieder möglich** → sie bleibt.
- **Nichts Benennbares** → sie wird entfernt.

### Frage 5 — Allgemeine Erkenntnis oder Teamregel?

- **Gilt für den ganzen Testcode und ist begründbar** → Kandidat für das Rule Board, mit Einordnung MUST, SHOULD, MAY oder DON'T.
- **Gilt nur für diesen Fall** → bleibt eine Entwurfsentscheidung.
- **Unklar** → als „noch offen" notieren.

---

## Der Denkweg auf einen Blick

```
Gewachsener Code, eine Änderung steht an
        ↓
Erst markieren: Verantwortung, Abhängigkeit, Zustand,
Vererbung, API, technische Kopplung
        ↓
Welche Änderungsursache?              keine → nicht umbauen
        ↓
Change Requests durchspielen → Hotspots
        ↓
Kleinste Maßnahme, die den Hotspot auflöst
        ↓
Abstraktion wieder entfernen – was wird schlechter?
        ↓ etwas Benennbares            nichts → entfernen
Zweiten Entwurf danebenlegen, Annahmen vergleichen
        ↓
Gilt die Entscheidung für den ganzen Testcode?
        ↓ ja                           nein → Entwurfsentscheidung
                 KANDIDAT FÜR DAS RULE BOARD
```

---

## Die eine Prüffrage

> **Welche Änderung macht dieser Entwurf leichter – und was kostet er dafür?**

Und die Gegenfrage für jede neue Abstraktion:

> **Was wäre schlechter, wenn wir sie wieder entfernen?**

---

## Gegenproben

| Prüfung | Wenn ja, dann |
|---|---|
| Wurde umgebaut, bevor markiert wurde? | Probleme wurden gelöst, bevor sie benannt waren |
| Gibt es eine Klasse, die keinen Change Request trägt? | Kandidat zum Entfernen |
| Gibt es ein Protocol mit genau einer Implementierung und ohne Test-Double? | der Vertrag hat noch keinen zweiten Nutzer |
| Steht `stop()` oder `close()` nach einem `try`-Block? | Aufräumen nur im Erfolgspfad |
| Braucht ein neuer Test Wissen über Objektnamen? | technische Details stehen noch im Testablauf |
| Würde ein neuer Kollege wissen, wo er einen Test beginnt? | wenn nicht, ist der Entwurf zu verteilt |

---

## Wenn die Entscheidung steht

**Referenz zuerst, Rest schrittweise.**
Ein umgebauter Test, an dem sich die übrigen orientieren, ist leichter zu prüfen als 46 umgebaute Klassen auf einmal.

**Den Lifecycle zuerst absichern.**
Folgefehler verfälschen jede weitere Messung. Solange ein Abbruch die Simulation laufen lässt, zeigt der Nachtlauf nicht, ob der Umbau hilft.

**Die verworfene Variante festhalten.**
Warum Entwurf B nicht gewählt wurde, ist eine Information für den Tag, an dem sich die Annahme ändert.

**Regeln erst nach der Entscheidung.**
Das Rule Board sammelt Kandidaten. Welche davon verbindlich werden, entscheidet das Team nach der Challenge, nicht währenddessen.

---

## Verwechslungen, die im Alltag vorkommen

| Verwechselt mit | Erkennungszeichen |
|---|---|
| Refactoring mit Neuschreiben | Refactoring erhält das Verhalten und geht in kleinen Schritten |
| Abstraktion mit Indirektion | eine Indirektion reicht nur weiter, eine Abstraktion verbirgt eine Entscheidung |
| guter Entwurf mit vielen Mustern | bewertet wird die Reaktion auf Änderungen, nicht die Zahl der Techniken |
| Testbarkeit mit Mockbarkeit | testbar heißt, Verhalten isoliert prüfen zu können, nicht jede Klasse zu mocken |
| Teamregel mit Geschmack | eine Regel lässt sich begründen und idealerweise prüfen |
