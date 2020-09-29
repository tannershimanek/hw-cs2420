from course import Course
from courselist import CourseList




def main():
    CL = CourseList()
    f = open('data.txt', 'r')

    lines = f.readlines()
    for line in lines:
        data = line.split(',')
        class_number = int(data[0])
        class_name = str(data[1])
        class_credit_hrs = float(data[2])
        class_grade = float(data[3])

        C = Course(class_number, class_name, class_credit_hrs, class_grade)
        # print(C)
        # print(C.number)
        # print(C.name)
        # print(C.credit_hr)
        # print(C.grade)

        CL.insert(C)

    # 1400

    print(CL)

    print(CL.find(2810))
    print('+++++++++++++++++++++++++++++++++++++++++++++')
    # print(CL)
    print(CL.find(2810))
    print('+++++++++++++++++++++++++++++++++++++++++++++')
    print(CL.calculate_gpa())
    # CL.insert(1400)
    # print(CL)
    print('+++++++++++++++++++++++++++++++++++++++++++++')
    # CL.remove(1030)
    # CL.remove(1400)
    # CL.insert(Course(2810, 'Computer Architecture', 3.0, 3.8))
    # CL.insert(Course(2810, 'Computer Architecture', 3.0, 3.8))
    # CL.insert(Course(2810, 'Computer Architecture', 3.0, 3.8))
    # CL.insert(Course(2810, 'Computer Architecture', 3.0, 3.8))
    # print(CL)
    print('+++++++++++++++++++++++++++++++++++++++++++++')
    # print(next(iter(CL)))
    # print(next(iter(CL)))
    # print(next(iter(CL)))
    # print(next(iter(CL)))
    # CL.remove_all(2810)
    CL.sort()
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
# constructor: must validate all parameters                                                             [IN PROGRESS]
# numbers(): retrieves a course number as an integer                                                    [DONE]
# name(): retrieves a course name as a string                                                           [DONE]
# credit_hr(): revieve credits as a floating-point number                                               [DONE]
# grade(): retrieve grade as a numeric value in range 4.0 - 0.0                                         [DONE]
# __str__(): returns a string representing a single course as shown in the program output section       [DONE]
# course information stored in data.txt                                                                 [DONE]
# readfile data.txt                                                                                     [DONE]


""" CourseList ADT """
# constructor to initialize all needed data for an empty list                                   [IN PROGRESS]
# insert(Course): insert the specified course in course number in ascending order               [IN PROGRESS]
# remove(number): remove the first occurrence of the specified course                           [DONE]
# remove_all(number): removes ALL occurrences of the specified course                           []
# find(number): find the first occurrance of the specified course in the list or return -1      [DONE]
# size(): return the number of items in the list                                                [DONE]
# calculate_gpa(): return the GPA using all courses in the list                                 [DONE]
# is_sorted(): return True if the list is sorted by course number, False if otherwise           []
# __str__(): returns a string with each course's data on a seperate line                        [DONE]
# __iter__() and __next__(): the list must be iterable                                          [DONE]


""" tasks """
# study linked lists and learn how to implement them        [IN PROGRESS]
# readfile data.txt and create an object                    [DONE]
# create and blueprint course.py                            [DONE]
# create and bluprint courselist.py                         [DONE]
# finish course.py                                          [IN PROGRESS]
# finish courselist.py                                      [IN PROGRESS]
# verify parameter types                                    []
# fix insert bug                                            [DONE]
# fix __str__ duplicate bug                                 [DONE]




""" resources """
# linked lists: https://www.educative.io/edpresso/how-to-create-a-linked-list-in-python
# linked lists: https://www.udemy.com/course/python-for-data-structures-algorithms-and-interviews/learn/lecture/3179598#overview
# __iter__() and __next__(): https://www.programiz.com/python-programming/iterator
