from Util import *

class Grade(Util):

    def __init__(self):
        self._percent:float = -1.0
        self._name:str = "NOT SET"

    def __init__(self, newPercent:float):
        self._percent = newPercent
        self._name = "NOT SET"

    def __str__(self):
        return "Current grade for " + self._name + ": " + str(self._percent)

    def setGradeFromUser(self): #just testing
        print("Enter a new grade out of 100.")
        try:
            choice = self.getStr()
            self._setGrade(choice)
        except ValueError:
            self.printBadInput(choice)
            self.setGradeFromUser()

    def _setGrade(self, newGrade:float):
        newGrade = float(newGrade)
        if newGrade > 100.0 or newGrade < 0.0:
            raise ValueError
        self._percent = newGrade