# Aufgabe: Ein einfaches Rechner-Programm
#
# Schritt 1:
#
# Benutzer gibt 2 Zahlen ein -> float, egl. und dt. Schreibweise erlaubt
# Benutzer gibt einen Operator ein (+ - * /)
# Die Rechenoperation wird ausgeführt, das Ergebnis ausgegeben
#
# Schritt 2: Der Benutzer kann das so lange laufen lassen, bis er exit eingibt,
# Es werden immer Einzelberechnungen ausgeführt
#
# Schritt 3: Und wenn der Benutzer Mist eingibt? -> dann kümmern wir und darum,
class IllegalOperatorError(Exception):
    pass

while True:
    # E
    try:
        zahl_1 = input("Zahl 1: ").replace(",", ".")
        zahl_2 = input("Zahl 2: ").replace(",", ".")

        zahl_1 = float(zahl_1)
        zahl_2 = float(zahl_2)

        operator = input("+ - * /:")
        if operator not in ["+", "-", "*", "/"]:
            raise IllegalOperatorError()

    # V
        ergebnis = None

        if operator == '+':
            ergebnis = zahl_1 + zahl_2
        elif operator == '-':
            ergebnis = zahl_1 - zahl_2
        elif operator == '*':
            ergebnis = zahl_1 * zahl_2
        elif operator == '/':
            ergebnis = zahl_1 / zahl_2

    # A
        print(f"{zahl_1} {operator} {zahl_2} = {ergebnis}")
    except ValueError:
        print("Fehlerhafte Eingabe:", zahl_1, zahl_2)
    except ZeroDivisionError:
        print("Division durch 0, abgebrochen", zahl_1, zahl_2)
    except IllegalOperatorError:
        print("Unbekannter Operator:", operator)

    if input("Weiter/Ende? ").lower() == "ende":
        break

print("Auf Wiedersehen")
