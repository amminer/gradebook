import __init__
from random import randint
from Grade import Demo
gs = [Demo(pointsPossible=i, pointsEarned = randint(0,i)) for i in range(1,1000)]

def test_getLetter() -> None:
    for g in gs:
        if g.getPercentage() >= 90:
            assert g.getLetter() == 'E'
        elif g.getPercentage() >= 80:
            assert g.getLetter() == 'P'
        elif g.getPercentage() >= 70:
            assert g.getLetter() == 'PW'
        elif g.getPercentage() >= 60:
            assert g.getLetter() == 'IP'
        elif g.getPercentage() >= 0:
            assert g.getLetter() == 'U'
        else:
            assert False #something is wrong with getPercentage

def test_needRetake() -> None:
    for g in gs:
        if g.getLetter() == "IP":
            assert g.needsRetake()
        else:
            assert not g.needsRetake()

def t_retake() -> None:
#TODO monkeypatch?
    for g in gs:
        g.retake()
        print("New score is", g.pointsEarned)
        if not g.passes():
            print("Better luck next time!")
        choice:str = input("\nagain? (y to continue, anything else to quit)\n")
        if not choice == 'y':
            break

if __name__ == "__main__":
    t_retake()