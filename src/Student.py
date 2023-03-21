from Util import *
from Grade import Grade, Demo, Asgmt, Exam
from LLL import LLL
import numpy as np

""" Amelia Miner;   Student.py;   6/2/2022
CLASS STUDENT
Manages a linear linked list of grades, defines a CLI for itself.
"""

#~~~~~~~~~~~~~~~~~~~~~~~CLASS STUDENT~~~~~~~~~~~~~~~~~~~~~~~~~#

class Student(Util):
    """ contains a list of grades and implements a user interface to be
    swapped in/out with the Gradebook UI.
    Note that there is no option for editing existing grades outside of
    retaking a proficiency demo.
    """
    def __init__(self, name:str = "NOT SET"):
        super().__init__(name)
        self._grades = LLL()

    def __str__(self):
        return f"Student {self.name}:\n{str(self._grades)}"

    def __eq__(self, other) -> bool:
        """ compares by name strings """
        if isinstance(other, Student):
            return self.name == other.name
        elif isinstance(other, str):
            return self.name == other
        elif other == None:
            return False
        else:
            raise ValueError(f"Type mismatch ({other} is not a name or Student)\n")
    
    def __le__(self, other) -> bool:
        """ compares by name strings """
        if isinstance(other, Student):
            return self.name <= other.name
        elif isinstance(other, str):
            return other > self.name
        else:
            raise ValueError(f"Type mismatch ({other} is not a name or Student)\n")

    def __ge__(self, other) -> bool:
        """ compares by name strings """
        if isinstance(other, Student):
            return self.name >= other.name
        elif isinstance(other, str):
            return other < self.name
        else:
            raise ValueError(f"Type mismatch ({other} is not a name or Student)\n")

    def __gt__(self, other) -> bool:
        """ compares by name strings """
        if isinstance(other, Student):
            return self.name > other.name
        elif isinstance(other, str):
            return other <= self.name
        else:
            raise ValueError(f"Type mismatch ({other} is not a name or Student)\n")

    def __lt__(self, other) -> bool:
        """ compares by name strings """
        if isinstance(other, Student):
            return self.name < other.name
        elif isinstance(other, str):
            return other >= self.name
        else:
            raise ValueError(f"Type mismatch ({other} is not a name or Student)\n")

    def addFromStdin(self):
        """ UI for adding a grade to the student's list """
        try:
            newGrade = self.presentInterface(
                "Which is the type of the new grade?"
                + "{exam}, Proficicency {demo},"
                + "or Programming {asgmt}?\n"
                +"({!q} to cancel)",
            ["exam", "demo", "asgmt"],
            [Exam, Demo, Asgmt])
            if newGrade.setup():
                self._addGrade(newGrade)
            else:
                print("Canceled addition")
        except UserCancelsException as canceled:
            print(canceled)
        except ValueError as ve:
            print(ve)
            self.addFromStdin()
    def _addGrade(self, newGrade:Grade):
        """ Function separated out for easier testing """
        if isinstance(newGrade, Grade):
            self._grades.pushBack(newGrade)
        else:
            raise ValueError(f"Type mismatch ({newGrade} is not a Grade)\n")

    def removeFromStdin(self):
        """ UI for removing a grade to the student's list """
        try:
            print("Enter the name of the grade you'd like to remove",
            "or {!q} to cancel:", sep='\n')
            name = getStr(1)
            self._removeGrade(name)
        except UserCancelsException as canceled:
            print(canceled)
        except ValueError as ve:
            print(ve)
            self.removeFromStdin()
    def _removeGrade(self, keyName:str):
        """ Function separated out for easier testing """
        if type(keyName) == str or isinstance(keyName, Grade):
            self._grades.remove(keyName)
        else:
            raise ValueError(f"Type mismatch ({keyName} is not a string or a Grade)\n")

    def retakeDemoFromStdin(self):
        """ UI for retaking (editing) a student's demo grade """
        print("Enter the name of the demo to retake, or {!q} to cancel:")
        try:
            choice = getStr(1)
            self.retakeDemo(choice)
        except UserCancelsException as canceled:
            print(canceled)
        except ValueError as ve:
            print(ve)
            self.retakeDemoFromStdin()

    def exam(self, thatExam:Exam or str):
        """ UI for interacting with a student's exam (adding or removing questions,
        practicing missed questions)
        """
        thisExam = self._grades.lookup(thatExam)
        if thisExam:
            try:
                self.presentInterface(
                    "Would you like to {add} a question, "
                    + "{rem}ove a question, "
                    + "or {practice}?\n{!q} to cancel",
                    ["add", "rem", "practice"],
                    [thisExam.addMissedQuestion,
                     thisExam.removeMissedQuestion,
                     thisExam.practice])
            except ValueError as ve:
                print(ve)
                self.exam(thatExam)
            except UserCancelsException as canceled:
                print(canceled)
        else:
            raise ValueError(f"Exam {thatExam} not found\n")

    def examFromStdin(self):
        """ UI for finding an exam by name to interact with """
        try:
            print("Enter the name of the exam, or {!q} to cancel:")
            name = getStr()
            self.exam(name)
        except UserCancelsException as canceled:
            print(canceled)
        except ValueError as ve:
            print(ve)
            self.examFromStdin()

    def retakeDemo(self, thatDemo:Demo):
        """ UI for interacting with a Demo grade (retaking)
        Note that Demo.retake may raise a
        UserCancelsException on user cancellation,
        which must be handled in calling code """
        thisDemo = self._grades.lookup(thatDemo)
        if thisDemo:
            if thisDemo.needsRetake():
                thisDemo.retake()
            else:
                print(f"{thisDemo.name} does not qualify for a retake")
        else:
            raise ValueError(f"Demo {thatDemo} not found\n")

    def cumulativeGrade(self) -> float:
        """ Computes all points so far, weighted and combined """
        if len(self._grades) == 0:
            return 0.0
        weightedPossible = \
            np.array([self._grades.at(i).pointsPossible*self._grades.at(i).weight
                 for i in range(len(self._grades))]).sum()
        weightedEarned = \
            np.array([self._grades.at(i).pointsEarned*self._grades.at(i).weight
                 for i in range(len(self._grades))]).sum()
        return weightedEarned / weightedPossible * 100

    def mainloop(self, cont = True) -> None:
        """ Top level interface for interacting with a student object;
        pass-off point between Student and Gradebook
        """
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
            
            except UserCancelsException as canceled:
                cont = False
                print("Returning to gradebook...")

            return self.mainloop(cont)
        else:
            return

#~~~~~~~~~~~~~~~~~~~END CLASS STUDENT~~~~~~~~~~~~~~~~~~~~~~~~~#
