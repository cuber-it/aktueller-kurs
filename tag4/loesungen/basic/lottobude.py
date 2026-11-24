"""Referenzlösung: Eingabeprüfung, Ziehung und Vergleich als Funktionen."""

import random


def pruefe_tipp(text):
    """Liest sechs verschiedene ganze Zahlen von 1 bis 49 aus einem Text."""
    teile = text.split()
    if len(teile) != 6:
        raise ValueError("Bitte genau sechs Zahlen eingeben.")
    try:
        zahlen = [int(teil) for teil in teile]
    except ValueError as fehler:
        raise ValueError("Alle Angaben müssen ganze Zahlen sein.") from fehler
    if any(zahl < 1 or zahl > 49 for zahl in zahlen):
        raise ValueError("Alle Zahlen müssen zwischen 1 und 49 liegen.")
    if len(set(zahlen)) != 6:
        raise ValueError("Zahlen dürfen nicht doppelt vorkommen.")
    return sorted(zahlen)


def ziehe_zahlen():
    """Liefert sechs verschiedene Zahlen aufsteigend sortiert."""
    return sorted(random.sample(range(1, 50), 6))


def ermittle_treffer(tipp, ziehung):
    """Liefert die gemeinsamen Zahlen zweier bereits gültiger Tipps."""
    return sorted(set(tipp) & set(ziehung))


def main():
    """Behandelt Eingabefehler an der Benutzeroberfläche."""
    try:
        tipp = pruefe_tipp(input("Sechs Zahlen, mit Leerzeichen getrennt: "))
    except ValueError as fehler:
        print(f"Ungültiger Tipp: {fehler}")
        return
    ziehung = ziehe_zahlen()
    treffer = ermittle_treffer(tipp, ziehung)
    print("Tipp:", tipp)
    print("Ziehung:", ziehung)
    print("Richtige:", treffer)
    print("Treffer:", len(treffer))


if __name__ == "__main__":
    main()
