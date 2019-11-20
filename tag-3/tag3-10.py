import xmltodict
import pprint

d = xmltodict.parse(open("books.xml", "r+b"))

pprint.pprint(d)