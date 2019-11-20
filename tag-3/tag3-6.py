from xml.dom import minidom

mydoc = minidom.parse('books.xml')

#authors = mydoc.getElementsByTagName('author')
books = mydoc.getElementsByTagName('book')

for book in books:
    print(book.attributes["id"].value)
    for node in book.childNodes:
       print(node)


