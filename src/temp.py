from Grade import *

def main():
    g = Asgmt("project one", pointsEarned=15)
    g.edit()
    print(g)
    if (g.passes()):
        print("Gratz!")
    else:
        print("Study!!")

main()
