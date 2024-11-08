import requests
from bs4 import BeautifulSoup

# URL der Commerzbank-Seite
url = "https://www.commerzbank.de"

try:
    # HTML-Inhalt der Seite abrufen
    response = requests.get(url)
    response.raise_for_status()  # Fehler auslösen, falls die Anfrage fehlschlägt

    # BeautifulSoup-Objekt erstellen
    soup = BeautifulSoup(response.text, 'html.parser')

    # Alle Links finden und ausgeben
    print("Liste aller Links auf der Seite:")
    for link in soup.find_all('a', href=True):
        print(link['href'])

except requests.RequestException as e:
    print(f"Fehler beim Abrufen der Seite: {e}")