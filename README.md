# Domain-Driven Design – 2-Tage-Kurs

## Rahmen

- 2 Tage
- Kurszeit: 09:00–12:00 und 13:00–16:30/17:00
- 7 Einheiten pro Tag
- 50 Minuten effektiv je Einheit
- Facheinheit: Fallbeispiel und Anforderung lesen lassen, vergleichen, dann einordnen
- Die Übung ist Teil der Facheinheit, keine separate Einheit
- Didaktischer Grundansatz: Problem → Konsequenz → Lösungsidee → Konzept → reparierte Fassung → Übertragung

## Tag 1 · Strategisches Design

| ID | Block | Inhalt | Übung |
|---|---|---|---|
| **1-1** | 1 | **Einführung und Abgrenzung:** Was DDD ist und was nicht; Problemraum und Lösungsraum | — |
| **1-2** | 2 | **Domäne und Modell:** Ein Modell ist eine Auswahl, kein Abbild; der Weg zum Modell | Domäne und Modell |
| **1-3** | 3 | **Ubiquitous Language:** gemeinsame Sprache zwischen Fachbereich und Entwicklung | Sprachkonflikt |
| **1-4** | 3 | **Ubiquitous Language festhalten:** Glossare je Kontext | Glossar |
| **1-5** | 4 | **Bounded Context:** Modellgrenzen; Zuständigkeit beschreiben und abgrenzen | Bounded Context Canvas |
| **1-6** | 5 | **Subdomains:** Core, Supporting, Generic; Abgrenzung zum Bounded Context | Subdomains |
| **1-7** | 6 | **Context Mapping:** Beziehungsmuster zwischen Kontexten — Anticorruption Layer, Shared Kernel, Customer/Supplier, Conformist, Open Host Service | Context Map |

## Tag 2 · Taktisches Design

| ID | Inhalt |
|---|---|
| **2-1** | **Vom strategischen zum taktischen Design:** wie aus Kontextgrenzen Code wird; Bausteine im Überblick |
| **2-2** | **Aggregates:** Konsistenzgrenze, Aggregate Root, Invarianten; Entity und Value Object |
| **2-3** | **Übung Aggregates:** Konsistenzgrenzen an einem Modell festlegen und begründen |
| **2-4** | **Domain Events:** Entkopplung über Ereignisse; Command und Event unterscheiden |
| **2-5** | **Event Storming:** Ablauf und Notation, gemeinsam angewandt |
| **2-6** | **Architektur und Implementierung:** Repository, Factory, Domain Service gegen Application Service; Schichten |
| **2-7** | **Legacy und Evolution:** Anticorruption Layer in der Praxis, schrittweise Ablösung; Abschluss und Gesamtvergleich |

## Behandlungstiefe

### Kernthemen mit Herleitung

- Ubiquitous Language
- Bounded Context
- Context Mapping
- Aggregate mit Konsistenzgrenze und Invarianten
- Domain Events

### Je nach verfügbarer Zeit vertieft

- Subdomains und ihre Abgrenzung zum Bounded Context
- Event Storming als Methode
- Repository, Factory, Domain Service

### Bewusst kompakter behandelt

- Event Sourcing
- CQRS
- Hexagonale und Onion-Architektur
- Legacy-Ablösung im Detail

## Abgrenzungspaare

| Paar | Trennfrage |
|---|---|
| Entity / Value Object | Hat es eine Identität über die Zeit? |
| Aggregate / Entity | Wo verläuft die Konsistenzgrenze? |
| Bounded Context / Subdomain | Lösungsraum oder Problemraum? |
| Domain Event / Command | Ist es geschehen oder wird es gefordert? |
| Repository / Factory | Holen oder erzeugen? |
| Domain Service / Application Service | Fachlogik oder Ablaufsteuerung? |
