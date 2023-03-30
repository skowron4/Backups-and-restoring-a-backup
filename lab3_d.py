import json
import subprocess
import sys
import os
from collections import Counter

def run_file_stats(paths):
    result = []

    for path in paths:
        proc = subprocess.Popen(['python', 'lab3.py'], stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE)
        file_stats, erorrs = proc.communicate(path.encode('utf-8'))
        result.append(json.loads(file_stats))

    return result

def aggregate_stats(files_stats):
    chars_count = 0
    words_count = 0
    lines_count = 0
    common_char = Counter()
    common_word = Counter()
    print(files_stats[0]['word'])
    print('powyzej')
    for fs in files_stats:
        chars_count += fs['chars']
        words_count += fs['words']
        lines_count += fs['lines']
        common_char.update({fs['char'][0]:fs['char'][1]})
        common_word.update({fs['word'][0]:fs['word'][1]})

    return {
        "Liczba przeczytanych plików":len(files_stats),
        "Sumaryczna liczba zanków":chars_count,
        "Sumaryczna liczba slow":words_count,
        "Sumaryczna liczba wierszy":lines_count,
        "Najczesciej wystepujacy znak":common_char.most_common()[0],
        "Najczesciej wystepujace slowo":common_word.most_common()[0]
    }

def file_processing():
    folder_path = sys.argv[1]
    files = [os.path.join(folder_path, f) for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
    file_stats = run_file_stats(files)
    agg_stats = aggregate_stats(file_stats)
    print(agg_stats)

if __name__ == "__main__":
    print("---------------------------------------------------")
    file_processing()
