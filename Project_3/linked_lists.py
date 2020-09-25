from course import Course
from courselist import Courselist




def main():
    CL = Courselist()
    f = open('data.txt', 'r')

    lines = f.readlines()
    for line in lines:
        course = Course(line)
        # print(course)
        CL.insert(course)
        




    # check size of linked list
    # print(CL.size())
    print(CL)
    





main()


""" TODO """
# You will write an application which stores the courses taken by a student and prints out a report. 
# Data will be read from a data.txt file. 
# Once all data has been read from the data.txt file, your program should print a report as shown in the Program Output section below. 
# After the list of courses has been printed, you should then calculate and display the cumulative GPA of all courses in the list.


""" CRITERIA """
# linked list is the underlying data structure.                 [IN PROGRESS]
# ALL list traversals must be  must be recursion (NO LOOPS)     [IN PROGRESS]
# each class must be in a different module (course.py)          [DONE]
# use recursion counter                                         [IN PROGRESS]
# pass with a pylint score of 8.5 or higher                     []
# pass the unit test in test_linked_list.py                     []


""" Course ADT """
# constructor: must have default parameters for all values                                              [DONE]
# constructor: must validate all parameters                                                             [DONE]
# numbers(): retrieves a course number as an integer                                                    [DONE]
# name(): retrieves a course name as a string                                                           [DONE]
# credit_hr(): revieve credits as a floating-point number                                               [DONE]
# grade(): retrieve grade as a numeric value in range 4.0 - 0.0                                         [IN PROGRESS]
# __str__(): returns a string representing a single course as shown in the program output section       [DONE]
# course information stored in data.txt                                                                 [DONE]
# readfile data.txt                                                                                     [DONE]


""" CourseList ADT """
# constructor to initialize all needed data for an empty list                                   []
# insert(Course): insert the specified course in course number in ascending order               [IN PROGRESS]
# remove(number): remove the first occurrence of the specified course                           []
# remove_all(number): removes ALL occurrences of the specified course                           []
# find(number): find the first occurrance of the specified course in the list or return -1      []
# size(): return the number of items in the list                                                [DONE]
# calculate_gpa(): return the GPA using all courses in the list                                 []
# is_sorted(): return True if the list is sorted by course number, False if otherwise           []
# __str__(): returns a string with each course's data on a seperate line                        [DONE]
# __iter__() and __next__(): the list must be iterable                                          []


""" tasks """
# study linked lists and learn how to implement them        [IN PROGRESS]
# readfile data.txt and create an object                    [DONE]
# create and blueprint course.py                            [DONE]
# create and bluprint courselist.py                         [DONE]
# finish course.py                                          [IN PROGRESS]
# finish courselist.py                                      [IN PROGRESS]




""" resources """
# linked lists: https://www.educative.io/edpresso/how-to-create-a-linked-list-in-python
# linked lists: https://www.udemy.com/course/python-for-data-structures-algorithms-and-interviews/learn/lecture/3179598#overview
# __iter__() and __next__(): https://www.programiz.com/python-programming/iterator
