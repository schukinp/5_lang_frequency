from collections import Counter
import re
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-file')
parser.add_argument('-n', type=int)
args = parser.parse_args()


def load_data():
    with open(args.file, 'r') as file:
        return file.read().lower()


def get_words():
    return re.findall('(?=\D)\w+', load_data())


def get_most_frequent_words():
    return Counter(get_words()).most_common(args.n)


if __name__ == '__main__':
    print('Most common words are (word, times):')
    print(*get_most_frequent_words(), sep='\n')
