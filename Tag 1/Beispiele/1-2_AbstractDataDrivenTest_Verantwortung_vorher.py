"""1-2 · vorher · AbstractDataDrivenTest: eine Konfiguration mit vier Aufgaben

Quelle: test_parameters/abstract_test_config.py (Testframework des Teams, gekürzt).
Abweichungen: pydantic.dataclasses durch dataclasses ersetzt; die Squish-Module
``testData`` und ``test_exec_helper`` sind durch Platzhalter ersetzt.

Die Klasse hält Konfigurationswerte, liest die TSV-Datei, wählt Testsätze nach
Tags aus und ergänzt eine Zufallsauswahl. Alles läuft beim Erzeugen ab.
"""
import random
from abc import ABC
from dataclasses import dataclass, field
from typing import List


# --- Platzhalter für Squish ---------------------------------------------------
class testData:
    ROWS = [{"name": "narrow", "tags": "smoke"},
            {"name": "wide", "tags": "full"},
            {"name": "boundary", "tags": "full, nightly"}]

    @staticmethod
    def dataset(file_name):
        return testData.ROWS

    @staticmethod
    def fieldNames(record):
        return list(record)

    @staticmethod
    def field(record, column):
        return record[column]


class _TestExecHelper:
    tags = ["smoke"]            # im Original aus der Umgebungsvariable SQUISH_TAGS


test_exec_helper = _TestExecHelper()
# ------------------------------------------------------------------------------

test_config = None


@dataclass
class AbstractTestSetDTO:
    display_name: str = ""
    test_set_tags: List[str] = field(default_factory=list)


@dataclass
class AbstractTest(ABC):
    data_set: str = "clear"

    def __post_init__(self):
        global test_config
        test_config = self


@dataclass
class AbstractDataDrivenTest(AbstractTest):
    _full_test_sets: List[AbstractTestSetDTO] = field(default_factory=list)
    test_sets: List[AbstractTestSetDTO] = field(default_factory=list)
    test_data_file_name: str = "data.tsv"
    random_test_data_num = {}

    def __post_init__(self):
        super().__post_init__()
        self.read_test_sets()
        self.select_test_sets()
        self.select_random_test_sets()

    def select_test_sets(self):
        self.test_sets = []
        for ds in self._full_test_sets:
            if any(tag in ds.test_set_tags for tag in test_exec_helper.tags):
                self.test_sets.append(ds)

    def select_random_test_sets(self):
        random_num_test_sets = 0
        for tag in test_exec_helper.tags:
            if tag in self.random_test_data_num:
                random_num_test_sets = max([self.random_test_data_num[tag], random_num_test_sets])
        not_selected_test_sets = [e for e in self._full_test_sets if e not in self.test_sets]
        random_num_test_sets = min([random_num_test_sets, len(not_selected_test_sets)])
        self.test_sets.extend(random.sample(not_selected_test_sets, random_num_test_sets))
        self.test_sets.sort(key=self._full_test_sets.index)

    def _provide_test_set(self):
        return AbstractTestSetDTO()

    def read_test_sets(self):
        self._full_test_sets = []
        for record in testData.dataset(self.test_data_file_name):
            self._full_test_sets.append(self.read_test_set(record, self._provide_test_set()))

    def read_test_set(self, record, cur_set):
        cur_set.display_name = self.get_data_value(record, "name", "")
        cur_set.test_set_tags += [e for e in self.get_data_value(record, "tags", [], is_list=True)
                                  if e not in cur_set.test_set_tags]
        return cur_set

    @staticmethod
    def get_data_value(record, column, def_val, is_bool=False, is_list=False, cast_type=None):
        ret = def_val
        if column in testData.fieldNames(record):
            value = testData.field(record, column).strip()
            if len(value) > 0:
                ret = value
                if is_list:
                    ret = [e.strip() for e in ret.split(",")]
        return ret


@dataclass
class _TestConfig(AbstractDataDrivenTest):
    random_test_data_num = {"smoke": 1}


config = _TestConfig()
print([s.display_name for s in config.test_sets])

# Welche Ereignisse würden diese Klasse ändern?
#   - ein neues Dateiformat für Testdaten (TSV -> JSON)
#   - eine neue Auswahlregel (z. B. nach Hardwarevariante)
#   - eine andere Zufallsstrategie oder ein fester Seed für reproduzierbare Läufe
#   - neue Konfigurationswerte
# Wer nur die Auswahlregel prüfen will, braucht testData, test_exec_helper und
# Zufall und bekommt bei jedem Lauf ein anderes Ergebnis.
assert test_config is config
print("vorher: läuft")
