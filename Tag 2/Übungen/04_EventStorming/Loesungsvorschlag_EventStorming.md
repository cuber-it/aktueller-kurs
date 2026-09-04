# Lösungsvorschlag · Event Storming durchführen

**Vorbemerkung:** Das Ergebnis eines Event Stormings ist von der Gruppe abhängig. Dieser Vorschlag zeigt ein plausibles Ergebnis und benennt, worauf es ankommt — nicht, was herauskommen muss.

---

## Ein plausibles Ergebnis

### Der Ablauf

```
Reservierung wurde bestätigt
        ↓
Fahrzeug wurde zugeteilt
        ↓
Zugangscode wurde versendet
        ↓
Mieter ist am Stellplatz eingetroffen        [Hotspot: woher wissen wir das?]
        ↓
Fahrzeug wurde geöffnet
        ↓
Zustand wurde festgestellt                   [HOTSPOT: durch wen?]
        ↓
Übernahme wurde bestätigt
        ↓
Fahrzeug wurde bewegt
        ↓
Fahrzeug wurde abgestellt                    [Hotspot: wo? gekennzeichneter Platz?]
        ↓
Rückgabe wurde gemeldet
        ↓
Kilometerstand wurde erfasst                 [HOTSPOT: durch wen?]
        ↓
Zustand wurde erneut festgestellt            [HOTSPOT: durch wen?]
        ↓
Vorgang wurde abgeschlossen
```

### Die Auslöser und Akteure

| Auslöser | Akteur | Führt zu |
|---|---|---|
| Reservierung bestätigen | System (Nachtlauf) | Reservierung wurde bestätigt |
| Fahrzeug zuteilen | Disposition | Fahrzeug wurde zugeteilt |
| Zugangscode anfordern | Mieter | Zugangscode wurde versendet |
| Fahrzeug öffnen | Mieter | Fahrzeug wurde geöffnet |
| Übernahme bestätigen | Mieter | Übernahme wurde bestätigt |
| Rückgabe melden | Mieter | Rückgabe wurde gemeldet |

### Die Aggregate-Kandidaten

| Kandidat | Taucht auf bei |
|---|---|
| Mietvorgang | Reservierung, Übernahme, Abschluss |
| Fahrzeug | Zuteilung, Öffnung, Abstellung |
| Zugangscode | Versand, Nutzung, Ablauf |
| Zustandsfeststellung | zweimal — bei Übernahme und Rückgabe |

---

## 1 · Die wichtigsten Hotspots

| Hotspot | Warum er entsteht |
|---|---|
| **Wer stellt den Zustand fest?** | Vier Bereiche, vier Antworten — der Fall aus dem Fallbeispiel |
| **Wer liest den Kilometerstand ab?** | Die Fakturierung braucht ihn, am Tresen steht niemand |
| **Wer sperrt ein Fahrzeug mit fälligem Prüftermin?** | Die Werkstatt fragt danach; im Ablauf gibt es keinen Schritt dafür |

**Weitere, die typischerweise entstehen:**

- Woher weiß das System, dass der Mieter am Stellplatz ist?
- Was passiert, wenn der Zugangscode nicht ankommt?
- Wo darf abgestellt werden — nur am Ausgangsort?
- Was, wenn der Mieter das Fahrzeug nicht abholt?

---

## 2 · Der Widerspruch aus dem Fallbeispiel

**Er taucht auf, sobald jemand „Zustand wurde festgestellt" an die Wand klebt.**

Der Ablauf ist der Grund: In einem zeitlich geordneten Verlauf **muss** jemand sagen, wann die Feststellung geschieht. Und sobald das dasteht, fragt jemand, wer es tut.

**Das ist der Unterschied zu Einzelgesprächen.** Dort sagte jeder Bereich seinen Satz, und die Analystin schrieb ihn an die Stelle, die zu ihrem Bereichskapitel passte. Vier Sätze, vier Kapitel, kein Zusammentreffen.

**Bemerkenswert:** Der Hotspot entsteht **zweimal** — bei Übernahme und bei Rückgabe. Im ursprünglichen Dokument standen genau diese beiden Stellen auf Seite 12 und Seite 31.

---

## 3 · Lücken im Ablauf

Typische Funde:

| Lücke | Was fehlt |
|---|---|
| Prüftermin-Sperre | Die Werkstatt braucht sie, im Ablauf gibt es keinen Schritt |
| Kilometerstand-Erfassung | Steht im Ablauf, aber ohne Akteur |
| Nicht abgeholtes Fahrzeug | Der Ablauf endet nicht — was geschieht nach Ablauf der Reservierung? |
| Fehlgeschlagene Öffnung | Was, wenn das Fahrzeug sich nicht öffnen lässt? |

**Die Lücken sind der zweite Ertrag** neben den Hotspots. Sie fallen auf, weil ein zeitlicher Ablauf keine Sprünge verträgt — im Gegensatz zu einem nach Bereichen gegliederten Dokument.

---

## 4 · Umgestellte Formulierungen

Erfahrungsgemäß werden diese zunächst als Geschehen geschrieben und sind Auslöser:

| Zuerst geschrieben | Tatsächlich |
|---|---|
| „Zugangscode versenden" | Auslöser → „Zugangscode wurde versendet" |
| „Fahrzeug öffnen" | Auslöser → „Fahrzeug wurde geöffnet" |
| „Zustand prüfen" | Auslöser → „Zustand wurde festgestellt" |

**Was dabei auffällt:** Bei „Zustand prüfen" fehlt der Akteur — und genau das ist der Hotspot. Ein Auslöser ohne Akteur ist immer eine offene Frage.

**Das ist ein übertragbarer Befund:** Wer einen Auslöser formuliert und keinen Akteur benennen kann, hat eine Lücke gefunden.

---

## 5 · Die Aggregate-Kandidaten

| Kandidat | Bewertung |
|---|---|
| Mietvorgang | eindeutig — taucht über den ganzen Ablauf auf |
| Fahrzeug | eindeutig |
| Zugangscode | **neu** — war in der bisherigen Planung nicht vorgesehen |
| Zustandsfeststellung | **neu** — und der Grund, warum der Hotspot entsteht |

**Der Zugangscode als eigener Gegenstand** ist ein Fund: Er hat einen Lebenszyklus (versendet, genutzt, abgelaufen) und eigene Regeln (nur einmal nutzbar, zeitlich begrenzt). In den Einzelgesprächen tauchte er nur als Merkmal auf.

**Die Zustandsfeststellung als Gegenstand** löst den Hotspot auf: Wenn sie ein eigenes Ding ist, muss sie einen Urheber haben. Die Frage „wer" ist dann nicht mehr umgehbar.

---

## 6 · Der Zeitvergleich

| | Einzelgespräche | Event Storming |
|---|---|---|
| Dauer der Erhebung | 5 × 90 min über fünf Wochen | ein halber Tag |
| Nachbereitung | 47-seitiges Dokument | Fotos der Wand |
| Bis zum Widerspruch | 11 Wochen | in der ersten Stunde |
| Nacharbeit | 6 Wochen | — |

**Der Vergleich ist nicht ganz fair:** Ein Event Storming liefert kein Anforderungsdokument. Wer eines braucht, muss es danach schreiben.

**Aber:** Er schreibt es dann auf Grundlage eines geklärten Ablaufs statt auf Grundlage von fünf Einzelaussagen.

---

## 7 · Was in Einzelgesprächen nicht gefunden werden kann

**Widersprüche zwischen Aussagen.** Sie treffen nie aufeinander. Jeder Satz ist für sich richtig; erst nebeneinander fällt der Konflikt auf.

**Lücken im Verlauf.** Ein Gespräch mit der Werkstatt ergibt Werkstattanforderungen — nicht die Erkenntnis, dass zwischen Zuteilung und Öffnung ein Schritt fehlt.

**Die Reihenfolge der Schritte.** Jeder Bereich kennt seinen Ausschnitt. Dass die Zustandsfeststellung an zwei verschiedenen Stellen beschrieben wird, sieht nur, wer beide sieht.

**Gegenstände, die niemand erwähnt.** Der Zugangscode kam in keinem Gespräch als eigenständige Sache vor — er entstand, als jemand fragte, was zwischen Versand und Öffnung geschieht.

**Der gemeinsame Wortschatz.** Wenn fünf Bereiche gemeinsam an einer Wand stehen, einigen sie sich nebenbei auf Begriffe. In Einzelgesprächen übersetzt die Analystin.

---

## 8 · Grenzen der Methode

**Sie entscheidet nichts.** Am Ende stehen Hotspots an der Wand — die Frage „wer stellt den Zustand fest" ist markiert, nicht beantwortet. Die Entscheidung muss danach getroffen werden, von jemandem, der sie treffen darf.

**Sie braucht die richtigen Leute.** Ohne Fachvertreter ist es eine Entwicklerrunde mit Zetteln. Vertretungen, die den Stoff nicht kennen, machen es schlimmer als Einzelgespräche — weil ihre Aussagen wie belastbare gelten.

**Das Ergebnis ist flüchtig.** Eine Wand voller Zettel überlebt selten mehr als ein paar Tage. Was nicht abfotografiert und übertragen wird, ist weg.

**Sie skaliert nicht beliebig.** Bei mehr als fünfzehn Leuten wird es unübersichtlich, bei weniger als vier fehlen die Sichten, die den Widerspruch erzeugen.

**Sie ist anstrengend.** Ein halber Tag konzentriertes Arbeiten an einer Wand ermüdet. Wer sechs Stunden ansetzt, bekommt in der letzten Stunde nichts Brauchbares mehr.

**Online ist sie geschwächt.** Das gleichzeitige Kleben vieler Hände ist der Kern; mit einem Mauszeiger je Person geht Tempo und Spontaneität verloren.

---

## Diskussionsanschluss

Am Ende stehen zwölf Hotspots an der Wand. Wer entscheidet sie — und was passiert mit denen, die niemand entscheiden will?
