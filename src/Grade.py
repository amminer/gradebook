from Util import * #Util, List

""" CLASS GRADE
Generalization of leaf classes Exam, Demo, and Asgmt.
    Has int attributes pointsPossible and pointsEarned to represent a score,
with a UI-entry-point edit function using Util.presentInterface and edit
subroutines for both attrs (Likely to be overridden in leaf classes? TODO).

"""

class Grade(Util):
    #TODO: think of more methods/"jobs"
    #any way to make this const per class/instance?
    countsTowardFinal = True #TODO use in gradebook, set False in Demo
    
    def __init__(self, name:str="NOT SET", pointsPossible:int=-1,
                pointsEarned:int=-1):
        super().__init__(name)
        self.pointsPossible = pointsPossible
        self.pointsEarned = pointsEarned

    def __str__(self):
        return "Current grade for " + self.name + ": " + str(self.pointsEarned) \
             + " out of " + str(self.pointsPossible)
    
    @property
    def pointsPossible(self):
        return self._pointsPossible

    @pointsPossible.setter
    def pointsPossible(self, newPoints:int):
        self._pointsPossible = newPoints

    @property
    def pointsEarned(self):
        return self._pointsEarned

    @pointsEarned.setter
    def pointsEarned(self, newPoints:int):
        if (newPoints > self.pointsPossible):
            raise ValueError
        self._pointsEarned = newPoints

    def editPEarned(self):
        print("Enter the new # of points earned (must be <= possible):")
        try:
            newPoints = self.getPosInt() #could pass in self.pointsPossible as max
            self.pointsEarned = newPoints
        except ValueError:
            self.printBadInput(newPoints)
            self.editPEarned()

    def editPPossible(self):
        print("Enter the new # of points possible:")
        try:
            newPoints = self.getPosInt()
            self.pointsPossible = newPoints
        except ValueError:
            self.printBadInput(newPoints)
            self.editPPossible()

    def edit(self):
        try:
            choice:str = None
            self.presentInterface(
                "Would you like to edit the\n{name}, points {pos}sible,"
            + "or points {ear}ned?",
                ["name", "pos", "ear"],
                [self.editName,
                self.editPPossible,
                self.editPEarned]
            )
        except ValueError:
            self.printBadInput(choice)
            self.edit()
        except RecursionError: #user cancels or recursion depth exceeded
            print("canceled!") #return to calling scope

    def passes(self, percentageNeeded:float=60.0):
        percentage = self.pointsEarned / self.pointsPossible * 100
        return percentage >= percentageNeeded

class Exam(Grade):
    #TODO
    pass

class Asgmt(Grade):
    #TODO
    def __init__(self):
        super().__init__()
        #self.stages:List[Grade] = [Grade(...) #TODO

class Demo(Grade):
    #TODO
    pass
