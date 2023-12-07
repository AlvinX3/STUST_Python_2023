# using getters & setters
class Student:

    def __init__(self, name):
        self.name = name

    @property
    def student_name(self):
        print(f'"{self.name}" was accessed.')
        return self.name
    
    @student_name.setter
    def student_name(self, values):
        print(f'"{self.name}" is now {values} .')
        self.name = values
    
    @student_name.deleter
    def student_name(self):
        print(f'"{self.name}" was delete.')
        del self.name


if __name__ == '__main__':
    st1 = Student("xxxxx")

    print(st1.student_name)
    st1.student_name = 'ooooo'
    del st1.student_name

    print(st1.student_name)
    