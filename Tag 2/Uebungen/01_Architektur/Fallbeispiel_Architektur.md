# Fallbeispiel · Eine gute Struktur, die nirgends beschrieben ist

**Situationstyp:** Eine gewachsene Architektur ist sauber geschnitten, aber nicht aufgeschrieben. Wer sie nicht kennt, sucht Änderungen an der falschen Stelle.

---

## Ausgangslage

Ein Squish-Testframework für Terminals mit rund tausend Testfällen: Controls kapseln die Squish-Aufrufe, UI-Module beschreiben die Menüs, Helper fassen häufige Wege zusammen, ein Test-Wrapper sorgt für Vor- und Nachbereitung. Das Team kennt diese Aufteilung, aufgeschrieben ist sie nicht.

## Wie es gewachsen ist

Die ersten Tests riefen Squish direkt auf. Als sich Objektnamen häuften, entstanden Controls, als sich Menüwege wiederholten, Helper. Jede Schicht war eine Antwort auf ein konkretes Problem. Neue Teammitglieder lernen die Aufteilung aus bestehenden Tests und durch Fragen.

## Was auffällt

**Die Architektur ist auf Änderungen vorbereitet.** Jeder Real Name steht genau einmal, im UI-Modul. Ein geänderter `objectName` ist eine Zeile.

**Die Fehlermeldung zeigt nicht auf den Ort.** „Did not become accessible within 20000 milliseconds“ passt zu einem Timing-Problem ebenso wie zu einem geänderten Namen. Wer die Struktur nicht kennt, sucht im Testfall.

**Manche Aufgaben sind versteckt.** `Control.wait()` wechselt vor jedem Zugriff den Anwendungskontext und verbindet die Anwendung bei Bedarf neu. Am Namen ist das nicht erkennbar.

## Naheliegende Ansätze

**Eine Wiki-Seite „Wie schreibe ich einen Test“.** Sie beschreibt Imports, nicht, welche Schicht wofür zuständig ist.

**Pair Programming für neue Teammitglieder.** Hilft, dauert aber, und das Wissen bleibt beim jeweiligen Paar.

## Diskussionsfragen

1. Warum hilft eine gute Architektur wenig, wenn sie nicht beschrieben ist?
2. Was müsste eine Fehlermeldung enthalten, damit die Suche beim UI-Modul beginnt?
3. Welche Aufgaben erledigt eine Schicht in Ihrem Framework, ohne dass ihr Name darauf hinweist?
4. Wo haben Sie so etwas?
