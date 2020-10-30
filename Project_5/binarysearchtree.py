"""
Author: Tanner Shimanek
Date: October 23, 2020
Description: Binary Search Tree ADT
"""

from recursioncounter import RecursionCounter


class Node(object):
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
        """Check if node has chldren and return True or False."""
        if self.data is None:
            return False
        if self.right_child is None and self.left_child is None:
            return True
        else:
            return False

    def update_height(self):
        """Update the height of the node."""
        # FIXME
        return self.height


class BinarySearchTree:
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
        self.output += self.output + '\n'
        self.output += str(self.root) + ' (' + str(level) + ')\n'
        self.__str__helper(self.root, level)
        return self.output
    
    def __str__helper(self, cursor, level):
        """Handles recursion for the __str__() method."""
        RecursionCounter()
        if cursor:
            if cursor.left_child is not None:
                if cursor.left_child.is_leaf():
                    self.output += str(cursor.left_child) + ' (' + str(level - 1) + ') [leaf]\n'
                    self.output += '[Empty}\n'
                    self.__str__helper(cursor.left_child, level - 1)
                else:
                    self.output += str(cursor.left_child) + ' (' + str(level - 1) + ')\n'
                    self.__str__helper(cursor.left_child, level - 1)
            elif cursor.left_child is None:
                if not cursor.is_leaf():
                    self.output += '[Empty]\n'
                self.__str__helper(cursor.left_child, level - 1)
            
            if cursor.right_child is not None:
                if cursor.right_child.is_leaf():
                    self.output += str(cursor.right_child) + ' (' + str(level-1) + ') [leaf]\n'
                    self.__str__helper(cursor.right_child, level-1)
                else:
                    self.output += str(cursor.right_child) + ' (' + str(level-1) + ')\n'
                    self.__str__helper(cursor.right_child, level-1)
            elif cursor.right_child is None:
                self.__str__helper(cursor.right_child, level-1)

        # if cursor:
        #     if len(self.output) == 0:
        #         self.output += str(cursor.data) + ', '

        #     if cursor.left_child is not None:
        #         self.output += str(cursor.left_child.data) + ', '
        #         self.__str__helper(cursor.left_child)
        #     elif cursor.left_child is None:
        #         self.__str__helper(cursor.left_child)
            
        #     if cursor.right_child is not None:
        #         self.output += str(cursor.right_child.data) + ', '
        #         self.__str__helper(cursor.right_child)
        #     elif cursor.right_child is None:
        #         self.__str__helper(cursor.right_child)

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
            return (self._length_helper(cursor.left_child) \
                 + 1 + self._length_helper(cursor.right_child))

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
        try:
            if cursor.data == item:
                # print(cursor.is_leaf())
                return item
            if self._find_helper(cursor.left_child, item):
                return item
            elif self._find_helper(cursor.right_child, item):
                return item
            else:
                return None
        except:
            return None

    def remove(self, item):
        """Remove an item from the tree."""
        # FIXME MAKE RECURSIVE
        if self.root is None:
            return None
        else:
            self._remove_helper(self.root, item)
                
    def _remove_helper(self, cursor, item):
        """Handles recursion for the remove() method."""
        RecursionCounter()

        def _lift_tree(top):
            parent = top
            currentNode = top.left_child
            while not currentNode.right_child == None:
                parent = currentNode
                currentNode = currentNode.right_child
            top.data = currentNode.data
            if parent == top:
                top.left_child = currentNode.left_child
            else:
                parent.right_child = currentNode.left_child
        
        if self.is_empty(): return None

        itemRemoved = None
        preRoot = Node(None)
        preRoot.left_child = cursor
        direction = 'left'
        currentNode = cursor
        while not currentNode == None:
            if currentNode.data == item:
                itemRemoved = currentNode.data
                break
            parent = currentNode
            if currentNode.data > item:
                direction = 'left'
                currentNode = currentNode.left_child
            else:
                direction = 'right'
                currentNode = currentNode.right_child
            
        if itemRemoved == None: return None

        if not currentNode.left_child == None \
            and not currentNode.right_child == None:
            _lift_tree(currentNode)
        else:
            if currentNode.left_child == None:
                newChild = currentNode.right_child
            else:
                newChild = currentNode.left_child
            
            if direction == 'left':
                parent.left_child = newChild
            else:
                parent.right_child

        if self.is_empty():
            cursor = None
        else:
            cursor = preRoot.left_child
        return itemRemoved

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
        if cursor is None:
            return -1
        return self._update_height(self._height_helper(cursor.left_child), self._height_helper(cursor.right_child)) + 1
    
    def _update_height(self, a, b):
        """Updates the height."""
        if a >= b:
            return a
        else:
            return b





# ______ TODO ______ #

# match test output             []
# update_height                 [IN PROGRESS]
# make remove() recursive       []
# clean up / coding standards   []
