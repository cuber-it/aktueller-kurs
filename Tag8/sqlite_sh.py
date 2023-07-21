# Aufurf: python sqlite_sh.py datenbankdateiname [--h_out Filename][--h_in Filename]

# Annahme der argumente
# Anpassung der Dateiendung -> datebankdateiname.sqlite
# Check dass Datei existiert

# connection aufbauen

### Loop bis ".exit" eingegeben
#
# Kommando ausführe - Fehler einfangen
# Bei Erfolg Ausgabe des ERgebnisse: status [und z.B. Datensätze bei SELECT]

# importvorschläge:
# argparse
# sqlite3

import argparse
import sqlite3


class SqliteShell:
    def __init__(self, connection_string):
        self.connection_string = connection_string
        self.connection = None
        self.cursor = None
        self.last_command = None
        self.history = []

    def connect(self, connection_string=None):
        if connection_string:
            self.connection_string = connection_string
        try:
            self.connection = sqlite3.connect(self.connection_string)
            self.cursor = self.connection.cursor()
        except Exception as e:
            print(e)
        return self

    def close(self):
        if self.connection:
            try:
                self.connection.close()
            except Exception as e:
                print(e)
            return self

    def _execute(self, commit=False):
        self.history.append(self.last_command)
        self.cursor.execute(self.last_command)
        if commit: self.connection.commit()

    def execute(self, command=None):
        if command:
            self.last_command = command
        try:
            if "SELECT" in self.last_command.upper():
                self._execute()
                return self.cursor.fetchall()
            elif "INSERT" in self.last_command.upper():
                self._execute(commit=True)
                return [ f"Total Changes: {self.connection.total_changes}" ]
            elif "DELETE" in self.last_command.upper():
                self._execute(commit=True)
                return [ f"Total Changes: {self.connection.total_changes}" ]
            else:
                self._execute()
                return [ "Erfolgreich "]
        except Exception as e:
            return [ f"Error: {e}"]


def parse_args():
    parser = argparse.ArgumentParser(description='SqlLite Shell')
    parser.add_argument('database_connection_string', type=str, help='The database name.')
    parser.add_argument('--h_out', type=str, help='The output history file name.')
    parser.add_argument('--h_in', type=str, help='The input history file name.')
    return parser.parse_args()

if __name__ == "__main__":
    import os

    args = parse_args()

    connection_string = args.database_connection_string + ".sqlite"

    if not os.path.exists(connection_string):
        print(f"Existiert nicht: {connection_string} - wird angelegt")

    sh = SqliteShell(connection_string)

    while True:
        cmd = input("Enter SQL or internal Command: ")
        if cmd == ".exit":
            break
        elif cmd == ".connect":
            sh.connect()
        elif cmd == ".close":
            sh.close()
        elif cmd == ".history":
            for id, line in enumerate(sh.history):
                print(f"{id:>3}: {line}")
        else:
            result = sh.execute(cmd)
            print(result)
