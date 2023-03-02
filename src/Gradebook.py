from Util import *
from Grade import Grade, Asgmt, Exam, Demo
from Student import Student
from BST import BST

""" Amelia Miner;   Gradebook.py;   6/7/2022
Entry point for the program
CLASS GRADEBOOK
Uses a BST to hold students, defines a CLI for itself.
"""

class Gradebook(Util):
    """ Manages a collection of students and presents the top level UI
    students are kept in a BST (_students)
    """
    def __init__(self, name: str = "NOT SET"):
        super().__init__(name)
        self._students: BST[Student] = BST()

    def addStudentFromStdin(self) -> None:
        """ prompts user to enter the name of a new student
        and adds that student to the BST
        """
        try:
            print("Enter the name of the new student:")
            name = getStr(1)
            newStudent = Student(name)
            self._students.insert(newStudent)
        except ValueError as ve:
            print(ve)
            return self.addStudentFromStdin()
        except UserCancelsException as canceled:
            print(canceled)
        return

    def removeStudentFromStdin(self):
        """ prompts user to enter the name of an existing student
        and removes that student from the BST
        """
        if len(self._students) == 0:
            print("No students to remove!")
            return
        try:
            print("Enter the name of the student to remove:")
            name = getStr(1)
            self._students.remove(name)
        except ValueError as ve:
            print(ve)
            return self.removeStudentFromStdin()
        except UserCancelsException as canceled:
            print(canceled)
        return

    def lookupStudentFromStdin(self):
        """ prompts the user to enter the name of an existing student
        and finds that student in the BST if there is a match.
        If so, prints the student's grades.
        """
        if len(self._students) == 0:
            print("No students to look up!")
            return
        try:
            print("Enter the name of the student:")
            name = getStr(1)
            thatOne = self._students.lookup(name)
            if thatOne != None:
                print(thatOne)
            else:
                raise ValueError(f"Unable to find {name}.\n")

        except ValueError as ve:
            print(ve)
            return self.lookupStudentFromStdin()

        except UserCancelsException as canceled:
            print(canceled)

        return

    def editStudentFromStdin(self):
        """ prompts the user to enter the name of an existing student
        and finds that student in the BST if there is a match.
        If so, passes UI control to the student object for editing.
        """
        if len(self._students) == 0:
            print("No students to edit!")
            return
        try:
            print("Enter the name of the student to edit:")
            name = getStr(1)
            thatOne = self._students.lookup(name)
            if thatOne != None:
                thatOne.mainloop()
            else:
                raise ValueError(f"Unable to find {name}.\n")

        except ValueError as ve:
            print(ve)
            return self.editStudentFromStdin()

        except UserCancelsException as canceled:
            print(canceled)

        return

    def display(self):
        """ prints the contents of the gradebook """
        if len(self._students) == 0:
            print("No students to display!")
        else:
            print("\n~GRADEBOOK~\n")
            self._students.display()

    def mainloop(self):
        """ top level menu for the program """
        cont = True
        print(" ___ "
              , "/ _ \\   _________________________", "|O O|  / Hi, I'm Clippy!         \\", "||U|||<  Welcome to Gradebook.py!｜", "||_||| \\_________________________/", "\\\\_//", sep='\n')
        while cont:
            try:
                self.presentInterface(
                    "\n~MAIN MENU~\nWould you like to...\n"
                    + "{Add} a new student,\n"
                    + "{Remove} a student,\n"
                    + "{Lookup} a student,\n"
                    + "{Edit} a student's grades,\n"
                    + "or {Display} the contents of the gradebook?\n"
                    + "Enter {!q} to quit.",
                    ["add", "remove", "lookup", "edit", "display"],
                    [self.addStudentFromStdin,
                     self.removeStudentFromStdin,
                     self.lookupStudentFromStdin,
                     self.editStudentFromStdin,
                     self.display])
            except UserCancelsException as canceled:
                cont = False
                print("Thanks for stopping by!")
            except ValueError as ve:
                print(ve)


if __name__ == "__main__":
    Gradebook().mainloop()
