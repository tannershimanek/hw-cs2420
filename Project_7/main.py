"""
Author: Tanner Shimanek
Date: November 21, 2020
Description: Driver Module for hashmap.py
"""

from hashmap import HashMap


def clean_line(raw_line):
    '''Removes all punctuation from input string and returns a
    list of all worsd which have a lenght greater than one.
    '''
    if not isinstance(raw_line, str):
        raise ValueError("Input must be a string")
    line = raw_line.strip().lower()
    line = list(line)
    for index in range(len(line)):  # pylint: disable-C0200
        if line[index] < 'a' or line[index] > 'z':
            line[index] = ' '
    cleaned = "".join(line)
    words = [word for word in cleaned.split() if len(word) > 1]
    return words


def get_most_used_words(hm):
    '''Get the top 15 most used words.'''
    hash_table = hm.hash_table()
    top_15 = []
    temp = []
    for index in hash_table:
        if index:
            top_15.append(list(index[0]))
    for i in range(1, len(top_15)):
        key = top_15[i]
        j = i - 1
        while j >= 0 and key[1] < top_15[j][1]:
            top_15[j + 1] = top_15[j]
            j -= 1
        top_15[j + 1] = key
    temp.append(top_15[-15:])
    top_15 = []
    top_15.append([el for el in reversed(temp[0])])
    for output in top_15[0]:
        print(output[0], '\t', output[1])


def main():
    '''Driver function for hashmap.py.'''
    hm = HashMap()
    with open('AliceInWonderland.txt','r') as file:
        for line in file:
            for word in clean_line(line):
                hm.set(word, 1)
    print('The most common words are:')
    get_most_used_words(hm)


main()
