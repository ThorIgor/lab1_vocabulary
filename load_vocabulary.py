import itertools
from argparse import ArgumentParser

from utils.load import load

if __name__ == "__main__":
    parser = ArgumentParser()

    parser.add_argument("-i", "--input", help = "file to laod (defualt: output/vocabulary.pickle)", type = str, default="output/vocabulary.pickle")

    args = parser.parse_args()

    vocabulary = load(args.input)

    print(f"Words: {len(vocabulary)}")
    print(f"Random 5 words: {[val for val in itertools.islice(vocabulary, 5)]}")

