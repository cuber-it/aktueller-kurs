# 3-6 · Vom Coding Agent zum Test-Agenten: MCP

Ein Coding Agent kann Testcode lesen und verändern, besitzt dadurch aber noch keinen direkten Zugang zur laufenden Testumgebung. Für einen Test-Agenten müssen **Code, Testwerkzeug und AUT über kontrollierte Werkzeugschnittstellen verbunden** werden.

- **Coding Agent** – Repository-Zugriff ermöglicht Analyse und Änderung von Testcode. Ob der erzeugte Test tatsächlich mit Squish und der AUT funktioniert, ist damit noch nicht bekannt.
- **Test-Agent** – Ein Test-Agent erweitert den Coding Agent um Fähigkeiten zur Ausführung und Beobachtung. Er kann dadurch nicht nur Code verändern, sondern Ergebnisse aus der realen Testumgebung in weitere Entscheidungen einbeziehen.
- **MCP** – Das Model Context Protocol stellt eine standardisierte Möglichkeit bereit, einem Agenten Werkzeuge und Ressourcen zugänglich zu machen. Die eigentliche Fachlogik bleibt in den angebundenen Systemen und Funktionen.
- **Tools** – Tools stellen gezielte Aktionen bereit, beispielsweise einen Test oder eine Suite zu starten, die AUT zu starten oder einen definierten Zustand abzufragen.
- **Resources** – Ressourcen können Informationen bereitstellen, die der Agent lesen und als Kontext verwenden kann, ohne daraus unmittelbar eine Aktion auszulösen.
- **Tool Contract** – Name, Zweck, Parameter, Rückgabewerte und Fehlerfälle eines Tools bilden einen Vertrag. Je eindeutiger dieser Vertrag ist, desto zuverlässiger kann ein Agent das Werkzeug auswählen und sein Ergebnis interpretieren.
- **Wahrnehmung** – Testergebnisse, Logs und definierte AUT-Zustände bilden die Beobachtungsseite des Agenten. Informationen müssen so strukturiert sein, dass relevante Ergebnisse von technischem Rauschen getrennt werden können.
- **Aktion** – Teststart, Suite-Ausführung oder kontrollierte Interaktionen erweitern den Aktionsraum. Jede zusätzliche Fähigkeit vergrößert gleichzeitig die möglichen Auswirkungen eines Fehlers.
- **Least Capability** – Ein Agent sollte nur die Werkzeuge und Berechtigungen erhalten, die für seinen vorgesehenen Workflow tatsächlich erforderlich sind. Ein kleines Toolset ist leichter zu verstehen, kontrollieren und testen.
- **Kontrollgrenze** – MCP macht Fähigkeiten erreichbar, entscheidet aber nicht, welche davon autonom verwendet werden dürfen. Berechtigungen, Freigaben und menschliche Kontrollpunkte bleiben Teil der Systemarchitektur.

## Leitgedanke

Der Übergang vom Coding Agent zum Test-Agenten entsteht nicht durch einen größeren Prompt, sondern durch **gezielt bereitgestellte Wahrnehmungs- und Aktionsmöglichkeiten mit klaren Verträgen und Grenzen**.

> **Merksatz:** Ein Test-Agent braucht nicht nur Projektwissen, sondern kontrollierten Zugriff auf die Testumgebung.
