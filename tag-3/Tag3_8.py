#import xml.etree.ElementTree as ET
#tree = ET.parse('books.xml')
#root = tree.getroot()
#for child in root:
#   print(child.tag, child.attrib)

import xmltodict
import pprint

d = xmltodict.parse(open("books.xml", "r+b"))
print("Autor|Titel|Preis")
for book in d["catalog"]["book"]:
   print("{}|{}|{}".format(
      book["author"],
      book["title"],
      book["price"].replace(".", ",")))