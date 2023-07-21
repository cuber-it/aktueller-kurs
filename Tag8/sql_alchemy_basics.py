from sqlalchemy import create_engine, Table, MetaData, select

# Create an engine that connects to the sqlite database
engine = create_engine('sqlite:///example.db')

metadata = MetaData()

# define the table
stocks = Table('stocks', metadata, autoload_with=engine)

# Start a new connection
with engine.connect() as connection:
    # Insert a new row
    connection.execute(stocks.insert().values(date='2006-01-05', trans='BUY', symbol='RHAT', qty=100, price=35.14))

    # Execute a select statement
    s = select(stocks).where(stocks.c.symbol == 'RHAT')

    result = connection.execute(s)
    for row in result:
        print(row)
