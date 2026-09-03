# Lösungsvorschlag · Die Context Map

**Vorbemerkung:** Ein Vorschlag. Bei mehreren Beziehungen sind zwei Muster vertretbar — bewertet wird die Begründung.

---

## 1 und 2 · Die Map

```
        ┌──────────────────┐         ┌──────────────────┐
        │  Partnernetzwerk │         │   Leasingportal  │
        │     (extern)     │         │     (extern)     │
        └────────┬─────────┘         └────────┬─────────┘
                 │ Conformist                 │ Customer/Supplier
                 │ (ohne Grenze!)             │
                 ▼                            ▼
        ┌──────────────────┐         ┌──────────────────────────┐
        │  Vertragsver-    │  C/S    │  Flotte und              │
        │  waltung         │────────▶│  Instandhaltung          │
        └────────┬─────────┘         └──────────┬───────────────┘
                 │ C/S                          │
                 ▼                              │ Shared Kernel
        ┌──────────────────┐◀──────────────────┘
        │    Anmietung     │
        └────────┬─────────┘
                 │ C/S
                 ▼
        ┌──────────────────┐         ┌──────────────────┐
        │   Fakturierung   │◀────────│ Schadensplattform│
        └────────┬─────────┘  Conf.  │     (extern)     │
                 │            + OHS  └──────────────────┘
                 │ Conformist
                 ▼
        ┌──────────────────┐
        │ Zahlungsdienst-  │
        │ leister (extern) │
        └──────────────────┘
```

### Die Beziehungen im Einzelnen

| Von | Nach | Muster | Begründung |
|---|---|---|---|
| Partnernetzwerk → Anmietung u.a. | | **Conformist** | „Auf deren Format haben wir null Einfluss", einer von zweihundert Anbietern |
| Leasingportal ↔ Flotte | | **Customer/Supplier** | „Wenn wir sagen, wir brauchen ein Feld, reden die mit uns. Hat zweimal geklappt" |
| Schadensplattform → Fakturierung | | **Conformist** auf einem **Open Host Service** mit **Published Language** | Verbandsformat, öffentliche Spezifikation, Gremium — der Anbieter bedient viele. Wir nehmen es unverändert |
| Zahlungsdienstleister → Fakturierung | | **Conformist** auf **Published Language** | Standardschnittstelle, die alle Banken so anbieten |
| Vertragsverwaltung → Anmietung | | **Customer/Supplier** | „Die Anmietung sagt mir, wenn eine Regelung nicht funktioniert. Dann passe ich sie an" |
| Anmietung → Fakturierung | | **Customer/Supplier**, schwach | „Ich hab keine Mitsprache, brauche ich auch nicht" — faktisch nahe am Conformist |
| Anmietung ↔ Flotte | | **Shared Kernel** | „Wir arbeiten mit denselben Fahrzeugdaten" |

---

## 3 · Wer zieht nach

| Beziehung | Ändert sich etwas bei… | …muss nachziehen |
|---|---|---|
| Partnernetzwerk | Vermittler | wir, vollständig |
| Leasingportal | beiden | in Absprache, mit Vorlauf |
| Schadensplattform | Gremium | wir |
| Zahlungsdienstleister | Bank | wir |
| Vertragsverwaltung → Anmietung | Vertragsverwaltung | Anmietung |
| Anmietung → Fakturierung | Anmietung | Fakturierung |
| Anmietung ↔ Flotte | **einem von beiden** | **beide, sofort** |

Die letzte Zeile ist die kritische — dazu Aufgabe 4.

---

## 4 · Was Herr Yilmaz beschreibt

> „Das ist eine gemeinsame Sache — wir arbeiten mit denselben Fahrzeugdaten. Wenn die was am Fahrzeugmodell ändern, betrifft uns das sofort."

**Das ist ein Shared Kernel.** Zwei Kontexte teilen sich einen Modellausschnitt — hier die Fahrzeugdaten.

**Der Preis:**

| | |
|---|---|
| Koordination | Jede Änderung am geteilten Teil muss mit dem anderen abgestimmt werden |
| Releases | Beide müssen gemeinsam ausgeliefert werden, sonst passt es nicht |
| Zuständigkeit | Der geteilte Teil gehört keinem allein — Entscheidungen dauern länger |
| Tempo | Der langsamere Kontext bestimmt das Tempo für beide |

**Shared Kernel ist das teuerste Muster im Katalog.** Es lohnt nur, wenn zwei Kontexte fachlich tatsächlich untrennbar sind und die Teams eng zusammenarbeiten.

**Ist es hier gerechtfertigt?** Streitbar. Anmietung und Flotte brauchen beide Fahrzeugdaten, aber Verschiedenes davon: Die Anmietung braucht Verfügbarkeit und Kennzeichen, die Flotte Lebenszyklus und Standort. Das spricht eher für zwei Modelle mit einer Übersetzung.

**Gegenargument:** Der Fahrzeugbestand ändert sich täglich durch Ausgabe und Rückgabe. Eine Übersetzung mit Verzögerung würde die Verfügbarkeitsanzeige unbrauchbar machen. Wer das für zwingend hält, behält den Shared Kernel — bewusst und mit Kenntnis des Preises.

---

## 5 · Wo die Grenze fehlt

Der Partnerstatus wird in **vier** Kontexten ausgewertet. Das bedeutet: Das Modell des Vermittlers ist in vier Kontexte eingedrungen.

**In der Map fehlt eine Grenze zwischen Partnernetzwerk und Anmietung.**

Richtig wäre:

```
   ┌──────────────────┐
   │  Partnernetzwerk │
   └────────┬─────────┘
            │
   ╔════════▼═════════╗
   ║  Anticorruption   ║   ← fehlt
   ║      Layer        ║
   ╚════════┬═════════╝
            ▼
   ┌──────────────────┐
   │    Anmietung     │   ← nur hier, nicht in vier Kontexten
   └──────────────────┘
```

**Die Wirkung eines Anticorruption Layer:** Der Partnerstatus wird an der Grenze in eigene Begriffe übersetzt. Die Anmietung kennt ihren eigenen Vorgangsstatus, nicht den des Vermittlers. Fakturierung, Flotte und Werkstatt sehen das Fremdformat nie.

**Bei der Formatumstellung** wäre eine Stelle betroffen gewesen statt 31.

**Wichtig:** Conformist bleibt die richtige Grundentscheidung — wir haben keinen Einfluss auf das Format. Der Fehler war nicht, es zu übernehmen, sondern es **nicht an der Grenze zu übersetzen**. Conformist und Anticorruption Layer schließen einander nicht aus: Man fügt sich dem Format **und** übersetzt es.

---

## 6 · Zwei Fragen an die Werkstatt

**Frage 1:** „Welche Entscheidung treffen Sie anhand dieses Wertes?"

Zielt darauf, die **fachliche Information** hinter dem technischen Feld zu finden. Vermutlich braucht die Werkstatt nicht den Partnerstatus, sondern etwas, das zufällig darin steckt — etwa ob ein Fahrzeug über einen Vermittler vermietet war, weil sich daraus eine andere Reinigungspflicht ergibt.

**Frage 2:** „Was würden Sie tun, wenn es dieses Feld nicht gäbe?"

Zielt darauf, ob die Auswertung überhaupt gebraucht wird. Bei einer Auswertung, die einmal jemand gebaut hat, ist die Antwort oft „nichts" — dann fällt die Abhängigkeit ersatzlos weg.

**Was nicht funktioniert:** „Warum werten Sie den Partnerstatus aus?" Die Antwort wäre „weil er da ist" oder „das war schon immer so".

---

## 7 · Wechsel des Zahlungsdienstleisters

**Aus der Map ablesbar:** Betroffen ist die **Fakturierung**. Die Beziehung ist Conformist auf einer Standardschnittstelle.

**Warum „kein großer Aufwand" trotzdem falsch sein kann:** Die Map zeigt die Beziehung, aber nicht, ob eine Grenze existiert. Ist das Format der Bank — wie beim Partnernetzwerk — in die Fakturierung durchgesickert, betrifft der Wechsel weit mehr als die Schnittstelle.

**Das ist genau die Frage, die vor dem Wechsel zu klären ist**, und die man beim Partnernetzwerk nicht gestellt hat.

**Was anders sein müsste:** Ein Anticorruption Layer zwischen Zahlungsdienstleister und Fakturierung. Dann ist der Wechsel tatsächlich der Austausch einer Übersetzung.

**Prüfvorschlag:** Volltextsuche nach Begriffen des Anbieters — Feldnamen, Statuscodes, Fehlercodes. Tauchen sie außerhalb der Anbindung auf, ist das Format durchgesickert.

---

## 8 · Die zwei ersten Änderungen

### Erstens: Anticorruption Layer zum Partnernetzwerk

| | |
|---|---|
| Risiko heute | hoch — 18 % der Anmietungen, kein Einfluss auf das Format, weitere Umstellungen angekündigt |
| Aufwand | mittel — die Übersetzung ist zu bauen, die 31 Stellen sind zu bereinigen |
| Warum zuerst | Der Schaden ist eingetreten und wird sich wiederholen |

### Zweitens: Prüfung des Zahlungsdienstleisters

| | |
|---|---|
| Risiko heute | unbekannt — und das ist das Problem |
| Aufwand | gering — es geht zunächst nur um die Feststellung |
| Warum zweitens | Der Wechsel steht an. Eine Fehleinschätzung wiederholt AV-2588 |

**Nicht zuerst: der Shared Kernel.** Er ist teuer, aber er funktioniert, und beide Seiten wissen davon. Ein Umbau wäre aufwendig ohne akuten Anlass.

**Nicht zuerst: Leasingportal und Schadensplattform.** Beim Leasingportal besteht Einfluss und Vorlauf. Bei der Schadensplattform ist das Format durch ein Gremium stabil.

---

## Diskussionsanschluss

Der Vorschlag lässt den Shared Kernel zwischen Anmietung und Flotte bestehen. Wenn das Fahrzeugmodell in zwei Kontexte aufgeteilt würde — wie ginge die Verfügbarkeitsanzeige an der Station dann noch in Echtzeit?
