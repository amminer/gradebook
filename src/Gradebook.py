from Grade import * #Util, Grade and subclasses, container typehints
from Student import Student
from BST import BST

""" Amelia Miner;   Gradebook.py;   6/7/2022
CLASS GRADEBOOK
Uses a BST to hold students, defines a CLI for itself.
"""

class Gradebook(Util):
    def __init__(self, name:str = "NOT SET"):
        super().__init__(name)
        self._students:BST[Student] = BST()
    
    def addStudentFromStdin(self) -> None:
        try:
            print("Enter the name of the new student:")
            name = self.getStr(1) #may throw RE or VE
            newStudent = Student(name)
            self._students.insert(newStudent)

        except ValueError as ve:
            print(ve)
            return self.addStudentFromStdin()
        
        except RecursionError as re:
            print(re)

        return

    def removeStudentFromStdin(self):
        if len(self._students) == 0:
            print("No students to remove!")
            return
        try:
            print("Enter the name of the student to remove:")
            name = self.getStr(1) #may raise VE
            self._students.remove(name) #may raise VE

        except ValueError as ve:
            print(ve)
            return self.removeStudentFromStdin()

        except RecursionError as re:
            print(re)

        return

    def lookupStudentFromStdin(self): #calls Student.mainloop on name match
        if len(self._students) == 0:
            print("No students to look up!")
            return
        try:
            print("Enter the name of the student:")
            name = self.getStr(1) #may raise VE
            thatOne = self._students.lookup(name)
            if thatOne != None:
                print(thatOne)
            else:
                raise ValueError(f"Unable to find {name}.\n")

        except ValueError as ve:
            print(ve)
            return self.lookupStudentFromStdin()
        
        except RecursionError as re:
            print(re)

        return

    def editStudentFromStdin(self): #calls Student.mainloop on name match
        if len(self._students) == 0:
            print("No students to edit!")
            return
        try:
            print("Enter the name of the student to edit:")
            name = self.getStr(1) #may raise VE
            thatOne = self._students.lookup(name)
            if thatOne != None:
                thatOne.mainloop()
            else:
                raise ValueError(f"Unable to find {name}.\n")

        except ValueError as ve:
            print(ve)
            return self.editStudentFromStdin()
        
        except RecursionError as re:
            print(re)

        return

    def display(self):
        if len(self._students) == 0:
            print("No students to display!")
        else:
            print("\n~GRADEBOOK~\n")
            self._students.display()

    def mainloop(self):
        cont = True
        print(" ___ " #TODO write Util.printClippyMessage(str)
             ,"/ _ \\   _________________________"
             ,"|O O|  / Hi, I'm Clippy!         \\"
             ,"||U|||<  Welcome to Gradebook.py! |"
             ,"||_||| \\__________________________/"
             ,"\\\\_//", sep='\n')
        while cont:
            try:
                self.presentInterface(
                    "\n~MAIN MENU~\nWould you like to...\n"
                   +"{Add} a new student,\n"
                   +"{Remove} a student,\n"
                   +"{Lookup} a student,\n"
                   +"{Edit} a student's grades,\n"
                   +"or {Display} the contents of the gradebook?\n"
                   +"Enter {!q} to quit.",
                   ["add", "remove", "lookup", "edit", "display"],
                   [self.addStudentFromStdin,
                   self.removeStudentFromStdin,
                   self.lookupStudentFromStdin,
                   self.editStudentFromStdin,
                   self.display])
            except RecursionError as re:
                cont = False
                print("Thanks for stopping by!")

if __name__ == "__main__":
    Gradebook().mainloop()
