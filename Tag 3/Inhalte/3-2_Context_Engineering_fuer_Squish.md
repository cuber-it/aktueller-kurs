# 3-2 · Context Engineering für Squish

Claude Code kann nur die Projektinformationen berücksichtigen, die im verfügbaren Kontext tatsächlich vorhanden sind. **Context Engineering** bezeichnet deshalb die gezielte Auswahl, Strukturierung und Bereitstellung des Wissens, das ein Coding Agent für eine konkrete Aufgabe benötigt.

- **Projektkontext** – Verzeichnisstruktur, zentrale Module, Testaufbau und technische Randbedingungen helfen dem Agenten, eine Änderung im vorhandenen System einzuordnen statt eine isolierte Lösung zu erzeugen.
- **Architekturregeln** – Page und Component Objects, Tasks, Domain APIs und andere vereinbarte Abstraktionen müssen als Teil des Projektvertrags bekannt sein. Andernfalls kann funktionierender Code entstehen, der die bestehende Architektur umgeht.
- **Projektregeln** – Coding-, Naming- und Strukturregeln sollten explizit und maschinenlesbar vorliegen. Implizites Teamwissen steht einem Agenten nicht automatisch zur Verfügung.
- **Referenzimplementierungen** – Gute vorhandene Tests und Komponenten zeigen nicht nur Syntax, sondern konkrete Architekturentscheidungen. Wenige gezielt ausgewählte Referenzen sind häufig nützlicher als große Mengen beliebigen Projektcodes.
- **Squish-spezifischer Kontext** – Object Map, Objektidentifikation, Synchronisationsstrategien, Testdaten, Setup und Cleanup sowie bekannte Eigenschaften der AUT beeinflussen die korrekte Umsetzung eines Tests.
- **Aufgabenkontext** – Eine konkrete Änderung benötigt zusätzlich lokale Informationen: betroffene Anforderung, relevante Tests, verwendete UI-Komponenten, erwartetes Verhalten und Akzeptanzkriterien.
- **Permanenter und temporärer Kontext** – Dauerhafte Projektregeln gehören in den stabilen Projektkontext. Aufgabenspezifische Informationen werden nur für die jeweilige Änderung benötigt. Diese Trennung reduziert Redundanz und widersprüchliche Vorgaben.
- **Kontextselektion** – Mehr Kontext ist nicht automatisch besser. Irrelevante Dateien, veraltete Beispiele oder konkurrierende Implementierungsvarianten können Entscheidungen erschweren und den relevanten Kontext verdrängen.
- **Kontextpflege** – Projektkontext ist Teil der Engineering-Infrastruktur. Ändern sich Architektur oder Teamregeln, müssen auch die für KI bereitgestellten Regeln und Referenzen angepasst werden.

## Leitgedanke

Context Engineering macht aus implizitem Projektwissen **verfügbaren und gezielt nutzbaren Arbeitskontext**. Entscheidend ist nicht die größtmögliche Informationsmenge, sondern der für die jeweilige Aufgabe relevante und verlässliche Kontext.

> **Merksatz:** Projektwissen gehört in den Projektkontext – die Aufgabe liefert nur den jeweils notwendigen Zusatzkontext.
