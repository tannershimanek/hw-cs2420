"""
Author: Tanner Shimanek
Date: October 23, 2020
"""

from binarysearchtree import BinarySearchTree
from binarysearchtree import Node


def main():
    bst = BinarySearchTree()
    data = [21,26,30,9,4,14,28,18,15,10,2,3,7]
    for i in data:
        bst.add(i)


    print('length:', bst.__len__())
    print('height:', bst.height())
    bst.preorder()

main()













# https://gist.github.com/jakemmarsh/8273963
# https://stackoverflow.com/questions/5444394/how-to-implement-a-binary-search-tree-in-python
# https://www.youtube.com/watch?v=lFq5mYUWEBk


# https://levelup.gitconnected.com/beginners-guide-to-understanding-binary-search-trees-fd2be2b086a




# https://www.youtube.com/watch?v=6oL-0TdVy28
# https://github.com/vprusso/youtube_tutorials/blob/master/data_structures/trees/binary_trees/binary_tree_recursive_dfs_traversals.py