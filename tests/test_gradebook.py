from re import S
from pytest import MonkeyPatch
import __init__
from Grade import *
from Student import Student
from LLL import LLL
from BST import BST
from Gradebook import Gradebook

def test_rough():
    g = Gradebook()
    a = Student("Alice")
    l = Student("Loretta")
    g.students.insert(a)
    g.students.insert(l)
    assert len(g.students) == 2

def test_addStudentFromStdin(monkeypatch):
    if not monkeypatch == False:
        inputs = iter(["billy", "joel", "", 446, "okay"])
        monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    g = Gradebook()
    g.addStudentFromStdin()
    g.addStudentFromStdin()
    g.addStudentFromStdin() #should fail twice then suceed on "ok"
    assert len(g.students) == 3

if __name__ == "__main__":
    test_addStudentFromStdin(False)