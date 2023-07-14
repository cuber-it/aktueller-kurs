import requests
import pprint

url = r"https://datausa.io/api/data?drilldowns=Nation&measures=Population"

r = requests.get(url)
if r.status_code == 200:
    pprint.pprint(r.json())
else:
    print("Failure")
