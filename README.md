# Vocabulary

## 1. Download data

```
python download_data.py
```

## 2. Build vocabulary

```
usage: build_vocabulary.py [-h] [-i INPUT] [-o OUTPUT] [-s]

options:
  -h, --help            show this help message and exit
  -i INPUT, --input INPUT
                        path to folder with input files (defualt: input)
  -o OUTPUT, --output OUTPUT
                        name of output file with file extension (default: vocabulary.pickle), (implemented: .pickle, .json, .txt)
  -s, --statistic       create file with statistic
```

## 3. Test loading vocabulary

```
usage: load_vocabulary.py [-h] [-i INPUT]

options:
  -h, --help            show this help message and exit
  -i INPUT, --input INPUT
                        file to laod (defualt: output/vocabulary.pickle)
```

