import requests

# Set the base URL of your Flask server
base_url = 'http://localhost:5000'

# Set up your tipp
tipp = "1.2.3.4.5.6"
response = requests.post(f'{base_url}/tipp', json={"tipp": tipp})
print(f"Response to tipp: {response.json()}")

# Start the game
response = requests.post(f'{base_url}/play')
print(f"Response to play: {response.json()}")

# Get the result
response = requests.get(f'{base_url}/result')
print(f"Response to result: {response.json()}")

