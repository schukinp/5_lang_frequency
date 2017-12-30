from collections import Counter


def load_data(filepath):
    with open(filepath, 'r') as text:
        return text.read().split()


def get_most_frequent_words(filepath, number):
    for word, count in Counter(load_data(filepath)).most_common(number):
        print('Word: '"'{}'"' | Frequency: {}'.format(word, count))


if __name__ == '__main__':
    pass

