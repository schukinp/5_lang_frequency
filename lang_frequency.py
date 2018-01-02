from collections import Counter
import re
import argparse


def parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('--file')
    parser.add_argument('-n', type=int)
    return parser.parse_args()


def load_data(filepath):
    with open(filepath, 'r') as file:
        return file.read().lower()


def get_words(filepath):
    return re.findall('(?=\D)\w+', load_data(filepath))


def get_most_frequent_words(filepath, n):
    return Counter(get_words(filepath)).most_common(n)


if __name__ == '__main__':
    filepath = parser().file
    n = parser().n
    print('Most common words are (word, times):')
    print(*get_most_frequent_words(filepath, n), sep='\n')


