# Fallbeispiel · Ein Muster für alles

**Situationstyp:** Ein Architekturmuster wird als Verbesserung für die ganze Suite vorgeschlagen. Ohne Maßstab bleibt die Diskussion bei Geschmack.

---

## Ausgangslage

Ein Squish-Framework mit rund tausend Testfällen: Tests rufen Squish nicht direkt auf, Screen Objects, Controls und Helper tragen die Bedienung. Es gibt zwei Rollen (Fahrer, Service) und einige Tests, die dieselbe Handlung auf zwei Anwendungen ausführen.

## Wie es gewachsen ist

Das Framework entstand schrittweise, jede Schicht aus einem konkreten Problem. Ein Muster wurde nie ausdrücklich gewählt. Screenplay wird in Vorträgen und Artikeln als lesbarer und besser strukturiert vorgestellt, meist an Webanwendungen mit vielen Rollen.

## Was auffällt

**Die typischen Beispiele passen nur teilweise.** Rollen mit unterschiedlichen Rechten spielen dort eine große Rolle, im Framework unterscheiden sich zwei Rollen über eine PIN-Eingabe.

**Wo Screenplay helfen würde, ist benennbar.** Dieselbe Handlung über zwei Anwendungen ist genau der Fall, für den es Fähigkeiten und Aufgaben trennt.

**Ohne Change Cases gibt es keinen Maßstab.** Lesbarkeit und Modernität lassen sich nicht gegeneinander abwägen.

## Naheliegende Ansätze

**Ein Prototyp mit wenigen Tests.** Er zeigt, dass Screenplay funktioniert, nicht, ob es sich lohnt.

## Diskussionsfragen

1. Welche Frage würde die Diskussion entscheiden?
2. Welche Teile von Screenplay gibt es im Framework schon in anderer Form?
3. Wo würde Screenplay konkret helfen?
4. Wo haben Sie so etwas?
