class Employee:
    def __init__(self,name,desi,salary):
        self.name=name
        self.desi=desi
        self.salary=salary

    def update_salary(self,new_salary):
        self.salary = new_salary

    def annual_income(self):
        return self.salary*12

    def print_employee_details(self):
        print("\nname: ",self.name)
        print("designation: ",self.desi)
        print("salary: ",self.salary)
     
        
emp1=Employee("Adams","Accountant",7000)
emp2=Employee("Jones","Clerk",5000)
emp3=Employee("Martin","Operator",6000)

print("employee 1 details:")
emp1.print_employee_details()
print("Annual income:",{emp1.annual_income()})
print("Updated salary:",emp1.update_salary(15000))
print()
print("employee 2 details:")
emp2.print_employee_details()
print("Annual income:",{emp2.annual_income()})
print("Updated salary:",emp2.update_salary(10000))
print()
print("employee 3 details:")
emp3.print_employee_details()
print("Annual income:",{emp3.annual_income()})
print("Updated salary:",emp3.update_salary(12000))
