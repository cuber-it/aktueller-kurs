import re

regex = r"(https?)://([+-ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789._~:/?#\[\]@!$&'()*,;=]+)"

test_str = ("Check out https://www.example.com and http://www.another-example.com anywhere in the text\n"
	"https://stackoverflow.com/questions/1547899/which-characters-make-a-url-invalid\n"
	"https://pythontutor.com/render.html#mode=edit\n"
	"https://www.oreilly.com/library/view/regular-expressions-cookbook/9780596802837/ch07s16.html")

matches = re.finditer(regex, test_str, re.MULTILINE)

for matchNum, match in enumerate(matches, start=1):

    print ("Match {matchNum} was found at {start}-{end}: {match}".format(matchNum = matchNum, start = match.start(), end = match.end(), match = match.group()))

    for groupNum in range(0, len(match.groups())):
        groupNum = groupNum + 1

        print ("Group {groupNum} found at {start}-{end}: {group}".format(groupNum = groupNum, start = match.start(groupNum), end = match.end(groupNum), group = match.group(groupNum)))
