# Pro und Contra · Die vorgeschlagene Context Map

Bewertet wird der Vorschlag aus dem Lösungspapier: acht Kontexte, sieben benannte Beziehungen, ein fehlender Anticorruption Layer zum Partnernetzwerk, Shared Kernel zwischen Anmietung und Flotte belassen.

---

## Pro

**Die Frage „wen trifft es" ist beantwortbar**
Vor einer Änderung liest man die Map, statt eine Volltextsuche zu starten. Bei AV-2588 hätte das elf Wochen auf drei reduziert.

**Die Abhängigkeitsrichtung steht fest**
Für jede Beziehung ist notiert, wer nachziehen muss. Das ist die Information, die in Schnittstellenlisten fehlt und in Verhandlungen mit Anbietern gebraucht wird.

**Der fehlende Anticorruption Layer wird sichtbar**
Dass ein Fremdcode in vier Kontexten ausgewertet wird, ist in der Map eine offensichtliche Anomalie. In einer Schnittstellenliste wäre es unsichtbar geblieben.

**Der Shared Kernel wird als solcher benannt**
Anmietung und Flotte teilen sich Fahrzeugdaten, was beide wussten, aber niemand als Muster mit Preis bezeichnet hatte. Jetzt ist der Koordinationsaufwand begründet statt zufällig.

**Conformist wird zur Entscheidung statt zum Zustand**
Beim Partnernetzwerk war Conformist nie entschieden worden — es ergab sich aus Zeitdruck. Die Map zwingt dazu, es zu benennen und damit zu prüfen.

**Der Zahlungsdienstleister-Wechsel bekommt eine Grundlage**
Die Aussage „technisch kein großer Aufwand" ist nun prüfbar: Man sieht die Beziehung und weiß, welche Frage zu stellen ist.

**Eine Seite genügt**
Acht Kästen, sieben Linien. Wird vor einer Änderung tatsächlich angesehen.

---

## Contra

**Die Map ist eine Momentaufnahme**
Sie beschreibt den Stand nach der Erhebung. Ohne Anlass zur Pflege veraltet sie — und eine veraltete Map ist schlechter als keine, weil man ihr glaubt.

**Die Beziehungsmuster sind interpretierbar**
Anmietung → Fakturierung wurde als Customer/Supplier eingestuft, obwohl Herr Krause sagt, er habe keine Mitsprache. Faktisch ist es näher am Conformist. Die Einstufung hängt davon ab, ob man die Möglichkeit oder die Praxis bewertet.

**Sie zeigt nicht, wie eng die Kopplung ist**
Zwischen Vertragsverwaltung und Anmietung fließen wenige Konditionsdaten, zwischen Anmietung und Flotte ein ganzes Modell. Beide sind eine Linie. Die Map unterscheidet die Art der Beziehung, nicht ihr Gewicht.

**Der Shared Kernel bleibt bestehen, ohne dass die Frage entschieden wäre**
Der Vorschlag belässt ihn mit dem Hinweis „streitbar". Das ist ehrlich, aber es ist keine Entscheidung — und der Koordinationsaufwand läuft weiter.

**Ein Anticorruption Layer kostet mehr als die 31 Stellen**
Die Übersetzung muss gebaut, getestet und gepflegt werden, und sie hat eigene Fehlerquellen. Bei einem Format, das sich alle drei Jahre ändert, ist die Rechnung nicht eindeutig.

**Vier Fremdsysteme sind vielleicht nicht alle**
Die Erhebung beruht auf Gesprächen. Ob es weitere Abhängigkeiten gibt — Datenexporte, Auswertungen, manuelle Übertragungen —, ist ungeprüft.

**Niemand ist zuständig**
Die Map hat keinen Eigentümer. Wer sie bei der nächsten Anbindung ergänzt, ist offen.

---

## Bewertung

Der Fall trägt die Map, weil **eine Änderung eingetreten ist, deren Umfang niemand kannte**, und weil **zwei weitere angekündigt sind**. Die Kosten der Unwissenheit sind beziffert: acht Wochen Verzug plus Vertragsstrafen.

Gegenprobe — *Map gedanklich weglassen, bleiben Nachteile?* Ja: Vor dem Wechsel des Zahlungsdienstleisters wiederholt sich dieselbe Fehleinschätzung, weil dieselbe Grundlage fehlt.

**Die Grenzen:**

1. **Ohne Pflegeanlass veraltet sie.** Die einzige tragfähige Regel: Bei jeder neuen Anbindung wird die Map ergänzt, bevor entwickelt wird. Turnusmäßige Überarbeitung funktioniert erfahrungsgemäß nicht.

2. **Die Einstufung von Anmietung → Fakturierung gehört geklärt.** Customer/Supplier setzt voraus, dass Absprache stattfindet. Findet sie nicht statt, ist es Conformist — und dann wäre eine Grenze zu prüfen.

3. **Der Anticorruption Layer braucht eine Rechnung.** „31 Stellen" ist ein Argument, aber keine Wirtschaftlichkeitsbetrachtung. Wie oft ändert sich das Format, was kostet die Übersetzung in der Pflege?

---

## Diskussionsfragen

1. Wie halten Sie eine Context Map aktuell, ohne einen Turnus einzuführen?
2. Anmietung → Fakturierung: Customer/Supplier oder Conformist? Was folgt daraus?
3. Die Map zeigt die Art der Beziehung, nicht ihr Gewicht. Wie ergänzen Sie das, ohne sie zu überfrachten?
4. Wann rechnet sich ein Anticorruption Layer nicht?
5. Wer sollte eine Context Map besitzen?
