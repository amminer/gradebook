from Grade import * #Util, Grade and subclasses, container typehints
from Student import Student
from BST import BST

""" CLASS GRADEBOOK
Uses a BST to hold students
"""

class Gradebook(Util):
    def __init__(self, name:str = "NOT SET"):
        super().__init__(name)
        self.students:BST[Student] = BST()
    
    def addStudentFromStdin(self) -> None:
        try:
            print("Enter the name of the new student:")
            name = self.getStr(1) #may throw RE or VE
            newStudent = Student(name)
            self.students.insert(newStudent)

        except ValueError as ve:
            print(ve)
            return self.addStudentFromStdin()
        
        except RecursionError as re:
            print(re)

        return

    def removeStudentFromStdin(self):
        pass

    def editStudentFromCin(self):
        pass

    def editStudentFromCin(self): #calls Student.mainloop on name match
        pass