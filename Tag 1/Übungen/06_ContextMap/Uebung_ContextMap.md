# Übung · Die Context Map

Sie kennen die vier internen Kontexte aus den vorigen Übungen. Jetzt kommen vier Fremdsysteme dazu — und die Frage, in welcher Beziehung alle zueinander stehen.

---

## Material A · Die Kontexte

### Intern

| Kontext | Verantwortet |
|---|---|
| **Vertragsverwaltung** | Rahmenverträge, Konditionen, Firmenkunden |
| **Anmietung** | Reservierung, Ausgabe, Rückgabe, Mietverträge |
| **Flotte und Instandhaltung** | Fahrzeugbestand, Standorte, Wartung, Reparatur |
| **Fakturierung** | Rechnungen, Kautionen, Mahnwesen |

### Extern

| System | Anbieter | Was es tut |
|---|---|---|
| **Partnernetzwerk** | internationaler Vermittler | liefert Buchungen, 18 % der Anmietungen |
| **Leasingportal** | Leasinggeber | Bestellung und Rückgabe von Fahrzeugen |
| **Schadensplattform** | Versicherungsverbund | Schadensmeldung und Regulierung |
| **Zahlungsdienstleister** | Bank | Kartenzahlung, Kautionssperrung |

---

## Material B · Aussagen aus der Erhebung

### Zum Partnernetzwerk — Herr Doblinger, IT-Leitung

> „Auf deren Format haben wir null Einfluss. Wenn die was ändern, kriegen wir eine Mail mit acht Wochen Vorlauf und können zusehen.
>
> Wir sind für die einer von zweihundert Anbietern. Da ruft niemand zurück."

### Zum Leasingportal — Frau Petrova, Flotte

> „Mit dem Leasinggeber haben wir einen Rahmenvertrag über 2.400 Fahrzeuge. Wenn wir sagen, wir brauchen eine zusätzliche Angabe im Rückgabeprotokoll, dann reden die mit uns. Hat schon zweimal geklappt.
>
> Umgekehrt sagen die uns auch Bescheid, wenn sich was ändert — meistens ein halbes Jahr vorher."

### Zur Schadensplattform — Herr Krause, Abrechnung

> „Das ist ein Verbandsformat. Fünfzehn Versicherer und ein paar hundert Betriebe nutzen dasselbe. Da gibt es ein Gremium, das das Format pflegt, und eine öffentliche Spezifikation.
>
> Wir könnten Änderungswünsche einbringen, machen wir aber nicht. Wir nehmen, was da ist."

### Zum Zahlungsdienstleister — Herr Doblinger

> „Standardschnittstelle, die alle Banken so anbieten. Wir wollen den Anbieter wechseln, weil er zu teuer ist. Technisch soll das kein großer Aufwand sein — angeblich."

### Zwischen Vertragsverwaltung und Anmietung — Frau Berger, Vertrieb

> „Wenn ich eine Konditionsstaffel ändere, muss die Anmietung das mitbekommen, sonst rechnen die Stationen falsch ab.
>
> Umgekehrt sagt mir die Anmietung, wenn eine Regelung praktisch nicht funktioniert. Dann passe ich sie an. Das läuft gut, wir sitzen im selben Haus."

### Zwischen Anmietung und Fakturierung — Herr Krause

> „Ich kriege abgeschlossene Vorgänge und mache daraus Rechnungspositionen. Wenn die Anmietung ihr Format ändert, muss ich nachziehen — das ist einfach so.
>
> Ich hab da keine Mitsprache, brauche ich auch nicht. Die Daten, die ich brauche, sind seit Jahren dieselben."

### Zwischen Anmietung und Flotte — Herr Yilmaz, Station

> „Wir melden Ausgabe und Rückgabe, damit die Flotte weiß, wo die Autos stehen. Und wir sehen, was verfügbar ist.
>
> Das ist eine gemeinsame Sache — wir arbeiten mit denselben Fahrzeugdaten. Wenn die was am Fahrzeugmodell ändern, betrifft uns das sofort."

---

## Material C · Der Befund aus AV-2588

Der Statuscode des Partnernetzwerks wird an 31 Stellen ausgewertet:

| Kontext | Stellen |
|---|---|
| Anmietung | 12 |
| Fakturierung | 9 |
| Flotte und Instandhaltung | 6 |
| davon Werkstatt | 4 (Herkunft ungeklärt) |

---

## Aufgabe

**1.** Zeichnen Sie eine Context Map. Acht Kästen (vier intern, vier extern), Linien für jede Beziehung, aus der Information fließt.

**2.** Benennen Sie für jede Beziehung das Muster. Zur Auswahl stehen:

   Customer/Supplier · Conformist · Anticorruption Layer · Open Host Service · Published Language · Shared Kernel · Partnership · Separate Ways

**3.** Markieren Sie an jeder Beziehung die Richtung: Wer muss nachziehen, wenn sich beim anderen etwas ändert?

**4.** Die Aussage von Herrn Yilmaz zur Flotte ist auffällig. Welches Muster beschreibt er, und was ist der Preis dieses Musters?

**5.** Der Befund aus Material C zeigt, dass der Partnerstatus in vier Kontexten ausgewertet wird. Was sagt das über die Anbindung? Zeichnen Sie ein, wo eine Grenze fehlt.

**6.** Die vier Stellen in der Werkstatt sind ungeklärt. Formulieren Sie zwei Fragen, mit denen Sie herausfinden, was dort tatsächlich gebraucht wird.

**7.** Der Zahlungsdienstleister soll gewechselt werden. Lesen Sie aus Ihrer Map ab, welche Kontexte betroffen wären. Was müsste anders sein, damit der Wechsel wirklich „kein großer Aufwand" ist?

**8.** Nennen Sie die zwei Beziehungen, die Sie als erstes ändern würden. Begründen Sie mit Risiko und Aufwand.

---

## Hinweise zur Bearbeitung

- Eine Beziehung ohne Richtung ist unvollständig. Wer nachzieht, ist die wichtigere Hälfte.
- Conformist ist keine schlechte Wahl. Prüfen Sie, ob sie **bewusst** getroffen wurde.
- Es müssen nicht alle acht Muster vorkommen. Manche passen mehrfach.
