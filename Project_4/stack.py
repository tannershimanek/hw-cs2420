"""stack.py

This module is an ADT for the stack. This stack does not
have a size limit. In addition I added isEmpty() to easily
check if the stack is empty.
"""

class Stack:

    def __init__(self):
        self.items = []

    def __str__(self):
        return f'{self.items}'

    def push(self, item):
        """Push an item onto the satck. Size increases by 1."""
        self.items.append(item)

    def pop(self):
        """Remove the top item from the stack and return it. Raise an IndexError if the stack is empty."""
        try:
            if self.size() > 0:
                top = self.top()
                self.items.pop()
                return top
            else:
                raise IndexError('Cannot pop item, stack is empty.')
        except IndexError as err:
            print(err)
            raise

    def top(self):
        """Return the item on top of the stack without removing it. Raise an IndexError if the stack is empty."""
        try:
            if self.size() > 0:
                return self.items[len(self.items) - 1]
            else:
                raise IndexError('Cannot get top item, stack is empty.')
        except IndexError as err:
            print(err)
            raise

    def size(self):
        """Return the number of items on the stack."""
        return len(self.items)

    def clear(self):
        """Empty the stack."""
        self.items = []
    
    def isEmpty(self):
        """Returns True if the stack is empty."""
        length = len(self.items)
        if length != 0:
            return False
        else:
            return True
