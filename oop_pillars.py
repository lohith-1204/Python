# OOP Pillars - Abstraction & Encapsulation

# Encapsulation

class BankAccount:
    
    def __init__(self, balance):
        self.__balance = balance   # private variable

    def deposit(self, amount):
        self.__balance += amount
        print("Deposited:", amount)

    def get_balance(self):
        return self.__balance


account = BankAccount(1000)

account.deposit(500)
print("Balance:", account.get_balance())

# Trying to access private variable (not recommended)
# print(account.__balance) ❌ Error

# Abstraction

from abc import ABC, abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def start(self):
        pass


class Car(Vehicle):

    def start(self):
        print("\nCar starts with a key")


class Bike(Vehicle):

    def start(self):
        print("Bike starts with a button")


# Creating objects
car = Car()
bike = Bike()

car.start()
bike.start()