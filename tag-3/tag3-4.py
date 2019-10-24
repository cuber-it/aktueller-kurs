import xmltodict
import xml.etree.ElementTree as ET
tree = ET.parse('daten.xml')
root = tree.getroot()

print(tree)

for child in root:
    for subchild in child:
        print(subchild.tag, subchild.attrib)
