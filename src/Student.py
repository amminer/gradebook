from Util import *
from Grade import *
from LLL import LLL
import numpy as np

""" Amelia Miner;   Student.py;   6/2/2022
CLASS STUDENT
Manages a linear linked list of grades, defines a CLI for itself.
"""

#~~~~~~~~~~~~~~~~~~~~~~~CLASS STUDENT~~~~~~~~~~~~~~~~~~~~~~~~~#

class Student(Util):

    def __init__(self, name:str = "NOT SET"):
        super().__init__(name)
        self._grades = LLL()

    def __str__(self):
        return f"Student {self.name}:\n{str(self._grades)}"

    def __eq__(self, other) -> bool:
        if isinstance(other, Student):
            return self.name == other.name
        elif isinstance(other, str):
            return self.name == other
        elif other == None:
            return False
        else:
            raise ValueError(f"Type mismatch ({other} is not a keyname or Student)\n")
    
    def __le__(self, other) -> bool:
        if isinstance(other, Student):
            return self.name <= other.name
        elif isinstance(other, str):
            return other > self.name
        else:
            raise ValueError(f"Type mismatch ({other} is not a keyname or Student)\n")

    def __ge__(self, other) -> bool:
        if isinstance(other, Student):
            return self.name >= other.name
        elif isinstance(other, str):
            return other < self.name
        else:
            raise ValueError(f"Type mismatch ({other} is not a keyname or Student)\n")

    def __gt__(self, other) -> bool:

        if isinstance(other, Student):
            return self.name > other.name
        elif isinstance(other, str):
            return other <= self.name
        else:
            raise ValueError(f"Type mismatch ({other} is not a keyname or Student)\n")

    def __lt__(self, other) -> bool:

        if isinstance(other, Student):
            return self.name < other.name
        elif isinstance(other, str):
            return other >= self.name
        else:
            raise ValueError(f"Type mismatch ({other} is not a keyname or Student)\n")

    def addFromStdin(self):
        try:
            print("Which is the type of the new grade?",
                  "{Exam}", "Proficicency {Demo}", "or Programming {Asgmt}?",
                  "({!q} to cancel)", sep='\n')
            type = self.getStr(4).lower()
            if type == "exam":
                newGrade = Exam()
            elif type == "demo":
                newGrade = Demo()
            elif type == "asgmt":
                newGrade = Asgmt()
            else:
                raise ValueError("Input must match exam, demo, asgmt, or !q\n")
            if newGrade.setup():
                self._addGrade(newGrade)
            else:
                print("Canceled addition")

        except RecursionError as re:
            print(re)

        except ValueError as ve:
            print(ve)
            self.addFromStdin()

    #may raise VE on type mismatch (must be Grade)
    def _addGrade(self, newGrade:Grade):
        if isinstance(newGrade, Grade):
            self._grades.pushBack(newGrade)
        else:
            raise ValueError(f"Type mismatch ({newGrade} is not a Grade)\n")

    def removeFromStdin(self):
        try:
            print("Enter the name of the grade you'd like to remove",
            "or {!q} to cancel:", sep='\n')
            name = self.getStr(1)
            self._removeGrade(name) #throws VE on not found

        except RecursionError as re:
            print(re)

        except ValueError as ve:
            print(ve)
            self.removeFromStdin()

    # accepts strings or Grades
    def _removeGrade(self, keyName:str):
        if type(keyName) == str or isinstance(keyName, Grade):
            self._grades.remove(keyName)
        else:
            raise ValueError(f"Type mismatch ({keyName} is not a string or a Grade)\n")

    def retakeDemoFromStdin(self):
        print("Enter the name of the demo to retake, or {!q} to cancel:")
        try:
            choice = self.getStr(1)
            self.retakeDemo(choice)
        except RecursionError as re:
            print(re)
        except ValueError as ve:
            print(ve)
            self.retakeDemoFromStdin()

    #forgot to use presentInterface here, oh well?
    def exam(self, thatExam:Exam or str):
        thisExam = self._grades.lookup(thatExam)
        if thisExam:
            try:
                print("Would you like to {add} a question, {rem}ove a question,",
                    "or {practice}?\n{!q} to cancel")
                choice = self.getStr().lower()
                if choice == "add":
                    thisExam.addMissedQuestion()
                elif choice == "rem":
                    thisExam.removeMissedQuestion()
                elif choice == "practice":
                    thisExam.practice()
                else:
                    raise ValueError(f"{choice} is not a valid selection\n")
            except ValueError as ve:
                print(ve)
                self.exam(thatExam)
            except RecursionError as re:
                print(re)
        else:
            raise ValueError(f"Exam {thatExam} not found\n")

    def examFromStdin(self):
        try:
            print("Enter the name of the exam, or {!q} to cancel:")
            name = self.getStr()
            self.exam(name)
        except RecursionError as re:
            print(re)
        except ValueError as ve:
            print(ve)
            self.examFromStdin()

    def retakeDemo(self, thatDemo:Demo):
        thisDemo = self._grades.lookup(thatDemo)
        if thisDemo:
            if thisDemo.needsRetake():
                thisDemo.retake() #may raise RE on cancel - catch in UI
            else:
                print(f"{thisDemo.name} does not qualify for a retake")
        else:
            raise ValueError(f"Demo {thatDemo} not found\n")

    """All points so far, weighted and combined"""
    def cumulativeGrade(self) -> float:
        """Ideally I would do this, but don't have time to write an iterator
        weightedPossible = sum([g.pointsPossible*g.weight for g in self._grades])
        weightedEarned = sum([g.pointsEarned * g.weight for g in self._grades])
        """
        if len(self._grades) == 0:
            return 0.0
        weightedPossible = \
            np.array([self._grades.at(i).pointsPossible*self._grades.at(i).weight
                 for i in range(len(self._grades))]).sum()
        weightedEarned = \
            np.array([self._grades.at(i).pointsEarned*self._grades.at(i).weight
                 for i in range(len(self._grades))]).sum()
        return weightedEarned / weightedPossible * 100

    """Generate a report with basic info about what a student's
    best and worst areas are in terms of grade types, maybe asgmt subgrades
    def report(self):
        pass #todo
    """

    def mainloop(self, cont = True) -> None:
        print('\n' + str(self))
        if cont:
            try:
                self.presentInterface(
                    "Would you like to...\n"
                +"{Add} a new grade,\n"
                +"{Rem}ove a grade,\n"
                +"{Retake} a proficiency demo,\n"
                +"Look at missed questions from an {exam},\n"
                +"or {calc}ulate your total/cumulative grade?\n"
                +"Enter {!q} to return.",
                ["add", "rem", "retake", "exam", "calc"],
                [self.addFromStdin, self.removeFromStdin,
                    self.retakeDemoFromStdin, self.examFromStdin,
                    lambda self=self: print(f"{self.cumulativeGrade():.2f}%")])
            
            except RecursionError as re:
                cont = False
                print("Returning to gradebook...")

            return self.mainloop(cont)
        else:
            return

#~~~~~~~~~~~~~~~~~~~END CLASS STUDENT~~~~~~~~~~~~~~~~~~~~~~~~~#

"""
if __name__ == "__main__":
    print("Welcome to assignment 4.")
    s = Student()
    s.editName()
    if s.name != "NOT SET":
        mainloop(s)
    print("Thanks for checking it out!")
"""
