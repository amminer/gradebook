import __init__
from Util import Util, List
from random import randint, choice
from string import ascii_letters
u = Util()

def randstr(l:int) -> str:
    return "".join(choice(ascii_letters) for _ in range(l))

def test_name() -> None:
    for i in range(0, 101):
        r = randstr(i)
        u.name = r
        assert u.name != ""
        assert u.name != None