# First name
# Last name
# Slack handle
# The student's cohort
# The collection of exercises that the student is currently working on

class Student():

    #builder
    def __init__(self, firstname, lastname, slackhandler, cohort, exercises=None):
        self.firstname = firstname
        self.lastname = lastname
        self.slackhandler = slackhandler
        self.cohort = cohort
        if exercises == None:
            self.exercises = []
        else:
            self.exercises = [exercises]