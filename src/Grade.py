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
    
    def __init__(self, name:str="NOT SET", pointsPossible:int=float('inf'),
                pointsEarned:int=0):
        super().__init__(name)
        self._pointsPossible = pointsPossible
        self._pointsEarned = pointsEarned

    def __str__(self):
        ret = self.name + ':'
        nameLen = len(self.name) + 1 #1 for colon
        numTabs = 5 #TODO change?
        while nameLen >= 8:
            numTabs -= 1
            nameLen -= 8
            if numTabs == 0:
                break
        ret += '\t' * numTabs
        ret += str(self.pointsEarned)   + '/' \
             + str(self.pointsPossible) + " points"
        return ret
    
    @property
    def pointsPossible(self):
        return self._pointsPossible

    @pointsPossible.setter
    def pointsPossible(self, newPoints:int):
        #TODO should I be printing here or raising?
        if newPoints >= self.pointsEarned >= 0:
            self._pointsPossible = newPoints

    @property
    def pointsEarned(self):
        return self._pointsEarned

    @pointsEarned.setter
    def pointsEarned(self, newPoints:int):
        #TODO should I be printing here or raising?
        if 0 <= newPoints <= self.pointsPossible:
            self._pointsEarned = newPoints

    def editPEarned(self) -> None:
        print("Enter the new # of points earned (must be <= points possible):")
        try:
            newPoints = self.getPosInt() #could pass in self.pointsPossible as max
            self.pointsEarned = newPoints
        except ValueError:
            self.printBadInput(newPoints)
            self.editPEarned()

    def editPPossible(self) -> None:
        print("Enter the new # of points possible:")
        try:
            newPoints = self.getPosInt()
            self.pointsPossible = newPoints
        except ValueError:
            self.printBadInput(newPoints)
            self.editPPossible()

    def edit(self) -> None:
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

    #should give an option for +/- system?
    def getLetter(self) -> str:
        percentage = self.getPercentage()
        if 0 <= percentage < 60:
            return 'F'
        elif 60 <= percentage < 70:
            return 'D'
        elif 70 <= percentage < 80:
            return 'C'
        elif 80 <= percentage < 90:
            return 'B'
        elif 90 <= percentage < 100:
            return 'A'

    def getPercentage(self) -> float:
        if self.pointsPossible == 0:
            percentage = 0.0
        else:
            percentage = self.pointsEarned / self.pointsPossible * 100
        return percentage

    def passes(self, percentageNeeded:float=60.0) -> bool:
        if percentageNeeded < 0: percentageNeeded = 0.0
        elif percentageNeeded > 100: percentageNeeded = 100.0
        return self.getPercentage() >= percentageNeeded
        

class Exam(Grade):
    #TODO
    pass

class Asgmt(Grade):

    #points possible always same for asgmts
    def __init__(self, name:str="NOT SET", pointsEarned:int=0):
        #       0           1           2           3           4           5
        #discussion1, draftheaders, discussion2, progsub1, progsub2, finalsub&writeups
        self.stages:List[Grade] = [Grade("discussion post 1", pointsPossible = 5),
                                   Grade("draft headers", pointsPossible = 5),
                                   Grade("discussion post 2", pointsPossible = 5),
                                   Grade("progress submission 1", pointsPossible = 10),
                                   Grade("progress submission 2", pointsPossible = 10),
                                   Grade("final submission and writeups", pointsPossible = 100)]
        super().__init__(
            name,
            sum([g.pointsPossible for g in self.stages]),
            pointsEarned
        )

    def __str__(self):
        ret = super().__str__() + "\nStages:\n"
        for grade in self.stages:
            ret += str(grade) + '\n'
        return ret

class Demo(Grade):
    #TODO
    pass
