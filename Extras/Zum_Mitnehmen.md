# Zum Mitnehmen

Zwei Seiten. Das, was nach dem Kurs bleiben soll.

---

## Die Prüffragen

| Wobei | Frage |
|---|---|
| Modell | Kann ein Fachvertreter dieses Modell lesen und sagen, ob es stimmt? |
| Sprache | Führt die Zusammenführung zu einem **Widerspruch** oder nur zu **mehr Feldern**? |
| Glossar | Lässt sich jeder Eintrag eindeutig formulieren — ohne „je nach Kontext"? |
| Kontextgrenze | Würde eine Änderung an dieser Aufgabe auch die **übrigen** Aufgaben betreffen? |
| Subdomain | Wäre ein Wettbewerber mit gleicher Fähigkeit gefährlich — und **können es alle**? |
| Beziehung | Wer muss **nachziehen**, und wie viel **Einfluss** hat er darauf? |
| Entity oder Wert | Interessiert es, ob es **dasselbe** ist — oder nur, ob es **gleich** ist? |
| Aggregate | Muss es im **selben Moment** stimmen? |
| Ereignis | **Berichtet** es oder **fordert** es? |
| Fachlogik | Würde der **Fachbereich** diese Regel kennen? |
| Ablösung | Woran erkennen wir, dass das Neue **trägt**? |

---

## Die Fragen an den Fachbereich

Nicht: „Welche Daten haben Sie?"

> **Welche Entscheidungen treffen Sie?**
> **Woran machen Sie sie fest?**
> **Was passiert, wenn Sie falsch entscheiden?**

Bei Konsistenzfragen:

> **Was passiert, wenn das für fünf Minuten nicht zusammenpasst?**

Bei Ereignissen:

> **Was passiert, wenn diese Meldung nie ankommt?**

Bei unausgesprochener Erfahrung:

> **Woran sehen Sie das?**
> **Bei welchen Fällen lagen Sie zuletzt daneben?**

---

## Die Abgrenzungen

| Paar | Trennfrage |
|---|---|
| Subdomain / Bounded Context | Problemraum oder Lösungsraum? |
| Entity / Value Object | Identität über die Zeit? |
| Aggregate / Entity | Was muss sofort stimmen? |
| Domain Event / Command | Geschehen oder gefordert? |
| Repository / Factory | Holen oder erzeugen? |
| Domain Service / Application Service | Fachlogik oder Ablaufsteuerung? |

---

## Die Beziehungsmuster, hergeleitet

```
Gibt es eine Beziehung?              nein → Separate Ways
        ↓ ja
Ist die Abhaengigkeit gegenseitig?   ja → Shared Kernel / Partnership
        ↓ nein
Einfluss durch Absprache?            ja → Customer / Supplier
        ↓ nein
Wird an der Grenze uebersetzt?       ja → Anticorruption Layer
        ↓ nein
                              Conformist
```

Aus Sicht des Lieferanten: **Open Host Service** und **Published Language**.

---

## Die drei Subdomain-Arten

| Art | Erkennungszeichen | Vorgehen |
|---|---|---|
| **Core** | Wettbewerber können es nicht; steht im Verkaufsgespräch | selbst bauen, beste Leute, laufend |
| **Supporting** | notwendig, branchenüblich, kein Vorteil | sparsam bauen oder zukaufen |
| **Generic** | überall gleich, Standardprodukte vorhanden | Standard nehmen, **nicht anpassen** |

**Kein Kriterium:** Umsatzanteil · Datenmenge · bisheriger Aufwand · Nutzerzahl · Kompliziertheit · gefühlte Wichtigkeit

---

## Die Warnzeichen

**Im Gespräch**

- „Das ist bei uns was anderes" — ein Wort, zwei Bedeutungen
- „Kommt darauf an, wen Sie fragen"
- „Das mache ich aus dem Kopf"
- „Gemäß bestehendem Verfahren" — jeder liest sein eigenes
- „Da war nie Kapazität" bei einem Kernthema

**Im System**

- Ein Begriff mit vielen Merkmalen, die meist leer sind
- Ein Wahrheitswert für einen fachlichen Sachverhalt
- Ein Zahlencode für einen Zustand
- Dieselbe Prüfung an mehreren Stellen
- Eine Regel, die nur mit laufender Umgebung prüfbar ist
- Vorgänge, die aufeinander warten, obwohl sie nichts miteinander zu tun haben

---

## Die Sätze

> Ein Modell ist eine **Auswahl**, kein Abbild.

> Die Bedeutungen sind nicht verhandelbar, weil sie aus der Arbeit folgen.

> Ein Glossar ist nur **innerhalb** eines Kontextes möglich.

> Ohne Abgrenzung wächst ein Kontext, weil im Zweifel er zuständig ist.

> Wichtig und unterscheidend sind **zweierlei**.

> Conformist ist eine **Wahl**, kein Versäumnis.

> Im Zweifel **Wert**.

> Ein Aggregate ist keine Ordnungsübung, sondern eine **Konsistenzentscheidung**.

> Ohne **Invariante** kein Aggregate.

> Der Sender kennt seine **Empfänger nicht**.

> **Zwingend** ist nicht **sofort**.

> Das Modell hängt von **nichts** ab. Alles andere hängt von ihm ab.

> Ein **Datum** ist kein **Kriterium**.

---

## Der erste eigene Schritt

Nicht das ganze System umbauen. Eines davon:

**Einen Begriff prüfen.**
Nehmen Sie ein Wort, das in Ihrem Haus mehrdeutig ist. Fragen Sie in zwei Bereichen, was es bedeutet. Prüfen Sie: Widerspruch oder mehr Felder?

**Eine Regel suchen.**
Nehmen Sie eine fachliche Regel. Fragen Sie: Was muss laufen, damit ich sie einmal ausführen kann? Und: An wie vielen Stellen steht sie?

**Eine Konsistenzfrage stellen.**
Nehmen Sie zwei Dinge, die immer zusammen geändert werden. Fragen Sie den Fachbereich: Was passiert, wenn das für fünf Minuten nicht zusammenpasst?

**Ein Canvas ausfüllen.**
Für den Bereich, in dem Sie arbeiten. Besonders das Feld „nicht zuständig für".

**Eine Aufrufkette ansehen.**
Wo ruft eine Stelle mehrere Empfänger nacheinander auf? Wie viele sind es geworden, und wer steht hinten?

---

## Wenn Sie weiterlesen wollen

Siehe `Literatur.md`.
