import sys
import tempfile
import unittest
from pathlib import Path
from contextlib import redirect_stdout
from io import StringIO
import random

BASE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(BASE))
from engine import load_questions, select_questions, score
from storage import Storage


class TestCatalog(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.questions = load_questions(BASE / "fragen")

    def test_count_and_days(self):
        self.assertEqual(len(self.questions), 120)
        for day in range(1, 5):
            self.assertEqual(sum(q.day == day for q in self.questions), 30)

    def test_outputs(self):
        for q in self.questions:
            if q.kind == "output":
                with self.subTest(q=q.id):
                    out = StringIO()
                    with redirect_stdout(out):
                        exec(q.code, {})
                    self.assertTrue(q.correct(out.getvalue()))

    def test_fill(self):
        for q in self.questions:
            if q.kind == "fill":
                with self.subTest(q=q.id):
                    for a in q.answers:
                        compile(q.code.replace("___", a), q.id, "exec")
                        self.assertTrue(q.correct(a))
                    self.assertFalse(q.correct("nicht_die_loesung"))

    def test_choice(self):
        for q in self.questions:
            if q.kind in ("single", "multiple"):
                with self.subTest(q=q.id):
                    self.assertTrue(q.correct(list(reversed(q.answers))))
                    self.assertFalse(q.correct([]))
                    for i in set(range(len(q.options))) - set(q.answers):
                        self.assertFalse(q.correct([*q.answers, i]))

    def test_selection(self):
        result = select_questions(self.questions, {1, 2, 3, 4}, "Alle", "Alle", 20,
                                  rng=random.Random(1))
        self.assertEqual(len(set(q.id for q in result)), 20)
        for day in range(1, 5):
            self.assertEqual(sum(q.day == day for q in result), 5)
        self.assertEqual(select_questions(self.questions, set(), "Alle", "Alle", 20), [])

    def test_score_and_storage(self):
        q = self.questions[0]
        answer = {q.id: list(q.answers)}
        self.assertEqual(score([q], answer), {(q.day, q.topic): (1, 1)})
        with tempfile.TemporaryDirectory() as directory:
            store = Storage(Path(directory) / "test.sqlite")
            store.save("Lernmodus", [q], {})
            self.assertEqual(store.wrong_ids(), {q.id})
            store.save("Lernmodus", [q], answer)
            self.assertEqual(store.wrong_ids(), set())
            self.assertEqual(len(store.history()), 2)


if __name__ == "__main__":
    unittest.main()
