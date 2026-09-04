# Übung · Event Storming durchführen

Diese Übung wird **gemeinsam** durchgeführt, nicht einzeln bearbeitet. Sie brauchen eine Wand, ein Whiteboard oder ein geteiltes Dokument.

**Gegenstand:** die Selbstöffnung aus dem Fallbeispiel.

---

## Material A · Die Ausgangslage

Mieter sollen ihr Fahrzeug ohne Tresenbesuch übernehmen können.

**Was feststeht:**

- Der Mieter hat vorab reserviert
- Er erhält einen Zugangscode auf sein Mobilgerät
- Das Fahrzeug steht auf einem gekennzeichneten Stellplatz
- Die Rückgabe erfolgt ebenfalls ohne Tresen
- Der Vorgang muss abrechenbar sein

**Was strittig ist:** alles Weitere.

## Material B · Die fünf Bereiche und ihre Sicht

Verteilen Sie die Rollen. Wer eine Rolle übernimmt, vertritt diese Sicht — auch wenn er sie nicht teilt.

### Anmietung

> „Der Mieter macht vor der Fahrt Fotos vom Fahrzeug, das reicht als Zustandsnachweis. Er bestätigt in der App, dass er übernommen hat. Fertig."

### Schadensabwicklung

> „Fotos vom Mieter sind vor Gericht wertlos. Ohne einen Zeugen kann ich keinen Schaden zurechnen. Deshalb: Selbstöffnung nur bei Firmenkunden, da haftet die Firma."

### Flotte

> „Ich muss wissen, wo das Fahrzeug ist. Wenn der Mieter es irgendwo abstellt, brauche ich eine Ortung. Und beim Hofrundgang prüfe ich ohnehin, was da steht."

### Fakturierung

> „Ich brauche einen Abschlusszeitpunkt und den Kilometerstand. Wenn niemand am Tresen steht, wer liest den ab?"

### Werkstatt

> „Mir ist wichtig, dass ein Fahrzeug nicht rausgeht, wenn ein Prüftermin fällig ist. Wer sperrt es dann?"

---

## Ablauf

### Schritt 1 · Geschehnisse sammeln (5 Minuten, still)

Jeder schreibt für sich auf, was bei einer Selbstöffnung **geschieht** — in der Vergangenheitsform.

Beispiele für die Form:

> „Zugangscode wurde versendet"
> „Fahrzeug wurde geöffnet"

**Regeln:**
- Ein Geschehen je Zettel
- Vergangenheitsform
- Nicht diskutieren, nur schreiben

### Schritt 2 · Ordnen (5 Minuten, gemeinsam)

Alle Zettel an die Wand, von links nach rechts nach zeitlichem Ablauf.

**Dabei entstehen:**
- Doppelungen — zusammenschieben
- Lücken — auffallen lassen, nicht sofort füllen
- Widersprüche — noch nicht auflösen

### Schritt 3 · Hotspots markieren (3 Minuten)

Jeder darf rote Zettel setzen, wo:
- zwei Aussagen sich widersprechen
- niemand die Antwort weiß
- jemand ein ungutes Gefühl hat

**Wichtig:** Hotspots werden markiert, nicht diskutiert.

### Schritt 4 · Auslöser ergänzen (5 Minuten)

Vor jedes Geschehen: Was hat es ausgelöst?

> „Zugangscode anfordern" → „Zugangscode wurde versendet"

### Schritt 5 · Akteure ergänzen (3 Minuten)

Wer löst den Auslöser aus? Mieter, Station, System, Fremdsystem?

### Schritt 6 · Aggregate finden (5 Minuten)

Wo werden die Auslöser verarbeitet? Welche Gegenstände tauchen wiederholt auf?

---

## Auswertung

**1.** Wie viele Hotspots sind entstanden? Nennen Sie die drei wichtigsten.

**2.** Ist der Widerspruch aus dem Fallbeispiel aufgetaucht — wer stellt den Fahrzeugzustand fest? An welcher Stelle?

**3.** Gibt es Lücken im Ablauf — Schritte, die niemand verantwortet?

**4.** Welche Geschehnisse haben Sie zunächst als Auslöser formuliert und dann umgestellt? Was ist Ihnen dabei aufgefallen?

**5.** Welche Gegenstände tauchten wiederholt auf? Sind das Aggregate-Kandidaten?

**6.** Vergleichen Sie mit dem Fallbeispiel: Wie lange dauerte Ihr Durchlauf, und wie lange dauerte die Einzelgespräch-Erhebung?

**7.** Was hätte in Einzelgesprächen **nicht** gefunden werden können?

**8.** Nennen Sie zwei Grenzen der Methode, die Ihnen beim Durchlauf aufgefallen sind.

---

## Hinweise zur Bearbeitung

- **Nicht diskutieren, während gesammelt wird.** Wer sofort widerspricht, bekommt die Meinung des Lautesten statt aller Sichten.
- **Hotspots sind erwünscht.** Ein Durchlauf ohne rote Zettel ist meist einer, bei dem niemand ehrlich war.
- **Die Rollen ernst nehmen.** Wer die Schadensabwicklung vertritt, vertritt sie — auch gegen die eigene Überzeugung.
- **Vollständigkeit ist nicht das Ziel.** Ein Big Picture zeigt den Verlauf, nicht jeden Sonderfall.
