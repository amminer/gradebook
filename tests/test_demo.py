import __init__
from random import randint
from Grade import Demo

""" Amelia Miner;   test_demo.py;  5/31/2022 """

def test_getLetter() -> None:
    gs = [Demo(pointsEarned = randint(0,20)) for i in range(1,1000)]
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
    gs = [Demo(pointsEarned = randint(0,20)) for i in range(1,1000)]
    for g in gs:
        if g.getLetter() == "IP":
            assert g.needsRetake()
        else:
            assert not g.needsRetake()

def t_retake() -> None:
    gs = [Demo(pointsEarned = randint(0,20)) for i in range(1,100)]
    #TODO monkeypatch?
    for g in gs:
        g.retake()
        print("New score:", g, sep='\n')
        choice:str = input("\nagain? (y to continue, anything else to quit)\n")
        if not choice == 'y':
            break

if __name__ == "__main__":
    t_retake()