import requests
import lxml.html
import pprint

target = "https://docs.python.org/3.1/howto/urllib2.html"
# requesting url
web_response = requests.get(target)

# building
element_tree = lxml.html.fromstring(web_response.text)
links = list(element_tree.iterlinks())
#pprint.pprint(links)
for l in links:
    if l[2].startswith("http"):
        print(l[2])

