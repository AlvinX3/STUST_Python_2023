from collections import defaultdict

class Student:
    def __init__(self):
        self.student_list = []

    def add_student(self, student_id):
        self.student_list.append(student_id)


class StudentMajor(Student):
    def __init__(self):
        super().__init__()
        self.major_dict = defaultdict(list)

    def add_major(self, student_id, major):
        self.major_dict[student_id].append(major)

    def remove_major(self, student_id, major):
        if student_id in self.major_dict:
            self.major_dict[student_id].remove(major)

    def get_major(self, student_id):
        if student_id in self.major_dict:
            return self.major_dict[student_id]
        else:
            return None

student = Student()
student_major = StudentMajor()

def admins():
    while 1:
        print("[1] add new student\n[2] add/delect student's major\n[3] check student\n[4] sing out\n")

        choice = input("choose:")
        
        if choice == "1":
                student_id = input("New student id:")
                student.add_student(student_id)
                print(f"add {student_id}.\n")

        elif choice == "2":
            print("[1] Add student's major\n[2] Delect student's major\n[3] exit\n")
            choice = input("choose:")
            student_id = input("student ID:")

            if choice == "1":
                major = input("Major:")
                student_major.add_major(student_id, major)
                print(f"add {student_id}'s major {major}.\n")

            elif choice == "2":
                major = input("Major:")
                student_major.remove_major(student_id,major)
                print(f"Delect {student_id}'s major.\n")


            elif choice == "3":
                print("exit.\n")
                break
        
        elif choice == "3":
            student_id = input("Student ID: ")
            major = student_major.get_major(student_id)
            if major is not None:
                print(f"Student {student_id}'s major: {major}.\n")
            else:
                print(f"Can't found {student_id}'s major.\n")
        
        elif choice == "4":
            print("Sign out")
            break


def login():
    user = input("userName(student ID): ")
    pwd = input("password: ")
    
    return user, pwd

if __name__ == '__main__':
    while 1:
        user, pwd = login()
        if user == "admin":
            admins()
        else:
            print("cant not found the user.")



    # while 1:
    #     print("[1] add new student\n[2] add/delect student's major\n[3] check student\n[4] sing out\n")

    #     choice = input("choose:")
        
    #     if choice == "1":
    #             student_id = input("New student id:")
    #             student.add_student(student_id)
    #             print(f"add {student_id}.\n")

    #     elif choice == "2":
    #         print("[1] Add student's major\n[2] Delect student's major\n[3] exit\n")

    #         student_id = input("student ID:")

    #         if choice == "1":
    #             major = input("Major:")
    #             student_major.add_major(student_id, major)
    #             print(f"add {student_id}'s major {major}.\n")

    #         elif choice == "2":
    #             student_major.remove_major(student_id)
    #             print(f"Delect {student_id}'s major.\n")


    #         elif choice == "3":
    #             print("exit.\n")
    #             break
        
    #     elif choice == "3":
    #         student_id = input("Student ID: ")
    #         major = student_major.get_major(student_id)
    #         if major is not None:
    #             print(f"Student {student_id}'s major: {major}.\n")
    #         else:
    #             print(f"Can't found {student_id}'s major.\n")