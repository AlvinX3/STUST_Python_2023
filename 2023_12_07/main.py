# ---- using getters & setters ----
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

# # ---- inheritance ----

class Sports:
    def __init__(self,name):
        self.name = name

    @property
    def sport_name(self):
        return self.name

    @sport_name.setter
    def student_name(self, values):
        print(f'"{self.name}" is now {values} .')
        self.name = values
    
    @sport_name.deleter
    def student_name(self):
        print(f'"{self.name}" was delete.')
        del self.name

    def practice(self):
        return "Doing " + str(self.name) + " practice."
        

class Land_Sports(Sports):
    def __init__(self,name , feild):
        super().__init__(name)
        self.feild = feild
    
    @property
    def Land_Sports_feild(self):
        return self.feild

    def practice(self):
        return "Doing " + str(self.name) + " practice in " + str(self.feild) + "."

class Water_Sprots(Sports):
    def __init__(self,name , activity):
        super().__init__(name)
        self.activity = activity
    
    @property
    def Land_Sports_activity(self):
        return self.activity
    
    def practice(self):
        return "Doing " + str(self.name) + " practice in " + str(self.feild) + "."

if __name__ == '__main__':
    # ----  using getters & setters ----
    # st1 = Student("xxxxx")

    # print(st1.student_name)
    # st1.student_name = 'ooooo'
    # del st1.student_name

    # print(st1.student_name)
    
    # ---- inheritance ----
    
    baseball = Land_Sports("baseball", "baseball field")
    print(baseball.sport_name)
    print(baseball.feild)
    print(baseball.practice())
    

    swim = Land_Sports("swim", "pool")
    print(swim.sport_name)
    print(swim.feild)
    print(swim.practice())

