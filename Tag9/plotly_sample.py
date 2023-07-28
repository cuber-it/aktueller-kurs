import pandas as pd
import plotly.graph_objects as go

path = r"E:\Workspaces\Kurse\aktueller-kurs\Material\HistoricalQuotes.csv"

def plot_stock_data(file_path, start_date, end_date, save_to_file=False):
    # Read CSV data into a pandas DataFrame
    df = pd.read_csv(file_path)

    # remove empty spaces
    df.rename(columns=lambda x: x.strip(), inplace=True)

    # Convert 'Date' column to datetime format
    df['Date'] = pd.to_datetime(df['Date'])

    # Remove dollar sign and convert to float
    df['Close/Last'] = df['Close/Last'].replace({'\$': '', ',': ''}, regex=True).astype(float)

    # Filter data between start and end dates
    mask = (df['Date'] > start_date) & (df['Date'] <= end_date)
    df = df.loc[mask]

    # Create plot
    fig = go.Figure(data=[go.Scatter(x=df['Date'], y=df['Close/Last'], mode='lines')])
    fig.update_layout(title='Closing Price Over Time', xaxis_title='Date', yaxis_title='Close Price')

    # Save the plot to a file if required
    if save_to_file:
        fig.write_image("stock_prices.jpg")
    else:
        fig.show()  # Display the plot

# Call the function without saving to a file
plot_stock_data(path, "2019-06-01", "2019-08-31", save_to_file=False)

# Call the function and save to a file
plot_stock_data(path, "2019-06-01", "2019-08-31", save_to_file=True)
