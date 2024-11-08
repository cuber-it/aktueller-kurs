import re
from typing import Iterator, Match
from pathlib import Path

def search_file_in_chunks(
    filepath: str | Path, 
    pattern: str, 
    chunk_size: int = 1024 * 1024  # 1MB chunks
) -> Iterator[Match]:
    """
    Durchsucht eine große Datei nach einem regex Pattern, indem die Datei in Chunks eingelesen wird.
    
    Args:
        filepath: Pfad zur Datei
        pattern: Regex-Pattern als String
        chunk_size: Größe der Chunks in Bytes (default: 1MB)
        
    Yields:
        Match-Objekte für jeden Fund
    """
    # Kompilieren des Regex-Patterns für bessere Performance
    regex = re.compile(pattern)
    
    # Überlappung definieren um Matches an Chunk-Grenzen zu finden
    overlap = 1024  # 1KB Überlappung
    
    with open(filepath, 'r', encoding='utf-8') as file:
        # Position im File merken
        file_pos = 0
        # Letzten Teil des vorherigen Chunks speichern
        last_chunk_tail = ''
        
        while True:
            # Zurück zur Position vor der Überlappung springen
            if file_pos > overlap:
                file.seek(file_pos - overlap)
            
            # Chunk einlesen
            chunk = file.read(chunk_size)
            
            # Wenn keine Daten mehr, Ende der Datei erreicht
            if not chunk:
                break
            
            # Aktuellen Chunk mit Ende des letzten Chunks kombinieren
            search_text = last_chunk_tail + chunk
            
            # Alle Matches im kombinierten Text finden
            for match in regex.finditer(search_text):
                # Nur Matches ausgeben, die nicht in der Überlappung liegen
                if match.start() >= len(last_chunk_tail):
                    yield match # <=== yield erhält die Funktion für den n Durchlauf, return beendet alles
            
            # Position aktualisieren
            file_pos = file.tell()
            # Ende des aktuellen Chunks für nächste Iteration speichern
            last_chunk_tail = chunk[-overlap:] if len(chunk) >= overlap else chunk

# Beispielnutzung
if __name__ == "__main__":
    # Beispiel: Suche nach E-Mail-Adressen
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    
    filepath = "large_file.txt"
    for match in search_file_in_chunks(filepath, email_pattern):
        print(f"Found email: {match.group(0)}")