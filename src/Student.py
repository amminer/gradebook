from multiprocessing.sharedctypes import Value
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
        try:
            print("Enter the name of the grade you'd like to remove",
            "or {!q} to cancel:", sep='\n')
            name = self.getStr(1)
            self.grades.remove(name) #throws VE on not found

        except RecursionError as re:
            print(re)

        except ValueError as ve:
            print(ve)
            self.removeFromStdin()

    # accepts strings or Grades
    def removeGrade(self, keyName:str):
        if type(keyName) == str or isinstance(keyName, Grade):
            self.grades.remove(keyName)
        else:
            raise ValueError(f"Type mismatch ({keyName} is not a string or a Grade)")

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

    def exam(self, thatExam:Exam or str):
        thisExam = self.grades.lookup(thatExam)
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
                    raise ValueError(f"{choice} is not a valid selection")
            except ValueError as ve:
                print(ve)
                self.exam(thatExam)
            except RecursionError as re:
                print(re)
        else:
            raise ValueError(f"Exam {thatExam} not found")

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
        if len(self.grades) == 0:
            return 0.0
        weightedPossible = \
            np.array([self.grades.at(i).pointsPossible*self.grades.at(i).weight
                 for i in range(len(self.grades))]).sum()
        weightedEarned = \
            np.array([self.grades.at(i).pointsEarned*self.grades.at(i).weight
                 for i in range(len(self.grades))]).sum()
        return weightedEarned / weightedPossible * 100

    """Generate a report with basic info about what a student's
    best and worst areas are in terms of grade types, maybe asgmt subgrades
    def report(self):
        pass #todo
    """

#~~~~~~~~~~~~~~~~~~~END CLASS STUDENT~~~~~~~~~~~~~~~~~~~~~~~~~#

def mainloop(student:Student, cont = True):
    print('\n' + str(s))
    print("Would you like to...",
          "   {Add} a new grade,",
          "   {Rem}ove a grade,",
          "   {Retake} a proficiency demo,",
          "   Look at missed questions from an {exam},"
          "or {Calc}ulate your total/cumulative grade?",
          "  ({!q} to quit)", sep='\n')
    try:
        choice = s.getStr().lower()
    except ValueError as ve:
        print(ve)
        return mainloop(s)
    except RecursionError as re:
        return
    if choice == "add":
        s.addFromStdin()
    elif choice == "rem":
        s.removeFromStdin()
    elif choice == "retake":
        s.retakeDemoFromStdin()
    elif choice == "exam":
        s.examFromStdin()
    elif choice == "calc":
        print(f"{s.cumulativeGrade():.2f}%")
    else:
        print("Invalid selection!")
    return mainloop(s)

if __name__ == "__main__":
    print("Welcome to assignment 4.")
    s = Student()
    s.editName()
    if s.name != "NOT SET":
        mainloop(s)
    print("Thanks for checking it out!")