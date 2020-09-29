class Course:

    def __init__(self, class_number=None, class_name=None, class_credit_hrs=None, class_grade=None):
        """Course ADT that gets a class number, name, credit hour, and grade.
        Once done, it returns a string representing a single course.
        """
        # self.data = data.split(',')

        # validate params
        self.class_number = class_number
        self.class_name = class_name
        self.class_credit_hrs = class_credit_hrs
        self.class_grade = class_grade

        # try:
        #     if type(self.number) is type(int):
        #             self.number = int(number)
        #     else:
        #         raise ValueError('class number not int')
        # except ValueError as err:
        #     print(err)
        #     raise

        # try:
        #     if type(self.name) is type(str):
        #             self.name = str(name)
        #     else:
        #         raise ValueError('class name is not str')
        # except ValueError as err:
        #     print(err)
        #     raise

        # try:
        #     if type(self.credit_hrs) is type(float):
        #             self.credit_hrs = float(credit_hrs)
        #     else:
        #         raise ValueError('class credit_hrs not float')
        # except ValueError as err:
        #     print(err)
        #     raise

        # try:
        #     if type(self.grade) is type(float):
        #             self.grade = float(grade)
        #     else:
        #         raise ValueError('class grade is not float')
        # except ValueError as err:
        #     print(err)
        #     raise

    def number(self):
        """Retrieves course number as an integer."""
        try:
            return self.class_number
        except ValueError:
            # print('Course number must be an integer.')
            raise ValueError('number must receive int type parameters. \n')

    def name(self):
        """Retrieves course name as a string."""
        try:
            return self.class_name
        except ValueError:
            raise ValueError('name must receive string type parameters. \n')

    def credit_hr(self):
        """Retrieves Credits as a floating-point number."""
        try:
            return self.class_credit_hrs
        except ValueError:
            raise ValueError(
                'credit_hr must receive float type parameters. \n')

    def grade(self):
        """Retrieves Grade as a numeric value in range 4.0 to 0.0."""
        try:
            return self.class_grade
        except ValueError:
            raise ValueError('grade must receive a float type parameter. \n')

    def __str__(self):
        """returns a string representing a single Course."""
        return f'cs{self.number()} {self.name()} Grade: {self.grade()} Credit hours: {self.credit_hr()}'