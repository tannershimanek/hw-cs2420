"""courselist.py

This module creates data provided from ourse.py to create
a linked list. Each method will has different job to manipulate
the data in the linked list.
"""

from recursioncounter import RecursionCounter


class Node:
    """Construct a single node for a singly linked list."""
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class CourseList:
    """Courselist implements a linked list."""

    def __init__(self, head=None):
        """Initializes a singly linked list."""
        self.head = head
        self.courselist = ''
        self.grade = 0.0
        self.credithrs = 0.0
        self.gpa = 0.0

    def __iter__(self):
        return self

    def __next__(self):
        if self.head is not None:
            item = self.head.data
            self.head = self.head.next
            return item

    def __str__(self):
        """Returns a string with each course's data on a seperate line."""
        self.courselist = ''
        if self.head is None:
            return 'The linked list is empty.'
        else:
            self.__str__helper(self.head)
            gpa = self.calculate_gpa()
            courses = self.courselist
            size = self.size()
            return f'Current List: ({size})\n{courses}\nCumulative GPA:{"%.3f"%gpa}\n'

    def __str__helper(self, current):
        """Handles the recursion for __str__."""
        _ = RecursionCounter()
        if current.next is not None:
            self.courselist = self.courselist + str(current.data) + '\n'
            self.__str__helper(current.next)
        elif current.next is None:
            self.courselist = self.courselist + str(current.data) + '\n'
            return self.courselist

    def insert(self, Course):
        """Insert the specified course by course number in ascending order."""
        newNode = Node(Course)
        if self.head:
            current = self.head
            self.insert_helper(current, newNode)
        else:
            self.head = newNode
        self.head = self.merge_sort(self.head)

    def insert_helper(self, current, newNode):
        """Handles recursion for insert()"""
        _ = RecursionCounter()
        if current.next is not None:
            current = current.next
            self.insert_helper(current, newNode)
        else:
            current.next = newNode

    def sorted_merge(self, a, b):
        """Handles the merging for the mergesort algorithm."""
        _ = RecursionCounter()
        result = None
        if a is None:
            return b
        if b is None:
            return a

        if a.data.number() <= b.data.number():
            result = a
            result.next = self.sorted_merge(a.next, b)
        else:
            result = b
            result.next = self.sorted_merge(a, b.next)
        return result

    def merge_sort(self, h):
        """Uses the mergesort algorithm to sort the linked list."""
        _ = RecursionCounter()
        if h is None or h.next is None:
            return h

        middle = self.get_middle(h)
        nexttomiddle = middle.next
        middle.next = None

        left = self.merge_sort(h)
        right = self.merge_sort(nexttomiddle)

        sortedlist = self.sorted_merge(left, right)
        return sortedlist

    def get_middle(self, head):
        """Finds the middle of the linked list."""
        if head is None:
            return head

        slow = head
        fast = head
        return self.get_middle_helper(slow, fast)

    def get_middle_helper(self, slow, fast):
        """Handles recursion for get_middle()."""
        _ = RecursionCounter()
        if fast.next is not None:
            if fast.next.next is not None:
                slow = slow.next
                fast = fast.next.next
                self.get_middle_helper(slow, fast)
        return slow

    def remove(self, number):
        """Removes the first occurance of the specified course."""
        current = self.head
        if current.data.number() == number:
            return self.__next__()
        else:
            self.remove_helper(current, number)

    def remove_helper(self, current, number):
        """Handles recursion for remove()"""
        _ = RecursionCounter()
        temp = current
        if current.next is not None:
            if temp.next.data.number() == number:
                temp.next = temp.next.next
                return self
            else:
                temp = temp.next
                self.remove_helper(temp, number)

    def remove_all(self, number):
        """Removes ALL occurances of the specified course."""
        _ = RecursionCounter()
        if self.head is None:
            return None

        if self.head is not None and self.head.data.number() == number:
            self.head = self.head.next
            self.remove_all(number)

        if self.head is not None:
            current = self.head
            self.remove_all_helper(current, number)

    def remove_all_helper(self, current, number):
        """Handles recursion for remove_all()"""
        _ = RecursionCounter()
        if current.next is not None:
            if current.next.data.number() == number:
                current.next = current.next.next
            else:
                current = current.next
            self.remove_all_helper(current, number)

    def find(self, number):
        """Finds the first occurance of the specified course in the list or returns -1."""
        return self.find_helper(self.head, number)

    def find_helper(self, current, number):
        """Handles recursion for find()"""
        _ = RecursionCounter()
        if not current:
            return -1

        if current.data.number() == number:
            return current.data
        return self.find_helper(current.next, number)

    def size(self):
        """Returns the number of items in the list."""
        return self.size_helper(self.head)

    def size_helper(self, node):
        """Handles recursion for size()"""
        _ = RecursionCounter()
        if not node:
            return 0
        else:
            return 1 + self.size_helper(node.next)

    def calculate_gpa(self):
        """Returns the GPA using ALL courses in the list."""
        self.calculate_gpa_helper(self.head)
        if self.credithrs != 0:
            self.gpa = float(self.grade) / float(self.credithrs)
        else:
            return 0
        if self.gpa > 4:
            self.gpa = 4.000
        elif self.gpa <= 0:
            self.gpa = 0.000
        return self.gpa

    def calculate_gpa_helper(self, current):
        """Helper function to calulate GPA."""
        _ = RecursionCounter()
        if current is not None:
            if not isinstance(current.data.number(), str):
                self.grade += current.data.grade() * current.data.credit_hr()
                self.credithrs += current.data.credit_hr()
                self.calculate_gpa_helper(current.next)

    def is_sorted(self):
        """Returns True of the list is sorted by course number, False if otherwise."""
        current = self.head
        if current is None:
            return True
        return self.is_sorted_helper(current)

    def is_sorted_helper(self, current):
        """Handles recursion for is_sorted()."""
        _ = RecursionCounter()
        if current.next is not None:
            temp = current
            if temp.data.number() >= temp.next.data.number():
                return False
            current = current.next
            self.is_sorted_helper(current)
        return True

