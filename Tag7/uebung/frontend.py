import requests

# Set the base URL of your Flask server
base_url = 'http://localhost:5000'

while True:
    # Set up your tipp
    tipp = input("Tipp in der Form 1.2.3.4.5.6 oder EXIT:")
    if tipp == "EXIT":
        break

    try:
        response = requests.post(f'{base_url}/tipp', json={"tipp": tipp})
        print(f"Response to tipp: {response.json()}")

        # Start the game
        response = requests.post(f'{base_url}/play')
        print(f"Response to play: {response.json()}")

        # Get the result
        response = requests.get(f'{base_url}/result')
        print(f"Response to result: {response.json()}")
    except Exception as e:
        print("Problem: ", e)
