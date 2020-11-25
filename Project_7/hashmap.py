"""
Author: Tanner Shimanek
Date: November 21, 2020
Description: Hashmap ADT
"""


class HashMap:
    """Represents a hashtable."""
# 65536
    INITAL_NUM_OF_BUCKETS = 8
    
    def __init__(self):
        self.num_of_buckets = 65536 # change inital value to 8
        self.map = [None] * self.num_of_buckets
        self.num_of_key_value_pairs = 0
        self.list_of_keys =[None] # remove
        # print(self.map)

    def get(self, key, default=None):
        """ Returns the associated value if key exists. """
        key_hash = abs(hash(key)) % self.num_of_buckets
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
        key_hash = abs(hash(key)) % self.num_of_buckets
        key_value_pair = [key, value]

        # print(key, key_hash)

        if self.map[key_hash] is None:
            self.map[key_hash] = list([key_value_pair])
            return
        elif self.map[key_hash] is not None:
            for pair in self.map[key_hash]:
                if pair[0] == key:
                    pair[1] = self.get(key) + value
                    break
            self.map[key_hash].append(list(key_value_pair))
            
                
        # print(self.num_of_buckets)
        # print(self.num_of_key_value_pairs)
        
        if (self.num_of_key_value_pairs / self.num_of_buckets) * 100 >= 80:
            self.rehash()
    
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
        temp = []
        # add all non empty indexes to temp list

        for x in range(0, len(self.map)):
            if self.map[x] is not None:
                self.map[x][0][1] = 1

        # for index in self.map:
        #     if index is not None:
        #         temp.append(index)
        self.keys()

        # for j in range(0, len(self.map)):
        #     self.map[j] = None
        self.clear()

        self.num_of_key_value_pairs = 0
        self.num_of_buckets = self.num_of_buckets * 2

        for _ in range(0, self.num_of_buckets):
            self.map.append(None)

        for i in range(0, len(temp) -1):
            for j in range(0, len(temp[i])):
                key = temp[i][j][0]
                value = temp[i][j][1]
                self.set(key, value)


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
  


