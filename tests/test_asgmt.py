import __init__
from Grade import Asgmt
a = Asgmt("Project 4")

""" Amelia Miner;   test_asgmt.py;  5/31/2022 """

def t_setup():
    a = Asgmt()
    if a.setup():
        print(a)
    else:
        print("quitting")

if __name__ == "__main__":
    t_setup()
