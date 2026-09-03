# AV-2612 · Abhängigkeiten zwischen Kontexten sichtbar machen

**Typ:** Story
**Komponente:** Fachliche Architektur
**Priorität:** Hoch
**Verweist auf:** AV-2588 (Formatumstellung Partnernetzwerk, 11 statt 3 Wochen, Vertragsstrafen)

---

## Story

**Als** Architekt
**möchte ich** vor einer Änderung wissen, welche Bereiche davon betroffen sind und in welcher Beziehung sie zueinander stehen,
**damit** eine Formatumstellung bei einem Fremdanbieter nicht zur Volltextsuche wird.

---

## Description

Die Formatumstellung des Partnernetzwerks (AV-2588) dauerte **elf statt drei Wochen**. Es entstanden Vertragsstrafen. Vier Wochen später lieferte die Verfügbarkeitsplanung falsche Zahlen, weil ein zusammengelegter Statuscode in zwei Kontexten unterschiedlich verstanden wurde.

**Ursache:** Das Modell des Fremdanbieters wurde bei der Anbindung unverändert in das eigene übernommen. Der Statuscode `partnerStatus` wird an **31 Stellen** ausgewertet:

| Kontext | Stellen | Fachlich begründet |
|---|---|---|
| Anmietung | 12 | ja |
| Fakturierung | 9 | ja |
| Flotte und Instandhaltung | 6 | teilweise |
| Werkstatt (innerhalb Flotte) | 4 | **nein — Herkunft ungeklärt** |

Es existiert keine Übersicht, welche Kontexte von welchen Fremdsystemen abhängen. Die 31 Stellen wurden per Volltextsuche ermittelt.

**Weitere Anbindungen nach demselben Muster:** Leasingportal, Schadensplattform. Beide haben Formatumstellungen angekündigt.

**Nicht Gegenstand dieses Tickets:** Der Umbau der Anbindungen. Es geht um Erhebung und Bewertung.

## Randbedingungen

- Vier interne Kontexte: Vertragsverwaltung, Anmietung, Flotte und Instandhaltung, Fakturierung
- Vier Fremdsysteme: Partnernetzwerk, Leasingportal, Schadensplattform, Zahlungsdienstleister
- 18 Prozent der Anmietungen kommen über das Partnernetzwerk
- Auf das Format der Fremdsysteme besteht kein Einfluss
- Beim Zahlungsdienstleister ist ein Wechsel des Anbieters in Prüfung

## Akzeptanzkriterien

- **AK1** – Für jedes Paar von Kontexten, zwischen denen Information fließt, ist die Beziehung benannt und begründet.
- **AK2** – Für jede Beziehung ist festgehalten, welcher Kontext bei einer Änderung nachziehen muss.
- **AK3** – Es ist erkennbar, wo fremde Modelle in eigene Kontexte eingedrungen sind.
- **AK4** – Für jedes Fremdsystem ist bewertet, welchen Einfluss das Unternehmen auf dessen Format hat.
- **AK5** – Es ist benannt, an welchen Stellen eine Übersetzung fehlt und wo sie liegen müsste.
- **AK6** – Für die vier ungeklärten Stellen in der Werkstatt ist festgestellt, welche Information dort tatsächlich gebraucht wird.
- **AK7** – Die Darstellung ist auf einer Seite lesbar.
- **AK8** – Für den geprüften Wechsel des Zahlungsdienstleisters ist der betroffene Umfang aus der Darstellung ablesbar.

## Hinweise

Eine Liste der Schnittstellen erfüllt AK1 nicht. Es geht um die **Art** der Beziehung, nicht um ihre Existenz.

AK7 ist ernst gemeint. Eine Darstellung, die drei Seiten braucht, wird vor einer Änderung nicht gelesen.

AK3 zielt auf den Kern des Vorfalls: Nicht die Schnittstelle war das Problem, sondern dass hinter ihr keine Grenze war.

---

## Für den Kurs

Dieses Ticket nennt kein Konzept. Arbeiten Sie entlang der Frage:

**Wer hängt von wem ab — und wer muss nachziehen, wenn sich etwas ändert?**

---
---

# Addendum · Die Beziehungsmuster zwischen Kontexten

Der Katalog kennt eine Reihe benannter Beziehungen. Die wichtigsten, mit ihrem Erkennungszeichen:

## Wer bestimmt, wer folgt

| Muster | Erkennungszeichen |
|---|---|
| **Customer / Supplier** | Der Abnehmer kann Anforderungen stellen, der Lieferant berücksichtigt sie. Es gibt eine Absprache. |
| **Conformist** | Der Abnehmer übernimmt das fremde Modell unverändert, weil er keinen Einfluss hat. Bewusste Entscheidung. |
| **Anticorruption Layer** | Der Abnehmer übersetzt das fremde Modell an der Grenze in sein eigenes. Schützt vor Durchsickern. |
| **Open Host Service** | Der Lieferant bietet eine veröffentlichte Schnittstelle für viele Abnehmer, statt jeden einzeln zu bedienen. |
| **Published Language** | Ein gemeinsames Austauschformat, auf das sich mehrere geeinigt haben. Oft mit Open Host Service zusammen. |

## Wer teilt was

| Muster | Erkennungszeichen |
|---|---|
| **Shared Kernel** | Zwei Kontexte teilen sich einen Modellausschnitt. Änderungen müssen abgestimmt werden. Hoher Koordinationsaufwand. |
| **Separate Ways** | Zwei Kontexte haben keine Verbindung. Bewusste Entscheidung gegen Integration. |
| **Partnership** | Zwei Teams stehen und fallen gemeinsam. Koordinierte Planung, gemeinsame Releases. |

## Big Ball of Mud

Kein Beziehungsmuster, sondern ein Befund: ein Bereich ohne erkennbare innere Grenzen. Wird in einer Context Map ausgewiesen, um klarzumachen, dass man dort nicht weiter aufteilt — sondern eine Grenze **darum** zieht.

## Die zwei Fragen, die jede Beziehung bestimmen

**1. Wer muss nachziehen, wenn sich etwas ändert?**
Der Abnehmer (upstream/downstream) oder beide (Partnership, Shared Kernel)?

**2. Wie viel Einfluss hat der Abnehmer?**
Kein Einfluss → Conformist oder Anticorruption Layer. Einfluss durch Absprache → Customer/Supplier.

## Conformist oder Anticorruption Layer?

Die häufigste Entscheidung in der Praxis:

| | Conformist | Anticorruption Layer |
|---|---|---|
| Fremdes Modell | wird übernommen | wird übersetzt |
| Aufwand bei Anbindung | gering | höher |
| Aufwand bei Formatänderung | hoch, trifft alles | gering, trifft die Übersetzung |
| Sinnvoll bei | stabilen Formaten, geringer Bedeutung | häufigen Änderungen, zentraler Bedeutung |

**Der Fehler im Fallbeispiel:** Conformist ist eine **legitime Wahl** — aber eine bewusste. Hier wurde sie nicht getroffen, sondern ergab sich aus Zeitdruck. Und sie wurde nicht auf die Anbindung begrenzt, sondern sickerte in vier Kontexte durch.
