# Creating a tuple of squares of even numbers from 0 to 9
#squares = (x**2 for x in range(10) if x % 2 == 0)
#
#print(type(squares))  # Output: (0, 4, 16, 36, 64)
#
#
#def read_file(filename):
#    with open(filename) as file:#
#
#        for line in file:
#            yield line.strip()

#for line in read_file("example.txt"):
#    print(line)

#def even_numbers():
#    for i in range(0, 11, 2):
#        print(f"Ausführung für {i}")
#        yield { "wert": i }


#for v in even_numbers():
#    print(v)

#x = even_numbers()
#print(next(x))
#print(next(x))
#print(next(x))
#print(next(x))


def read_file_in_chunks(filename, chunk_size=1024):
    with open(filename, "rb") as file:
        while True:
            chunk = file.read(chunk_size)
            if not chunk:
                break
            yield chunk

for chunk in read_file_in_chunks(r"E:\Workspaces\Kurse\aktueller-kurs\Material\HistoricalQuotes.csv"):
    print(len(chunk))
