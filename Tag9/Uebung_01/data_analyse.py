import pandas as pd
path = r"E:\Workspaces\Kurse\aktueller-kurs\Material\WA_Fn-UseC_-Telco-Customer-Churn.csv"


df = pd.read_csv(path)
print(df)

# Aufgabe:
# tenuer = Laufzeit, Monthly, Total Charges extrahieren
# Welche Datentypen liegen im df vor für die drei
# Warum könnte es "Probleme" geben?
# Wo gibt es sie?
# Was ist die Ursache?
# Reparieren Sie es, wenn es Probleme gibt
df_kosten = df[["tenure", "MonthlyCharges", "TotalCharges"]]
print(df_kosten)
