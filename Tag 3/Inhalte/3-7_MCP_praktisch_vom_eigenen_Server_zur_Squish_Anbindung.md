# 3-7 · MCP praktisch: vom eigenen Server zur Squish-Anbindung

Ein MCP-Server bildet die technische Grenze zwischen Agent und realer Funktionalität. Für die Integration mit einer Testumgebung ist deshalb weniger die Anzahl der Tools entscheidend als deren **klar definierte, robuste und überprüfbare Schnittstelle**.

- **MCP-Server** – Der Server stellt ausgewählte Fähigkeiten eines vorhandenen Systems als Werkzeuge oder Ressourcen bereit. Er ist Adapter und Kontrollgrenze, nicht Ersatz für die eigentliche Testlogik.
- **Tooldefinition** – Ein Tool benötigt einen eindeutigen Namen und eine präzise Beschreibung seiner Aufgabe. Überlappende oder mehrdeutige Tools erschweren dem Agenten die Auswahl.
- **Parameter** – Eingaben sollten klein, typisiert und fachlich eindeutig sein. Der Agent sollte keine internen Implementierungsdetails kennen müssen, die der Server selbst bestimmen kann.
- **Rückgabewerte** – Ergebnisse müssen kompakt und strukturiert genug sein, damit der Agent Erfolg, Fehler und relevante Befunde unterscheiden kann. Ungefilterte Logmengen sind selten eine gute Werkzeugschnittstelle.
- **Fehlerbehandlung** – Erwartbare Fehler gehören zum Tool Contract. Timeout, nicht gestartete AUT, unbekannter Test oder fehlgeschlagene Ausführung sollten unterscheidbare Ergebnisse liefern.
- **Deterministische Werkzeugschicht** – Das Tool selbst sollte möglichst deterministisch arbeiten. Die probabilistische Entscheidung des Modells, welches Werkzeug wann verwendet wird, darf nicht unnötig in die technische Ausführung hineinreichen.
- **Squish-Fähigkeiten** – Sinnvolle erste Werkzeuge können beispielsweise Teststart, Suite-Ausführung, Ergebnisabfrage, Logzugriff oder kontrollierter AUT-Start sein. Welche Fähigkeiten benötigt werden, ergibt sich aus dem gewünschten Workflow.
- **Zustand und Synchronisation** – Eine GUI-Testumgebung besitzt Lifecycle und Zustand. Tools müssen berücksichtigen, ob AUT und Squish bereit sind, welche Ausführung läuft und wann ein Ergebnis tatsächlich verfügbar ist.
- **Berechtigungen** – Der MCP-Server definiert, was technisch möglich ist. Nicht benötigte Datei-, Prozess- oder Systemzugriffe sollten nicht nebenbei mit freigegeben werden.
- **Erweiterbarkeit** – Neue Tools werden hinzugefügt, wenn ein konkreter Workflow sie benötigt. Ein möglichst vollständiges Universalinterface erhöht Komplexität und Aktionsraum ohne automatisch zusätzlichen Nutzen.

## Leitgedanke

Ein brauchbarer MCP-Server übersetzt komplexe technische Möglichkeiten in **wenige klar abgegrenzte Agentenfähigkeiten**. Die Qualität der Schnittstelle bestimmt wesentlich, wie zuverlässig diese Fähigkeiten genutzt werden können.

> **Merksatz:** Gute Agentenwerkzeuge sind klein, eindeutig, überprüfbar und auf ihren Zweck begrenzt.
