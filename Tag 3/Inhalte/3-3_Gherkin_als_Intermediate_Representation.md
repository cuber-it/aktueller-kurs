# 3-3 · Von Anforderungen zu Testfällen: Gherkin als Intermediate Representation

Zwischen einer fachlichen Anforderung und ausführbarem Squish-Code liegt eine eigenständige Testdesign-Aufgabe. Gherkin kann dabei als **strukturierte Intermediate Representation (IR)** dienen: verständlich genug für fachliches Review und formal genug, um daraus systematisch eine technische Implementierung abzuleiten.

- **Testanalyse vor Implementierung** – Eine Anforderung beschreibt nicht automatisch alle notwendigen Testfälle. Relevante Szenarien, Varianten, Vorbedingungen, Grenzfälle und erwartete Ergebnisse müssen zunächst identifiziert werden.
- **Intermediate Representation** – Gherkin bildet eine Zwischendarstellung zwischen natürlicher Anforderung und technischem Testcode. Dadurch kann die fachliche Testabsicht geprüft werden, bevor Implementierungsdetails entstehen.
- **Given** – Beschreibt den für das Szenario notwendigen Ausgangszustand. Ein Given ist keine Anleitung, wie dieser Zustand technisch hergestellt werden muss.
- **When** – Beschreibt die fachlich relevante Aktion oder das Ereignis, dessen Verhalten geprüft werden soll.
- **Then** – Beschreibt eine beobachtbare Erwartung. Die technische Realisierung des Testorakels gehört erst in die Implementierung.
- **Szenarien statt Codepfade** – Gute Szenarien orientieren sich am Verhalten des Systems und nicht an Methoden, Widgets oder einzelnen technischen Aktionen der GUI.
- **Mehrdeutigkeiten sichtbar machen** – Unklare Vorbedingungen, fehlende erwartete Ergebnisse oder widersprüchliche Anforderungen werden in einer strukturierten Szenariobeschreibung früher sichtbar als während der Codegenerierung.
- **KI als Analysepartner** – Claude Code kann aus Anforderungen Szenariovorschläge, Varianten und mögliche Lücken ableiten. Diese Vorschläge sind Ergebnisse einer Analyse und müssen fachlich geprüft werden.
- **Review-Grenze** – Gherkin schafft einen expliziten Kontrollpunkt zwischen Testanalyse und Implementierung. Erst nach der Prüfung der Szenarien wird entschieden, welche davon automatisiert und technisch umgesetzt werden.
- **Kein BDD-Zwang** – Die Verwendung von Gherkin als IR setzt weder einen vollständigen BDD-Prozess noch zwingend eine ausführbare Gherkin-Infrastruktur voraus. Entscheidend ist die strukturierte Zwischendarstellung.

## Leitgedanke

Die direkte Übersetzung einer Anforderung in Testcode vermischt Testanalyse und Implementierung. Eine explizite Zwischendarstellung macht **Testabsicht, Vorbedingungen und erwartetes Verhalten vor der technischen Umsetzung überprüfbar**.

> **Merksatz:** Erst den Test präzisieren, dann den Testcode erzeugen.
