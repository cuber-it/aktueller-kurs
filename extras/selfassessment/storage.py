"""Lokale Ergebnisdatenbank; keine personenbezogenen Daten."""
import json
import sqlite3
from contextlib import closing
from datetime import datetime, timezone
from pathlib import Path


class Storage:
    def __init__(self, path):
        self.path = Path(path)
        self.path.parent.mkdir(parents=True, exist_ok=True)
        with closing(sqlite3.connect(self.path)) as db, db:
            db.execute("""CREATE TABLE IF NOT EXISTS attempts (
                id INTEGER PRIMARY KEY,
                created TEXT NOT NULL, mode TEXT NOT NULL,
                correct INTEGER NOT NULL, total INTEGER NOT NULL
            )""")
            db.execute("""CREATE TABLE IF NOT EXISTS answers (
                attempt_id INTEGER NOT NULL REFERENCES attempts(id),
                question_id TEXT NOT NULL, response TEXT,
                correct INTEGER NOT NULL,
                PRIMARY KEY (attempt_id, question_id)
            )""")

    def save(self, mode, questions, answers):
        rows = [(q.id, json.dumps(answers.get(q.id), ensure_ascii=False),
                 int(q.id in answers and q.correct(answers[q.id]))) for q in questions]
        with closing(sqlite3.connect(self.path)) as db, db:
            cur = db.execute("INSERT INTO attempts(created,mode,correct,total) VALUES(?,?,?,?)",
                             (datetime.now(timezone.utc).isoformat(), mode, sum(r[2] for r in rows), len(rows)))
            db.executemany("INSERT INTO answers VALUES(?,?,?,?)",
                           [(cur.lastrowid, *row) for row in rows])

    def wrong_ids(self):
        with closing(sqlite3.connect(self.path)) as db:
            return {row[0] for row in db.execute("""
                SELECT a.question_id FROM answers a
                WHERE a.correct=0 AND a.attempt_id=(
                    SELECT MAX(b.attempt_id) FROM answers b WHERE b.question_id=a.question_id)
            """)}

    def history(self):
        with closing(sqlite3.connect(self.path)) as db:
            return db.execute("SELECT created,mode,correct,total FROM attempts ORDER BY id DESC LIMIT 50").fetchall()
