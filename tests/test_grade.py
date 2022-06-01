import __init__
from random import randint
from Grade import Grade

def test_getPercentage() -> None:
    gs = [Grade(pointsPossible=i, pointsEarned = randint(0,i)) for i in range(1,1000)]
    for g in gs:
        assert g.pointsEarned/g.pointsPossible * 100 == g.getPercentage()
        

def test_getLetter() -> None:
    gs = [Grade(pointsPossible=i, pointsEarned = randint(0,i)) for i in range(1,1000)]
    for g in gs:
        if g.getPercentage() >= 90:
            assert g.getLetter() == 'A'
        elif g.getPercentage() >= 80:
            assert g.getLetter() == 'B'
        elif g.getPercentage() >= 70:
            assert g.getLetter() == 'C'
        elif g.getPercentage() >= 60:
            assert g.getLetter() == 'D'
        elif g.getPercentage() >= 0:
            assert g.getLetter() == 'F'
        else:
            assert False #something is wrong with getPercentage

def test_points() -> None:
    g = Grade()
    for i in range(999999):
            i = randint(-999999999,999999999)
            j = randint(-999999999,999999999)
            beforePossible = g.pointsPossible 
            beforeEarned = g.pointsEarned 
            try:
                g.pointsPossible = i
                g.pointsEarned = j
            except ValueError:
                assert g.pointsPossible == beforePossible \
                    or g.pointsEarned == beforeEarned
                continue #input filtering is working
            assert g.pointsPossible >= 0
            assert g.pointsEarned >= 0
            assert g.pointsEarned <= g.pointsPossible

def test_passes() -> None:
    gs = [Grade(pointsPossible=i, pointsEarned = randint(0,i)) for i in range(1,1000)]
    for i in range(0,101): #passing percentages flattened to [0,100] by func
        for g in gs:
            perc = g.pointsEarned / g.pointsPossible * 100 
            if perc >= i:
                assert g.passes(i)
            else:
                assert not g.passes(i)

def t_setup():
    g = Grade()
    if g.setup():
        print(g)
    else:
        pass #should print about cancellation from obj

#Obsolete to test_points
"""
def test_pointsPossible() -> None:
    for i in range(-1000, 1000):
        g.pointsPossible = i
        assert g.pointsPossible >= 0
        assert g.pointsEarned <= g.pointsPossible
"""

#Obsolete to test_points
"""
def test_pointsEarned() -> None:
    for i in range(-1000, 1000):
        g.pointsEarned = i
        assert g.pointsEarned >= 0
        assert g.pointsEarned <= g.pointsPossible
"""

if __name__ == "__main__":
    t_setup()
