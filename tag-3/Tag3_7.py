import json
import yaml

yaml.dump(
    json.load(open("config.json")),
    open("new_config.yaml", "w")
)