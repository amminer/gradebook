import __init__
from Grade import Grade
from random import randint
g = Grade()

def test_points() -> None: #TODO do tests work like this ? ...
    for i in range(100000):
            i = randint(-100,1000000)
            j = randint(-100,1000000)
            g.pointsPossible = i
            g.pointsEarned = j
            assert g.pointsPossible >= 0
            assert g.pointsEarned >= 0
            assert g.pointsEarned <= g.pointsPossible


def test_pointsPossible() -> None:
    for i in range(-1000, 1000):
        g.pointsPossible = i
        assert g.pointsPossible >= 0
        assert g.pointsEarned <= g.pointsPossible

def test_pointsEarned() -> None:
    for i in range(-1000, 1000):
        g.pointsEarned = i
        assert g.pointsEarned >= 0
        assert g.pointsEarned <= g.pointsPossible

def test_passes() -> None:
    gs = [Grade("midterm one", pointsPossible=20, pointsEarned=15),
          Grade("midterm two", pointsPossible=20, pointsEarned=9),
          Grade("some quiz", 10, 6)]
    assert      gs[0].passes()
    assert      gs[2].passes()
    assert not  gs[1].passes()
