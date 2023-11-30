class Student:
    
    ### 類別屬性(Class Attribute) (常用的東西 可以避免重複輸入)
    school = "stust"
    school_addr = "stust.edu.com"

    ### 實體屬性(instnce Attribute)
    def __init__(self,  major, student_id, grade, point, GPA,student_addr):
        self.major =major
        self.student_id =student_id
        self.grade =grade
        self.point =point
        self.GPA =GPA
        self.student_addr = student_addr

    def set_school_name(self,school_name):
        self.school = school_name
        print("school name is change to " + str(school_name))
        
    def get_school_name(self):
        print("school name : " + str(self.school))

    def set_major(self, major):
        self.major = major
        print("Major is changed to " + str(major))

    def get_major(self):
        print("Major: " + str(self.major))

    def set_student_id(self, student_id):
        self.student_id = student_id
        print("Student ID is changed to " + str(student_id))

    def get_student_id(self):
        print("Student ID: " + str(self.student_id))

    def set_grade(self, grade):
        self.grade = grade
        print("Grade is changed to " + str(grade))

    def get_grade(self):
        print("Grade: " + str(self.grade))

    def set_point(self, point):
        self.point = point
        print("Point is changed to " + str(point))

    def get_point(self):
        print("Point: " + str(self.point))

    def set_GPA(self, GPA):
        self.GPA = GPA
        print("GPA is changed to " + str(GPA))

    def get_GPA(self):
        print("GPA: " + str(self.GPA))

    def set_self_addr(self, self_addr):
        self.self_addr = self_addr
        print("Self address is changed to " + str(self_addr))

    def get_self_addr(self):
        print("Self address: " + str(self.self_addr))

    def set_school_addr(self, school_addr):
        self.school_addr = school_addr
        print("School address is changed to " + str(school_addr))

    def get_school_addr(self):
        print("School address: " + str(self.school_addr))


st1 = Student("csie","4b0g0123","3","200","A","xxx.st1.xxx")

st1.get_school_addr()

st2 = Student("csie","4b0g0456","3","200","c","xxx.st2.xxx")

st2.get_school_addr()