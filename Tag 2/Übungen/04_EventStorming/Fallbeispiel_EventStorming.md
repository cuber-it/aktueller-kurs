# Fallbeispiel · Der Workshop, der Interviews ersetzen sollte

**Situationstyp:** Anforderungen werden einzeln erhoben — und niemand merkt, dass sich die Aussagen widersprechen.

---

## Ausgangslage

Derselbe Autovermieter. Ein neues Vorhaben steht an: die **Selbstöffnung** — Mieter sollen ihr Fahrzeug ohne Tresenbesuch übernehmen können.

Das Vorhaben berührt fünf Bereiche: Anmietung, Flotte, Fakturierung, Werkstatt und die Schadensabwicklung.

## Wie es gewachsen ist

Die Anforderungserhebung lief wie immer: Eine Analystin führte Einzelgespräche, eines je Bereich, jeweils neunzig Minuten. Daraus entstand ein Anforderungsdokument von 47 Seiten.

Das Dokument ging in Abstimmung. Alle fünf Bereiche gaben ihr Einverständnis.

Die Umsetzung begann.

## Der Vorfall

Nach elf Wochen, kurz vor der ersten Vorführung, stellte ein Entwickler eine Frage:

> „Wenn der Mieter das Fahrzeug selbst öffnet — wer stellt fest, ob ein Schaden vorhanden ist?"

Die Antworten:

| Bereich | Antwort |
|---|---|
| Anmietung | „Der Mieter. Er macht Fotos vor der Fahrt." |
| Schadensabwicklung | „Niemand. Deshalb wollten wir Selbstöffnung nur für Firmenkunden." |
| Flotte | „Die Station beim nächsten Hofrundgang." |
| Werkstatt | „Das steht doch im Konzept — bei der Rückgabe." |

**Vier Bereiche, vier Antworten.** Jeder hatte sein Einverständnis gegeben.

**Die Ursache:** Im Anforderungsdokument stand auf Seite 19 „Schadensfeststellung erfolgt gemäß bestehendem Verfahren". Jeder Bereich las das als sein eigenes Verfahren.

**Die Folge:** Sechs Wochen Nacharbeit. Die Selbstöffnung wurde zunächst nur für Firmenkunden freigegeben, weil dort die Haftungsfrage anders geregelt ist.

## Was bei der Aufarbeitung auffiel

**Die Widersprüche standen im Dokument.** Auf Seite 12 hieß es, der Mieter dokumentiere den Zustand; auf Seite 31, die Station prüfe bei Rückgabe. Beide Sätze stammten aus verschiedenen Gesprächen.

**Niemand las das ganze Dokument.** Jeder Bereich prüfte den Abschnitt, der ihn betraf, und stimmte zu.

**Die Bereiche sprachen nie miteinander.** Alle fünf Gespräche fanden einzeln statt, mit einer Woche Abstand.

**Die offenen Fragen waren nirgends festgehalten.** Die Analystin hatte während der Gespräche Unklarheiten notiert — in ihrem eigenen Block. Sie tauchten im Dokument nicht auf, weil ein Anforderungsdokument Anforderungen enthält, keine Zweifel.

**Der zeitliche Ablauf fehlte.** Das Dokument war nach Bereichen gegliedert, nicht nach dem Verlauf einer Anmietung. Dass die Schadensfeststellung an zwei verschiedenen Zeitpunkten beschrieben war, fiel deshalb nicht auf.

## Was bisher versucht wurde

**Ein Review-Termin.** Alle fünf Bereiche wurden eingeladen, das Dokument vorab verschickt. Zwei kamen, drei schickten Vertretungen, die den Stoff nicht kannten. Ergebnis: Zustimmung.

**Eine Anforderungsverfolgung.** Jede Anforderung bekam eine Nummer und einen Verantwortlichen. Verhindert, dass etwas verloren geht — nicht, dass sich zwei widersprechen.

## Diskussionsfragen

1. Alle fünf Bereiche hatten zugestimmt. Warum hat das nichts genützt?
2. Warum ist der Widerspruch in Einzelgesprächen nicht aufgefallen?
3. Was hätte die Gliederung nach Ablauf statt nach Bereichen geändert?
4. Wo haben Sie so etwas?
