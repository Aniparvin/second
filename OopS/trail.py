# class Person ():
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
    
#     @property
#     def name(self):
#         return self._name
#     @name.setter
#     def name(self, new_name):
#         if new_name.strip() == "":
#             print("Name cannot be empty!")
#         else:
#             self._name = new_name

#     @property
#     def age(self):
#         return self._age
#     @age.setter
#     def age(self, new_age):
#         if new_age <= 0:
#             print("Age must be greater than 0!")
#         else:
#             self._age = new_age

# class Student(Person):         
#     def show_role(self):
#         print(f"{self.name} ({self.age} years old) is a Student")


# class CollegeStudent(Student): 
#     def show_level(self):
#         print(f"{self.name} ({self.age} years old) is a College Student")

# class Teacher(Person):        
#     def show_role(self):
#         print(f"{self.name} ({self.age} years old) is a Teacher")

# cs = CollegeStudent("Alice", 19)
# cs.show_role()
# cs.show_level()

# cs.age = -5      
# cs.age = 20      
# print("Updated age:", cs.age)
# print()
# t = Teacher("Rahul", 40)
# t.show_role()


# Base Class
class Person:
    def __init__(self, name, age):
        self._name = name       # private-like variable
        self._age = age         # private-like variable

    # ----- Getter & Setter for name -----
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        if new_name.strip() == "":
            print("Name cannot be empty!")
        else:
            self._name = new_name

    # ----- Getter & Setter for age -----
    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, new_age):
        if new_age <= 0:
            print("Age must be greater than 0!")
        else:
            self._age = new_age


# ----- Multilevel Inheritance -----
class Student(Person):  # Person → Student
    def __init__(self, name, age, student_id):
        super().__init__(name, age)   # calling Person constructor
        self.student_id = student_id

    def show_role(self):
        print(f"{self.name} ({self.age}) is a Student. ID: {self.student_id}")


class CollegeStudent(Student):  # Person → Student → CollegeStudent
    def __init__(self, name, age, student_id, dept):
        super().__init__(name, age, student_id)  # calling Student constructor
        self.dept = dept

    def show_details(self):
        print(f"{self.name} ({self.age}) | ID: {self.student_id} | Dept: {self.dept}")


cs = CollegeStudent("Alice", 19, "S101", "Computer Science")

# Display
cs.show_role()
cs.show_details()

# Using Setter
cs.age = -10     # invalid
cs.age = 20      # valid

print("Updated age:", cs.age)

