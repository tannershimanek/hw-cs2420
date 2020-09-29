from recursioncounter import RecursionCounter

class Node:
    """Construct a single node for a singly linked list."""
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class CourseList:
    """Courselist implements a linked list to hold an UNLIMITED number of courses."""

    def __init__(self, head=None):
        """Initializes a singly linked list."""
        self.head = head
        self.courselist = ''
        self.grade = 0.0
        self.credithrs = 0.0
        self.gpa = 0.0

    def insert(self, Course):
        """Insert the specified course by course number in ascending order."""
        # TODO SORT
        newNode = Node(Course)
        if(self.head):
            current = self.head
            self.insert_helper(current, newNode)
        else:
            self.head = newNode

    def insert_helper(self, current, newNode):
        """Handles recursion for insert()"""
        _ = RecursionCounter()
        if current.next is not None:
            current = current.next
            self.insert_helper(current, newNode)
        else:
            current.next = newNode

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
        # https://www.geeksforgeeks.org/remove-occurrences-duplicates-sorted-linked-list/
        pass

    def remove_all_helper(self, current, data):
        """Handles recursion for remove_all()"""
        pass

    def find(self, number):
        """Finds the first occurance of the specified course in the list or returns -1."""
        return self.find_helper(self.head, number)

    def find_helper(self, current, number):
        """Handles recursion for find()"""
        _ = RecursionCounter()
        if not current:
            return -1
        if current.data.number() == number:
            return current
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
        return f'Cumulative GPA: {"%.3f"%self.gpa}'
    
    def calculate_gpa_helper(self, current):
        """Helper function to calulate GPA."""
        _ = RecursionCounter()
        if current.next is not None:
            self.grade = self.grade + current.data.grade() * current.data.credit_hr()
            self.credithrs = self.credithrs + current.data.credit_hr()
            self.calculate_gpa_helper(current.next)
        elif current.next is None:
            self.gpa = self.grade / self.credithrs
            if self.gpa > 4:
                self.gpa = 4.000
            elif self.gpa < 0:
                self.gpa = 0.000

    def is_sorted(self):
        """Returns True of the list is sorted by course number, False if otherwise."""
        pass

    def __str__(self):
        """Returns a string with each course's data on a seperate line."""
        self.courselist = ''
        if self.head is None:
            return 'The linked list is empty.'
        else:
            self.__str__helper(self.head)
            return f'Current List: ({self.size()}) \n{self.courselist}'

    def __str__helper(self, current):
        """Handles the recursion for __str__.""" 
        _ = RecursionCounter()
        if current.next is not None:
            self.courselist = self.courselist + str(current.data) + '\n'
            self.__str__helper(current.next)
        elif current.next is None:
            self.courselist = self.courselist + str(current.data) + '\n'
            return self.courselist

    def __iter__(self):
        return self

    def __next__(self):
        if self.head is not None:
            item = self.head.data
            self.head = self.head.next
            return item
        else:
            raise StopIteration
