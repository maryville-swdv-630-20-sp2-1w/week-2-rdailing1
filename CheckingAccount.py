# Week 2 submission
# CheckingAccount.py
# Application containing one class: CheckingAccount

# Get the random integer generator for creating test account numbers
from random import randint

class CheckingAccount:
    # Initialize the instance
    def __init__(self, name):
        self.name = name
        self.address = ''
        self.phone = ''
        self.email = ''
        self._balance = 0.0
        self.accountNumber = randint(150000, 200000)

    # Update the address
    def updateAddress(self, address):
        self.address = address

    # Get the address
    def getAddress(self):
        return self.address

    # Update the phone number
    def updatePhone(self, phoneNumber):
        self.phone = phoneNumber

    # Get the phone number
    def getPhone(self):
        return self.phone

    # Update the email address
    def updateEmail(self, email):
        self.email = email

    # Get the email address
    def getEmail(self):
        return self.email

    # Credit the account
    def creditAccount(self, amount):
        self._balance += amount

    # Debit the account
    def debitAccount(self, amount):
        self._balance -= amount

    # Get the name on the account
    def getName(self):
        return self.name

    # Get the account number
    def getAccountNumber(self):
        return self.accountNumber

    # Get the current balance
    def getBalance(self):
        return self._balance
