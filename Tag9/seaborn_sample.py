import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

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
    plt.figure(figsize=(10,6))
    sns.lineplot(data=df, x="Date", y="Close/Last")
    plt.title('Closing Price Over Time')
    plt.xlabel('Date')
    plt.ylabel('Close Price')

    # Save the plot to a file if required
    if save_to_file:
        plt.savefig("stock_prices.jpg")
    else:
        plt.show()  # Display the plot

# Call the function without saving to a file
plot_stock_data(path, "2019-06-01", "2019-08-31", save_to_file=False)

# Call the function and save to a file
plot_stock_data(path, "2019-06-01", "2019-08-31", save_to_file=True)
