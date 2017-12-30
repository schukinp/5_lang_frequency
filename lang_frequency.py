import os
from random import choice

file = choice(os.listdir('data'))

def load_data():
    with open(os.path.join('data', file), 'r') as f:
            return f.read().split()

data = load_data()

def get_most_frequent_words():
    unique_words = []
    for word in data:
        if word not in unique_words:
            unique_words.append(word)
    counts = []
    for item in unique_words:
        count = 0
        for word in data:
            if word == item:
                count += 1
        counts.append([count, item])
    counts.sort()
    counts.reverse()
    print('Часто повторяющиеся слова')
    for index in range(min(10, len(counts))):
        count, word = counts[index]
        print('Слово: "' + word + '"' + ',', 'Количество повторений: ' + str(count))


if __name__ == '__main__':
    get_most_frequent_words()
