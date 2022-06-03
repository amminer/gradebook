from Util import *
from Grade import *
from LLL import LLL
import numpy as np

""" CLASS STUDENT
    Manages a linear linked list of grades
"""

#~~~~~~~~~~~~~~~~~~~~~~~CLASS STUDENT~~~~~~~~~~~~~~~~~~~~~~~~~#

class Student(Util):

    def __init__(self, name:str = "NOT SET"):
        super().__init__(name)
        self.grades = LLL()

    def __str__(self):
        return f"Student {self.name}:\n{str(self.grades)}"

    def addFromStdin(self):
        try:
            print("Which type of grade is this?",
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
                raise ValueError("Input must match exam, demo, asgmt, or !q")
            if newGrade.setup():
                self.grades.pushBack(newGrade)
            else:
                print("Canceled addition")

        except RecursionError as re:
            print(re)

        except ValueError as ve:
            print(ve)
            self.addFromStdin()

    #may raise VE on type mismatch (must be Grade)
    def addGrade(self, newGrade:Grade):
        if isinstance(newGrade, Grade):
            self.grades.pushBack(newGrade)
        else:
            raise ValueError(f"Type mismatch ({newGrade} is not a Grade)")

    def removeFromStdin(self):
        pass #TODO

    # accepts strings or Grades
    def removeGrade(self, keyName:str):
        if type(keyName) == str or isinstance(keyName, Grade):
            self.grades.remove(keyName)
        else:
            raise ValueError(f"Type mismatch ({keyName} is not a string or a Grade)")

    def retakeDemoFromStdin(self):
        print("Enter the name of the demo to retake:")
        try:
            choice = self.getStr(1)
            self.retakeDemo(choice)
        except RecursionError as re:
            print(re)
        except ValueError as ve:
            print(ve)
            self.retakeDemoFromStdin()

    """ 
    TODO define some methods for interacting with exam.questions from stdin
    """

    def retakeDemo(self, thatDemo:Demo):
        thisDemo = self.grades.lookup(thatDemo)
        if thisDemo:
            if thisDemo.needsRetake():
                thisDemo.retake() #may raise RE on cancel - catch in UI
            else:
                print(f"{thisDemo.name} does not qualify for a retake")
        else:
            raise ValueError(f"Demo {thatDemo} not found")

    """All points so far, weighted and combined"""
    def cumulativeGrade(self) -> float:
        """Ideally I would do this, but don't have time to write an iterator
        weightedPossible = sum([g.pointsPossible*g.weight for g in self.grades])
        weightedEarned = sum([g.pointsEarned * g.weight for g in self.grades])
        """
        weightedPossible = \
            sum([self.grades.at(i).pointsPossible*self.grades.at(i).weight
                 for i in range(len(self.grades))])
        weightedEarned = \
            sum([self.grades.at(i).pointsEarned*self.grades.at(i).weight
                 for i in range(len(self.grades))])
        print(str(weightedEarned), "out of", str(weightedPossible))
        return weightedEarned / weightedPossible * 100

    """Generate a report with basic info about what a student's
    best and worst areas are in terms of grade types, maybe asgmt subgrades
    def report(self):
        pass #TODO
    """

#~~~~~~~~~~~~~~~~~~~END CLASS STUDENT~~~~~~~~~~~~~~~~~~~~~~~~~#

if __name__ == "__main__":
    print ("TODO implement a main menu? Want to wait until we have a gradebook...")