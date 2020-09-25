from recursioncounter import RecursionCounter

class Node:

    def __init__(self, data = None, next  = None):
        self.data = data
        self.next = next


class Courselist:

    def __init__(self):
        """ Courselist implements a linked list to hold an UNLIMITED number of courses. """
        # create a linked list of all courses linking to the single course linked list
        self.head = None
        self.courselist = ''

    def insert(self, Course):
        """ Insert the specified course by course number in ascending order. """
        # make recursive
        newNode = Node(Course)
        if(self.head):
            current = self.head
            while(current.next):
                current = current.next
            current.next = newNode
        else:
            self.head = newNode

    def remove(self, number):
        """ Removes the first occurance of the specified course. """
        pass

    def remove_all(self, number):
        """ Removes ALL occurances of the specified course. """
        pass
    
    def find(self, number):
        """ Finds the first occurance of the specified course in the list or returns -1. """
        pass

    def size(self):
        """ Returns the number of items in the list. """
        return self.size_rec_helper(self.head)

    def size_rec_helper(self, node):
        """ Handles recursion for size() """
        _ = RecursionCounter()
        if (not node):
            return 0
        else:
            return 1 + self.size_rec_helper(node.next)

    def calculate_gpa(self):
        """ Returns the GPA using ALL courses in the list. """
        pass

    def is_sorted(self):
        """ Returns True of the list is sorted by course number, False if otherwise. """
        pass

    def __str__(self):
        """ Returns a string with each course's data on a seperate line. """
        if self.head is None:
            return 'The linked list is empty.'
        else:
            self.__str__helper(self.head)
            return f'Current List: ({self.size()}) \n{self.courselist}'

    def __str__helper(self, current, f = ''):
        _ = RecursionCounter()
        if current.next != None:
            self.courselist = self.courselist + str(current.data)
            self.__str__helper(current.next)
        elif current.next == None:
            self.courselist = self.courselist + str(current.data)
            return self.courselist

    def __iter__(self):
        # https://www.programiz.com/python-programming/iterator
        pass

    def __next__(self):
        # https://www.programiz.com/python-programming/iterator
        pass