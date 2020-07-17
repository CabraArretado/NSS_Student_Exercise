# First name
# Last name
# Slack handle
# The instructor's cohort
# The instructor's specialty (e.g. dad jokes, excitement, dancing, etc.)
# A method to assign an exercise to a student

class Instructor():
    #builder
    def __init__(self, firstname, lastname, slackhandler, cohort, specialty ):
        self.firstname = firstname
        self.lastname = lastname
        self.slackhandler = slackhandler
        self.cohort = cohort
        self.specialty  = specialty

    def assignExercise(self, student, *exercise):
        student.exercises.extend([exercise])