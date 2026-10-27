while True:
    eingabe = input("Wert oder exit: ")
    if eingabe.lower() == "exit":
        break;

    try:
        ergebnis = 1 / int(eingabe)
        print("Ergbnis:", ergebnis)
    except ZeroDivisionError:
        pass
    except ValueError:
        print("Eingabe fehlerhaft:", eingabe)
    #finally:
    #    print("Kommt immer")
