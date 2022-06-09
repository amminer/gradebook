from typing import List, Tuple, Dict, Callable

""" CLASS UTIL
contains name:str attribute w/ edit function,
and basic methods needed by most other classes:
getStr, getPosInt, printBadInput,
and presentInterface for generalized menu-ing
"""

class Util():
    cursor = "~>"

    def __init__(self, newName:str="NOT SET"):
        self.name = newName

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, newName:str):
        if len(newName) > 0:
            self._name = str(newName)

    #handles any RecursionError or ValueError
    #(must be called from leaf-class's edit() function!)
    def editName(self):
        print("Enter a new name" 
            + "(recommended maximum of 39 characters for display integrity)",
              sep = '\n')
        try:
            newName = self.getStr(1)
            self.name = newName
        except ValueError as ve:
            print(ve)
            self.setName()
        except RecursionError as re: #user cancels or recursion depth exceeded
            print(re) #return to calling scope

    #may throw RecursionError or ValueError
    #(float('inf') produces a number larger than all others)
    def getPosInt(self, min:int=0, max:int=float('inf')) -> int:
        ret = input(self.cursor) #cast to int?
        if ret == "!q":
            raise RecursionError("Canceled!")
        else:
            ret = int(ret)
        if ret < min or ret > max:
            raise ValueError(f"Input must be between {min} and {max} inclusive\n")
        return ret #TODO test
    
    def getStr(self, min:int=0) -> str:
        ret:str = str(input(self.cursor))
        if ret == "!q":
            raise RecursionError("Canceled!")
        if len(ret) < min:
            raise ValueError(f"Input must be at least {min} characters\n")
        return ret #TODO test

    def printBadInput(self, badInput:str="") -> None:
        output = ""
        output += "Invalid input!"
        if badInput != None and badInput != "":
            output += f" (\"{badInput}\" is bad input)"
        print(output)
        return

        """ PRESENTINTERFACE
                Takes a string prompt, a list of strings `options`, and
            a list of functions 'routines' which must be set up as parallel
            arrays.
                Prints the prompt and the options, takes input, checks input
            against the options and calls *ALL* matching-indexed function calls
            based on the strings in the options list.
                subroutines must take no args (for now? TODO)
        """ 
    #May raise a RE that must be handled in client code!
    #Handles own ValueErrs
    def presentInterface(self, prompt:str, options:List[str],
                         routines:List[Callable]):
        print(prompt)
        try:
            choice = self.getStr() #! May raise RecursionError if user cancels
            for opt in options:    #  Catch in client code
                if opt == choice:
                    routines[options.index(opt)]()  #call subroutine
                    break
            else: #only executes if break is not reached
                raise ValueError(f"{choice} is not a valid option\n")
        except ValueError as ve:
                print(ve)
                self.presentInterface(prompt, options, routines)
