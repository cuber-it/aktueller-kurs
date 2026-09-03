# 1-1 · Einführung und Abgrenzung: Was DDD ist und was nicht

Domain-Driven Design ist ein Vorgehen, bei dem die **Fachlichkeit** die Struktur der Software bestimmt — nicht die Technik, nicht die Datenhaltung, nicht das Organigramm. Der Ansatz geht auf Eric Evans (2003) zurück.

Der Kern lautet: **Software wird aus der Sprache und den Regeln der Fachdomäne heraus entworfen**, in enger Zusammenarbeit mit denen, die diese Domäne kennen.

- **Domäne** – Der fachliche Bereich, in dem ein Unternehmen tätig ist; das, worum es inhaltlich geht, unabhängig von jeder Software.
- **Problemraum** – Was das Unternehmen tut und welche fachlichen Fragen zu lösen sind; wird durch das Geschäft bestimmt, nicht durch den Entwurf.
- **Lösungsraum** – Wie die Software geschnitten wird, um den Problemraum abzudecken; hier fallen Entwurfsentscheidungen.
- **Strategisches Design** – Befasst sich mit Grenzen, Sprache und Beziehungen im Großen: Wo verlaufen Modellgrenzen, wie hängen Teile zusammen, wo lohnt Aufwand.
- **Taktisches Design** – Befasst sich mit dem Bau des Modells im Einzelnen: Aggregate, Entities, Value Objects, Domain Events, Repositories.
- **Zusammenarbeit mit dem Fachbereich** – Kein Beiwerk, sondern Voraussetzung; ein Modell, das der Fachbereich nicht prüfen kann, ist nicht überprüfbar.
- **Was DDD nicht ist** – Keine Architektur, kein Framework, keine Technologieentscheidung; die Wahl zwischen Microservices, Monolith oder Schichtenarchitektur folgt daraus nicht zwingend.
- **Wann es sich lohnt** – Bei fachlicher Komplexität, die über Datenverwaltung hinausgeht; bei langlebigen Systemen; wo Fachwissen verstreut ist und Missverständnisse teuer werden.
- **Wann es sich nicht lohnt** – Bei einfacher Datenverwaltung, kurzlebigen Anwendungen, technisch dominierten Problemen ohne fachliche Regeln.
- **Der Preis** – Höherer Abstimmungsaufwand, mehr Struktur, längere Anlaufzeit; der Nutzen zeigt sich erst bei fortlaufender Änderung.
- **Abgrenzung zur Datenmodellierung** – Ein normalisiertes Schema beschreibt die Speicherung; ein fachliches Modell beschreibt Regeln und Vorgänge. Beides kann gleichzeitig richtig und unvereinbar sein.
