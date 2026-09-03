# Fallbeispiel · Die Station, die sich selbst blockierte

**Situationstyp:** Alles, was sachlich zusammengehört, wurde zu einer Einheit gemacht — jetzt behindern sich Vorgänge, die nichts miteinander zu tun haben.

---

## Ausgangslage

Derselbe Autovermieter. Der Kontext **Anmietung** verwaltet Reservierungen, Ausgaben, Rückgaben und Verlängerungen.

Bei der Umstellung vor drei Jahren wurde entschieden, die **Station** als zentrale Einheit zu führen. Die Begründung war einleuchtend: An einer Station hängt alles zusammen — die Fahrzeuge, die dort stehen, die laufenden Vorgänge, die Reservierungen, die Öffnungszeiten, die Mitarbeiter.

## Wie es gewachsen ist

Die Station umfasst heute:

| Bestandteil | Umfang bei einer mittleren Station |
|---|---|
| Fahrzeuge auf dem Hof | 40 bis 90 |
| Laufende Mietvorgänge | 30 bis 70 |
| Reservierungen der nächsten 30 Tage | 100 bis 300 |
| Rückläufer in Aufbereitung | 5 bis 15 |
| Öffnungszeiten und Sonderregelungen | 10 bis 20 Einträge |

Die Regel, die alles zusammenhält, lautet: **Ein Fahrzeug kann nicht gleichzeitig ausgegeben und reserviert sein.** Um sie zu sichern, wird bei jeder Änderung die ganze Station als Einheit behandelt.

## Der Vorfall

An einem Freitagnachmittag im Dezember meldete die Station Frankfurt-Flughafen, dass Ausgaben nicht mehr möglich seien. Die Bildschirme zeigten Wartemeldungen.

Die Untersuchung ergab keinen Ausfall. Das System arbeitete — nur langsam.

**Was geschah:** Vier Mitarbeiter am Tresen, ein Nachtlauf für Reservierungsbestätigungen, die Verfügbarkeitsanzeige der Webseite und die Rückgabeerfassung im Hof griffen gleichzeitig auf dieselbe Station zu. Jeder Zugriff behandelte die ganze Station als Einheit; sie warteten aufeinander.

**Eine Ausgabe dauerte an diesem Nachmittag im Mittel 90 Sekunden**, an ruhigen Tagen sind es zwei.

**Elf Kunden gingen**, nachdem sie länger als zwanzig Minuten gewartet hatten.

## Was bei der Aufarbeitung auffiel

**Die meisten Zugriffe hatten nichts miteinander zu tun.** Wer ein Fahrzeug ausgibt, berührt eine Reservierung von übermorgen nicht. Trotzdem warteten beide aufeinander.

**Die eigentliche Regel ist viel kleiner.** „Ein Fahrzeug kann nicht gleichzeitig ausgegeben und reserviert sein" betrifft **ein** Fahrzeug — nicht neunzig.

**Die Öffnungszeiten wurden mitgesperrt.** Wer sie ändert, hat mit laufenden Vorgängen nichts zu tun. Trotzdem blockierte die Änderung den Tresen.

**Große Stationen sind schlechter dran als kleine.** Frankfurt-Flughafen hat 90 Fahrzeuge, eine Kleinstadtstation zwölf. Der Engpass wächst mit der Größe — und die großen Stationen sind die wichtigen.

**Bei jeder Ausgabe wird die ganze Station geladen.** Neunzig Fahrzeuge, dreihundert Reservierungen, alle Sonderregelungen — für einen Vorgang, der zwei Fahrzeuge betrifft.

## Was bisher versucht wurde

**Mehr Rechenleistung.** Half für ein halbes Jahr, dann war der Zuwachs aufgezehrt.

**Der Nachtlauf wurde auf zwei Uhr verlegt.** Beseitigte einen Verursacher, nicht die Ursache.

**Eine Wartewarteschlange mit Zeitüberschreitung.** Verhindert das Hängenbleiben, führt aber dazu, dass Ausgaben scheitern und wiederholt werden müssen.

## Diskussionsfragen

1. Die Entscheidung, die Station als Einheit zu führen, war 2021 begründet. Was war der Denkfehler?
2. Welche Regel rechtfertigt tatsächlich eine Klammer — und wie groß muss sie sein?
3. Warum sind große Stationen stärker betroffen als kleine?
4. Wo haben Sie so etwas?
