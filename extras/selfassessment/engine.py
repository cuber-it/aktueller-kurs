"""Fragenkatalog und Auswertung, unabhängig von der GUI."""
import ast
import json
import random
import tokenize
from dataclasses import dataclass
from io import StringIO
from pathlib import Path

@dataclass(frozen=True)
class Question:
    id: str
    day: int
    topic: str
    level: str
    kind: str
    prompt: str
    code: str
    options: tuple[str, ...]
    answers: tuple
    explanation: str

    def correct(self, answer):
        if self.kind in ("single", "multiple"):
            return set(answer) == set(self.answers)
        if not isinstance(answer, str):
            return False
        if self.kind == "fill":
            return any(tokens(answer) == tokens(a) for a in self.answers)
        return any(answer.strip("\n") == a.strip("\n") for a in self.answers)

    def solution(self):
        if self.kind in ("single", "multiple"):
            return "\n".join(self.options[i] for i in self.answers)
        return " / ".join(self.answers)


def tokens(value):
    """Leerraum außerhalb von Literalen ignorieren; niemals Eingaben ausführen."""
    try:
        return tuple((t.type, t.string) for t in tokenize.generate_tokens(StringIO(value.strip()).readline)
                     if t.type not in (tokenize.ENDMARKER, tokenize.NEWLINE, tokenize.NL))
    except (tokenize.TokenError, IndentationError):
        return None


def load_questions(directory):
    questions = []
    seen = set()
    for day in range(1, 5):
        path = Path(directory) / f"tag{day}.json"
        for item in json.loads(path.read_text(encoding="utf-8")):
            q = Question(day=day, options=tuple(item.get("options", [])),
                         answers=tuple(item["answers"]), code=item.get("code", ""),
                         **{k: item[k] for k in ("id", "topic", "level", "kind", "prompt", "explanation")})
            if q.id in seen or not q.prompt or not q.explanation or not q.answers:
                raise ValueError(f"Ungültige oder doppelte Frage: {q.id}")
            if q.level not in ("Grundlagen", "Anwendung", "Vertiefung"):
                raise ValueError(f"Unbekannte Stufe: {q.id}")
            if q.kind in ("single", "multiple"):
                if len(q.options) < 2 or len(set(q.options)) != len(q.options) or any(type(i) is not int or not 0 <= i < len(q.options) for i in q.answers):
                    raise ValueError(f"Ungültige Optionen: {q.id}")
                if len(set(q.answers)) != len(q.answers) or (q.kind == "single" and len(q.answers) != 1):
                    raise ValueError(f"Ungültige Lösung: {q.id}")
            elif q.kind in ("fill", "output"):
                if any(not isinstance(a, str) or not a.strip() for a in q.answers):
                    raise ValueError(f"Ungültige Textlösung: {q.id}")
                if q.kind == "fill" and (q.code.count("___") != 1 or any(tokens(a) is None for a in q.answers)):
                    raise ValueError(f"Ungültige Lücke: {q.id}")
            else:
                raise ValueError(f"Unbekannter Fragetyp: {q.id}")
            seen.add(q.id)
            questions.append(q)
    return questions


def select_questions(questions, days, topic, level, count, retry_ids=None, rng=None):
    pool = [q for q in questions if q.day in days and
            (topic == "Alle" or q.topic == topic) and
            (level == "Alle" or q.level == level) and
            (retry_ids is None or q.id in retry_ids)]
    rng = rng or random.Random()
    # Verteilt Fragen möglichst gleichmäßig auf gewählte Tage.
    groups = {day: [q for q in pool if q.day == day] for day in sorted(days)}
    for group in groups.values():
        rng.shuffle(group)
    result = []
    while len(result) < count and any(groups.values()):
        order = list(groups)
        rng.shuffle(order)
        for day in order:
            if groups[day] and len(result) < count:
                result.append(groups[day].pop())
    return result


def score(questions, answers):
    result = {}
    for q in questions:
        correct = q.id in answers and q.correct(answers[q.id])
        key = (q.day, q.topic)
        hit, total = result.get(key, (0, 0))
        result[key] = (hit + int(correct), total + 1)
    return result
