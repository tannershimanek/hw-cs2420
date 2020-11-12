"""
Author: Tanner Shimanek
Date: November 5, 2020
Driver module for binarysearchtree.py.
"""

from binarysearchtree import BinarySearchTree


def main():
    """Driver function for a binary search tree."""
    bst = BinarySearchTree()
    data = [21,26,30,9,4,14,28,18,15,10,2,3,7]
    # data = [25, 50, 57, 100, 125, 150, 200]
    for i in data:
        bst.add(i)

    print('21, 9, 4, 2, 3, 7, 14, 10, 18, 15, 26, 30, 28,')
    bst.preorder()
    print(bst)

    # data2 = [21,9,4,18,15,7]
    # for i in data2:
    #     bst.remove(i)

    # bst.preorder()
    # print(bst)

    print('inorder: ', bst.inorder())
    print('Height: ', bst.height())
    print('Length: ', bst.__len__())
    bst.remove(14)
    bst.remove(7)
    bst.remove(9)
    print(bst.rebalance_tree())
    print('Height: ', bst.height())
    bst.display()
    print('-=-=-')
    bst._is_balanced()
    print('------')
    bst.display()
    

main()

#### ADD TO BST.PY FOR TESTING PURPOSES ####
def display(self):
    """TESTING REMOVE LATER."""
    print(self.root)
    print(self.root.left_child)
    print(self.root.right_child)