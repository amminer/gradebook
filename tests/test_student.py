import __init__
from Student import Student
from Grade import *
from Gradebook import Gradebook

def test_str():
    s = Student("Hieronymus")
    assert str(s) == "Student Hieronymus:\nEmpty\n"

def test_eq():
    s = Student("Alice")
    t = Student("Alice")
    y = Student("Loretta")
    assert s == "Alice"
    assert s == t
    assert s != y
    assert y != "Jim"

def test_le():
    t = Student("Alice")
    y = Student("Loretta")
    assert isinstance(t, Student) and isinstance(y, Student)
    assert t <= y
    assert not y <= t

def test_addGrade():
    s = Student("Hieronymus")
    g = Exam("FINAL!", pointsPossible = 100, pointsEarned = 90)
    s._addGrade(g)
    assert s.grades.at(0) == "FINAL!"
    assert len(s.grades) == 1

def test_removeGrade():
    s = Student("Hieronymus")
    a = Asgmt("Assignment 4", pointsEarned = 10) #oof
    b = Exam("Midterm 1", pointsPossible = 200, pointsEarned = 0) #busy partying
    c = Demo("Midterm Demo", pointsEarned = 15)
    try:
        s._removeGrade("test")
        assert False #should have failed on bad name input
    except ValueError:
        assert True #good
    s._addGrade(a)
    s._addGrade(b)
    s._addGrade(c)
    s._removeGrade("Assignment 4")
    assert s.grades.at(0) == b
    assert len(s.grades) == 2
    s._removeGrade(b)
    assert s.grades.at(0) == c
    assert len(s.grades) == 1
    s._addGrade(b)
    s._removeGrade(b)
    assert s.grades.at(0) == c
    assert len(s.grades) == 1
    s._removeGrade(c)
    assert len(s.grades) == 0

def test_cumulativeGrade():
    s = Student("Hieronymus")
    a = Asgmt("Assignment 3", pointsEarned = 17)
    b = Exam("Midterm 2", pointsPossible=200,pointsEarned=187, extraCredit=True)
    c = Demo("Final Demo", pointsEarned = 14)
    aw = a.weight
    bw = b.weight
    cw = c.weight
    s._addGrade(a)
    s._addGrade(b)
    s._addGrade(c)
    #points times weights, all together
    assert s.cumulativeGrade() == (17*aw + 187*bw + 14*cw) \
                                / (135*aw + 200*bw + 20*cw)*100

def t_addFromCin():
    s = Student("Hieronymus")
    s.addFromStdin()
    print(s) #TODO automate

def t_removeFromCin():
    s = Student("Hieronymus")
    a = Asgmt("a", pointsEarned = 10) #oof
    s._addGrade(a)
    s.removeFromStdin()
    print(s) #TODO automate

def t_retakeDemo():
    s = Student("Hieronymus")
    c = Demo("Midterm Demo", pointsEarned = 12)
    d = Demo("Final Demo", pointsEarned = 18)
    f = Exam("FINAL EXAM!")
    s._addGrade(c)
    s._addGrade(f)
    s._addGrade(d)
    s.retakeDemoFromStdin() #try a bad name
    s.retakeDemoFromStdin() #try the right name
    print(s)

if __name__ == "__main__":
    test_le()
