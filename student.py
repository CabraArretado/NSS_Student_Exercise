from person import NSSPerson

class Student(NSSPerson):

    #builder
    def __init__(self, firstname, lastname, slackhandler, cohort, exercises=None):
        super().__init__(firstname, lastname, slackhandler, cohort)
        if exercises == None:
            self.exercises = []
        else:
            self.exercises = [exercises]