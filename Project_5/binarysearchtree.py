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

    def update_height(self, a, b):
        """Update the height of the tree."""
        if a >= b:
            return a
        else:
            return b


class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.size = 0
        self.ordered_list = list()
        self.output = ''

    def __str__(self):
        """Return a string that shows the shape of the tree."""
        # FIXME 
        self.output = ''
        if self.root is None:
            return None
        else:
            self.__str__helper(self.root)
            return self.output
    
    def __str__helper(self, cursor):
        # FIXME make it look pretty
        """Handles recursion for the __str__() method."""
        RecursionCounter()

        if cursor:
            if len(self.output) == 0:
                self.output += str(cursor.data)

            if cursor.left_child is not None:
                self.output += str(cursor.left_child.data)
                self.__str__helper(cursor.left_child)
            elif cursor.left_child is None:
                self.__str__helper(cursor.left_child)
            
            if cursor.right_child is not None:
                self.output += str(cursor.right_child.data)
                self.__str__helper(cursor.right_child)
            elif cursor.right_child is None:
                self.__str__helper(cursor.right_child)

    def __len__(self):
        """Return the number of items in a list."""
        return self.size 

    def _length_helper(self):
        """Handles recursion for the __len__() method."""
        RecursionCounter()
        # FIXME i dont really need this
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
        # when deleteing a node, remember it can only have at most one child
        # FIXME
        if self.root is None:
            return self.root
        else:
            self._remove_helper(self.root, item)
        
    def _remove_helper(self, cursor, item):
        """Handles recursion for the remove() method."""
        RecursionCounter()
        # if item < cursor.data:
        #     cursor.left_child = self._remove_helper(cursor.left_child, item)
        # elif item > cursor.data:
        #     cursor.right_child = self._remove_helper(cursor.right_child, item)
        # else:
        #     if cursor.left_child is None:
        #         temp = cursor.right_child
        #         cursor = None
        #         return temp
        #     elif cursor.right_child is None:
        #         temp = cursor.right_child
        #         cursor = None
        #         return temp
            
        #     temp = self._min_val(cursor.right_child)
        #     cursor.data = temp.data
        #     cursor.right_child = self._remove_helper(cursor.right_child, temp.data)

    # def _min_val(self, cursor):
    #     current = cursor
    #     while current.right_child is not None:
    #         current = current.left_child
    #     return current
    
    def preorder(self):
        """Return a list that performs a preorder traversal of the tree."""
        # root -> left -> right
        # output = list() # maybe define in __init__? 
        self.ordered_list = []
        self._preorder_helper(self.root, self.ordered_list) 
        print(self.ordered_list) # FIXME keep for now, change to return later

    def _preorder_helper(self, cursor, output):
        """Handles recursion for the preorder() method."""
        RecursionCounter()
        if cursor:
            # print(str(cursor.data) + ', ', end='')
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
        if cursor is None:
            return -1
        return cursor.update_height(self._height_helper(cursor.left_child), self._height_helper(cursor.right_child)) + 1


            


    # def inorder(self):
    #     lyst = list()
    #     def recurse(node):
    #         if node is not None:
    #             recurse(node.left_child)
    #             lyst.append(node.data)
    #             recurse(node.right_child)
    #     recurse(self.root)
    #     return iter(lyst)





# ______ TODO ______ #

# height()          [DONE]
# remove()          []
# length_helper     []
# __str__()         [IN PROGRESS]
# update_height()   [DONE]
# validation        []
# testing           []
# final clean up     []