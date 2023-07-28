import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import dash
import dash_core_components as dcc
from dash import html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.graph_objs as go

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

def set_0_for_missing(df):
    df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce").fillna(0)
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
df_kosten_3 = set_0_for_missing(df_kosten)

print(len(df_kosten_1))
print(len(df_kosten_2))
print(len(df_kosten_3))

# mit Grafik:
# 1. tenure vs TotalCharge X-Achse vs Y-Achse - z.B. als Linie oder Scatterplot
# 2. Monthly vs Total
# 3. tenure vs. Monthly
# a: mit matplotlib
def show_plot(df, col_a, col_b, header=None, x_label=None, y_label=None):
    if not x_label:
        x_label = col_a
    if not y_label:
        y_label = col_b
    if not header:
        header = f"{col_a} vs {col_b}"

    plt.figure(figsize=(14,7))
    #ax = plt.gca()  # Get the current axes instance
    #ax.yaxis.set_major_locator(ticker.MaxNLocator(integer=True))
    plt.scatter(df[col_a], df[col_b])
    plt.title(header)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.show()

#show_plot(df_kosten_2, "tenure", "TotalCharges")

df = df_kosten_2 # damit ich überall df schreiben kann

app = dash.Dash(__name__)

min_charge = df['TotalCharges'].min()
max_charge = df['TotalCharges'].max()

app.layout = html.Div([
    dcc.Slider(
        id='charge-slider',
        min=min_charge,
        max=max_charge,
        step=0.5,
        value=min_charge,
        marks={i: '{}'.format(i) for i in range(int(min_charge), int(max_charge)+1)},
    ),
    dcc.Graph(id='graph'),
])

@app.callback(
    Output('graph', 'figure'),
    [Input('charge-slider', 'value')]
)
def update_graph(charge_range):
    start_charge, end_charge = charge_range - 100, charge_range + 100
    dff = df.loc[(df['TotalCharges'] >= start_charge) & (df['TotalCharges'] <= end_charge)]
    figure = go.Figure(
        data=[go.Scatter(x=dff['tenure'], y=dff['TotalCharges'], mode='markers')],
        layout=go.Layout(title='TotalCharges Over Tenure', showlegend=True)
    )
    return figure

if __name__ == '__main__':
    app.run_server(debug=True)
