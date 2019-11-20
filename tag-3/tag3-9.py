import yaml

with open("config.yaml") as f:
    data_loaded = yaml.safe_load(f)

print(type(data_loaded))
print(data_loaded.keys())
print(data_loaded["nodes"])

