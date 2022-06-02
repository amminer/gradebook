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

    #may raise VE on type mismatch (must be Grade)
    def addGrade(self, newGrade:Grade):
        if type(newGrade) == Grade:
            LLL.pushBack(newGrade)
        else:
            raise ValueError(f"Type mismatch ({newGrade} is not a Grade)")

    def removeGrade(self, keyName:str):
        pass

    def retakeDemo(self):
        pass

    """All grades together so far - weight is built into points"""
    def cumulativeGrade(self):
        pass

    """Generate a report with basic info about what a student's
    best and worst areas are in terms of grade types, maybe asgmt subgrades"""
    def report(self):
        pass

#~~~~~~~~~~~~~~~~~~~END CLASS STUDENT~~~~~~~~~~~~~~~~~~~~~~~~~#
