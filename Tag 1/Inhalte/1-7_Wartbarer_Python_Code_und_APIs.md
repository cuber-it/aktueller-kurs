# 1-7 · Wartbarer Python-Code & APIs

Gutes OO-Design wird erst dauerhaft wirksam, wenn der Code eine **konsistente und verständliche öffentliche Oberfläche** besitzt. Dazu gehören API-Design ebenso wie Projektstruktur und gemeinsame Konventionen.

- **Public API** – Die öffentliche Schnittstelle sollte klein, verständlich und stabil sein. Nicht jedes technisch erreichbare Attribut ist Teil des vorgesehenen Vertrags.
- **Implementierungsdetails** – Interne Hilfsmethoden und Datenstrukturen dürfen sich ändern können, ohne alle Nutzer der Klasse anzupassen.
- **Naming** – Namen transportieren Entwurfsabsicht. Klassen benennen Konzepte und Verantwortlichkeiten; Methoden beschreiben Verhalten.
- **Module und Packages** – Struktur sollte fachliche bzw. technische Verantwortlichkeiten sichtbar machen. Eine Ordnerstruktur ist selbst Teil der Architektur.
- **PEP 8** – Gemeinsame Format- und Naming-Konventionen reduzieren unnötige Unterschiede. Automatisierbare Stilfragen sollten möglichst nicht in Reviews diskutiert werden müssen.
- **Type Hints** – Annotationen machen Schnittstellen präziser und unterstützen Analysewerkzeuge, ohne die Laufzeitsemantik grundsätzlich zu ändern.
- **Docstrings** – Dokumentation ist besonders dort wertvoll, wo Zweck, Vertrag, Randbedingungen oder nicht offensichtliche Entscheidungen erklärt werden müssen.
- **Properties** – Ermöglichen kontrollierten Attributzugriff, ohne von Beginn an Java-artige Getter und Setter einzuführen.
- **`dataclass`** – Reduziert Boilerplate für datenorientierte Objekte. Nicht jede Klasse ist jedoch lediglich ein Datenträger.
- **Konsistenz** – Ein Teamstandard ist wertvoll, wenn Entwickler nicht bei jeder Datei dieselben Grundsatzentscheidungen neu treffen müssen.
- **Automatisierung** – Formatter, Linter, Type Checker und Tests können einen Teil der Regeln objektiv prüfen. Ein Style Guide sollte zwischen automatisierbaren und architektonischen Regeln unterscheiden.

## Vom Stil zur Corporate Rule

Nicht jede Best Practice muss ein `MUST` werden. Sinnvoll ist die Unterscheidung:

- **MUST** – verbindliche Regel,
- **SHOULD** – begründete Standardentscheidung mit möglichen Ausnahmen,
- **MAY** – zulässige Option,
- **DON'T** – bewusst vermiedenes Vorgehen.

> **Merksatz:** Eine gute API macht den richtigen Gebrauch einfach und hält Implementierungsdetails austauschbar.
