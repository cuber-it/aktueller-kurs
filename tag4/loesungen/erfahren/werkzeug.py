"""Referenzlösung: Textfunktionen ohne Ein- oder Ausgabe bereitstellen."""


def ist_palindrom(text):
    """Prüft den Text ohne Großschreibung und Leerraum; leerer Text ergibt False."""
    ohne_leerraum = "".join(text.split())
    normalisiert = ohne_leerraum.casefold()
    if not normalisiert:
        return False
    return normalisiert == normalisiert[::-1]


def vokale_zaehlen(text):
    """Zählt a, e, i, o, u sowie ä, ö, ü, unabhängig von Großschreibung."""
    anzahl = 0
    for zeichen in text.casefold():
        if zeichen in "aeiouäöü":
            anzahl += 1
    return anzahl


if __name__ == "__main__":
    for wort in ["Anna", "Otto", "Python"]:
        print(wort, ist_palindrom(wort), vokale_zaehlen(wort))
