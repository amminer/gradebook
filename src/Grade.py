from Util import *
from random import shuffle

""" Amelia Miner;   Grade.py;   5/24/2022
CLASS GRADE
Generalization of leaf classes Exam, Demo, and Asgmt.
Has int attributes pointsPossible and pointsEarned to represent a score,
methods for calculating percentage and letter grades, and a method for
determining whether the grade passes.

CLASS EXAM (extends Grade)
Subclass Exam has boolean attribute _extraCredit and dict[str:str] _questions,
which maps missed questions to their correct answers, plus methods to add and remove
missed questions to the dict and to practice the missed questions like flash cards -
contrived, unsure if appropriate but had a hard time thinking of "jobs". Exams have a
weight of 4.

CLASS ASGMT (extends Grade)
Subclass Asgmt has a list of subgrades (List[Grade]) _stages, and calculates its
pointsEarned differently using this collection. Asgmts have a weight of 1.

CLASS DEMO (extends Grade)
Subclass Demo has additional methods for determining whether a retake is available
and for performing a retake (editing pointsEarned). It also overrides getLetter(). Demos
have a weight of 0.
"""

#~~~~~~~~~~~~~~~~~~~~~~~CLASS GRADE~~~~~~~~~~~~~~~~~~~~~~~~~~~#
""" Expects minimum pointsPossible of 1 (0? todo)
"""

class Grade(Util):
    """ Parent class for all grade subtypes -
    stores points earned/points possible and contains methods for calculating percent
    """
    weight = 1
    
    def __init__(self, name:str="NOT SET", pointsPossible:float=float('inf'),
                pointsEarned:int=-1):
        super().__init__(name)
        self._pointsPossible = pointsPossible
        self._pointsEarned = pointsEarned

    def __eq__(self, other):
        """ Compares this grade's name with that of another grade, or a string """
        if type(other) == str:
            return self.name == other
        elif isinstance(other, Grade):
            return self.name == other.name 
        else:
            return False

    def __str__(self):
        """ prints this grade's name, the number of points earned and the
        number of points possible, the grade as a percent, and the associated
        letter grade for that percent value. Uses the length of the name to
        pad output with tabs for consistent table-like display.
        """
        nameLen = len(self.name) + 1
        numTabs = 5
        while nameLen >= 8:
            numTabs -= 1
            nameLen -= 8
            if numTabs == 0:
                break
        if len(self.name) <= 37:
            ret = self.name + ':'
        else:
            ret = self.name[:37] + "..."
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

    def setup(self) -> bool:
        """ UI and business logic for setting up a new grade object
        unique in that it returns a boolean for whether the object was
        successfully set up so that the calling code knows whether it has
        a complete grade - if it does, add it to the student, else discard
        """
        choice:str = ""
        try:
            if self.name == "NOT SET":
                print("Enter a name/title for this grade:")
                choice = getStr(1)
                self.name = choice
            if self.pointsPossible == float('inf'):
                print(f"Enter the number of possible points (must be > {self.pointsEarned}):")
                choice = getPosInt()
                self.pointsPossible = choice
            if self.pointsEarned == -1:
                print(f"Enter the number of points earned out of {self.pointsPossible}:")
                choice = getPosInt()
                self.pointsEarned = choice
        except UserCancelsException as canceled:
            print(canceled)
            return False
        except ValueError as ve:
            print(ve)
            self.setup()
        return True

    def edit(self) -> None:
        """ UI and business logic for editing an existing grade object """
        try:
            self.editName()
        except UserCancelsException as canceled:
            print(canceled)

    def getLetter(self, letters:Tuple[str]=['F','D','C','B','A']) -> str:
        """ uses Grade.getPercentage to determine a letter grade;
        letters argument allows for different grading schemes
        """
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
        """ uses pointsPossible and pointsEarned to calculate a percentage grade """
        if self.pointsPossible == 0:
            percentage = 0.0
        else:
            percentage = self.pointsEarned / self.pointsPossible * 100
        return percentage

    def passes(self, percentageNeeded:float=70.0) -> bool:
        """ uses Grade.getPercentage to determine whether the grade is passing
        percentageNeeded argument allows for different requirements for passing
        """
        if percentageNeeded < 0: percentageNeeded = 0.0
        elif percentageNeeded > 100: percentageNeeded = 100.0
        return self.getPercentage() >= percentageNeeded

#~~~~~~~~~~~~~~~~~~~END CLASS GRADE~~~~~~~~~~~~~~~~~~~~~~~~~~~#




#~~~~~~~~~~~~~~~~~~~~~~~CLASS EXAM~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

class Exam(Grade):
    """ Includes basic Grade functionality, plus boolean extra credit data member
    which is applied to percent value on calculation.
    Also contains a map of missed questions -> correct answers so that missed questions can be studied by the student, and methods for managing this map.
    """
    weight = 4

    def __init__(self, name:str="NOT SET",
                 pointsPossible:int=float('inf'), pointsEarned:int=-1,
                 questions:Dict[str,str]=dict(), extraCredit=False):
        self._questions:Dict[str,str] = questions
        self._extraCredit = extraCredit
        super().__init__(name, pointsPossible=pointsPossible,
                         pointsEarned=pointsEarned)

    def setup(self, superIsSetUp:bool = False) -> bool:
        if not superIsSetUp:
            super().setup()
        choice:int = 0
        try:
            print("Apply extra credit to this exam? Enter {y} or {n},\n"
                + "or {!q} to cancel:")
            choice = getStr(1)
            if choice == 'y':
                self._extraCredit = True
            elif choice == 'n':
                self._extraCredit = False
            else:
                raise ValueError("Input must be \"y\" or \"n\"")
        except ValueError as ve:
            print(ve)
            return self.setup(True)
        except UserCancelsException as canceled:
            print(canceled)
            return False
        
        return True

    def __str__(self) -> str:
        """ Calls base class __str__ and handles missed questions """
        ret:str = ""
        if self._questions:
            ret += "\nMissed questions:\n"
        for q in self._questions.keys():
            ret += q + '\n'
        return super().__str__() + ret
        
    def getPercentage(self) -> float:
        """ same as superclass but incorporates extra credit """
        ret:float = super().getPercentage()
        if self._extraCredit:
            ret += 5.0
        return ret

    def addMissedQuestion(self):
        """ adds a missed question to the map """
        print("Enter the new question:")
        try:
            newQuestion = getStr(1)
            print("Enter the correct answer:")
            newAnswer = getStr(1)
            self._questions[newQuestion] = newAnswer
        except ValueError as ve:
            print(ve)
            self.addMissedQuestion()
        except UserCancelsException as canceled:
            print(canceled)

    def removeMissedQuestion(self):
        """ removes a missed question from the map """
        toRem:str = ""
        print("Enter the name of the question to remove:")
        try:
            toRem = getStr(1)
            del self._questions[toRem]
        except (ValueError, KeyError):
            print(f"{toRem} was not found...")
            self.removeMissedQuestion()
        except UserCancelsException as canceled:
            print(canceled)

    def practice(self):
        answer:str = ""
        if not self._questions:
            print("Nothing to practice!")
        for q in shuffle(list(self._questions.items())):
            print(q[0])
            print("Enter your answer:")
            try:
                answer = getStr(1)
                print ("Correct answer:", q[1], sep='\n')
            except UserCancelsException or ValueError as e:
                print(e)
                print("Skipping for now...")
                continue

#~~~~~~~~~~~~~~~~~~~END CLASS EXAM~~~~~~~~~~~~~~~~~~~~~~~~~~~~#




#~~~~~~~~~~~~~~~~~~~~~~~CLASS ASGMT~~~~~~~~~~~~~~~~~~~~~~~~~~~#

class Asgmt(Grade):
    """ includes basic Grade functionality, but contains a list of sub-grades
    one for each stage of the assignment. Points possible and points earned for the
    overall assignment are calculated based on sums from this list.
    """
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
        """ calls superclass __str__ as well as handling stages """
        ret = super().__str__() + "\nStages:\n"
        for grade in self._stages:
            ret += str(grade) + '\n'
        return ret

    def setup(self, superIsSetUp:bool = False) -> bool:
        """ calls superclass setup as well as prompting user to fill out stages """
        if not superIsSetUp:
            super().setup()
        choice:int = 0
        try:
            for g in self._stages:
                if g.pointsEarned != -1:
                    continue
                print(f"For {g.name}, enter the number of points earned "
                    + f"out of {g.pointsPossible}:")
                choice = getPosInt(max=g.pointsPossible) #unnecessary max?
                g.pointsEarned = choice
        except UserCancelsException as canceled:
            print(canceled)
            return False
        except ValueError as ve:
            print(ve)
            self.setup(True)
        self.pointsEarned = sum([g.pointsEarned for g in self._stages])
        return True

#~~~~~~~~~~~~~~~~~~~END CLASS ASGMT~~~~~~~~~~~~~~~~~~~~~~~~~~~#




#~~~~~~~~~~~~~~~~~~~~~~~CLASS DEMO~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

class Demo(Grade):
    """ demos are a little odd in that they don't play into the final grade
    for the course. Demos must be passed with at least a letter grade of "PW".
    As long as all demos pass this barrier, the student passes the class overall.
    """
    weight = 0
    
    def __init__(self, name:str="NOT SET", pointsPossible:int=20,
                pointsEarned:int=-1):
        super().__init__(name, pointsPossible, pointsEarned)

    def getLetter(self) -> str:
        """ uses a different grading scheme """
        return super().getLetter(['U', "IP", "PW", 'P', 'E'])

    def needsRetake(self) -> bool:
        """ demos must exceed this letter grade to pass """
        return self.getLetter() == "IP"

    def retake(self) -> None:
        """ allows students to retake their demos - students get one opportunity
        to do so if their demo doesn't pass the first time
        """
        try:
            newPoints:int = None
            print("Enter the new # of points earned out of",
                  str(self.pointsPossible), "or !q to cancel:")
            newPoints:str = getPosInt()
            self.pointsEarned = newPoints
        except ValueError as ve:
            print(ve)
            self.retake()
        except UserCancelsException as canceled:
            print(canceled)

#~~~~~~~~~~~~~~~~~~~END CLASS DEMO~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
