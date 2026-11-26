import stock_tools

def main():
    stock_data = stock_tools.read_stock_data("materialien/HistoricalQuotes.csv")
    profit = stock_tools.calc_profits_by_timeinterval(stock_data, "01.01.2026", "26.11.2026")
    print(profit)

main()
