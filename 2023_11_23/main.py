class Employee_Data:
    def __init__(self, name, id, salary, sector):
        self.name = name
        self.id = id
        self.salary = salary
        self.sector = sector

    def assign_department(self, new_sector):
        self.sector = new_sector
        print("sector is change\nnew sector is "+ new_sector)

    def print_employee_details(self):
        print("\nname: " + self.name + "\nid: "  + self.id + "\nsalary: " +str( self.salary) + "\nsector: " + self.sector + "\n")

    def calculate_emp_salary(self, salary, hours_worked):
            overtime = hours_worked - 50
            Overtime_amount = (overtime * (salary / 50))
            print("total salary is " + str(int(Overtime_amount+self.salary)))



person1 = Employee_Data("ADAMS", "E7876", 50000, "ACCOUNTING")
person1.print_employee_details()
person1.assign_department("RESEARCH")
person1.print_employee_details()
person1.calculate_emp_salary(5000,51)


# "ADAMS", "E7876", 50000, "ACCOUNTING"
# "JONES", "E7499", 45000, "RESEARCH"
# "MARTIN", "E7900", 50000, "SALES"
# "SMITH", "E7698", 55000, "OPERATIONS"