from Util import * #Util, List
from random import shuffle

""" Amelia Miner;   Grade.py;   5/24/2022
CLASS GRADE
Generalization of leaf classes Exam, Demo, and Asgmt.
    Has int attributes pointsPossible and pointsEarned to represent a score,
methods for calculating percentage and letter grades, and a method for
determining whether the grade passes.
    Subclass Exam has boolean attribute _extraCredit and dict[str:str] _questions,
which maps missed questions to their correct answers, plus methods to add and remove
missed questions to the dict and to practice the missed questions like flash cards -
contrived, unsure if appropriate but had a hard time thinking of "jobs". Exams have a
weight of 4.
    Subclass Asgmt has a list of subgrades (List[Grade]) _stages, and calculates its
pointsEarned differently using this collection. Asgmts have a weight of 1.
    Subclass Demo has additional methods for determining whether a retake is available
and for performing a retake (editing pointsEarned). It also overrides getLetter(). Demos
have a weight of 0.
"""

#~~~~~~~~~~~~~~~~~~~~~~~CLASS GRADE~~~~~~~~~~~~~~~~~~~~~~~~~~~#
""" Expects minimum pointsPossible of 1 (0? todo)
"""

class Grade(Util):
    weight = 1
    
    def __init__(self, name:str="NOT SET", pointsPossible:float=float('inf'),
                pointsEarned:int=-1):
        #any way to make this const per class/instance?
        super().__init__(name)
        self._pointsPossible = pointsPossible
        self._pointsEarned = pointsEarned #asgmt subgrades need direct access

    #for string keynames or Grades
    def __eq__(self, other):
        if type(other) == str:
            return self.name == other
        elif isinstance(other, Grade):
            return self.name == other.name 
        else:
            return False

    def __str__(self):
        ret = self.name + ':'
        nameLen = len(self.name) + 1 #1 for colon
        numTabs = 5 #todo change?
        while nameLen >= 8:
            numTabs -= 1
            nameLen -= 8
            if numTabs == 0:
                break
        ret += '\t' * numTabs
        ret += f"{self.pointsEarned}/{self.pointsPossible} points (" \
             + f"{self.getPercentage():.2f}%, {self.getLetter()})"
        return ret
    
    @property
    def pointsPossible(self):
        return self._pointsPossible

    @pointsPossible.setter
    def pointsPossible(self, newPoints:int):
        if newPoints >= self.pointsEarned:
            self._pointsPossible = newPoints
        else:
            raise ValueError("Invalid # of points possible (must be at least "
                           + str(self.pointsEarned) + ")\n")

    @property
    def pointsEarned(self):
        return self._pointsEarned

    @pointsEarned.setter
    def pointsEarned(self, newPoints:int):
        if 0 <= newPoints <= self.pointsPossible:
            self._pointsEarned = newPoints
        else:
            raise ValueError("Invalid # of points earned (must be at most "
                           + str(self.pointsPossible) + ")\n")

    """ removed - only need to edit on Exam.retake
    def editPEarned(self) -> None:
        print("Enter the new # of points earned, or !q to cancel",
              "(must be <= points possible):")
        try:
            newPoints = self.getPosInt() #could pass in self.pointsPossible as max
            self.pointsEarned = newPoints
        except ValueError:
            self.printBadInput(newPoints)
            self.editPEarned()
        except RecursionError: #user cancels or recursion depth exceeded
            print("canceled!") #return to calling scope
    """

    """ removed - only need to edit on Exam.retake
    def editPPossible(self) -> None:
        print("Enter the new # of points possible, or !q to cancel:")
        try:
            newPoints = self.getPosInt()
            self.pointsPossible = newPoints
        except ValueError:
            self.printBadInput(newPoints)
            self.editPPossible()
        except RecursionError: #user cancels or recursion depth exceeded
            print("canceled!") #return to calling scope
    """

    #Allows RecursionErrors to be passed to client code if user cancels
    #MUST handle in client code - RecursionError signifies user cancelling setup,
    #should cancel addition of new grade object
    def setup(self) -> None:
        choice:str = ""
        try:
            if self.name == "NOT SET":
                print("Enter a name/title for this grade:")
                choice = self.getStr(1)
                self.name = choice
            if self.pointsPossible == float('inf'):
                print(f"Enter the number of possible points (must be > {self.pointsEarned}):")
                choice = self.getPosInt()
                self.pointsPossible = choice
            if self.pointsEarned == -1:
                print(f"Enter the number of points earned out of {self.pointsPossible}:")
                choice = self.getPosInt()
                self.pointsEarned = choice
        except RecursionError as re:
            print(re)
            return False
        except ValueError as ve:
            print(ve)
            self.setup()
        return True

    def edit(self) -> None:
        try:
            self.editName()
            """ removed - only need to edit on Exam.retake
            self.presentInterface( #Catches ValueErrors
                "Would you like to edit the\n{name}, points {pos}sible,"
            + "or points {ear}ned?",
                ["name", "pos", "ear"],
                [self.editName,
                self.editPPossible,
                self.editPEarned]
            )
            """
        except RecursionError as re: #user cancels or recursion depth exceeded
            print(re) #return to calling scope

    #should give an option for +/- system?
    def getLetter(self, letters:Tuple[str]=['F','D','C','B','A']) -> str:
        percentage = self.getPercentage()
        if percentage < 60.0:
            return letters[0]
        elif 60 <= percentage < 70.0:
            return letters[1]
        elif 70 <= percentage < 80.0:
            return letters[2]
        elif 80 <= percentage < 90.0:
            return letters[3]
        elif 90 <= percentage:
            return letters[4]

    def getPercentage(self) -> float:
        if self.pointsPossible == 0:
            percentage = 0.0
        else:
            percentage = self.pointsEarned / self.pointsPossible * 100
        return percentage

    def passes(self, percentageNeeded:float=70.0) -> bool:
        if percentageNeeded < 0: percentageNeeded = 0.0
        elif percentageNeeded > 100: percentageNeeded = 100.0
        return self.getPercentage() >= percentageNeeded

#~~~~~~~~~~~~~~~~~~~END CLASS GRADE~~~~~~~~~~~~~~~~~~~~~~~~~~~#




#~~~~~~~~~~~~~~~~~~~~~~~CLASS EXAM~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
# I had a really hard time thinking of a "job" for this class
#so it keeps a dict of missed _questions and allows client code to "practice"
#against predetermined correct answers, maybe a bit of an overreach for
#a grade object but here it is
        
class Exam(Grade):
    weight = 4

    def __init__(self, name:str="NOT SET",
                 pointsPossible:int=float('inf'), pointsEarned:int=-1,
                 questions:Dict[str,str]=dict(), extraCredit=False):
        self._questions:Dict[str,str] = questions #get/set via add/remove class funcs
        self._extraCredit = extraCredit #planning future feature
        super().__init__(name, pointsPossible=pointsPossible,
                         pointsEarned=pointsEarned)

    """ Wanted to incorporate extra credit - future feature
    def setup(self, superIsSetUp:bool = False) -> bool:
        if not superIsSetUp:
            super().setup()
        choice:int = 0
        try:
            print("Apply extra credit to this exam? Enter {y} or {n},\n"
                + "or {!q} to cancel:")
            choice = self.getStr(1)
            if choice == 'y':
                self._extraCredit = True
            elif choice == 'n':
                self._extraCredit = False
            else:
                raise ValueError("Input must be \"y\" or \"n\"")

        except ValueError as ve:
            print(ve)
            return self.setup(True)

        except RecursionError as re:
            print(re)
            return False
        
        return True
    """

    def __str__(self) -> str:
        ret:str = ""
        if self._questions:
            ret += "\nMissed _questions:\n"
        for q in self._questions.keys():
            ret += q + '\n'
        return super().__str__() + ret
        
    def getPercentage(self) -> float:
        ret:float = super().getPercentage()
        #if self._extraCredit:
        #    ret += 5.0 #unsure if this is how to handle this
        return ret

    #viewMissedQuestions(self)? Maybe in a later update

    def addMissedQuestion(self):
        print("Enter the new question:")
        try:
            newQuestion = self.getStr(1)
            print("Enter the correct answer:")
            newAnswer = self.getStr(1)
            self._questions[newQuestion] = newAnswer
        except ValueError as ve:
            print(ve)
            self.addMissedQuestion()
        except RecursionError as re:
            print(re) #return to calling scope

    def removeMissedQuestion(self):
        toRem:str = ""
        print("Enter the name of the question to remove:")
        try:
            toRem = self.getStr(1)
            del self._questions[toRem]
        except (ValueError, KeyError):  #I deeply dislike this syntax
            print(f"{toRem} was not found...")
            self.removeMissedQuestion()
        except RecursionError as re:         #Why not `except x or y`?
            print(re) #return to calling scope

    def practice(self):
        answer:str = ""
        if not self._questions:
            print("Nothing to practice!")
        questions = list(self._questions.items()) #make a copy
        shuffle(questions) #mix it up
        for q in questions:
            print(q[0])
            print("Enter your answer:")
            try:
                answer = self.getStr(1)
                print ("Correct answer:", q[1], sep='\n')
            except RecursionError or ValueError as e:
                print(e)
                print("Skipping for now...")
                continue

#~~~~~~~~~~~~~~~~~~~END CLASS EXAM~~~~~~~~~~~~~~~~~~~~~~~~~~~~#




#~~~~~~~~~~~~~~~~~~~~~~~CLASS ASGMT~~~~~~~~~~~~~~~~~~~~~~~~~~~#

class Asgmt(Grade):
    #points possible always same for asgmts; pointsE determined in setup
    def __init__(self, name:str="NOT SET", pointsEarned:int=0):
        #     0          1           2           3           4          5
        #  discuss1, draftheaders, discuss2,  progsub1,  progsub2, final/writeup
        self._stages:List[Grade] = [Grade("discussion post 1",
                                         pointsEarned = -1, pointsPossible=5),
                                   Grade("draft headers",
                                         pointsEarned = -1, pointsPossible = 5),
                                   Grade("discussion post 2",
                                         pointsEarned = -1, pointsPossible=5),
                                   Grade("progress submission 1",
                                         pointsEarned = -1, pointsPossible = 10),
                                   Grade("progress submission 2",
                                         pointsEarned = -1, pointsPossible = 10),
                                   Grade("final submission and writeups",
                                         pointsEarned = -1, pointsPossible = 100)]
        super().__init__(name, sum([g.pointsPossible for g in self._stages]),
                         pointsEarned)

    def __str__(self):
        ret = super().__str__() + "\nStages:\n"
        for grade in self._stages:
            ret += str(grade) + '\n'
        return ret

    #Allows RecursionErrors to be passed to client code if user cancels
    #MUST handle in client code - RecursionError signifies user cancelling setup,
    #should cancel addition of new grade object
    def setup(self, superIsSetUp:bool = False) -> bool:
        if not superIsSetUp:
            super().setup()
        choice:int = 0
        try:
            for g in self._stages:
                if g.pointsEarned != -1:
                    continue
                print(f"For {g.name}, enter the number of points earned "
                    + f"out of {g.pointsPossible}:")
                choice = self.getPosInt(max=g.pointsPossible) #unnecessary max?
                g.pointsEarned = choice
        except RecursionError as re:
            print(re)
            return False
        except ValueError as ve:
            print(ve)
            self.setup(True)
        self.pointsEarned = sum([g.pointsEarned for g in self._stages])
        return True

#~~~~~~~~~~~~~~~~~~~END CLASS ASGMT~~~~~~~~~~~~~~~~~~~~~~~~~~~#




#~~~~~~~~~~~~~~~~~~~~~~~CLASS DEMO~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

class Demo(Grade):
    weight = 0
    
    def __init__(self, name:str="NOT SET", pointsPossible:int=20,
                pointsEarned:int=-1):
        super().__init__(name, pointsPossible, pointsEarned)

    def getLetter(self) -> str:
        return super().getLetter(['U', "IP", "PW", 'P', 'E'])

    def needsRetake(self) -> bool:
        return self.getLetter() == "IP"

    def retake(self) -> None:
        try:
            newPoints:int = None
            print("Enter the new # of points earned out of",
                  str(self.pointsPossible), "or !q to cancel:")
            newPoints:str = self.getPosInt() #may throw RE or VE
            self.pointsEarned = newPoints
        except ValueError as ve:
            print(ve)
            self.retake()
        except RecursionError as re: #user cancels or recursion depth exceeded
            print(re) #return to calling scope

#~~~~~~~~~~~~~~~~~~~END CLASS DEMO~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
