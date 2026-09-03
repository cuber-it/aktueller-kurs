# AV-2104 · Fachliche Vorgänge im Modell auffindbar machen

**Typ:** Story
**Komponente:** Datenmodell / Fachliche Architektur
**Priorität:** Hoch
**Verweist auf:** AV-2088 (Falscher Tagessatz bei Verlängerung, 11 Tage Analyse, eine von drei Stellen übersehen)

---

## Story

**Als** Entwicklerin
**möchte ich** im Modell die Stelle finden, an der ein fachlicher Vorgang stattfindet,
**damit** eine Korrektur nicht elf Tage Analyse braucht und trotzdem eine Stelle übersieht.

---

## Description

Das Modell umfasst **61 Klassen**, die den 61 Tabellen der Datenbank entsprechen. Klassennamen benennen, wo Daten liegen: `MietvertragPosition`, `FahrzeugStatusHistorie`, `KundeKontaktZuordnung`.

**Vorfall AV-2088:** Bei Verlängerungen wurde in bestimmten Fällen ein falscher Tagessatz berechnet. Die Analyse dauerte **elf Tage** — nicht wegen der Berechnung, sondern weil nicht feststellbar war, wo eine Verlängerung im Code stattfindet.

Eine Verlängerung besteht aus Änderungen an fünf Klassen:

| Klasse | Was geschieht |
|---|---|
| MietvertragPosition | neuer Satz |
| MietvertragKopf | Änderung |
| PreisHistorie | Eintrag |
| FahrzeugStatusHistorie | Statusänderung |
| AbrechnungVorschau | Neuberechnung |

**Der Begriff „Verlängerung" kommt im Code nicht vor.** Er existiert im Fachbereich, in der Oberfläche und in den Anforderungen.

Bei der Analyse wurden **drei Stellen** gefunden, an denen verlängert wird — Oberfläche, Partnerschnittstelle, Nachtlauf. Sie taten fachlich Verschiedenes. Die Korrektur erfasste zwei; die dritte fiel vier Monate später auf.

**Weitere Befunde:**

- Die Frage „Ist dieser Vorgang abgeschlossen?" ergibt sich aus vier Feldern in drei Tabellen. Die Regel steht an sechs Stellen in vier Varianten.
- Die Klassen enthalten Getter und Setter. Fachliche Regeln liegen außerhalb.

**Nicht Gegenstand:** Ein Umbau des Datenbankschemas. Es geht um das Modell in der Anwendung.

## Randbedingungen

- 61 Klassen, 1:1 zu Tabellen
- Das Datenbankschema ist normalisiert und fachlich korrekt
- Ein Datenmodell-Diagramm existiert und ist aktuell
- Eine Umbenennungsaktion (`MVP` → `MietvertragPosition`) hat die Lesbarkeit verbessert, aber keine fachliche Frage beantwortbar gemacht

## Akzeptanzkriterien

- **AK1** – Für die fachlichen Vorgänge des Mietgeschäfts existiert im Modell jeweils **eine** Stelle, an der sie stattfinden.
- **AK2** – Die Namen im Modell entsprechen den Begriffen des Fachbereichs. Ein Fachvertreter erkennt sie wieder.
- **AK3** – Fachliche Regeln liegen im Modell, nicht in aufrufendem Code.
- **AK4** – Die Frage „Ist dieser Vorgang abgeschlossen?" wird an genau einer Stelle beantwortet.
- **AK5** – Für jeden Vorgang ist erkennbar, welche Bedingungen gelten müssen, damit er zulässig ist.
- **AK6** – Das Modell ist unabhängig davon beschreibbar, wie die Daten gespeichert werden.
- **AK7** – Ein Entwickler kann anhand einer Anforderung sagen, welche Klasse zu ändern ist.
- **AK8** – Für die drei Verlängerungswege ist festgestellt, worin sie sich fachlich unterschieden und ob das gewollt war.

## Hinweise

Eine Umbenennung erfüllt AK2 nicht allein. `MietvertragPosition` ist lesbarer als `MVP` und trotzdem kein fachlicher Begriff — der Fachbereich spricht von Verlängerungen, nicht von Positionen.

AK6 ist der Kern: Solange das Modell die Tabellenstruktur wiederholt, folgt es der Speicherung statt der Fachlichkeit.

AK1 und AK7 sind der praktische Prüfstein. Wenn beide erfüllt sind, hätte AV-2088 einen Tag gedauert.

---

## Für den Kurs

Dieses Ticket nennt kein Konzept. Arbeiten Sie entlang der Frage:

**Was bildet dieses Modell ab — und was sollte es abbilden?**

---
---

# Addendum · Woran erkennt man ein Modell, das die Fachlichkeit nicht trifft

## Im Code

| Signal | Konkret |
|---|---|
| Klassen entsprechen 1:1 den Tabellen | die Speicherung bestimmt die Struktur |
| Klassennamen enthalten technische Begriffe | `Kopf`, `Position`, `Historie`, `Zuordnung`, `Mapping` |
| Klassen haben nur Getter und Setter | das Modell trägt Daten, kein Verhalten |
| Fachliche Begriffe fehlen im Code | „Verlängerung" existiert überall, nur nicht im Modell |
| Eine Regel steht an mehreren Stellen | weil es keinen Ort dafür gibt |
| Ein Vorgang berührt viele Klassen | ohne dass eine davon der Vorgang ist |
| Ungültige Zustände sind konstruierbar | nichts hindert daran |

## Im Gespräch

| Signal | Beispiel |
|---|---|
| Der Fachbereich erkennt die Begriffe nicht wieder | „Was ist eine Mietvertragsposition?" |
| Entwickler übersetzen bei jedem Gespräch | „Sie meinen die Verlängerung — das ist bei uns ein Positionssatz" |
| Die Frage „wo findet X statt" hat keine kurze Antwort | |
| Einarbeitung besteht darin, das Datenmodell zu lernen | die Fachlichkeit kommt danach, wenn überhaupt |

## Was ein Modell ausmacht

**Ein Modell ist eine Auswahl, kein Abbild.**

Es bildet die Wirklichkeit nicht ab, sondern trifft eine Entscheidung darüber, was für einen bestimmten Zweck wichtig ist. Was weggelassen wird, ist Teil des Modells.

| Ein gutes Modell | Ein schlechtes Modell |
|---|---|
| beantwortet die Fragen, die im Betrieb gestellt werden | beantwortet, wo Daten liegen |
| trägt die Sprache des Fachbereichs | trägt die Sprache der Datenhaltung |
| macht ungültige Zustände unmöglich | erlaubt alles, prüft anderswo |
| hat einen Ort für jeden fachlichen Vorgang | verteilt Vorgänge über Strukturen |
| lässt sich mit dem Fachbereich besprechen | braucht Übersetzung |

**Der Prüfstein:** Kann ein Fachvertreter das Modell lesen und sagen, ob es stimmt?

## Warum Normalisierung nicht hilft

Ein normalisiertes Schema vermeidet Redundanz. Das ist eine Eigenschaft der **Speicherung**, keine der Fachlichkeit.

Beides kann gleichzeitig richtig sein: Das Schema ist sauber normalisiert, und das Modell trifft die Fachlichkeit nicht. Im Ticketfall ist genau das der Befund — der Berater hat gute Arbeit geleistet, für eine andere Frage.
