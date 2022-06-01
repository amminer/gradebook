import __init__
from Grade import Asgmt
a = Asgmt("Project 4")
print(a)

def t_setup():
    a = Asgmt()
    if a.setup():
        print(a)
    else:
        pass #should print about cancellation from obj
if __name__ == "__main__":
    t_setup()