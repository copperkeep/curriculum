import json

def save_settings(settings, path):
    with open(path, "w") as f:
        json.dump(settings, f)

def load_settings(path):
    with open(path) as f:
        return json.load(f)
