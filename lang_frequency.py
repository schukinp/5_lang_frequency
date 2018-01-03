from collections import Counter
import re
import argparse


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('--file')
    parser.add_argument('--word_num', type=int)
    return parser.parse_args()


def load_data(filepath):
    with open(filepath, 'r') as file:
        return file.read()


def get_words(text):
    return re.findall('(?=\D)\w+', text.lower())


def get_most_frequent_words(word_list, word_num):
    return Counter(word_list).most_common(word_num)


if __name__ == '__main__':
    args = create_parser()
    text = load_data(args.file)
    word_list = get_words(text)
    print('Most common words are (word - times):')
    print('\n'.join('\'{}\' - {}'.format(word, count)
                    for word, count in get_most_frequent_words(word_list, args.word_num)))


