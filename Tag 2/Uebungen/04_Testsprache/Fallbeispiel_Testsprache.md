# Fallbeispiel · Tests, die nur ihre Autoren lesen

**Situationstyp:** Tests sind technisch sauber, aber die fachliche Aussage steckt zwischen Bedienungsschritten. Wer die Fachlichkeit beurteilen soll, findet sie schwer.

---

## Ausgangslage

Die GNSS-Einstellungen eines Terminals bieten drei Quellen, danach zeigt ein Diagnosemenü Satellitenwerte. Für jede Quelle gibt es Tests mit simulierten Fahrten. Die Tests nutzen Helper für Menüwege und Prüfungen und greifen für die Auswahl der Quelle direkt auf Controls zu.

## Wie es gewachsen ist

Lange Wege wurden in Helper gekapselt, kurze Schritte blieben im Test. Neue Tests entstanden durch Kopieren und Ändern eines Attributnamens.

## Was auffällt

**Die fachliche Aussage steht im Attributnamen.** Welche Quelle ein Test wählt, zeigt `masetth.submenu_gnss_source.sae_j1939_btn`. Das Enum `GnssSource` gibt es, die Tests nutzen es nicht.

**Die Prüfung ist sichtbar, die Einstellung nicht.** `assert_gnss_diagnostics_values(gnss_ref)` ist verständlich, die Auswahl der Quelle nicht.

**Positionsargumente sind mehrdeutig.** `test_wrapper(None, False)` lässt sich leicht als „ohne Mock-Backend“ lesen; gemeint ist `replace_data=False`.

## Naheliegende Ansätze

**Kommentare über jedem Block.** Beim Kopieren werden sie leicht nicht angepasst.

**Eine Liste der Tests außerhalb des Codes.** Sie veraltet mit jeder Änderung.

## Diskussionsfragen

1. Warum hilft das vorhandene Enum `GnssSource` heute nicht?
2. Welche Zeilen müsste die Fachabteilung lesen können, welche nicht?
3. Wann wird eine fachliche Operation zu viel?
4. Wo haben Sie so etwas?
