from abc import ABC, abstractmethod

# -------------------- TASK 1 --------------------
class Animal(ABC):

    @abstractmethod
    def speak(self):
        pass

# -------------------- TASK 2 --------------------
class Dog(Animal):
    def speak(self):
        return "Dog barks: Woof Woof!"

class Cat(Animal):
    def speak(self):
        return "Cat meows: Meow Meow!"
print("\n")

# -------------------- TASK 3 --------------------
class PaymentGateway(ABC):

    @abstractmethod
    def pay(self, amount):
        pass


class PayPal(PaymentGateway):
    def pay(self, amount):
        return f"Paid ₹{amount} using PayPal."


class Stripe(PaymentGateway):
    def pay(self, amount):
        return f"Paid ₹{amount} using Stripe."
print("\n")

# ------------ TESTING ------------
dog = Dog()
cat = Cat()
print(dog.speak())
print(cat.speak())

paypal = PayPal()
stripe = Stripe()
print(paypal.pay(500))
print(stripe.pay(750))
