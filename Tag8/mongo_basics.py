from pymongo import MongoClient

# Establish a connection to the database.
# This will create the database if it doesn't exist.
client = MongoClient("mongodb://username:password@localhost:27017/")  # replace with your MongoDB connection string

# Access the database (this will create it if it doesn't exist).
db = client["example"]

# Access the collection (similar to a table in relational databases).
# This will create the collection if it doesn't exist.
stocks = db["stocks"]

# Insert a row of data.
stocks.insert_one({
    'date': '2006-01-05',
    'trans': 'BUY',
    'symbol': 'RHAT',
    'qty': 100,
    'price': 35.14
})

# Query some data.
result = stocks.find_one({'symbol': 'RHAT'})
print(result)

# Close the connection.
client.close()
