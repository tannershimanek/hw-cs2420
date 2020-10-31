"""
Author: Tanner Shimanek
Date: October 23, 2020
Driver module for binarysearchtree.py.
"""

from binarysearchtree import BinarySearchTree


def main():
    """Driver function for a binary search tree."""
    bst = BinarySearchTree()
    data = [21,26,30,9,4,14,28,18,15,10,2,3,7]
    for i in data:
        bst.add(i)

    print('21, 9, 4, 2, 3, 7, 14, 10, 18, 15, 26, 30, 28,')
    bst.preorder()
    print(bst)

    data2 = [21,9,4,18,15,7]
    for i in data2:
        bst.remove(i)

    bst.preorder()
    print(bst)

main()
