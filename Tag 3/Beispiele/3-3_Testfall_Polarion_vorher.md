# 3-3 · vorher · Ein Testfall im Format des Teams

Nachgebildet nach dem Aufbau der Testspezifikation des Teams (Polarion, Integrationstests), Inhalt in eigenen Worten. Kennung und Texte sind geändert.

---

**TC-2001 · Werkseinstellungen wiederherstellen**  
Art: manuell · Status: Active

| Schritt | Beschreibung | Erwartetes Ergebnis |
|---|---|---|
| Systemeinstellungen öffnen | Einstellungsmenü öffnen, System wählen | Die Systemeinstellungen werden angezeigt, im Abschnitt „Aktualisierung und Sicherung“ steht „Werkseinstellungen wiederherstellen“. |
| Werkseinstellungen wählen | „Werkseinstellungen wiederherstellen“ antippen | Eine Warnung erscheint mit rotem X (Abbrechen) und Haken (Bestätigen). |
| Zurücksetzen bestätigen | Haken in der Warnung antippen | Die Warnung schließt, das Terminal startet neu. |
| Neustart abwarten | warten, bis der Neustart abgeschlossen ist | Der Hauptbildschirm wird angezeigt. |

---

## Was dieser Testfall prüft

Den Bedienweg: Menü, Eintrag, Warnung, Neustart, Hauptbildschirm.

Ob danach tatsächlich die Werkseinstellungen gelten, prüft er nicht. Ein Terminal, das nach dem Bestätigen nur neu startet, besteht den Test.
