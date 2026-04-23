# Advanced Banking System using OOP

class BankAccount:
    def __init__(self, name, balance=0):
        self.name = name
        self._balance = balance   # protected variable

    def deposit(self, amount):
        self._balance += amount
        print("Deposited:", amount)

    def withdraw(self, amount):
        if amount > self._balance:
            print("Insufficient balance!")
        else:
            self._balance -= amount
            print("Withdrawn:", amount)

    def display_balance(self):
        print("Balance:", self._balance)


# -------------------------------
# Savings Account (Inheritance)
# -------------------------------

class SavingsAccount(BankAccount):
    def add_interest(self):
        interest = self._balance * 0.05
        self._balance += interest
        print("Interest added:", interest)


# -------------------------------
# Current Account (Polymorphism)
# -------------------------------

class CurrentAccount(BankAccount):
    def withdraw(self, amount):  # overriding
        if amount > self._balance + 500:  # overdraft
            print("Overdraft limit exceeded!")
        else:
            self._balance -= amount
            print("Withdrawn:", amount)


# -------------------------------
# Main Program
# -------------------------------

print("1. Savings Account")
print("2. Current Account")

choice = input("Choose account type: ")
name = input("Enter your name: ")

if choice == '1':
    acc = SavingsAccount(name, 1000)
elif choice == '2':
    acc = CurrentAccount(name, 1000)
else:
    print("Invalid choice")
    exit()

while True:
    print("\n1. Deposit\n2. Withdraw\n3. Balance\n4. Exit")

    ch = input("Enter choice: ")

    if ch == '1':
        amt = float(input("Enter amount: "))
        acc.deposit(amt)

    elif ch == '2':
        amt = float(input("Enter amount: "))
        acc.withdraw(amt)

    elif ch == '3':
        acc.display_balance()

    elif ch == '4':
        break

    else:
        print("Invalid option")