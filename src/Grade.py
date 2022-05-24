from Util import * #Util, List

class Grade(Util):
    
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
        except RecursionError: #user cancels or recursion depth exceeded
            pass #return to calling scope

    def editPPossible(self):
        print("Enter the new # of points possible:")
        try:
            newPoints = self.getPosInt()
            self.pointsPossible = newPoints
        except ValueError:
            self.printBadInput(newPoints)
            self.editPPossible()
        except RecursionError: #user cancels or recursion depth exceeded
            pass #return to calling scope

    def edit(self):
        self.presentInterface(
            "Would you like to edit the\n{name}, points {pos}sible,"
          + "or points {ear}ned?",
            ["name", "pos", "ear"],
            [self.editName,
             self.editPPossible,
             self.editPEarned]
        )

    def passes(self, percentageNeeded:float=60.0) -> bool:
        if self.pointsEarned / self.pointsPossible * 100 < percentageNeeded:
            return False
        else
            return True