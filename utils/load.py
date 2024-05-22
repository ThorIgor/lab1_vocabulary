import pickle
import json

def load_pickle(file: str):
    with open(file, "rb") as f:
        return pickle.load(f)

def load_json(file: str):
    with open(file, "r", encoding="utf8") as f:
        return set(json.load(f)['words'])

def load_txt(file: str):
    with open(file, "r", encoding="utf8") as f:
        return set(f.read())

def load(file: str):
    ext = file.split(".")[-1]
    if ext == "pickle":
        return load_pickle(file)
    elif ext == "json":
        return load_json(file)
    elif ext == "txt":
        return load_txt(file)
    else:
        raise NotImplementedError()