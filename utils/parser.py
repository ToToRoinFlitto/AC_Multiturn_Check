import os
import json

def extract_korean_from_json(path):
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    return data['script']

def get_all_json_paths(directory):
    return [os.path.join(directory, fname) for fname in os.listdir(directory) if fname.endswith(".json")]
