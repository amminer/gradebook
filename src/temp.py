from Grade import *

def main():
    g = Grade("midterm one", pointsPossible=20, pointsEarned=15)
    g.edit()
    print(g)
    if (g.passes()):
        print("Gratz!")
    else:
        print("Study!!")

main()
