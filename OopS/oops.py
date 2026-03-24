class Demo:

    # Class variable (shared by all objects)
    object_count = 0

    def __init__(self, name):
        # Instance variable (unique for each object)
        self.name = name
        Demo.object_count += 1

    # 1️⃣ Instance Method (uses self)
    def instance_method(self):
        return f"Instance Method: My name is {self.name}"

    # 2️⃣ Class Method (uses cls)
    @classmethod
    def class_method(cls):
        return f"Class Method: Total objects created = {cls.object_count}"

    # 3️⃣ Static Method (uses no self or cls)
    @staticmethod
    def static_method(a, b):
        return f"Static Method: {a} + {b} = {a + b}"


# ---------------- Example Usage ----------------

obj1 = Demo("Alice")
obj2 = Demo("Bob")

print(obj1.instance_method())      # Instance method
print(Demo.class_method())         # Class method
print(Demo.static_method(10, 20))  # Static method
print("\n")

#2
class User:

    # Class variable to track total users
    user_count = 0

    def __init__(self, name):
        self.name = name               # instance variable
        User.user_count += 1           # increase class count

    # Method to display user count
    @classmethod
    def display_user_count(cls):
        print(f"Total users created: {cls.user_count}")


# ---------------- Example Usage ----------------

u1 = User("Alice")
u2 = User("Bob")
u3 = User("Charlie")

User.display_user_count()    # Displays: Total users created: 3

