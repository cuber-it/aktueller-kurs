import pandas as pd
import matplotlib.pyplot as plt

path = r"E:\Workspaces\Kurse\aktueller-kurs\Material\HistoricalQuotes.csv"

import pandas as pd
import matplotlib.pyplot as plt

def plot_stock_data(file_path, start_date, end_date, file_name=None):
    # Read CSV data into a pandas DataFrame
    df = pd.read_csv(file_path)

    # remove empty spaces
    df.rename(columns=lambda x: x.strip(), inplace=True)
    df['Close/Last'] = df['Close/Last'].replace({'\$': '', ',': ''}, regex=True).astype(float)


    # Convert 'Date' column to datetime format and sort by date
    df['Date'] = pd.to_datetime(df['Date'])

    # Filter data for the date range
    mask = (df['Date'] >= start_date) & (df['Date'] <= end_date)
    df = df.loc[mask]

    # Plot closing prices over time
    plt.figure(figsize=(14,7))
    plt.plot(df['Date'], df['Close/Last'])
    plt.title('Closing Price Over Time')
    plt.xlabel('Date')
    plt.ylabel('Close Price')

    if file_name:
        plt.savefig(file_name, bbox_inches='tight')
        plt.plot()
    else:
        plt.show()





# Call the function with the path to your CSV file
plot_stock_data(path, '2011-01-01', '2019-12-31', "Apple.jpg")
