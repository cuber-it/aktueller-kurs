import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.graph_objs as go

path = r"E:\Workspaces\Kurse\aktueller-kurs\Material\HistoricalQuotes.csv"
# Read CSV data into a pandas DataFrame
df = pd.read_csv(path)

df.rename(columns=lambda x: x.strip(), inplace=True)

# Remove '$' sign from 'Close/Last' and convert to float
df['Close/Last'] = df['Close/Last'].replace({'\$': ''}, regex=True).astype('float')

# Convert 'Date' column to datetime format
df['Date'] = pd.to_datetime(df['Date'])

# Dash app
app = dash.Dash(__name__)

# Layout
app.layout = html.Div([
    dcc.DatePickerRange(
        id='date-picker',
        start_date=df['Date'].min(),
        end_date=df['Date'].max()
    ),
    dcc.Graph(id='graph'),
])

# Callback
@app.callback(
    Output('graph', 'figure'),
    [Input('date-picker', 'start_date'),
     Input('date-picker', 'end_date')]
)
def update_graph(start_date, end_date):
    dff = df.loc[(df['Date'] >= start_date) & (df['Date'] <= end_date)]
    figure = go.Figure(
        data=[go.Scatter(x=dff['Date'], y=dff['Close/Last'], mode='lines')],
        layout=go.Layout(title='Closing Price Over Time', showlegend=False)
    )
    return figure

if __name__ == '__main__':
    app.run_server(debug=True)
