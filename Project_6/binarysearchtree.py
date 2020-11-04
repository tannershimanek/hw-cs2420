"""
Author: Tanner Shimanek
Date: October 23, 2020
Description: Binary Search Tree ADT
"""

from recursioncounter import RecursionCounter


class Node:
    """Creates a node for a binary search tree."""
    def __init__(self, data, left_child=None, right_child=None):
        self.data = data
        self.left_child = left_child
        self.right_child = right_child
        self.height = 0

    def __str__(self):
        """Return a string type of the node."""
        return str(self.data)

    def is_leaf(self):
        """Returns True if the node is a leaf."""
        if self.data is None:
            return False
        if self.right_child is None and self.left_child is None:
            return True
        else:
            return False

    def update_height(self):
        """Update the height of the node."""
        if self.left_child and self.right_child:
            self.height = 0
        elif self.left_child or self.right_child:
            self.height += 1
        return self.height


class BinarySearchTree:
    """Creates and manipulates a binary search tree."""
    def __init__(self):
        self.root = None
        self.ordered_list = list()
        self.output = ''

    def __str__(self):
        """Return a string that shows the shape of the tree."""
        if self.root is None:
            return None
        level = self.height()
        self.output = ''
        self.output += str(self.root) + ' (' + str(level) + ')\n'
        self.__str__helper(self.root, level)
        return self.output

    def __str__helper(self, cursor, level):
        """Handles recursion for the __str__() method."""
        RecursionCounter()
        if cursor:
            if cursor.left_child is not None:
                if cursor.left_child.is_leaf():
                    self.output += (str(cursor.left_child)
                                    + ' (' + str(level - 1) + ') [leaf]\n')
                    self.output += '[Empty}\n'
                    self.__str__helper(cursor.left_child, level - 1)
                else:
                    self.output += (str(cursor.left_child)
                                    + ' (' + str(level - 1) + ')\n')
                    self.__str__helper(cursor.left_child, level - 1)
            elif cursor.left_child is None:
                if not cursor.is_leaf():
                    self.output += '[Empty]\n'
                self.__str__helper(cursor.left_child, level - 1)

            if cursor.right_child is not None:
                if cursor.right_child.is_leaf():
                    self.output += (str(cursor.right_child)
                                    + ' (' + str(level-1) + ') [leaf]\n')
                    self.__str__helper(cursor.right_child, level-1)
                else:
                    self.output += (str(cursor.right_child)
                                    + ' (' + str(level-1) + ')\n')
                    self.__str__helper(cursor.right_child, level-1)
            elif cursor.right_child is None:
                self.__str__helper(cursor.right_child, level-1)

    def __len__(self):
        """Return the number of items in a list."""
        if self.root is None:
            return 0
        else:
            return self._length_helper(self.root)

    def _length_helper(self, cursor):
        """Handles recursion for the __len__() method."""
        RecursionCounter()
        if cursor is None:
            return 0
        else:
            return self._length_helper(cursor.left_child) \
                  + 1 + self._length_helper(cursor.right_child)

    def is_empty(self):
        """Return True of empty, False if otherwise."""
        return len(self) == 0

    def add(self, item):
        """Add item to its proper place in the tree."""
        if self.is_empty():
            self.root = Node(item)
        else:
            self._add_helper(self.root, item)

    def _add_helper(self, cursor, item):
        """Handles recursion for the add() method."""
        RecursionCounter()
        if item < cursor.data:
            if cursor.left_child is None:
                # add item to the left subtree
                cursor.left_child = Node(item)
            else:
                self._add_helper(cursor.left_child, item)
        elif cursor.right_child is None:
                # add item to the right subtree
            cursor.right_child = Node(item)
        else:
            self._add_helper(cursor.right_child, item)

    def find(self, item):
        """Return the matched item. If the item is not in the tree returns None."""
        if self.root is None:
            return None
        else:
            return self._find_helper(self.root, item)

    def _find_helper(self, cursor, item):
        """Handles recursion for the find() method."""
        RecursionCounter()
        if cursor.data > item:
            if cursor.left_child is not None:
                cursor.left_child = self._find_helper(cursor.left_child, item)
        elif cursor.data < item:
            if cursor.right_child is not None:
                cursor.right_child = self._find_helper(cursor.right_child, item)
        else:
            return cursor

    def remove(self, item):
        """Remove an item from the tree."""
        if self.root is None:
            return None
        else:
            self._remove_helper(self.root, item)

    def _remove_helper(self, cursor, item):
        """Handles recursion for the remove() method."""
        RecursionCounter()
        if not cursor:
            return cursor
        # finds the node
        if cursor.data > item:
            # traverse down the left of the tree
            if cursor.left_child is not None:
                cursor.left_child = self._remove_helper(cursor.left_child, item)
        elif cursor.data < item:
            # traverse down the right of the tree
            if cursor.right_child is not None:
                cursor.right_child = self._remove_helper(cursor.right_child, item)
        else:
            # found the node --> check if it is a leaf
            if cursor.is_leaf():
                cursor = None
                return cursor
            elif cursor.left_child is not None and cursor.right_child is not None:
                cursor.data = self._min_value(cursor.right_child)
                cursor.right_child = self._remove_helper(cursor.right_child, cursor.data)
            elif cursor.right_child is not None:
                cursor = cursor.right_child
                return cursor
            elif cursor.left_child is not None:
                cursor = cursor.left_child
                return cursor
        return cursor

    def _min_value(self, test):
        """Finds the min value in the tree."""
        if test.left_child is None:
            return test.data
        else:
            return self._min_value(test.left_child)

    def preorder(self):
        """Return a list that performs a preorder traversal of the tree."""
        # root -> left -> right
        self.ordered_list = []
        self._preorder_helper(self.root, self.ordered_list)
        return self.ordered_list

    def _preorder_helper(self, cursor, output):
        """Handles recursion for the preorder() method."""
        RecursionCounter()
        if cursor:
            if len(output) == 0:
                output.append(cursor.data)
            if cursor.left_child is not None:
                output.append(cursor.left_child.data)
                self._preorder_helper(cursor.left_child, output)
            elif cursor.left_child is None:
                self._preorder_helper(cursor.left_child, output)

            if cursor.right_child is not None:
                output.append(cursor.right_child.data)
                self._preorder_helper(cursor.right_child, output)
            elif cursor.right_child is None:
                self._preorder_helper(cursor.right_child, output)

    def height(self):
        """Return the the height of the tree."""
        cursor = self.root
        return self._height_helper(cursor)

    def _height_helper(self, cursor):
        """Handles recursion for height."""
        def _update_height(left, right):
            """Updates the height."""
            if left >= right:
                return left
            else:
                return right
        if cursor is None:
            return -1
        return _update_height(self._height_helper(cursor.left_child) \
                             , self._height_helper(cursor.right_child)) + 1
