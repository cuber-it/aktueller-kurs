"""Konfig laden: Vererbung vs. has-a vs. Dependency Injection.

Bisher JSON, jetzt kommt YAML dazu (pip install pyyaml).
"""
import json
import os
import tempfile

import yaml


class JsonConfig:
    def load(self, path):
        with open(path) as f:
            return json.load(f)


class YamlConfig:
    def load(self, path):
        with open(path) as f:
            return yaml.safe_load(f)


# 1) Vererbung: App IST ein JsonConfig
class AppInherit(JsonConfig):
    def __init__(self, path):
        self.config = self.load(path)


# Fuer YAML braucht es eine zweite App-Klasse
class AppInheritYaml(YamlConfig):
    def __init__(self, path):
        self.config = self.load(path)


# 2) Has-a: App erzeugt ihren Loader selbst
class AppHasA:
    def __init__(self, path):
        if path.endswith(".json"):
            self.loader = JsonConfig()
        elif path.endswith((".yaml", ".yml")):
            self.loader = YamlConfig()
        else:
            raise ValueError(f"Unbekanntes Format: {path}")
        self.config = self.loader.load(path)


# 3) Dependency Injection: Loader kommt von aussen
class AppDI:
    def __init__(self, loader, path):
        self.config = loader.load(path)


class FakeConfig:
    def __init__(self, data):
        self.data = data

    def load(self, path):
        return self.data


if __name__ == "__main__":
    tmp = tempfile.mkdtemp()
    json_path = os.path.join(tmp, "app.json")
    yaml_path = os.path.join(tmp, "app.yaml")
    with open(json_path, "w") as f:
        json.dump({"host": "localhost", "port": 8080}, f)
    with open(yaml_path, "w") as f:
        f.write("host: localhost\nport: 8080\n")

    print(AppInherit(json_path).config)
    print(AppInheritYaml(yaml_path).config)

    print(AppHasA(json_path).config)
    print(AppHasA(yaml_path).config)

    print(AppDI(JsonConfig(), json_path).config)
    print(AppDI(YamlConfig(), yaml_path).config)

    app = AppDI(FakeConfig({"host": "test", "port": 1}), "egal")
    assert app.config == {"host": "test", "port": 1}
    print("Test mit FakeConfig OK")
