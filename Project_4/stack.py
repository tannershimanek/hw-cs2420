"""stack.py

This module... TODO
"""


class Stack:

    def __init__(self):
        self.items = []

    def push(self, item):
        """Push an item onto the satck. Size increases by 1."""
        self.items.append(item)

    def pop(self):
        """Remove the top item from the stack and return it. Raise an IndexError if the stack is empty."""
        if self.size() > 0:
            top = self.top()
            if self.size() > 0:
                self.items.pop()
            return top

    def top(self):
        """Return the item on top of the stack without removing it. Raise an IndexError if the stack is empty."""
        # TODO ValueError
        if len(self.items) > 0:
            return self.items[len(self.items) - 1]
        else:
            return None

    def size(self):
        """Return the number of items on the stack."""
        return len(self.items)

    def clear(self):
        """Empty the stack."""
        self.items = []

    def __str__(self):
        return f'{self.items}'
    
    def isEmpty(self):
        length = len(self.items)
        if length != 0:
            return False
        else:
            return True
