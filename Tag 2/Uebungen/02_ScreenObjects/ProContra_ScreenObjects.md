# Pro und Contra · Navigationsoperationen in den Screen Objects

Bewertet wird der Vorschlag aus dem Lösungspapier: Navigationsmethoden, die das Screen Object des Ziels zurückgeben, Operationen für wiederkehrende Abfolgen, Varianten von Controls ohne veränderten Zustand.

---

## Pro

**Ein Menüumbau betrifft eine Methode**
Ändert sich das Ziel eines Zurück-Buttons, ändert sich `go_back()`, nicht jeder Aufrufer.

**Die Snooze-Regel bleibt eingehalten**
Das Team hat seine Regel „kein `snooze` nach Navigation“ im aktiven Code umgesetzt. Steht das Warten in der Navigationsmethode, bleibt es dabei, auch wenn jemand die Regel nicht kennt.

**Wege werden kurz**
`close_machine_settings_menus` wird eine Kette von `go_back()`.

**Falsche Wege fallen früh auf**
Gibt `go_back()` ein anderes Screen Object zurück, passen die folgenden Aufrufe im Test nicht mehr. Die IDE oder ein Type Checker zeigt das.

**Kein geteilter Zustand in Controls**
Eine Exception im Ablauf hinterlässt keinen veränderten Real Name.

---

## Contra

**Mehr Methoden in den Screen Objects**
Jeder Weg wird eine Methode. Bei vielen Menüs wächst jedes UI-Modul.

**Zwei Stile nebeneinander**
Alte Tests nutzen Controls, neue Operationen. Neue Kolleginnen und Kollegen sehen beides.

**Rückgabewerte schaffen Abhängigkeiten zwischen Screen Objects**
`SubMenuGNSSSource.go_back()` kennt `SubMenuTractionUnit`. Zyklische Importe zwischen UI-Modulen sind möglich.

**Nicht jede Wartezeit ist abfragbar**
Wo eine Animation keinen Endzustand liefert, bleibt ein `snooze`, dann in der Operation.

---

## Bewertung

Der Vorschlag trägt, weil **Wege sich ändern und heute in vielen Tests stehen**. Die Real Names stehen schon an einer Stelle, die Wege noch nicht.

Gegenprobe – *nur die `snooze` durch `click_and_wait` ersetzen, keine neuen Operationen, bleiben Nachteile?* Ja: Die Wartezeiten sinken, aber der Test weiß weiterhin, worauf er wartet. Ein geändertes Zielmenü träfe weiterhin jeden Aufrufer.

**Die Grenzen:**

1. **Umstellung braucht Zeit.** Neue Operationen helfen neuen Tests. Bestehende Tests profitieren erst, wenn sie umgestellt werden.
2. **Zyklische Importe.** Screen Objects, die sich gegenseitig zurückgeben, brauchen einen gemeinsamen Zugriffspunkt, im Framework der `helper` je Modul.
3. **Prüfen oder nicht.** Ob eine Operation über das Warten hinaus prüft, ist eine Teamentscheidung (2-7).

---

## Diskussionsfragen

1. Mit welchen Wegen würden Sie beginnen?
2. Sollen bestehende Tests umgestellt werden, oder nur neue die Operationen verwenden?
3. Wie verhindern Sie zyklische Importe zwischen UI-Modulen?
4. Welche Wartezeiten aus der Snooze-Policy würden in welche Operation wandern?
