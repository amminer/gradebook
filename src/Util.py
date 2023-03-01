from typing import List, Tuple, Dict, Callable

""" CLASS UTIL
contains name:str attribute w/ edit function,
and basic methods needed by most other classes:
getStr, getPosInt, printBadInput,
and presentInterface for generalized menu-ing
"""


class Util:
    """ base class for almost everything else in the program,
    contains basic data and functions - may be an overzealous abstraction?
    """
    cursor = "~>"

    def __init__(self, newName: str = "NOT SET"):
        self.name = newName

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, newName: str):
        if len(newName) > 0:
            self._name = str(newName)

    def editName(self):
        """ edits name param,
        handling exceptions for bad vals and user cancellation
        """
        print(
            "Enter a new name"
            + "(recommended maximum of 39 characters for display integrity)",
            sep="\n",
        )
        try:
            newName = self.getStr(1)
            self.name = newName
        except ValueError as ve:
            print(ve)
            self.setName()
        except RecursionError as re:  # user cancels or recursion depth exceeded
            print(re)  # return to calling scope

    def getPosInt(self, min: int = 0, max: int = float("inf")) -> int:
        """ takes user input in the form of a positive integer, with some flexibility;
        calling code may allow for negative integers, but default min of 0
        may raise a ValueError if user gives bad input,
        or a RecursionError if user cancels
        """
        ret = input(self.cursor)  # cast to int?
        print()
        if ret == "!q":
            raise RecursionError("Canceled!")
        else:
            ret = int(ret)
        if ret < min or ret > max:
            raise ValueError(f"Input must be between {min} and {max} inclusive\n")
        return ret 

    def getStr(self, min: int = 0) -> str:
        """ takes user input in the form of a string, allowing for calling code
        to demand that the input have a certain length
        may raise a ValueError if user gives bad input,
        or a RecursionError if user cancels
        """
        ret: str = str(input(self.cursor))
        print()
        if ret == "!q":
            raise RecursionError("Canceled!")
        if len(ret) < min:
            raise ValueError(f"Input must be at least {min} characters\n")
        return ret

    def presentInterface(
        self, prompt: str, options: List[str], routines: List[Callable]):
        """Takes a string prompt, a list of strings `options`, and
        a list of functions 'routines'
        which must be set up as parallel arrays
        Prints the prompt and the options, takes input, checks input
        against the options and calls *ALL* matching-indexed function calls
        based on the strings in the options list.
        subroutines must take no args...
        Note that this does not catch RecursionErrors that may be raised
        by getStr - if user cancels, must handle in client code
        """
        print(prompt)
        try:
            choice = self.getStr()
            for opt in options:
                if opt == choice:
                    routines[options.index(opt)]()
                    break
            else:
                raise ValueError(f"{choice} is not a valid option\n")
        except ValueError as ve:
            print(ve)
            self.presentInterface(prompt, options, routines)
