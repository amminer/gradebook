import __init__
from Grade import Grade
g = Grade()

def test_pointsPossible(): #TODO do tests work like this ? ...
    for i in range(-100, 100):
        g.pointsPossible = i
        assert g._pointsPossible >= 0
        assert g._pointsEarned <= g._pointsPossible

def test_pointsEarned(): #TODO or like this?
    assert g._pointsEarned >= 0
    assert g._pointsEarned <= g._pointsPossible

def test_passes():
    gs = [Grade("midterm one", pointsPossible=20, pointsEarned=15),
          Grade("midterm two", pointsPossible=20, pointsEarned=9),
          Grade("some quiz", 10, 6)]
<<<<<<< HEAD
    assert(gs[0].passes())
    assert(gs[2].passes())
    assert(not gs[1].passes())

def main():
    #testEdit()
    test_passes()

main()
=======
    assert      gs[0].passes()
    assert      gs[2].passes()
    assert not  gs[1].passes()
>>>>>>> 38925979dd6c5e087e6f429b81aa07eceb87144a
