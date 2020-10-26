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
        self.height = -1 # standard for empty tree to be -1

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
        # FIXME update height
        if self.left_child and self.right_child is None:
            self.height = -1
        elif self.left_child or self.right_child is not None:
            self.height += 1
        return self.height


class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.size = 0
        self.ordered_list = list()

    def __str__(self):
        """Return a string that shows the shape of the tree."""
        # FIXME
        if self.root is None:
            return None
        else:
            return self.__str__helper(self.root, 0)
    
    def __str__helper(self, node, level):
        # FIXME
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
                print(cursor.is_leaf())
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
        print(self.ordered_list) # FIXME keep for now, remove later

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

    def height(self, node=None):
        """Return the the height of the tree."""
        # TODO get height tree
        return -1
        # retirn self.height from Node()
        # return self.root.update_height()
        # node = self.root
        # if node is None:
        #     return -1

        # return node.update_height(self.height(node.left_child), self.height(node.right_child)) + 1


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

# height()          []
# remove()          []
# length_helper     []
# __str__()         []
# update_height()   []
# validation        []
# testing           []
# final clean up     []