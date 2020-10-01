"""Course.py.

This module retrieves the needed information for course.py. The __init__
method makes sure to validate all information passed in.
"""


class Course:
    """Retreves data for course.py."""

    def __init__(self, class_number=0, class_name='',
                 class_credit_hrs=0.0, class_grade=0.0):
        """Course ADT that gets a class number, name, credit hour, and grade.
        Once done, it returns a string representing a single course.
        """
        self.next = None
        try:
            if isinstance(class_number, int):
                self.class_number = int(class_number)
                if self.class_number < 0:
                    raise ValueError('class number should be positive.')
            else:
                raise ValueError('class number not int.')
        except ValueError as err:
            print(err)
            raise
        try:
            if isinstance(class_name, str):
                self.class_name = str(class_name)
            else:
                raise ValueError('class name is not str.')
        except ValueError as err:
            print(err)
            raise
        try:
            if isinstance(class_credit_hrs, float):
                self.class_credit_hrs = float(class_credit_hrs)
                if self.class_credit_hrs < 0:
                    raise ValueError('class credit hours should'
                                     + ' not be negative.')
            else:
                raise ValueError('class credit_hrs not float.')
        except ValueError as err:
            print(err)
            raise
        try:
            if isinstance(class_grade, float):
                self.class_grade = float(class_grade)
                if self.class_grade < 0:
                    raise ValueError('class grade should not be negative.')
            else:
                raise ValueError('class grade is not float.')
        except ValueError as err:
            print(err)
            raise

    def number(self):
        """Retrieves course number as an integer."""
        return self.class_number

    def name(self):
        """Retrieves course name as a string."""
        return self.class_name

    def credit_hr(self):
        """Retrieves Credits as a floating-point number."""
        return self.class_credit_hrs

    def grade(self):
        """Retrieves Grade as a numeric value in range 4.0 to 0.0."""
        return self.class_grade

    def __str__(self):
        """returns a string representing a single Course."""
        return (f'cs{self.number()} {self.name()}'
                + f' Grade: {self.grade()} Credit Hours: {self.credit_hr()}')
