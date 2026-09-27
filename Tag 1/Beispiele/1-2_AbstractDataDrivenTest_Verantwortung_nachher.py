"""1-2 · nachher · Lesen, Auswählen und Konfigurieren getrennt

Eine mögliche Richtung. Jede Aufgabe hat einen eigenen Ort:

- ``read_test_sets``: macht aus Datensätzen Testsätze (Dateiformat)
- ``TestSetSelection``: wählt nach Tags und ergänzt eine Zufallsauswahl (Auswahlregel)
- ``DataDrivenTestConfig``: hält nur Werte (Konfiguration)

Beim Erzeugen passiert nichts außer dem Speichern von Werten. Wie die Teile
zusammenfinden und wer sie übergibt, ist Thema von 1-5.
"""
import random
from dataclasses import dataclass, field
from typing import Dict, Iterable, List, Mapping, Set, Tuple


@dataclass(frozen=True)
class TestSet:
    display_name: str
    tags: Tuple[str, ...] = ()


def read_test_sets(records: Iterable[Mapping[str, str]]) -> List[TestSet]:
    """Wandelt Datensätze mit den Spalten ``name`` und ``tags`` in Testsätze um."""
    result = []
    for record in records:
        tags = tuple(t.strip() for t in record.get("tags", "").split(",") if t.strip())
        result.append(TestSet(record.get("name", "").strip(), tags))
    return result


@dataclass
class TestSetSelection:
    """Wählt Testsätze nach Tags aus und ergänzt je Tag eine Anzahl zufälliger weiterer."""

    tags: Set[str]
    random_counts: Dict[str, int] = field(default_factory=dict)
    rng: random.Random = field(default_factory=random.Random)

    def select(self, test_sets: List[TestSet]) -> List[TestSet]:
        chosen = [s for s in test_sets if self.tags & set(s.tags)]
        rest = [s for s in test_sets if s not in chosen]
        extra = max((self.random_counts.get(t, 0) for t in self.tags), default=0)
        chosen += self.rng.sample(rest, min(extra, len(rest)))
        return sorted(chosen, key=test_sets.index)


@dataclass
class DataDrivenTestConfig:
    data_set: str = "clear"
    test_data_file_name: str = "data.tsv"


# Jede Aufgabe lässt sich ohne Squish und reproduzierbar prüfen:
rows = [{"name": "narrow", "tags": "smoke"},
        {"name": "wide", "tags": "full"},
        {"name": "boundary", "tags": "full, nightly"}]
all_sets = read_test_sets(rows)
assert all_sets[2].tags == ("full", "nightly")

only_tagged = TestSetSelection({"smoke"}).select(all_sets)
assert [s.display_name for s in only_tagged] == ["narrow"]

with_random = TestSetSelection({"smoke"}, {"smoke": 1}, random.Random(4711)).select(all_sets)
assert len(with_random) == 2 and with_random[0].display_name == "narrow"

print([s.display_name for s in with_random])
print("nachher: alle Beobachtungen bestätigt")
