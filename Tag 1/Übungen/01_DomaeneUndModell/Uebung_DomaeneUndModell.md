# Übung · Zwei Modelle für denselben Sachverhalt

Sie sehen zwei Entwürfe für denselben Ausschnitt der Autovermietung. Beide sind lauffähig, beide bilden dieselben Daten ab.

---

## Material A · Wie der Fachbereich spricht

Aus einem Gespräch mit einer Stationsleiterin:

> „Ein Vorgang beginnt mit der Reservierung. Wenn der Kunde kommt, geben wir aus — dann läuft der Vorgang.
>
> Verlängern kann er einmal, telefonisch oder vor Ort. Zweimal geht nicht, das muss dann eine neue Anmietung sein.
>
> Bei der Rückgabe nehmen wir das Fahrzeug an, prüfen auf Schäden und schließen ab. Wenn was offen ist — Schaden, Tankfüllung, Kaution — bleibt der Vorgang offen, auch wenn das Auto schon da steht.
>
> Ausgeben dürfen wir nur, wenn eine gültige Fahrerlaubnis vorliegt und die Kaution durchgeht. Ohne das geht gar nichts."

---

## Material B · Modell 1

```
Klasse MietvertragKopf
    id
    kundeId
    fahrzeugId
    stationId
    beginnDatum
    endeDatum
    statusCode          (1=reserviert, 2=aktiv, 3=zurueck, 4=abgeschlossen)
    kautionBetrag
    kautionStatusCode   (0=keine, 1=gesperrt, 2=freigegeben, 3=verrechnet)
    fahrerlaubnisGeprueft
    anlageZeitpunkt
    aenderungsZeitpunkt

Klasse MietvertragPosition
    id
    kopfId
    positionsTyp        (1=grundmiete, 2=verlaengerung, 3=zusatzleistung)
    vonDatum
    bisDatum
    tagessatz
    menge

Klasse FahrzeugStatusHistorie
    id
    fahrzeugId
    statusCode
    gueltigVon
    gueltigBis
    vorgangId

Klasse SchadenErfassung
    id
    kopfId
    beschreibung
    erfassungsZeitpunkt
    erledigt
```

Alle Klassen haben Getter und Setter für jedes Feld. Die Regeln liegen in Klassen namens `MietvertragService`, `KautionsService` und `StatusManager`.

---

## Material C · Modell 2

```
Klasse Mietvorgang
    nummer
    mieter
    fahrzeug
    station
    zeitraum
    kaution
    zustand             (Reserviert | Laufend | Zurueckgenommen | Abgeschlossen)
    offenePunkte        (Liste)

    kannAusgegebenWerden()      -> ja/nein mit Begründung
    ausgeben(fahrerlaubnis)
    verlaengernBis(datum)       -> nur einmal zulässig
    zurücknehmen(zustandsbefund)
    abschliessen()              -> nur wenn keine offenen Punkte
    istAbgeschlossen()

Klasse Zeitraum
    von
    bis
    verlaengertUm               (leer, wenn nicht verlängert)
    tage()

Klasse Kaution
    betrag
    zustand                     (Gesperrt | Freigegeben | Verrechnet)
    sperren()
    freigeben()
    verrechnenMit(schaden)

Klasse OffenerPunkt
    art                         (Schaden | Tankfuellung | Kaution)
    beschreibung
    istErledigt()
```

Die Regeln liegen in den Klassen selbst. Es gibt keinen `MietvertragService`.

---

## Aufgabe

**1.** Nennen Sie fünf Begriffe aus Material A, die im Modell 1 **nicht** vorkommen.

**2.** Nennen Sie für jeden dieser Begriffe die Stelle, an der er in Modell 2 auftaucht.

**3.** Die Regel „verlängern geht nur einmal" steht in Material A. Wo würde sie in Modell 1 stehen? Wo steht sie in Modell 2?

**4.** Die Regel „ausgeben nur bei gültiger Fahrerlaubnis und durchgegangener Kaution" — dasselbe. Wo jeweils?

**5.** In Modell 1 kann man einen `MietvertragKopf` mit `statusCode = 4` (abgeschlossen) und einer nicht erledigten `SchadenErfassung` anlegen. Ist das fachlich möglich? Was sagt das über das Modell?

**6.** Modell 1 hat ein Feld `fahrerlaubnisGeprueft` als Wahrheitswert. Was fehlt daran, gemessen an Material A?

**7.** Ein Fachvertreter soll prüfen, ob das Modell stimmt. Welches der beiden Modelle können Sie ihm vorlegen? Begründen Sie.

**8.** Modell 1 hat 4 Klassen und 28 Felder, Modell 2 hat 4 Klassen und weniger Felder, dafür Methoden. Welches ist einfacher — und was heißt „einfach" hier?

**9.** Was **kann** Modell 1, was Modell 2 nicht kann? Nennen Sie mindestens einen Punkt.

---

## Hinweise zur Bearbeitung

- Beide Modelle sind lauffähig. Es geht nicht um richtig oder falsch, sondern darum, **was sie abbilden**.
- Achten Sie bei Aufgabe 9 darauf, dass jede Entscheidung einen Preis hat. Modell 2 ist nicht in jeder Hinsicht überlegen.
- Die Frage bei Aufgabe 8 ist nicht die Zahl der Zeilen.
