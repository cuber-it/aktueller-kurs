import requests
import re

# Get the webpage content
url = "https://www.otto.de"
response = requests.get(url)

# Find all 'a' links
links = re.findall('<a href="(.*?)">', response.text, re.DOTALL)

for link in links:
    print(link)
