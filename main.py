from student import Student
from exercise import Exercise
from cohort import Cohort
from instructor import Instructor

# Create 4, or more, exercises.
# Create 3, or more, cohorts.
# Create 4, or more, students and assign them to one of the cohorts.
# Create 3, or more, instructors and assign them to one of the cohorts.
# Have each instructor assign 2 exercises to each of the students.

#Exercises
packages = Exercise("Packages", "Python")
classes = Exercise("Classes", "Python")
functions = Exercise("Functions", "Python")
operators = Exercise("Operators", "Python")

#Cohorts
cohort39 = Cohort("Cohort39")
cohort40 = Cohort("Cohort40")
cohort41 = Cohort("Cohort41")

#Students
felipe = Student("Felipe", "Moura", "Felipe", cohort40, packages)
daniel = Student("Daniel", "Meza", "Danim", cohort40, functions)
zane = Student("Zane", "Smith", "Zzane", cohort39, operators)
roxxane = Student("Roxxane", "Smith", "Roxx", cohort41, operators)

#Instructors
bryan = Instructor("Brian", "Smith","Bry", cohort40, "superdance")
joe = Instructor("Joe", "Jojo","joes", cohort41, "dad's jokes")
mandi = Instructor("Mandi", "Gaga","mandi", cohort39, "sing")

students = [felipe, daniel, zane, roxxane]
exercises = [packages, classes, functions, operators]

def printExercises(slist):
    for student in slist:
        for ex in student.exercises:
            print(f"{student.firstname} is working on {ex.name}")

printExercises(students)