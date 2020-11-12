"""
Author: Tanner Shimanek
Date: November 5, 2020
Description: Binary Search Tree ADT (part 2)
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
    """Creates and manipulates a binary search tree. For every 5
    nodes added or removed, the Binary Search tree will balance
    itself.
        """
    def __init__(self):
        self.root = None
        self.preordered_list = list()
        self.inordered_list = list()
        self.output = ''
        self.new_list = list()

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
                    self.output += '[Empty]\n'
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
        # check if tree is balanced every 5 nodes added or removed
        if self.__len__() % 5 == 0:
            self._is_balanced()

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
        # check if tree is balanced every 5 nodes added or removed
        if self.__len__() % 5 == 0:
            self._is_balanced()

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
        self.preordered_list = []
        self._preorder_helper(self.root, self.preordered_list)
        return self.preordered_list

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

    def inorder(self):
        """Returns a list that performs an inorder traversal of a tree."""
        self.inordered_list = []
        self._inorder_helper(self.root)
        return self.inordered_list

    def _inorder_helper(self, cursor):
        """Handles recursion for the inorder() method."""
        RecursionCounter()
        if cursor:
            self._inorder_helper(cursor.left_child)
            self.inordered_list.append(cursor.data)
            self._inorder_helper(cursor.right_child)

    def rebalance_tree(self):
        """Rebalance the binary search tree."""
        self.new_list = []
        self._rebalance_tree_helper(self.inorder())
        self.new_list = [el for el in reversed(self.new_list)]
        # clear the tree of the unordered nodes
        self.root = None
        def _build(lyst, index):
            """Recursively rebuilds the tree."""
            RecursionCounter()
            if index < len(lyst):
                self.add(lyst[index].data)
                _build(lyst, index + 1)
        # add ordered items to the tree
        _build(self.new_list, 0)

    def _rebalance_tree_helper(self, inorder_list):
        """Handles recursion for the rebalence_tree() method."""
        RecursionCounter()
        if not inorder_list:
            return None
        middle = len(inorder_list) // 2
        self.new_list.append(
            Node(
            data=inorder_list[middle],
            left_child=self._rebalance_tree_helper(inorder_list[:middle]),
            right_child=self._rebalance_tree_helper(inorder_list[middle + 1:])
            ))

    def _is_balanced(self):
        """Checks if either the left side or the right side has
        a difference greater than 3 nodes and rebalances the tree.
        If the tree does not have a difference in 3 nodes the tree
        will not change.
        """
        cursor = self.root
        def _balance(cursor, counter):
            """Recursively counts nodes on one side of the tree."""
            RecursionCounter()
            if not cursor:
                return cursor
            if cursor.left_child is not None:
                counter += 1
                _balance(cursor.left_child, counter)
            if cursor.right_child is not None:
                counter += 1
                _balance(cursor.right_child, counter)
            return int(counter)

        if cursor.left_child is not None and cursor.right_child is not None:
            left_count = _balance(cursor.left_child, 0)
            right_count = _balance(cursor.right_child, 0)
            difference = left_count - right_count
            if difference > 3 or difference < -3:
                self.rebalance_tree()
            else:
                return
        else:
            return
