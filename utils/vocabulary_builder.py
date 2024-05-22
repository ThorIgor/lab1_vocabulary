import os
import itertools
from time import time
from nltk.tokenize import word_tokenize

import multiprocessing

class VocabularyBuilder:
    
    def map(self, file: str):
        with open(file, "r", encoding = "utf8") as f:
            words = word_tokenize(f.read().lower().replace("\n", " "))
            voc = set(words)
            return voc


    def reduce(self, vocs: list[set]):
        return set.union(*vocs)

    def map_reduce(self, files: list[str]):
        with multiprocessing.Pool() as pool:
            mapped = pool.map(self.map, files)
        vocabulary = self.reduce(mapped)
        return vocabulary
    
    
if __name__ == "__main__":
    in_dir = "input"
    input = [os.path.join(in_dir, f) for f in os.listdir(in_dir) if os.path.isfile(os.path.join(in_dir, f))]
    db = VocabularyBuilder()
    
    start = time()
    voc = db.map_reduce(input)
    end = time()
    print(f"time: {end - start}")
    print(f"count: {len(voc)}")
    print(f"words: {[val for val in itertools.islice(voc, 5)]}")
