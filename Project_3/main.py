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
        CL.insert(C)
    print(CL)


main()
