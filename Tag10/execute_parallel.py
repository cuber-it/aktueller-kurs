import requests
import concurrent.futures

# Here's a list of URLs to fetch, but in your case it could be a list of 30,000+ URLs
urls = ["http://example.com", "http://example.org", "http://example.net"]

def fetch(url):
    """Function to send HTTP request and return the response"""
    response = requests.get(url)
    return response.text

# Using ThreadPoolExecutor as context manager
with concurrent.futures.ThreadPoolExecutor() as executor:
    # Start the load operations and mark each future with its URL
    future_to_url = {executor.submit(fetch, url): url for url in urls}

    for future in concurrent.futures.as_completed(future_to_url):
        url = future_to_url[future]
        try:
            data = future.result()
            print(f'Fetched data from {url}')
        except Exception as exc:
            print(f'{url} generated an exception: {exc}')

