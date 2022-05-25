import __init__
from Grade import Grade

def test_edit():
    g = Grade()
    g.edit()
    print(g)
    g.editName()
    g.editPEarned()
    g.editPPossible()
    print(g)

def test_passes():
    gs = [Grade("midterm one", pointsPossible=20, pointsEarned=15),
          Grade("midterm two", pointsPossible=20, pointsEarned=9),
          Grade("some quiz", 10, 6)]
    assert(gs[0].passes())
    assert(gs[2].passes())
    assert(not gs[1].passes())

def main():
    #testEdit()
    test_passes()

main()
