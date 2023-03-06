import pickle

# Define a dictionary to be serialized
data = {
    "name": "John",
    "age": 30,
    "email": "john@example.com"
}

# Serialize the dictionary to a file
with open("data.pickle", "wb") as file:
    pickle.dump(data, file)

# Deserialize the dictionary from the file
with open("data.pickle", "rb") as file:
    loaded_data = pickle.load(file)

# Print the deserialized dictionary
print(loaded_data)
