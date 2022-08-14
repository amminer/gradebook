import __init__
from random import randint
from Grade import Exam
es = [Exam(pointsEarned = randint(0,20)) for i in range(1,1000)] #TODO ?

""" Amelia Miner;   test_exam.py;  5/31/2022
    I learned how to use monkeypatch when writing this file,
from this Medium post: https://pavolkutaj.medium.com
/simulating-single-and-multiple-inputs-using-pytest-and-
monkeypatch-6968274f7eb9
"""

def test_addMissedQuestion(monkeypatch):
    ex = Exam("Final!!!", pointsPossible=100, pointsEarned=88)
    assert not ex._questions
    #iterator containing multiple user inputs
    inputs = iter(["some question", "an answer", '', '', '', '',
                   "!q", "more stuff", "which should not be entered"])
    #patch into input one at a time via a function _, which gets the next input
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    ex.addMissedQuestion()
    assert ex._questions
    assert ex._questions["some question"] == "an answer"
    ex.addMissedQuestion() #empties should just get skipped, then we cancel at !q
    assert len(ex._questions) == 1
    #one more
    inputs = iter(["another one", "another answer"])
    ex.addMissedQuestion()
    assert ex._questions["some question"] == "an answer"
    assert ex._questions["another one"] == "another answer"
    assert len(ex._questions) == 2

def test_removeMissedQuestion(monkeypatch):
    ex = Exam("Final!!!", pointsPossible=100, pointsEarned=88)
    inputs = iter(["some question", "an answer", #q1
                   "another one", "another answer", #q2
                    #rem1,              none,               2
                   "some question", "not in the dict", "another one"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    ex.addMissedQuestion()
    ex.addMissedQuestion()
    ex.removeMissedQuestion()
    try:
        print(ex._questions["some question"])
        assert False #should not work
    except KeyError:
        assert True #good
    ex.removeMissedQuestion() #should report bad input and recursively call,
    #recursive call will then receive "another one"
    assert not ex._questions #should be empty now

def t_practice():
    ex = Exam("Final!!!", pointsPossible=100, pointsEarned=88)
    ex.addMissedQuestion()
    ex.addMissedQuestion()
    ex.practice()

if __name__ == "__main__":
    t_practice()