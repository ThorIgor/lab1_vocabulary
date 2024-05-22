import os
from datetime import datetime
from argparse import ArgumentParser

from utils.vocabulary_builder import VocabularyBuilder
from utils.save import save

if __name__ == "__main__":
    parser = ArgumentParser()

    parser.add_argument("-i", "--input", help = "path to folder with input files (defualt: input)", type = str, default="input")
    parser.add_argument("-o", "--output", help = "name of output file with file extension (default: vocabulary.pickle), (implemented: .pickle, .json, .txt)", type = str, default="vocabulary.pickle")
    
    parser.add_argument("-s", "--statistic", help = "create file with statistic", action="store_true")

    args = parser.parse_args()

    dict_builder = VocabularyBuilder()
    input = [os.path.join(args.input, f) for f in os.listdir(args.input) if os.path.isfile(os.path.join(args.input, f))]

    print(f"Building vocabulary: {datetime.now()}")
    vocabulary = dict_builder.map_reduce(input)

    print(f"Saving results: {datetime.now()}")
    output = os.path.join("output", args.output)
    save(output, vocabulary)

    stats = f"{output} : {datetime.now()} : words={len(vocabulary)} : file_size={os.path.getsize(output)}bytes\n"
    print(stats)

    if args.statistic:
        with open("output/stats.txt", "a+", encoding="utf8") as f:
            f.write(stats)
