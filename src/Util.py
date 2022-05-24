from typing import List
class Util():
    cursor = "~>"

    def __init__(self, newName:str="NOT SET"):
        self.name = newName

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, newName:str):
        self._name = newName

    def editName(self):
        print("Enter a new name:")
        try:
            newName = self.getStr(1)
            self.name = newName
        except ValueError:
            self.printBadInput(newName)
            self.setName()
        except RecursionError: #user cancels or recursion depth exceeded
            pass #return to calling scope

    #float('inf') produces a number larger than all others
    def getPosInt(self, min:int=0, max:int=float('inf')) -> int:
        ret = int(input(self.cursor))                #!may raise VE
        if ret == "!q":
            raise RecursionError                #is this appropriate?
        if ret < min or ret > max:
            raise ValueError                        #!may raise VE
        return ret #TODO test
    
    def getStr(self, min:int=0) -> str:
        ret:str = input(self.cursor)
        if ret == "!q":
            raise RecursionError                #is this appropriate?
        if len(ret) < min:
            raise ValueError                        #!may raise VE
        return ret #TODO test

    def printBadInput(self, badInput:str="") -> None:
        print("I can't believe you've done this..."
            + "({} is bad input)".format(badInput)
        )
        return #TODO
    
        """ PRESENTINTERFACE
                Takes a string prompt, a list of strings `options`, and
            a list of functions 'routines' which must be set up as parallel
            arrays.
                Prints the prompt and the options, takes input, checks input
            against the options and calls *ALL* matching-indexed function calls
            based on the strings in the options list.
                subroutines must take no args (for now? TODO)
        """ 
    def presentInterface(self, prompt:str, options:List, routines:List):
        #TODO test
        print(prompt, self.cursor, sep='\n')
        for opt in options:
            print(opt)
        try:
            choice = self.getStr(1);
            for opt in options:
                if opt == choice:
                    routines[options.index(opt)]()  #call subroutine
                    break
            else: #only executes if break is not reached
                raise ValueError
        except ValueError:
                self.printBadInput(choice)          #recurse
                self.presentInterface(prompt, options, routines)