import __init__
from Student import Student
from Grade import *

def test_str():
    s = Student("Hieronymus")
    assert str(s) == "Student Hieronymus:\nEmpty"

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
    c = Demo("Midterm Demo", pointsEarned = 15)
    s.removeGrade("test") #should fail silently
    s.addGrade(a)
    s.addGrade(b)
    s.addGrade(c)
    s.removeGrade("Assignment 4")
    assert s.grades.at(0) == b
    assert len(s.grades) == 2
    s.removeGrade(b)
    assert s.grades.at(0) == c
    assert len(s.grades) == 1
    s.addGrade(b)
    s.removeGrade(b)
    assert s.grades.at(0) == c
    assert len(s.grades) == 1
    s.removeGrade(c)
    assert len(s.grades) == 0

def test_cumulativeGrade():
    s = Student("Hieronymus")
    a = Asgmt("Assignment 3", pointsEarned = 17)
    b = Exam("Midterm 2", pointsPossible=200,pointsEarned=187, extraCredit=True)
    c = Demo("Final Demo", pointsEarned = 14)
    aw = a.weight
    bw = b.weight
    cw = c.weight
    s.addGrade(a)
    s.addGrade(b)
    s.addGrade(c)
    #points times weights, all together
    assert s.cumulativeGrade() == (17*aw + 187*bw + 14*cw) \
                                / (135*aw + 200*bw + 20*cw)*100

def t_addFromCin():
    s = Student("Hieronymus")
    s.addFromStdin()
    print(s) #TODO automate

def t_retakeDemo():
    s = Student("Hieronymus")
    c = Demo("Midterm Demo", pointsEarned = 12)
    d = Demo("Final Demo", pointsEarned = 18)
    f = Exam("FINAL EXAM!")
    s.addGrade(c)
    s.addGrade(f)
    s.addGrade(d)
    s.retakeDemoFromStdin() #try a bad name
    s.retakeDemoFromStdin() #try the right name
    print(s)

if __name__ == "__main__":
    t_addFromCin()
