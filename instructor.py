from person import NSSPerson


class Instructor(NSSPerson):
    #builder
    def __init__(self, firstname, lastname, slackhandler, cohort, specialty ):
        super().__init__(firstname, lastname, slackhandler, cohort)
        self.specialty  = specialty

    def assignExercise(self, student, *exercise):
        student.exercises.extend([exercise])