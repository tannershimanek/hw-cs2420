class Course:

    def __init__(self, data = None):
        """ Course ADT that gets a class number, name, credit hour, and grade. Then it returns a string representing a single course. """
        # TODO STORE EACH METHOD IN A LINKED LIST     
        self.data = data.split(',')

    def number(self):
        """ Retrieves course number as an integer. """
        try:
            class_number = int(self.data[0])
            return class_number
        except ValueError:
            print('Course number must be an integer.')
            raise ValueError('number must receive int type parameters')

    def name(self):
        """ Retrieves course name as a string. """
        try:
            class_name = str(self.data[1])
            return class_name
        except ValueError:
            raise ValueError('name must receive string type parameters. \n')

    def credit_hr(self):
        """ Retrieves Credits as a floating-point number. """
        try:
            credit_hrs = float(self.data[2])
            return credit_hrs
        except ValueError:
            raise ValueError('credit_hr must receive float type parameters. \n') 

    def grade(self):
        """ Retrieves Grade as a numeric value in range 4.0 to 0.0. """
        try:
            class_grade = float(self.data[3])
            return class_grade
        except ValueError:
            raise ValueError('grade must receive a float type parameter. \n')

    def __str__(self):
        """ returns a string representing a single Course as shown in the Program Output section. """
        return f'cs{self.number()} {self.name()} Grade: {self.grade()} Credit Hours: {self.credit_hr()} \n'