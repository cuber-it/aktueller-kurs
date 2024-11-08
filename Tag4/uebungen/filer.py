import os
import os.path
import sys

def file_collector(directory, file_extension):
    """
    Geht durch directory und subdirectories und findet Dateien mit der  extension, bibt die Liste der Pfade zurück
    """
    matched_files = []
    
    # Durchlaufe den Verzeichnisbaum rekursiv
    for curdir, _, files in os.walk(directory):
        for file in files:
            # Prüfe, ob die Datei die gesuchte Erweiterung hat
            if file.endswith(file_extension):
                # Baue den vollständigen Pfad der Datei
                full_path = os.path.join(curdir, file)
                matched_files.append(full_path)
                
    return matched_files

if __name__ == "__main__":
    dir = sys.argv[1]
    ext = sys.argv[2]

    found = file_collector(dir, ext)

    print("\n".join(found))