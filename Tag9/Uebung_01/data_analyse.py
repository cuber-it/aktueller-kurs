import pandas as pd
import numpy as np

path = r"E:\Workspaces\Kurse\aktueller-kurs\Material\WA_Fn-UseC_-Telco-Customer-Churn.csv"



def data_repair(df):
    # Das geht sicher auch in pandas oder numpy, aber wir haben es selbst gemacht, da einfacher :-D
    daten = df.to_dict(orient="records")
    for row in daten:
        try:
            row["TotalCharges"] = float(row["TotalCharges"])
        except ValueError:
            row["TotalCharges"] = int(row["tenure"]) * float(row["MonthlyCharges"])
    return pd.DataFrame(daten)

def filter_missing_values(df): # .loc um copy-Warning zu vermeiden
    df = df.loc[df["TotalCharges"] != " "].copy()
    df["TotalCharges"] = pd.to_numeric(df["TotalCharges"])
    return df

# Aufgabe:
# tenuer = Laufzeit, Monthly, Total Charges extrahieren
# Welche Datentypen liegen im df vor für die drei
# Warum könnte es "Probleme" geben?
# Wo gibt es sie?
# Was ist die Ursache?
# Reparieren Sie es, wenn es Probleme gibt
df = pd.read_csv(path)
df_kosten = df[["tenure", "MonthlyCharges", "TotalCharges"]]

print(df_kosten.dtypes)
print(df_kosten[df_kosten['TotalCharges'] == ' '].index)

df_kosten_1 = filter_missing_values(df_kosten)
df_kosten_2 = data_repair(df_kosten)

print(len(df_kosten_1))
print(len(df_kosten_2))
