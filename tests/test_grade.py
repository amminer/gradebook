import __init__
from Grade import Grade
from random import randint
g = Grade()

#def test_getPercentage() -> None: TODO
#def test_getLetter() -> None: TODO

def test_points() -> None:
    for i in range(999999):
            i = randint(-999999999,999999999)
            j = randint(-999999999,999999999)
            g.pointsPossible = i
            g.pointsEarned = j
            assert g.pointsPossible >= 0
            assert g.pointsEarned >= 0
            assert g.pointsEarned <= g.pointsPossible

#Obsolete to test_points
def test_pointsPossible() -> None:
    for i in range(-1000, 1000):
        g.pointsPossible = i
        assert g.pointsPossible >= 0
        assert g.pointsEarned <= g.pointsPossible

#Obsolete to test_points
def test_pointsEarned() -> None:
    for i in range(-1000, 1000):
        g.pointsEarned = i
        assert g.pointsEarned >= 0
        assert g.pointsEarned <= g.pointsPossible

def test_passes() -> None:
    gs = [Grade(pointsPossible=i, pointsEarned = randint(0,i)) for i in range(0,1000)]
    for i in range(0,101): #passing percentages flattened to [0,100] by func
        for g in gs:
            if g.pointsPossible == 0:
                perc = 0
            else:
                perc = g.pointsEarned / g.pointsPossible * 100 
            if perc >= i:
                assert g.passes(i)
            else:
                assert not g.passes(i)