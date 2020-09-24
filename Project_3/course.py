class Course:

    def __init__(self, data = None):
        """ Course ADT that gets a class number, name, credit hour, and grade. Then it returns a string representing a single course. """
        # TODO STORE EACH METHOD IN A LINKED LIST
        # TODO VALIDATE EACH PARAMETER
        
        self.data = data

    def number(self):
        """ Retrieves course number as an integer """
        return self.data.split(',')[0]

    def name(self):
        """ Retrieves course name as a string. """
        return self.data.split(',')[1]

    def credit_hr(self):
        """ Retrieves Credits as a floating-point number. """
        return self.data.split(',')[2]

    def grade(self):
        """ Retrieves Grade as a numeric value in range 4.0 to 0.0. """
        grade = self.data.split(',')[3]
        if grade[-1] == '\n':
            return grade[:-1]
        else:
            return grade

    def __str__(self):
        """ returns a string representing a single Course as shown in the Program Output section. """
        return f'cs{self.number()} {self.name()} Grade: {self.grade()} Credit Hours: {self.credit_hr()}'
