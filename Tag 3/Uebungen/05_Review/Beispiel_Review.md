# Beispiel · Prüfskript, KI-Review oder bessere API? – in klein

Dieselbe Aufgabe an einem kleineren Gegenstand, vollständig durchgeführt.

---

## Der Gegenstand

Ein Team schreibt Infrastruktur-Konfigurationen für eine Webanwendung. Vier Regeln:

| Nr. | Regel |
|---|---|
| R1 | Speicher-Buckets sind nie öffentlich lesbar. |
| R2 | Jede Ressource trägt das Kennzeichen `owner`. |
| R3 | Datenbanken mit Kundendaten haben Backups mit mindestens 30 Tagen Aufbewahrung. |
| R4 | Neue Dienste bekommen nur die Rechte, die sie brauchen. |

---

## Schritt 1 · Einordnen

| Regel | Prüfart | Begründung |
|---|---|---|
| R1 | statisch | Attribut `public = true` eindeutig erkennbar |
| R2 | statisch | Kennzeichen vorhanden oder nicht |
| R3 | statisch + Urteil | Aufbewahrung prüfbar; „mit Kundendaten“ braucht Wissen |
| R4 | KI-Review | „nur die Rechte, die sie brauchen“ verlangt Verständnis des Dienstes |

---

## Schritt 2 · Eine Prüfung, die still bleibt, wenn sie unsicher ist

```python
def check_backup_retention(resource):
    if resource.type != "database":
        return None
    if "customer_data" not in resource.tags:
        return None                       # unklar, ob Kundendaten: nicht raten
    if resource.backup_days < 30:
        return f"{resource.name}: backup retention {resource.backup_days} < 30 days"
```

---

## Schritt 3 · KI-Review für R4

```text
Prüfe die Rechte des neuen Dienstes "invoice-mailer" gegen unsere Regel R4
(docs/standards.md, Abschnitt Rechte). Liste jede Berechtigung, die der Code des Dienstes
nicht verwendet, mit Datei und Zeile, in der sie vergeben wird. Keine Vorschläge für andere Dienste.
```

Ergebnis als Kommentar im Pull Request, nicht als Blockade.

---

## Was dieses Beispiel zeigt

**Statisch, wo eindeutig.** R1 und R2 brauchen kein Modell.

**Still, wo unsicher.** Die Backup-Prüfung meldet nur, wenn das Kennzeichen „Kundendaten“ gesetzt ist.

**KI-Review mit Maßstab.** Der Auftrag nennt die Regel und die Quelle, nicht „prüfe auf Sicherheit“.
