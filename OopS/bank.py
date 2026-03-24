class BankAccount():
    def __init__(self, balance , pin):
        self._balance = balance
        self.__pin = pin

    #private method to check pin
    def __check__pin(self,entered_pin):
        return entered_pin == self.__pin
    
    #public method to access the balance
    def get_balance(self):
        return self._balance
    
    #public method to deposite
    def deposite(self,amount,entered_pin):
        if self.__check__pin(entered_pin):
                self._balance+=amount
                print(f"deposite amount : {amount}")
                print(f"the deposite is successful. New balance : {self._balance}")
        else:
            print("incorrect pin...") 
    
    #public method to withdraw
    def withdraw(self,amount, entered_pin):
        if self.__check__pin(entered_pin):
            if self._balance>=amount:
                self._balance-=amount
                print(f"withdraw amount : {amount}")
                print(f"the withdrawal is successful. New balance : {self._balance}")
            else:
                print("insufficient balance")
        else:
            print("incorrect pin...")
              
        
account = BankAccount(2000, "2002")
#direct access to public attribute

print(account._balance)
print(account.get_balance)
account.withdraw(200, "2002")
account.deposite(2000, "2002")




    