# Encapsulation Example
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner  # Public attribute
        self.__balance = balance  # Private attribute

    # Public method to access private balance
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"{amount} deposited. Current balance: {self.__balance}")
        else:
            print("Deposit amount must be positive.")

    # Public method to access private balance
    def withdraw(self, amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
            print(f"{amount} withdrawn. Remaining balance: {self.__balance}")
        else:
            print("Invalid withdrawal amount.")

    # Getter for balance (encapsulation)
    def get_balance(self):
        return self.__balance

# Test Encapsulation
account = BankAccount("John", 1000)
account.deposit(500)
account.withdraw(200)
print("Balance:", account.get_balance())
