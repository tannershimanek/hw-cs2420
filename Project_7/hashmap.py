"""
Author: Tanner Shimanek
Date: November 21, 2020
Description: Hashmap ADT
"""


class HashMap:
    """Represents a hashtable."""

    INITAL_NUM_OF_BUCKETS = 8

    def __init__(self, num_of_buckets=8):
        self.num_of_buckets = num_of_buckets
        self.map = [None] * self.num_of_buckets
        self.list_of_keys = [None]

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
        """
        self.list_of_keys.append(key)
        key_hash = abs(hash(key)) % self.num_of_buckets
        key_value_pair = [key, value]
        if self.map[key_hash] is None:
            self.map[key_hash] = list([key_value_pair])
        elif self.map[key_hash] is not None:
            for pair in self.map[key_hash]:
                if pair[0] == key:
                    pair[1] = self.get(key) + value
                    break
                self.map[key_hash].append(list(key_value_pair))
        # test load factor and rehash
        num = len(self.list_of_keys)
        if (num / self.num_of_buckets) >= .80:
            self.rehash()

    def clear(self):
        """ Empty the hashmap."""
        self.map = [None] * self.INITAL_NUM_OF_BUCKETS

    def capacity(self):
        """Return the currect capacity --number of current
        buckets-- in the map.
        """
        return self.num_of_buckets

    def size(self):
        """Returns the number of key-value pairs in the map."""
        return len(self.list_of_keys) - 1

    def keys(self):
        """Return a list of keys in the hashmap."""
        return self.list_of_keys[1:]

    def rehash(self):
        """Rebuild the table to reduce the load factor. The
        new table will be twice the capacity of the current table.
        """
        self.clear()
        self.num_of_buckets = self.num_of_buckets * 2
        self.map = [None] * self.num_of_buckets

        for key in self.list_of_keys:
            key_hash = abs(hash(key)) % self.num_of_buckets
            if self.map[key_hash] is None:
                self.map[key_hash] = [[key, 1]]
            else:
                for pair in self.map[key_hash]:
                    if pair[0] == key:
                        pair[1] = self.get(key) + 1
                        break
                self.map[key_hash].append(list([key, 1]))

    def hash_table(self):
        """Returns the hash table."""
        return self.map
