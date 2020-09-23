def main():
    print('main')



main()


""" TODO """
# You will write an application which stores the courses taken by a student and prints out a report. 
# Data will be read from a data.txt file. 
# Once all data has been read from the data.txt file, your program should print a report as shown in the Program Output section below. 
# After the list of courses has been printed, you should then calculate and display the cumulative GPA of all courses in the list.


""" CRITERIA """
# linked list is the underlying data structure.                 []
# ALL list traversals must be  must be recursion (NO LOOPS)     []
# each class must be in a different module (course.py)          []
# use recursion counter                                         []
# pass with a pylint score of 8.5 or higher                     []
# pass the unit test in test_linked_list.py                     []


""" Course ADT """
# constructor: must have default parameters for all values                                              []
# constructor: must validate all parameters                                                             []
# numbers(): retrieves a course number as an integer                                                    []
# name(): retrieves a course name as a string                                                           []
# credit_hr(): revieve credits as a floating-point number                                               []
# grade(): retrieve grade as a numeric value in range 4.0 - 0.0                                         []
# __str__(): returns a string representing a single course as shown in the program outpus section       []
# course information stored in data.txt                                                                 [DONE]
# readfile data.txt[]


""" CourseList ADT """
# constructor to initialize all needed data for an empty list                                   []
# insert(Course): insert the specified course in course number in ascending order               []
# remove(number): remove the first occurrence of the specified course                           []
# remove_all(number): removes ALL occurrences of the specified course                           []
# find(number): find the first occurrance of the specified course in the list or return -1      []
# size(): return the number of items in the list                                                []
# calculate_gpa(): return the GPA using all courses in the list                                 []
# is_sorted(): return True if the list is sorted by course number, False if otherwise           []
# __str__(): returns a string with each course's data on a seperate line                        []
# __iter__() and __next__(): the list must be iterable                                          []


""" tasks """
# study linked lists and learn how to implement them        []
# readfile data.txt and create a linked list                []
# create and blueprint course.py                            [DONE]
# create and bluprint courselist.py                         [DONE]
# finish course.py                                          []
# finish courselist.py                                      []




""" resources """
# linked lists: https://www.educative.io/edpresso/how-to-create-a-linked-list-in-python
# linked lists: https://www.udemy.com/course/python-for-data-structures-algorithms-and-interviews/learn/lecture/3179598#overview
# __iter__() and __next__(): https://www.programiz.com/python-programming/iterator
