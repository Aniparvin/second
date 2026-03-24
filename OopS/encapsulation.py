#1
class BankAccount:
    def __init__(self, initial_balance):
        self.__balance = initial_balance  # private variable

    @property
    def balance(self):
        """Getter method for balance"""
        return self.__balance

    @balance.setter
    def balance(self, amount):
        """Setter method with validation"""
        if amount < 0:
            raise ValueError("Balance cannot be negative.")
        self.__balance = amount


# Example usage
account = BankAccount(100)

print(account.balance) 

account.balance = 250    
print(account.balance)   

#2

class PasswordManager:
    def __init__(self, initial_password):
        self.__password = None      # private variable
        self.password = initial_password  # uses setter for validation

    @property
    def password(self):
        """Getter: returns masked version of the password."""
        return "*" * len(self.__password)

    @password.setter
    def password(self, new_password):
        """Setter: validates password before changing it."""
        if not self.__is_valid(new_password):
            raise ValueError(
                "Password must be at least 8 characters long, "
                "contain a number, and contain an uppercase letter."
            )
        self.__password = new_password

    def __is_valid(self, pwd):
        """Private validation method."""
        if len(pwd) < 8:
            return False
        if not any(ch.isdigit() for ch in pwd):
            return False
        if not any(ch.isupper() for ch in pwd):
            return False
        return True


# Example usage
pm = PasswordManager("Secure123")
print(pm.password)      # *********

pm.password = "NewPass9"
print(pm.password)      # ********

# This will raise a ValueError (fails validation):
# pm.password = "short"
