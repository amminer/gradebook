import __init__
from Student import Student
from Grade import *

def test_addGrade():
    s = Student("Hieronymus")
    g = Exam("FINAL!", pointsPossible = 100, pointsEarned = 90)
    s.addGrade(g)
    assert s.grades.at(0) == "FINAL!"
    assert len(s.grades) == 1

def test_removeGrade():
    s = Student("Hieronymus")
    a = Asgmt("Assignment 4", pointsEarned = 10) #oof
    b = Exam("Midterm 1", pointsPossible = 200, pointsEarned = 0) #busy partying
    s.addGrade(a)
    s.addGrade(b)
    s.removeGrade("Assignment 4")
    assert s.grades.at(0) == b
    assert len(s.grades) == 1

if __name__ == "__main__":
    test_removeGrade()
