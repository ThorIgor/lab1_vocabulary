import pickle
import json

def save_pickle(filename: str, vocabulary: set[str]):
    with open(filename, "wb") as f:
        pickle.dump(vocabulary, f)

def save_json(filename: str, vocabulary: set[str]):
    dict = {"len": len(vocabulary), "words": list(vocabulary)}
    with open(filename, "w", encoding = "utf8") as f:
        json.dump(dict, f)

def save_txt(filename: str, vocabulary: set[str]):
    with open(filename, "w", encoding = "utf8") as f:
        f.write(str(vocabulary))

def save(filename: str, vocabulary: set[str]):
    ext = filename.split(".")[-1]
    if ext == 'pickle':
        save_pickle(filename, vocabulary)
    elif ext == 'json':
        save_json(filename, vocabulary)
    elif ext == 'txt':
        save_txt(filename, vocabulary)
    else:
        raise NotImplementedError()