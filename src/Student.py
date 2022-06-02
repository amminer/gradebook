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

    def addFromStdin(self):
        pass #TODO

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

    def retakeDemo(self):
        pass #TODO

    """All grades together so far - weight is built into points"""
    def cumulativeGrade(self):
        pass #TODO

    """Generate a report with basic info about what a student's
    best and worst areas are in terms of grade types, maybe asgmt subgrades"""
    def report(self):
        pass #TODO

#~~~~~~~~~~~~~~~~~~~END CLASS STUDENT~~~~~~~~~~~~~~~~~~~~~~~~~#
