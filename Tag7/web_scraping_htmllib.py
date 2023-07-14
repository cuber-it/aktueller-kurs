import requests
from lxml import html

# Get the webpage content
url = "http://otto.de"
response = requests.get(url)

# Parse the HTML content
tree = html.fromstring(response.content)

# Find all 'a' links
links = tree.xpath('//a/@href')

for link in links:
    print(link)
