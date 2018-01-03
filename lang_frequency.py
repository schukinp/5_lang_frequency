from collections import Counter
import re
import argparse


def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('--file')
    parser.add_argument('--word_num', type=int)
    args = parser.parse_args()
    return args.file, args.word_num


def load_data(filepath):
    with open(filepath, 'r') as file:
        return file.read()


def get_words(loaded_data):
    return re.findall('(?=\D)\w+', loaded_data.lower())


def get_most_frequent_words(converted_file, word_num):
    return Counter(converted_file).most_common(word_num)


if __name__ == '__main__':
    filepath, word_num = get_arguments()
    loaded_data = load_data(filepath)
    converted_file = get_words(loaded_data)
    print('Most common words are (word - times):')
    print('\n'.join('\'{}\' - {}'.format(word, count)
                    for word, count in get_most_frequent_words(converted_file, word_num)))


