# Fallbeispiel · Ein allgemeines Werkzeug für alles

**Situationstyp:** Ein Agent bekommt ein allgemeines Werkzeug, weil er viele kleine Dinge damit tun muss. Damit darf er auch die wenigen gefährlichen.

---

## Ausgangslage

Ein Claude-Code-Skill braucht viele Shell-Befehle: suchen, Dateien lesen, Skripte aufrufen. Damit nicht jeder Befehl eine Rückfrage auslöst, wird `Bash` zu Beginn der Sitzung freigegeben.

## Wie es gewachsen ist

Zuerst liefen Tests über die Squish-IDE. Dann kam ein Skript, das einen Test aus der Shell startet. Der Skill ruft es auf, nachdem er gefragt hat; die Rückfrage steht als Regel im Skill und als Kommentar im Skript.

## Was auffällt

**Die Freigabe ist pauschal.** `Bash` erlaubt `grep` und den Testlauf gleichermaßen.

**Die Ausgabe ist Text.** Ob ein Lauf nicht gestartet ist oder fehlschlug, liest der Agent aus Meldungen.

**Die Laufbegrenzung zählt das Modell.** Nach Kontextverdichtung in langen Sitzungen ist unsicher, ob es richtig zählt.

## Naheliegende Ansätze

**Freigaben nur noch einzeln.** Sitzungen werden zäh, die pauschale Freigabe kommt schnell zurück.

## Diskussionsfragen

1. Welche Befehle braucht der Agent ohne Rückfrage, welche nie ohne?
2. Wie trennt man beide, ohne die Sitzung zäh zu machen?
3. Was sollte der Agent nach einem Lauf zurückbekommen?
4. Wo haben Sie so etwas?
