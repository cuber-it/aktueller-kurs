from bs4 import BeautifulSoup
import requests

url = 'http://otto.de'
response = requests.get(url)

# Parse the HTML content of the page with BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

# Find all 'a' tags and print their href attribute
for link in soup.find_all('a'):
    print(link.get('href'))
