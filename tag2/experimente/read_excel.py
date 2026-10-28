import pandas as pd
import sqlite3

datei = r"/home/ucuber/Workspace/kurse/kurse/aktueller-kurs/materialien/aapl.xlsx"

# Erstes Tabellenblatt lesen; erste Zeile wird als Spaltenüberschrift verwendet
df = pd.read_excel(datei, sheet_name=0)

# Vollständig ausgeben, ohne zusätzlichen Zeilenindex
#print(df.to_string(index=False))

# als JSON bereitstellen
df.to_json(
    "apple_kursdaten.json",
    orient="records",
    date_format="iso",
    force_ascii=False,
    indent=2,
)

df.to_xml(
    "apple_kursdaten.xml",
    index=False,
    root_name="kursdaten",
    row_name="kurs",
    encoding="utf-8",
    parser="etree",
)

with sqlite3.connect("kursdaten.db") as connection:
    df.to_sql(
        "kurse",
        connection,
        if_exists="replace",
        index=False,
    )
