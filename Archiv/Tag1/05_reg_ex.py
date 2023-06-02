import re

#
# Regulärer Ausdruck, um alle validen ipv4 Adressen zu matchen
#
regex = r"(?:(?:25[0-5]|2[0-4]\d|[01]?\d\d?)\.){3}(?:25[0-5]|2[0-4]\d|[01]?\d\d?)"

test_str = open(r"E:\Workspaces\Kurse\aktueller-kurs\Material\Sample.log").read()

matches = re.finditer(regex, test_str, re.MULTILINE)

for matchNum, match in enumerate(matches, start=1):

    print (f"Match {matchNum:>5} was found at {match.start():<10}-{match.end():>10}: {match.group()}")

    for groupNum in range(0, len(match.groups())):
        groupNum = groupNum + 1

        print ("Group {groupNum} found at {start}-{end}: {group}".format(groupNum = groupNum, start = match.start(groupNum), end = match.end(groupNum), group = match.group(groupNum)))
