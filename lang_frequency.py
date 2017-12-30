import os
from random import choice
from collections import Counter


def load_data():
    with open(os.path.join('data', choice(os.listdir('data'))), 'r') as f:
            return f.read().split()


def get_most_frequent_words():
    for word, count in Counter(load_data()).most_common(10):
        print('Слово: {} Количество повторений: {}'.format(word, count))


if __name__ == '__main__':
    print('Часто повторяющиеся слова')
    get_most_frequent_words()
