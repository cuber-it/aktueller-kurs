path = r"/home/ucuber/Workspace/kurse/aktueller-kurs/Material/lorem_ipsum_1000.txt"

with open(path) as fd:
    raw = fd.read().splitlines()

words = {}
characters = {}

for line in raw:
    line_words = line.replace(".", "").replace(",", "").split(" ")
    for word in line_words:
        word = word.replace(" ", "")
        words[word] = words.get(word, 0) + 1
        for char in list(word):
            characters[char] = characters.get(char, 0) + 1

print("Report: Worthäufigkeiten")
for k, v in sorted(words.items(), key=lambda item: item[1], reverse=True):
    print(f"{k:<20s}: {'*' * v} ({v})")

print("-" * 80, "\n")

print("Report: Zeichenhäufigkeiten")
for k, v in sorted(characters.items(), key=lambda item: item[1], reverse=True):
    print(f"{k:<4s}: {'#' * v} ({v})")
