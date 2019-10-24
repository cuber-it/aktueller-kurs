import urllib.request
import json
import pprint

with urllib.request.urlopen('http://dummy.restapiexample.com/api/v1/employees') as response:
    data = response.read()

data = json.loads(data)
pprint.pprint(data)
