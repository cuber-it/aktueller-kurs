#!/usr/bin/env python3
import sys

def main():
    lfd_nr = 1
    # Zeilen von stdin lesen
    for line in sys.stdin:
        # Beispielverarbeitung: Leerzeichen am Ende entfernen
        processed_line = line.rstrip()
        
        # Ausgabe an stdout
        print(f"{lfd_nr:>5}: {processed_line}")
        lfd_nr += 1
        
if __name__ == "__main__":
    main()
