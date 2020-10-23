"""
Author: Tanner Shimanek
Date: October 23, 2020
"""

from recursioncounter import RecursionCounter


class Node(object):
    def __init__(self, data, left_child=None, right_child=None):
        self.data = data
        self.left_child = left_child
        self.right_child = right_child
        self.height = -1 # standard for empty tree to be -1
        # print(self.data)

    def __str__(self):
        return str(self.data)

    def is_leaf(self):
        """Check if node has chldren."""
        if self.left_child or self.right_child:
            return True
        else:
            return False

    def update_height(self):
        """Update the height of the tree."""
        if self.left_child and self.right_child is None:
            self.height = -1
        elif self.left_child or self.right_child is not None:
            self.height += 1
        return self.height


class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.size = 0

    def __str__(self):
        """Return a string that shows the shape of the tree."""
        if self.root is None:
            return None
        else:
            return self.__str__helper(self.root, 0)
    
    def __str__helper(self, node, level):
        """Handles recursion for the __str__() method."""
        RecursionCounter()
        output = ''
        if node is not None:
            output += self.__str__helper(node.right_child, level + 1)
            output += "| " * level
            output += str(node.data) + '\n'
            output += self.__str__helper(node.left_child, level + 1)


    def __len__(self):
        """Return the number of items in a list."""
        return self.size

    def _length_helper(self):
        """Handles recursion for the __len__() method."""
        RecursionCounter()
        pass

    def is_empty(self):
        """Return True of empty, False if otherwise."""
        return len(self) == 0

    def add(self, item):
        """Add item to its proper place in the tree."""
        if self.is_empty():
            self.root = Node(item)
        else:
            self._add_helper(self.root, item)
        # increment size of tree
        self.size += 1

    def _add_helper(self, cursor, data):
        """Handles recursion for the add() method."""
        RecursionCounter()      
        if data < cursor.data:
            if cursor.left_child is None:
                # add item to the left subtree
                cursor.left_child = Node(data)
            else:
                self._add_helper(cursor.left_child, data)
        elif cursor.right_child is None:
                # add item to the right subtree
            cursor.right_child = Node(data)
        else:
            self._add_helper(cursor.right_child, data)

    def find(self, item):
        """Return the matched item. If the item is not in the tree returns None."""
        pass

    def _find_helper(self, cursor, item):
        """Handles recursion for the find() method."""
        RecursionCounter()
        pass

    def remove(self, item):
        """Remove an item from the tree."""
        pass

    def _remove_helper(self, cursor, item):
        """Handles recursion for the remove() method."""
        RecursionCounter()
        pass

    def preorder(self):
        """Return an iterator that performs a preorder traversal of the tree."""
        lyst = list()
        self._preorder_helper(self.root, lyst)


    def _preorder_helper(self, cursor, output):
        """Handles recursion for the preorder() method."""
        RecursionCounter()
        # list
        if cursor:
            # print(str(cursor.data) + ', ', end='')
            self._preorder_helper(cursor.left_child, output.append(cursor.left_child))
            self._preorder_helper(cursor.right_child, output.append(cursor.right_child))
            print(output)

    def height(self):
        """Return the the height of the tree."""
        # retirn self.height from Node()
        return self.root.height


    # def inorder(self):
    #     lyst = list()
    #     def recurse(node):
    #         if node is not None:
    #             recurse(node.left_child)
    #             lyst.append(node.data)
    #             recurse(node.right_child)
    #     recurse(self.root)
    #     return iter(lyst)
