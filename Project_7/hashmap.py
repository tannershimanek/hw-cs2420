"""
Author: Tanner Shimanek
Date: November 21, 2020
Description: Hashmap ADT
"""


class HashMap:
    """Represents a hash based dictionary."""
# 65536
    INITAL_NUM_OF_BUCKETS = 8
    
    def __init__(self):
        self.num_of_buckets = 8 # change inital value to 8
        self.map = [None] * self.num_of_buckets
        self.num_of_key_value_pairs = 0
        # print(self.map)

    def get(self, key, default=None):
        """ Returns the associated value if key exists. """
        key_hash = self._hash(key)
        if self.map[key_hash] is not None:
            for pair in self.map[key_hash]:
                if pair[0] == key:
                    return pair[1]
        return default

    def set(self, key, value):
        """Add the key value pair to the hashMap. if the
        load-factor >= 80%, rehash the map into a map double
        its current capacity.
        """ # load factor f = n / k
        
        self.num_of_key_value_pairs += 1 # increment size
        key_hash = self._hash(key)
        key_value_pair = [key, value]

        # print(key, key_hash)

        if self.map[key_hash] is None:
            self.map[key_hash] = list([key_value_pair])
        elif self.map[key_hash] is not None:
            for pair in self.map[key_hash]:
                if pair[0] == key:
                    pair[1] = self.get(key, value) + value
                else:
                    # self._find_new_index(key_hash)
                    self.map[self._find_new_index(key_hash)] = list([key_value_pair])
                self.map[key_hash].append(list(key_value_pair))
                break

        # print(self.num_of_buckets)
        print(self.num_of_key_value_pairs)

        # if self.map[key_hash] is None: 
        #     self.map[key_hash] = list([key_value_pair])
        # elif self.map[key_hash] is not None:
        #     # self.map[bucket][first kvp][first index of first kvp]
        #     if self.map[key_hash][0][0] == key:
        #         self.map[key_hash][0][1] = self.get(key, value) + 1
        #         self.map[key_hash].append(list(key_value_pair))
        #     else:
        #         # find next empty index
        #         self.map[self._find_new_index(key_hash)] = list([key_value_pair])

        if (self.num_of_key_value_pairs / self.num_of_buckets) >= .8:
            self.rehash()

        # TODO: if the load-factor >= 80%, 
        #       rehash the map into a map double its current capacity.

    def _find_new_index(self, index):
        while self.map[index] is not None:
            index += 1
            if index > self.num_of_buckets:
                index = 0
            else:
                continue
        return index

    def _hash(self, item):
        return abs(hash(item)) % self.num_of_buckets
    
    def clear(self):
        """ Empty the hasmap."""
        self.map = [None] * self.INITAL_NUM_OF_BUCKETS

    def capacity(self):
        """Return the currect capacity --number of current
        buckets-- in the map.
        """
        return self.num_of_buckets

    def size(self):
        """Returns the number of key-value pairs in the map."""
        return self.num_of_key_value_pairs

    def keys(self):
        """Return a list of keys in the hashmap."""
        list_of_keys = []
        for i in range(len(self.map)):
            if self.map[i] is not None:
                list_of_keys.append(self.map[i][0][0])
        return list_of_keys

    def rehash(self):
        """Rebuild the table to reduce the load factor. The
        new table shold be twice the capacity of the current table.
        typically this is internal use only."""
        # TODO: Shrink that docstring before submission
        # load factor f = n / k
        # if n / k >= .8:
        for _ in range(0, self.num_of_buckets):
            self.map.append(None)
        self.num_of_buckets = self.num_of_buckets * 2



    # ----testing methods----
    def display(self): #delete later / testing only
        print('-----HASHMAP-----')
        for item in self.map:
            if item is not None:
                print(str(item))

    def write(self):
        test_file = open('testing.txt', 'w')
        for item in self.map:
            if item is not None:
                test_file.write(str(item))
                test_file.write('\n')
        test_file.close()
        
        print('\n\t-----------MESSAGE-----------\n')
        print('\t data printed in testing.txt\n')
        print('\t-----------MESSAGE-----------\n')
  


# https://coderbook.com/@marcus/how-to-create-a-hash-table-from-scratch-in-python/