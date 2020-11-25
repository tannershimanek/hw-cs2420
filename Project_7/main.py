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
    hm = HashMap()
    # testcounter = 0
    with open('AliceInWonderland.txt','r') as file:
        for line in file:
            # print(clean_line(line))
            for word in clean_line(line):
                hm.set(word, 1)
                # testcounter += 1 # remove

    # print(h.size())

    # print('\n\n\n\n\n\n\n\n\n')
    # hm.display()
    print('size:\t', hm.size())
    print('cap:\t', hm.capacity())
    print('the:\t', hm.get('the'))
    print('alice:\t', hm.get('alice'))
    # print(hm.keys())
    # hm.clear()
    # print(testcounter) # remocve

    # write output to file for testing
    hm.write()

main()



def testing():
    hashmap = [None]* 3
    print(hashmap)
    for _ in range( 0, 8):
        hashmap.append(None)
    print(hashmap)

# testing()