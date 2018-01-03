from collections import Counter
import re
import argparse


def parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('--file')
    parser.add_argument('--word_num', type=int)
    return parser.parse_args()


def load_data(filepath):
    with open(filepath, 'r') as file:
        return file.read().lower()


def get_words(filepath):
    return re.findall('(?=\D)\w+', load_data(filepath))


def get_most_frequent_words(filepath, word_num):
    return Counter(get_words(filepath)).most_common(word_num)


if __name__ == '__main__':
    filepath = parser().file
    word_num = parser().word_num
    print('Most common words are (word, times):')
    print(*get_most_frequent_words(filepath, word_num), sep='\n')


