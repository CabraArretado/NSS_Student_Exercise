# The cohort's name (Evening Cohort 6, Day Cohort 26, etc.)
# The collection of students in the cohort.
# The collection of instructors in the cohort.

class Cohort():
    def __init__(self, name, students=None, intructors=None):
        self.name = name
        self.students = students
        self.intructors = intructors