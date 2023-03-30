import sys
from collections import Counter
import json
import os

def real_splitter(line):
    return [word.lower() for word in (x.strip(',.:;?!}{[])(_-@#$%^&*|\\/><\t') for x in line.split()) if word.isalpha()]

def file_analysis(destination):
    n_chars = 0
    n_words = 0
    n_line = 0
    chars = Counter()
    words = Counter()
    words_list = []

    with open(destination, encoding='utf-8') as file:
        while True:
            line = file.readline()
            if line == "":
                break
            # print(line)
            chars.update(line)
            n_chars += len(line)
            words_list = real_splitter(line)
            n_words += len(words_list)
            n_line += 1
            words.update(words_list)
    # print()

    data = {"path": destination, "chars" : n_chars, "words" : n_words, "lines" : n_line, "char" : chars.most_common()[0],
     "word" : words.most_common()[0]}

    return json.dumps(data)
    # return destination

if __name__ == "__main__":
    print(file_analysis(sys.stdin.read()))

