# Fallbeispiel · Die Adresse, die eine Geschichte bekam

**Situationstyp:** Etwas, das ein bloßer Wert sein sollte, wurde zu einem Ding mit Lebenslauf — und zieht seither Aufwand nach sich, den niemand gewollt hat.

---

## Ausgangslage

Derselbe Autovermieter. Der Kontext **Fakturierung** stellt Rechnungen und führt das Mahnwesen.

Zu einer Rechnung gehört eine Rechnungsanschrift. Sie kommt aus dem Rahmenvertrag oder wird beim Mietvorgang erfasst.

## Wie es gewachsen ist

Anfangs war die Anschrift Teil der Rechnung: Straße, Hausnummer, Postleitzahl, Ort, Land. Fünf Angaben, die zusammen einen Wert ergeben.

Dann kam die Anforderung, dass Firmenkunden mehrere Rechnungsanschriften haben können — je Landesgesellschaft eine. Die Anschrift bekam eine eigene Kennung, damit man sie auswählen konnte.

Dann sollte nachvollziehbar sein, wann eine Anschrift geändert wurde. Die Anschrift bekam ein Änderungsdatum und einen Bearbeitervermerk.

Dann wurde festgestellt, dass manche Anschriften nicht mehr gültig sind, in alten Rechnungen aber weiterhin stehen müssen. Die Anschrift bekam einen Gültigkeitszeitraum.

Dann kam die Anforderung, fehlerhafte Anschriften zu markieren, wenn Post zurückkommt. Die Anschrift bekam ein Merkmal „unzustellbar" und einen Vermerk dazu.

**Heute hat die Anschrift** eine Kennung, ein Anlagedatum, ein Änderungsdatum, einen Bearbeitervermerk, einen Gültigkeitszeitraum, ein Unzustellbarkeitsmerkmal und einen Vermerk — dazu die fünf ursprünglichen Angaben.

## Der Vorfall

Ein Firmenkunde meldete, dass eine Rechnung an eine Anschrift ging, die er vor zwei Jahren abgemeldet hatte.

Die Untersuchung ergab: Die Anschrift war als ungültig markiert, wurde aber weiterverwendet, weil die Rechnung auf die **Kennung** verwies und nicht auf die Werte. Beim Erstellen wurde die Kennung aufgelöst — und dabei die Gültigkeit nicht geprüft.

**Bei der Nachrecherche** fanden sich weitere Auffälligkeiten:

- **Vierzehn Anschriften** waren doppelt vorhanden, mit identischen Werten und verschiedenen Kennungen. Sie waren zu verschiedenen Zeitpunkten neu erfasst worden, weil niemand die vorhandene fand.
- Bei **drei Kunden** war die Anschrift eines anderen Kunden verknüpft. Vermutlich durch eine Verwechslung bei der Auswahl.
- **Achtzig Anschriften** hatten einen Gültigkeitszeitraum, der in der Zukunft begann — offenbar Tippfehler bei der Erfassung, die nie auffielen.

## Was bei der Aufarbeitung auffiel

**Die Anschrift wurde behandelt, als hätte sie eine Geschichte.** Sie hat aber keine. Eine Anschrift ist eine Anschrift; wenn sie sich ändert, ist es eine **andere** Anschrift.

**Der eigentliche Gegenstand ist die Zuordnung**, nicht die Anschrift selbst. Nicht die Anschrift „gilt bis", sondern die Zuordnung „Kunde X verwendet Anschrift Y von–bis".

**Die Kennung war eine Notlösung.** Sie wurde eingeführt, um zwischen mehreren Anschriften eines Kunden auswählen zu können. Damit wurde aus einem Wert ein Ding — mit allen Folgen: Doppelte, Verwechslungen, Verwaltungsaufwand.

**Was auf einer Rechnung stehen muss, ist der Wert.** Eine Rechnung von 2023 zeigt die Anschrift, die 2023 galt — unabhängig davon, was seither geschah. Ein Verweis auf eine Kennung leistet genau das nicht.

## Was bisher versucht wurde

**Eine Dublettenprüfung.** Beim Anlegen wird geprüft, ob eine Anschrift mit gleichen Werten existiert. Verhindert neue Doppelte, löst die vorhandenen nicht auf.

**Ein Pflegewerkzeug.** Eine Maske, mit der Anschriften zusammengeführt werden können. Wurde dreimal benutzt.

## Diskussionsfragen

1. Jede einzelne Erweiterung war begründet. Warum ist das Ergebnis trotzdem falsch?
2. Was ist der Unterschied zwischen „die Anschrift gilt bis" und „die Zuordnung gilt bis"?
3. Was müsste auf einer Rechnung von 2023 stehen — der Wert oder ein Verweis?
4. Wo haben Sie so etwas?
