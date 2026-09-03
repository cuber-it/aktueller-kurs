# AV-3488 · Anforderungen bereichsübergreifend erheben

**Typ:** Story
**Komponente:** Vorhaben Selbstöffnung
**Priorität:** Hoch
**Verweist auf:** AV-3471 (Selbstöffnung, widersprüchliche Schadensfeststellung, 6 Wochen Nacharbeit)

---

## Story

**Als** Vorhabensverantwortliche
**möchte ich**, dass Widersprüche zwischen Bereichen sichtbar werden, bevor entwickelt wird,
**damit** nicht nach elf Wochen auffällt, dass vier Bereiche vier verschiedene Vorstellungen hatten.

---

## Description

Die Anforderungen zur Selbstöffnung wurden in fünf Einzelgesprächen erhoben, je 90 Minuten, mit einer Woche Abstand. Daraus entstand ein Dokument von 47 Seiten, dem alle fünf Bereiche zustimmten.

**Vorfall AV-3471:** Nach elf Wochen fragte ein Entwickler, wer bei Selbstöffnung den Fahrzeugzustand feststellt.

| Bereich | Antwort |
|---|---|
| Anmietung | der Mieter, per Foto vor der Fahrt |
| Schadensabwicklung | niemand — deshalb nur für Firmenkunden |
| Flotte | die Station beim Hofrundgang |
| Werkstatt | bei der Rückgabe |

**Ursache:** Im Dokument stand „Schadensfeststellung erfolgt gemäß bestehendem Verfahren". Jeder Bereich las das als sein eigenes Verfahren.

**Weitere Befunde:**

- Auf Seite 12 und Seite 31 standen widersprüchliche Aussagen aus verschiedenen Gesprächen
- Jeder Bereich prüfte nur den Abschnitt, der ihn betraf
- Die Bereiche sprachen während der Erhebung nie miteinander
- Offene Fragen der Analystin standen in ihrem Block, nicht im Dokument
- Das Dokument war nach Bereichen gegliedert, nicht nach dem Ablauf

**Folge:** Sechs Wochen Nacharbeit, Freigabe zunächst nur für Firmenkunden.

**Nicht Gegenstand:** Die Selbstöffnung selbst. Es geht um das Vorgehen bei der Erhebung.

## Randbedingungen

- Fünf beteiligte Bereiche, teils an verschiedenen Standorten
- Die Fachvertreter sind für höchstens einen halben Tag am Stück verfügbar
- Ein Review-Termin wurde bereits versucht: zwei kamen, drei schickten Vertretungen
- Eine Anforderungsverfolgung mit Nummern und Verantwortlichen ist vorhanden

## Akzeptanzkriterien

- **AK1** – Die Erhebung findet mit allen beteiligten Bereichen **gleichzeitig** statt.
- **AK2** – Der Ablauf wird zeitlich dargestellt, nicht nach Bereichen gegliedert.
- **AK3** – Widersprüche zwischen Bereichen werden während der Erhebung sichtbar und festgehalten.
- **AK4** – Offene Fragen sind Teil des Ergebnisses, nicht Notizen einzelner Beteiligter.
- **AK5** – Für jeden Schritt im Ablauf ist erkennbar, wer ihn auslöst.
- **AK6** – Lücken im Ablauf werden sichtbar — Schritte, die niemand verantwortet.
- **AK7** – Das Ergebnis ist ohne Nachbereitung lesbar. Es entsteht während der Erhebung, nicht danach.
- **AK8** – Die Erhebung dauert höchstens einen halben Tag.

## Hinweise

Ein weiterer Review-Termin erfüllt AK1 nicht. Der erste Versuch scheiterte daran, dass Vertretungen kamen, die den Stoff nicht kannten — ein Review setzt voraus, dass alle das Dokument gelesen haben.

AK2 zielt auf die Ursache: Widersprüche in einem nach Bereichen gegliederten Dokument stehen auf verschiedenen Seiten und fallen nicht auf.

AK4 ist der Punkt, an dem klassische Anforderungsdokumente scheitern. Sie enthalten Anforderungen, keine Zweifel.

AK7 schließt Verfahren aus, bei denen erst nachbereitet werden muss.

---

## Für den Kurs

Dieses Ticket nennt keine Methode. Arbeiten Sie entlang der Frage:

**Wie wird ein Widerspruch zwischen zwei Bereichen sichtbar, bevor er teuer wird?**

---
---

# Addendum · Was eine gemeinsame Erhebung leistet

## Warum Einzelgespräche Widersprüche verbergen

| Ursache | Wirkung |
|---|---|
| Jeder spricht nur mit der Analystin | zwei Aussagen treffen nie aufeinander |
| Die Analystin übersetzt | ein Widerspruch wird zu zwei Formulierungen |
| Gliederung nach Bereichen | Widersprüche stehen auf verschiedenen Seiten |
| Jeder prüft nur seinen Teil | niemand liest das Ganze |
| „Gemäß bestehendem Verfahren" | jeder liest sein eigenes |

## Was eine gemeinsame Erhebung anders macht

**Alle hören dieselbe Aussage.** Wenn die Anmietung sagt „der Mieter macht Fotos", hört die Schadensabwicklung es — und widerspricht sofort.

**Der Ablauf ordnet.** Ein zeitlicher Verlauf zeigt, wenn derselbe Schritt zweimal auftaucht oder ein Schritt fehlt.

**Zweifel bekommen einen Platz.** Was strittig ist, wird markiert statt geglättet.

## Der Einstieg über das Geschehen

Der didaktische Kern jeder gemeinsamen Erhebung:

> Fragen Sie einen Sachbearbeiter nach seinem Datenmodell — Sie bekommen nichts.
> Fragen Sie ihn, **was passiert** — Sie bekommen alles.

Deshalb beginnt man mit dem, was geschehen ist. Alles andere wird daraus abgeleitet:

| Schritt | Was gesammelt wird |
|---|---|
| 1 | Geschehnisse in der Vergangenheitsform |
| 2 | Ordnung auf einer Zeitachse |
| 3 | Streitpunkte und offene Fragen |
| 4 | Was ein Geschehen auslöst |
| 5 | Wer es auslöst |
| 6 | Wo es verarbeitet wird |

## Die Farbkonvention

Bei Event Storming haben sich Farben eingebürgert. Sie variieren je nach Quelle — wichtig ist die Einheitlichkeit im Raum, nicht die Übereinstimmung mit einem Buch.

| Farbe | Bedeutung |
|---|---|
| orange | Geschehen (Domain Event) |
| blau | Auslöser (Command) |
| gelb, klein | Akteur |
| hellgelb | Aggregate |
| **rot** | **Hotspot — Streit oder offene Frage** |
| grün | was jemand sehen muss, um zu entscheiden |
| rosa | externes System |

## Die Hotspots sind das Ergebnis

Der Punkt, den Anfänger übersehen.

Ein roter Zettel bedeutet: Hier sind sich zwei nicht einig, oder niemand weiß es. Das ist kein Störfall, sondern der eigentliche Ertrag — solche Stellen sind sonst unsichtbar und tauchen erst nach elf Wochen auf.

**Im Fallbeispiel wäre der Hotspot beim ersten Durchlauf entstanden**, sobald jemand das Wort „Schadensfeststellung" an die Wand geklebt hätte.

## Was die Methode nicht leistet

- **Sie ersetzt keinen Entwurf.** Das Ergebnis ist Rohmaterial.
- **Sie entscheidet nichts.** Hotspots werden markiert, nicht aufgelöst.
- **Sie ersetzt nicht den Fachbereich.** Ohne die Leute, die es wissen, ist es eine Entwicklerrunde mit Zetteln.
