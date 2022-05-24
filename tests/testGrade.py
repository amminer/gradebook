#TODO actual pytest stuff
from Grade import *

def main():
    g = Grade("midterm one", pointsPossible=20, pointsEarned=15)
    g.edit()
    print(g)

main()