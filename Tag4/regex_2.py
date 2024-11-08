import re

regex = r"^(MODUL_.) = (.*)$"

test_str = ("# Ein Text der auch matcht\n"
	"print(\"Ich lade!!!\")\n"
	"MODUL_X = 99\n"
	"MODUL_Y = 99\n"
	"MODUL_Z = 99\n"
	"def machWas():\n"
	"    return 2 * 2")

matches = re.finditer(regex, test_str, re.MULTILINE)

for matchNum, match in enumerate(matches, start=1):
    
    print ("Match {matchNum} was found at {start}-{end}: {match}".format(matchNum = matchNum, start = match.start(), end = match.end(), match = match.group()))
    
    for groupNum in range(0, len(match.groups())):
        groupNum = groupNum + 1
        
        print ("Group {groupNum} found at {start}-{end}: {group}".format(groupNum = groupNum, start = match.start(groupNum), end = match.end(groupNum), group = match.group(groupNum)))