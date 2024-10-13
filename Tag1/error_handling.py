import traceback

a = None
b = 12345
error_code = 0

user_input = input("Enter a number: ")

try:
    value = int(user_input)

    a = b / value
    print("Ergebnis:", a)
except ValueError:
    print(f"{user_input} is not an integer.")
    error_code = 1
except ZeroDivisionError:
    print(f"Keine Division durch 0!")
    error_code = 2
except Exception as e:
    print("An error occurred:")
    print(traceback.format_exc())
    error_code = 99
finally:
    print("Bei Erfolg/Fehler: aufräumen!")

if error_code != 0:
    print("Fehlerabbruch")
    exit(error_code)

print("Erfolgreich")
exit(error_code)