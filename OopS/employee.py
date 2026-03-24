class Employee():

    def __init__(self, name, id, salary):
           self.name = name
           self.id = id
           self.salary = salary
               
    def get_details(self):
          print("print employe details :-")
          print(f"employe name: {self.name}")
          print(f"id: {self.id}")
          print(f"salary: {self.salary}" )
          print("-" * 30)

employees = [
    Employee("akash", 101, 10000),
    Employee("akshay", 102, 50000),
    Employee("akhil", 103, 20000),
    Employee("aysha", 105, 70000),
    Employee("daliya", 106, 30000),
    Employee("diya", 107, 15000),
    Employee("emin", 108, 10000),
    Employee("fathima", 110, 30000),
    Employee("geetha", 111, 20000),
    Employee("hari", 112, 10000),
    Employee("krishna", 113, 15000)
]
print("=== EMPLOYEE DETAILS ===")
print()

for emp in employees:
    emp.get_details()


