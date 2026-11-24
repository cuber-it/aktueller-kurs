"""Referenzlösung: Kursbelegungen mit Mengenoperationen auswerten."""

python_kurs = {"Anna", "Ben", "Cem", "Dora"}
sql_kurs = {"Ben", "Dora", "Emil"}
web_kurs = {"Anna", "Emil", "Frida"}

print("Mindestens ein Kurs:", sorted(python_kurs | sql_kurs | web_kurs))
print("Python und SQL:", sorted(python_kurs & sql_kurs))
print("Nur Python:", sorted(python_kurs - sql_kurs - web_kurs))
print("Genau Python oder SQL:", sorted(python_kurs ^ sql_kurs))
