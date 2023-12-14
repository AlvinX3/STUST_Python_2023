class Student:
    def __init__(self, name, studentID, major, books=None):
        self._name = name
        self._studentID = studentID
        self._major = major
        self._Subject = {name : [major]}
        self._Books = {name : [books]} if books else {}

class StudentMajor(Student):
    def __init__(self, name, studentID, major):
        super().__init__(name, studentID, major)
    
    def AddSubjects(self,newMajor):
        if self._name in self._Subject:
            self._Subject[self._name].append(newMajor)
        else:
            self._Subject[self._name] = [newMajor]
        print("add a new major: " + str(newMajor) + "\n" + "major: " + str(self._Subject[self._name]) + "\n")


    def WithdrawSubjects(self, delMajor):
        self._Subject[self._name].remove(delMajor)
        print("remove a old major: " + str(delMajor) + "\n" + "major: " + str(self._Subject[self._name]) + "\n")


    def InquireSubjects(self):
        print("name : " + str(self._name) + "\nmajor: " + str(self._Subject[self._name]) + "\n")


class StudentBooks(Student):
    def __init__(self, name, studentID, major, books=None):
        super().__init__(name, studentID, major, books)
        self._Books = {name : [books]} if books else {}

    def Borrow_books(self,newBook):
        if self._name in self._Subject:
            self._Books[self._name].append(newBook)
        else:
            self._Books[self._name] = [newBook]
        print("Borrow a books: " + str(newBook) + "\n" + "books: " + str(self._Books[self._name]) + "\n")

    def Return_Books(self, delBook):
        self._Books[self._name].remove(delBook)
        print("Return a Books: " + str(delBook) + "\n" + "books: " + str(self._Books[self._name]) + "\n")

    def InquireBook(self):
        print("name : " + str(self._name) + "\nbooks: " + str(self._Books[self._name]) + "\n")

st1 = StudentMajor("John", "1234", "Computer Science")
st1.InquireSubjects()
st1.AddSubjects("Mathematics")
st1.InquireSubjects()
st1.WithdrawSubjects("Computer Science")
st1.InquireSubjects()

st2 = StudentBooks("Mary", "5678", "Biology", "The Origin of Species")
st2.InquireBook()
st2.Borrow_books("The Selfish Gene")
st2.InquireBook()
st2.Return_Books("The Origin of Species")
st2.InquireBook()
