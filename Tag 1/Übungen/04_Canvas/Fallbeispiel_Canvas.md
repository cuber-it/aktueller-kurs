# Fallbeispiel · Der Kontext, den keiner beschreiben konnte

**Situationstyp:** Ein Bereich ist benannt, aber niemand kann sagen, wofür er zuständig ist und wofür nicht — jede Anfrage landet dort.

---

## Ausgangslage

Derselbe Autovermieter. Die vier Kontexte stehen seit zwei Jahren.

Der Kontext **Anmietung** ist der größte. Er umfasst Reservierung, Ausgabe, Rückgabe, Verlängerung, Schadensaufnahme bei Rückgabe und die Verfügbarkeitsanzeige. Sechs Entwickler, ein Product Owner.

## Wie es gewachsen ist

Anfangs war die Zuständigkeit klar: alles, was am Tresen passiert.

Dann kam die Frage, wo die Schadensaufnahme hingehört. Der Schaden wird bei der Rückgabe festgestellt, also an der Station — die Anmietung übernahm sie.

Dann die Verfügbarkeitsanzeige für die Webseite. Sie zeigt, was buchbar ist. Buchbarkeit ist eine Frage der Anmietung — sie übernahm sie.

Dann die Kautionssperrung. Sie geschieht bei der Ausgabe — Anmietung.

Dann die Berechnung der Zusatzleistungen (Navigationsgerät, Kindersitz, Zweitfahrer). Wird an der Station gebucht — Anmietung.

Dann die Prüfung der Fahrerlaubnis mit Anbindung an einen externen Prüfdienst. Geschieht am Tresen — Anmietung.

## Der Vorfall

Es gab keinen einzelnen. Stattdessen häuften sich drei Beobachtungen:

**Erstens:** Der Anmietungs-Kontext hatte 41 Prozent aller offenen Tickets, bei einem Viertel der Entwickler. Die Durchlaufzeit lag beim Dreifachen der anderen Kontexte.

**Zweitens:** Bei der Quartalsplanung konnte der Product Owner drei von elf Anforderungen nicht zuordnen. Sie betrafen Dinge, die in der Anmietung passieren, aber nicht zu ihr zu gehören schienen — etwa eine Auswertung, welche Zusatzleistungen sich lohnen.

**Drittens:** Ein neuer Entwickler fragte nach zwei Wochen, wofür der Kontext eigentlich zuständig sei. Die Antwort seines Teamleiters lautete: „Alles, was am Tresen passiert." Der Entwickler fragte, ob die Verfügbarkeitsanzeige auf der Webseite am Tresen passiere. Darauf gab es keine Antwort.

## Was der Klärungsversuch ergab

Ein Workshop sollte die Zuständigkeit festhalten. Nach drei Stunden stand eine Liste mit 14 Aufgaben und der Feststellung, dass sechs davon strittig sind.

Die Diskussion drehte sich im Kreis, weil unterschiedliche Kriterien vermischt wurden:

- **„Wo passiert es?"** — die Schadensaufnahme passiert an der Station
- **„Wer braucht es?"** — die Schadensdaten braucht die Fakturierung und die Werkstatt
- **„Wer hat es gebaut?"** — die Anmietung, weil sie damals Kapazität hatte
- **„Was gehört fachlich zusammen?"** — hier wurde es unklar

Ohne gemeinsames Kriterium ließ sich nichts entscheiden.

## Was dauerhaft stört

- Jede neue Anforderung löst die Zuordnungsdiskussion aus.
- Der Kontext wächst weiter, weil im Zweifel er zuständig ist.
- Die sechs Entwickler arbeiten an Dingen, die fachlich wenig miteinander zu tun haben. Wissen verteilt sich nicht.
- Beim letzten Personalwechsel dauerte die Einarbeitung vier Monate.

## Diskussionsfragen

1. Warum war jede einzelne Zuordnungsentscheidung nachvollziehbar — und das Ergebnis trotzdem falsch?
2. Welches Kriterium fehlte im Workshop?
3. Was wäre der Preis, den Kontext zu teilen?
4. Wo haben Sie so etwas?
