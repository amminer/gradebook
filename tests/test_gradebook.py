from re import S
from random import shuffle, randint, choice
from pytest import MonkeyPatch
import __init__
from Gradebook import Gradebook
from string import ascii_letters

""" Amelia Miner;   test_gradebook.py;  6/6/2022 """

def randstr(l:int) -> str:
    return "".join(choice(ascii_letters) for _ in range(l))

def test_addStudentFromStdin(monkeypatch):
    if not monkeypatch == False:
        inputs = iter(["billy", "joel", "", 446, "okay"])
        monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    g = Gradebook()
    g.addStudentFromStdin()
    g.addStudentFromStdin()
    g.addStudentFromStdin() #should fail twice then suceed on "ok"
    assert len(g._students) == 3

#WARNING run with pytest --show-capture=no to prevent catastrophic
#failure of stdout during testing...
#is this worth doing at all?
def test_shotgun(monkeypatch):
    g = Gradebook()
    #Every now and then it may be useful to
    #set MAX to 100,000,000 and wait a while
    MAX = 1000000
    inputs = ["add" for _ in range(MAX)] + ["remove" for _ in range(MAX)] \
           + ["rem" for _ in range(MAX)] + ["lookup" for _ in range(MAX)] \
           + ["edit" for _ in range(MAX)] + ["calc" for _ in range(MAX)] \
           + [str(randint(-2,300)) for _ in range(MAX)]
    shuffle(inputs)
    inputs.append("!q")
    inputs = iter(inputs)
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    try:
        g.mainloop()
    except BaseException as e:
        print(e)
        assert False #user sees exception
    assert True # we made it

if __name__ == "__main__":
    test_addStudentFromStdin(False)