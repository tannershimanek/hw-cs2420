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


def main():
    '''Driver function for hashmap.py.'''
    with open('AliceInWonderland.txt','r') as file:
        for line in file:
            print(clean_line(line))


main()