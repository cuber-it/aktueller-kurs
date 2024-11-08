import re

def grep(pattern, text, **options):
    """
    Bildet die Funktionalität von egrep nach
    """
    occurrences = []
    regex = re.compile(pattern, re.MULTILINE)

    lines = text.splitlines()
    for line_number, line in enumerate(lines, start=1):
        for match in regex.finditer(line):
            occurrences.append({
                'line_number': line_number,
                'start': match.start(),
                'end': match.end(),
                'match': match.group()
            })
    return occurrences


if __name__ == '__main__':
    """
    Nachbau des egrep wird eingesetzt

    Aufruf: patternTools.py pattern datei
    """
    def read(fname):
        with open(fname) as fd:
            return fd.read()

    import sys
    import os

    if len(sys.argv) != 3:
        print(f"usage: {os.path.basename(sys.argv[0])} pattern file", file=sys.stderr)
        exit(1)
    
    pattern = sys.argv[1]
    file    = sys.argv[2]

    text    = read(file)
    matches = grep(pattern, text)

    for match in matches:
        print(f"{match.get('line_number', '-')}:", match['match'])