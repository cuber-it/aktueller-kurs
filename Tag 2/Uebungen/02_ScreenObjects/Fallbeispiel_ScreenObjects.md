# Fallbeispiel · Screen Objects ohne Wege

**Situationstyp:** Screen Objects beschreiben Menüs, die Wege zwischen ihnen stehen in Tests und Helpern. Ändert sich ein Weg, ändern sich alle, die ihn gehen.

---

## Ausgangslage

Für jedes Untermenü der Maschineneinstellungen gibt es ein Screen Object mit den Controls des Menüs, die Real Names stehen dort an genau einer Stelle. Tests und Helper bedienen die Controls über diese Screen Objects: `masetth.submenu_gnss_source.back_btn.click_and_wait(...)`.

## Wie es gewachsen ist

Die Screen Objects entstanden, damit Real Names nicht in jedem Test stehen. Das ist gelungen. Die Navigation blieb bei den Aufrufern. Mit der eigenen Regel „kein `snooze` nach Navigation“ wurde das Warten auf Zeit durch das Warten auf ein Objekt des Zielmenüs ersetzt.

## Was auffällt

**Das Screen Object weiß nicht, wohin sein Zurück-Button führt.** Das wissen die Aufrufer: 58-mal `back_btn.click_and_wait(<Objekt des Zielmenüs>)`.

**Ähnliche Navigationsmethoden gibt es doppelt.** Einstellungen eines Geräts und des Standardtraktors öffnen unterscheidet sich nur in Button und Text.

**Die Coding-Regeln des Teams gehen schon in diese Richtung.** Für Wege über mehrere Menüs verlangen sie eine Funktion, die den erreichten Page Helper zurückgibt.

## Naheliegende Ansätze

**Suchen und Ersetzen**, wenn sich ein Zielmenü ändert. Stellen mit Zeilenumbruch oder in Helpern werden leicht übersehen.

**Die Konvention „Navigation immer mit `click_and_wait`“.** Sie ersetzt Zeit durch Zustand, verlagert das Wissen über das Ziel aber nicht aus dem Aufrufer.

## Diskussionsfragen

1. Die Real Names stehen an einer Stelle. Warum hilft das nicht, wenn sich ein Weg ändert?
2. Welches Objekt sollte wissen, wohin ein Zurück-Button führt?
3. Was ändert eine Methode `go_back()`, die das Zielmenü zurückgibt?
4. Wo haben Sie so etwas?
