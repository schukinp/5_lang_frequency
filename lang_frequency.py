from collections import Counter
import re


filepath = input('Enter path to file (e.g. c:/path/file.txt): ')
words_number = int(input('Enter number of most common words to display: '))

def load_data(filepath):
    with open(filepath, 'r') as file:
        return re.findall('(?=\D)\w+', file.read().lower())
        
def get_most_frequent_words(words_number):
    return Counter(load_data(filepath)).most_common(words_number)

def print_result():
    for element in get_most_frequent_words(words_number):
        print('\'%s\' %d' % element)

print('\nMost common words are (word, times):')
print_result()
    
if __name__ == '__main__':
      pass
    
