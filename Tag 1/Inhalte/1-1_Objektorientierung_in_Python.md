# 1-1 · Objektorientierung in Python

Objektorientierung in Python folgt denselben Grundideen wie in anderen OO-Sprachen, setzt sie aber mit einem **dynamischen Objektmodell und pythonischen Konventionen** um. Für erfahrene Entwickler steht deshalb nicht die Einführung in Klassen im Mittelpunkt, sondern die Frage, wie OO in Python idiomatisch eingesetzt wird.

- **Alles ist ein Objekt** – Auch Klassen, Funktionen und Module sind Objekte und können referenziert, übergeben und zur Laufzeit untersucht werden.
- **Klasse und Instanz** – Eine Klasse definiert Verhalten und gemeinsame Struktur; Instanzen besitzen Identität und individuellen Zustand.
- **Dynamisches Objektmodell** – Attribute und Verhalten werden zur Laufzeit aufgelöst. Python benötigt deshalb weniger formale Konstrukte als statisch typisierte OO-Sprachen.
- **Methodenbindung** – Methoden sind Funktionen, die beim Zugriff über eine Instanz an diese gebunden werden. `self` ist explizit und macht den Objektbezug sichtbar.
- **Konvention statt Zugriffssperre** – Python verwendet keine klassische private/public-Kapselung. Ein führender Unterstrich kennzeichnet Implementierungsdetails; Name Mangling mit `__name` löst ein anderes Problem und ersetzt kein Private.
- **Properties** – Zugriff kann wie auf ein Attribut aussehen und dennoch kontrolliertes Verhalten auslösen. Properties erlauben, eine öffentliche Schnittstelle stabil zu halten, ohne vorsorglich Getter und Setter einzuführen.
- **Magic Methods** – `__init__`, `__repr__`, `__eq__` oder `__enter__`/`__exit__` integrieren eigene Typen in das Python-Objektmodell. Sie werden eingesetzt, wenn ein Objekt tatsächlich das entsprechende Protokoll erfüllen soll.
- **Duck Typing** – Zusammenarbeit benötigt häufig keine gemeinsame Basisklasse. Entscheidend ist zunächst, ob ein Objekt das benötigte Verhalten anbietet.
- **Pythonisch statt übertragen** – Java- oder C#-Strukturen lassen sich in Python nachbauen, sind dadurch aber nicht automatisch gutes Python-Design. Weniger formale Struktur kann dieselbe Entwurfsidee klarer ausdrücken.

## Leitgedanke

OO in Python bedeutet nicht, möglichst viele Klassenmechanismen einzusetzen. Entscheidend ist, **Verantwortlichkeiten und Zusammenarbeit so auszudrücken, dass der Code verständlich, veränderbar und für Python natürlich bleibt**.

> **Merksatz:** Gutes OO-Design in Python nutzt die Möglichkeiten und Konventionen von Python, statt andere Sprachen nachzubauen.
