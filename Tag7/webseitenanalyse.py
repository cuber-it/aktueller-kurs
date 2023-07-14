import requests
import bs4

response = requests.get("https://www.uc-it.de")
#print(response.status_code)
#print(response.text[:1000])
soup = bs4.BeautifulSoup(response.text, 'html.parser')
#print(soup.contents)
print([link.get("href") for link in soup.find_all("a")])
