class Node:
    def __init__(self, data, left_child=None, right_child=None):
        self.data = data
        # self.height = height
        self.left_child = left_child
        self.right_child = right_child

    def __str__(self):
        return f'{self.data} {self.left_child} {self.right_child}'

    def is_leaf(self):
        #bool
        # if does not have children then it is a leaf
        pass

    def update_height(self, item):
        # add child
        if self.data == item:
            # return False
            return
        elif item < self.data:
            # add item in left subtree
            if self.left_child:
                return self.left_child.update_height(item)
            else:
                self.left_child = Node(item)
                # return True
        else:
            # add item in right subtree
            if self.right_child:
                return self.right_child.update_height(item)
            else:
                self.right_child = Node(item)
                # return True 
