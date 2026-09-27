"""1-6 · vorher · application_contexts: ein Klassenattribut als geteilter Zustand

Quelle: target_helper/abstract_target_helper.py, local_target_helper.py,
terminal_target_helper.py (Testframework des Teams, gekürzt).
Abweichung: ``squish`` durch Platzhalter ersetzt.

``application_contexts = {}`` steht im Klassenkörper. Das Dictionary gehört damit
der Klasse ``AbstractTargetHelper`` und wird von allen Instanzen aller
Unterklassen geteilt. Im Testframework gibt es zwei solche Instanzen:
``local_target_helper`` und ``terminal_target_helper``.
"""
from abc import ABC


class squish:
    @staticmethod
    def attachToApplication(name, timeoutSecs=10):
        return f"<context {name}>"


class AbstractTargetHelper(ABC):
    application_contexts = {}

    def attach_application(self, application_name):
        self.application_contexts[application_name] = squish.attachToApplication(application_name, timeoutSecs=10)

    def detach_all_applications(self):
        self.application_contexts.clear()      # im Original: ctx.detach() für jeden Kontext


class _LocalTargetHelper(AbstractTargetHelper): ...
class _TerminalTargetHelper(AbstractTargetHelper): ...


local_target_helper = _LocalTargetHelper()
terminal_target_helper = _TerminalTargetHelper()

terminal_target_helper.attach_application("terminalui_launcher")
assert "terminalui_launcher" in local_target_helper.application_contexts   # sieht den Kontext des Terminals
assert local_target_helper.application_contexts is terminal_target_helper.application_contexts

local_target_helper.detach_all_applications()
assert terminal_target_helper.application_contexts == {}                   # auch beim Terminal weg

# Dasselbe gilt im Testframework für AbstractDataDrivenTest.random_test_data_num = {}:
# ohne Annotation kein Datenklassenfeld, sondern ein Klassenattribut.
print("vorher: alle Beobachtungen bestätigt")
