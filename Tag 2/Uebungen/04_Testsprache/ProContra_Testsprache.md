# Pro und Contra · Fachliche Operationen für GNSS-Einstellungen

Bewertet wird der Vorschlag aus dem Lösungspapier: `select_gnss_source(GnssSource)` als Facade, Prüfungen sichtbar im Test, Schlüsselwortargumente für `test_wrapper`.

---

## Pro

**Die Aussage steht im Test**
Quelle, Simulation, Prüfung. Die Applikationstechnik liest `GnssSource.sae_j1939` statt eines Attributnamens.

**Das vorhandene Enum wird genutzt**
Tippfehler wie `nmea_2000_btn` im Variablennamen und `rs232_nmea_0183_btn` im Aufruf sind nicht mehr möglich.

**Wege an einer Stelle**
Ändert sich der Weg zur GNSS-Quelle, ändert sich `select_gnss_source`.

**Prüfungen bleiben sichtbar**
`assert_selected_gnss_source` steht im Test, auch wenn die Auswahl in einer Operation steckt.

---

## Contra

**Eine Ebene mehr**
Wer einen Fehler sucht, springt vom Test in die Operation, dann ins Screen Object.

**Meldungen müssen mitwachsen**
Wenn `select_gnss_source` scheitert, muss die Meldung sagen, welches Control fehlte.

**Namen werden verhandelt**
Was „Quelle wählen“ genau umfasst (mit oder ohne Zurück-Navigation), muss festgelegt werden.

**Nur für häufige Abläufe lohnend**
Für einen einmaligen Test ist die Operation mehr Aufwand als Gewinn.

---

## Bewertung

Der Vorschlag trägt, weil **die fachliche Aussage heute im Attributnamen steckt** und das Review daran gescheitert ist.

Gegenprobe – *nur Kommentare über den Blöcken, keine Operationen, bleiben Nachteile?* Ja: Kommentare werden beim Kopieren nicht angepasst, der Fall aus dem Review wiederholt sich.

**Die Grenzen:**

1. **Fluent API zurückgestellt.** Für 14 Tests genügen Funktionen.
2. **Meldungen.** Jede Operation braucht eine Meldung, die das Control nennt.
3. **Begriffe.** Die Namen der Operationen sollte die Applikationstechnik mitbestimmen.

---

## Diskussionsfragen

1. Welche Einstellungen außer der GNSS-Quelle würden Sie als Nächstes fachlich formulieren?
2. Soll die Zurück-Navigation Teil von `select_gnss_source` sein?
3. Wer entscheidet über die Begriffe?
4. Wann würden Sie eine Fluent API einführen?
