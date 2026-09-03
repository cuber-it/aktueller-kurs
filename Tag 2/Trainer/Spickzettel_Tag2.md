# Spickzettel Tag 2

Eine Seite für den Trainer.

---

## Die Leitfrage des Tages

> **Was muss zusammen gültig bleiben, und was darf auseinanderlaufen?**

| Einheit | Beitrag zur Frage |
|---|---|
| 2-1 | setzt sie |
| 2-2 | liefert die Dinge, die geklammert werden |
| 2-3 | was zusammen muss → Aggregate |
| 2-4 | wie das Getrennte zusammenkommt → Events |

---

## Die Prüffragen

| Einheit | Prüffrage |
|---|---|
| **2-2** Entity/Value | Interessiert es, ob es **dasselbe** ist — oder nur, ob es **gleich** ist? |
| **2-3** Aggregate | Muss es im **selben Moment** stimmen? |
| **2-4** Event | **Berichtet** es oder **fordert** es? |
| **2-6** Service | Würde der **Fachbereich** diese Regel kennen? |
| **2-7** Ablösung | Woran erkennen wir, dass das Neue **trägt**? |

---

## Die Abgrenzungspaare

| Paar | Trennfrage |
|---|---|
| Entity / Value Object | Identität über die Zeit? |
| Aggregate / Entity | Was muss sofort stimmen? |
| Domain Event / Command | Geschehen oder gefordert? |
| Repository / Factory | Holen oder erzeugen? |
| Domain Service / Application Service | Fachlogik oder Ablaufsteuerung? |

---

## Einstiegsfragen, die funktionieren

| Einheit | Frage |
|---|---|
| 2-1 | „Was war gestern die wichtigste Erkenntnis?" |
| 2-2 | „Ich leihe Ihnen zwanzig Euro — anderer Schein zurück, in Ordnung? Und beim Fahrrad?" |
| 2-3 | „Bestellung, Positionen, Summe — wo verläuft die Klammer? Gehört der Kunde hinein?" |
| 2-4 | Vier Sätze sortieren lassen: „Rechnung erstellen" · „Vorgang abgeschlossen" · „Fahrzeug zurücknehmen" · „Kaution freigegeben" |
| 2-6 | „Was müssen Sie starten, um die Regel ,nur einmal verlängerbar' zu prüfen?" |
| 2-7 | „Wer arbeitet an einem System älter als fünf Jahre? Wer könnte es an einem Wochenende ersetzen?" |

---

## Die Sätze, die tragen

> Ein Aggregate ist keine **Ordnungsübung**, sondern eine **Konsistenzentscheidung**.

> Ohne **Invariante** kein Aggregate.

> Nicht das Ding entscheidet, sondern der **Kontext**.

> Ein Ereignis **berichtet**, ein Command **fordert**.

> Der Sender kennt seine **Empfänger nicht**.

> Das Modell hängt von **nichts** ab. Alles andere hängt von ihm ab.

> Kontextgrenzen sind die **Schnittlinien** für die Ablösung.

---

## Die häufigen Fehler

**2-2** Alles zur Entity machen · Werte als bloße Zahlen führen

**2-3** Nach Zugehörigkeit statt nach Regel schneiden · zu große Aggregate, weil bequem

**2-4** Ereignisse als Aufforderung formulieren · zu viele Ereignisse · auf Antwort warten

**2-6** Repository gibt Datenstrukturen zurück · Domain Service als Sammelstelle

**2-7** Anbau ohne Grenze · alles auf einmal ablösen wollen

---

## Wenn die Gruppe feststeckt

| Bei | Frage stellen |
|---|---|
| 2-3, Aggregate zu groß | „Welche **Regel** verbindet die beiden?" |
| 2-3, Gruppe unschlüssig | „Was passiert, wenn das für **fünf Minuten** nicht zusammenpasst?" |
| 2-4, technische Ereignisse | „Würde ein **Fachvertreter** das sagen?" |
| 2-6, alles im Service | „Wenn Ihr Domain Service dreißig Methoden hat — was ist passiert?" |
| überall | „Wo haben Sie so etwas?" |

---

## Was in gemischten Gruppen zurückzustellen ist

| Frage | Antwort |
|---|---|
| „Wie speichert man Value Objects?" | Später — erst die fachliche Entscheidung |
| „Wie sperrt man ein Aggregate?" | Umsetzungsdetail |
| „Was ist Event Sourcing?" | Etwas anderes: Events als **Speicherform**. Kurz abgrenzen |
| „Brauchen wir einen Message Broker?" | Nein, nicht zwingend |
| „Was ist CQRS?" | Getrennte Lesemodelle. Nennen, nicht vertiefen |
| Hexagonal / Onion / Clean vergleichen | Drei Namen, ein Gedanke — nicht vergleichen |

---

## Zeitverteilung

| | Minuten | Besonderheit |
|---|---|---|
| 2-1 | 45 | gekürzt, Puffer für 2-3 |
| 2-2 | 50 | |
| **2-3** | **60** | überzieht erfahrungsgemäß |
| 2-4 | 50 | |
| 2-5 | 45 | Board vorher einrichten |
| 2-6 | 50 | kürzen, wenn PO/Management überwiegen |
| **2-7** | **55** | davon 15 Kursabschluss |

---

## Die drei Abschlussfragen

> „Was würden Sie nächste Woche als Erstes tun?"

> „Wo sind Sie unsicher geblieben?"

> „Was hätten Sie weggelassen?"

**Antworten notieren** — die beste Grundlage für die nächste Durchführung.
