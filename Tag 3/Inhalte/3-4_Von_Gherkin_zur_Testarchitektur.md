# 3-4 · Von Gherkin zur bestehenden Testarchitektur

Ein fachlich gutes Szenario bestimmt noch nicht seine technische Implementierung. Die Umsetzung muss die vorhandene Squish-Testarchitektur nutzen, statt für jedes Szenario neue technische Zugriffswege oder parallele Abstraktionsschichten zu erzeugen.

- **Verhalten und Implementierung trennen** – Gherkin beschreibt, was aus fachlicher Sicht geschieht. Page Objects, Component Objects, Tasks und Domain APIs bestimmen, wie dieses Verhalten technisch mit Squish umgesetzt wird.
- **Vorhandene Abstraktionen zuerst** – Bevor neuer Testcode entsteht, müssen bestehende APIs und Komponenten untersucht werden. Eine bereits vorhandene fachliche Operation sollte wiederverwendet statt erneut aus elementaren Squish-Aktionen aufgebaut werden.
- **Domain API** – Fachlich formulierte Schritte können häufig direkt auf eine vorhandene Domain API abgebildet werden. Dadurch bleibt das Szenario unabhängig von Widgets, Objektbezeichnern und Navigationsdetails.
- **Task und Workflow Layer** – Schritte, die einen wiederkehrenden Ablauf über mehrere UI-Bereiche beschreiben, gehören gegebenenfalls in vorhandene Tasks oder Workflows statt in einzelne Page Objects.
- **Page und Component Objects** – UI-nahe Aktionen und Zustände werden dort gekapselt, wo die jeweilige Oberfläche bzw. Komponente bekannt ist. Object-Map-Zugriffe und Synchronisation bleiben hinter dieser Grenze.
- **Step Definitions** – Werden ausführbare Gherkin-Schritte verwendet, sollten Step Definitions möglichst dünn bleiben. Sie verbinden Szenariosprache mit der bestehenden Test-API und bilden nicht zusätzlich dieselbe Architektur noch einmal nach.
- **Keine Parallelarchitektur** – Automatisch erzeugte Helper, neue Locator-Zugriffe oder zusätzliche Workflow-Implementierungen können vorhandene Strukturen duplizieren. Architekturkonformität ist deshalb ein eigenes Prüfkriterium.
- **Projektanalyse vor Generierung** – Claude Code muss relevante vorhandene Implementierungen suchen und verstehen, bevor es entscheidet, welche Klassen, Methoden oder Abstraktionen ergänzt werden müssen.
- **Änderung am richtigen Ort** – Ein neues Szenario kann eine Änderung am Test, an einer Domain API, an einem Task oder an einem Component Object erfordern. Die fachliche Änderung und der technische Änderungsort sind nicht identisch.

## Leitgedanke

Gherkin liefert die strukturierte Testabsicht, aber **die bestehende Architektur bleibt der technische Vertrag für die Implementierung**. KI-generierter Code muss sich diesem Vertrag unterordnen.

> **Merksatz:** Gherkin beschreibt das Verhalten – die bestehende Testarchitektur bestimmt die technische Umsetzung.
