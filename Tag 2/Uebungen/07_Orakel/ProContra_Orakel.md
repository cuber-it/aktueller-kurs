# Pro und Contra · Aktion und Prüfung trennen

Bewertet wird der Vorschlag aus dem Lösungspapier: Setzen und Prüfen getrennt, `expect_value` mit ausdrücklicher Umwandlung, Abbruch bei gescheiterter Aktion.

---

## Pro

**Die Ursache steht allein**
Bricht der Schritt nach „Keyboard didn't open“ ab, folgen keine vier Abweichungen.

**Keine versteckten Umwandlungen**
`parse=float` steht im Test. `bool` aus Text wird nicht versehentlich `True`.

**Rohwert in der Meldung**
Zeigt, was das Control geliefert hat.

**Weniger Folgefehler**
Bricht der Schritt nach einer gescheiterten Aktion ab, fehlen die drei Folgefehler.

---

## Contra

**Zwei Zeilen statt einer**
16 Stellen mit `set_setting=True` würden länger.

**Weniger Befunde je Lauf**
Ein Abbruch verhindert auch unabhängige Befunde im selben Schritt.

**Zwei Wege zu prüfen**
`UIElementTest` und `expect_value` nebeneinander.

**Aktionen müssen melden können**
Nicht jedes `set()` erkennt heute, dass es gescheitert ist.

---

## Bewertung

Der Vorschlag trägt, weil **die Analyse an einer Meldung scheiterte**, nicht an einem fehlenden Test.

Gegenprobe – *nur die Meldung von `UIElementTest` um den Rohwert erweitern, bleiben Nachteile?* Ja: Die Tastaturmeldung stünde weiter zwischen vier Folgefehlern.

**Die Grenzen:**

1. **Bestand.** 16 Stellen bleiben, bis sie angefasst werden.
2. **Abbruch pro Schritt.** Nicht pro Test, damit unabhängige Schritte weiterlaufen.
3. **Aktionen prüfen.** Welche `set()`-Varianten ihr Scheitern melden, muss erhoben werden.

---

## Diskussionsfragen

1. Wie viele Befunde je Lauf sind Ihnen wichtiger als eine klare Ursache?
2. Soll `expect_value` Teil von `UIElementTest` werden?
3. Welche `set()`-Varianten melden ihr Scheitern heute nicht?
4. Welche Regel schreiben Sie in den Standard?
