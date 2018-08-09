import sys
import random
file_to_open = open('/usr/share/dict/words','r')
word_file = file_to_open.readlines()

def num_words(num):
    words_list = []
    for num in range(num):
        rand_index = random.randint(0, len(word_file) - 1)
        appended_word = word_file[rand_index]
        appended_word = appended_word.replace(r'\n','')
        words_list.append(appended_word)
    print(''.join(words_list))
if __name__ == '__main__':
    num_words(int(sys.argv[1]))
