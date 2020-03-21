# Week 2 submission
# Driver.py
# Driver application to instantiate a CheckingAccount object and perform tasks on the object

# Import the CheckingAccount module
from CheckingAccount import *

def main():
    # Instantiate the account with my name
    account1 = CheckingAccount('Randy Dailing')

    # Print the name, randomly generated account number and the beginning balance of $0
    print('Name: ' + account1.getName())
    print('Account Number: ' + str(account1.getAccountNumber()))
    print('Balance: $' + str(account1.getBalance()) + '\n')

    # Credit the account
    print ('Crediting $15.32')
    account1.creditAccount(15.32)
    print ('Balance:  $' + str(account1.getBalance()) + '\n')

    # Credit the account
    print ('Crediting $119.29')
    account1.creditAccount(119.29)
    print ('Balance:  $' + str(account1.getBalance()) + '\n')

    # Debit the account
    print ('Debiting $5.00')
    account1.debitAccount(5.00)
    print ('Balance  $' + str(account1.getBalance()) + '\n')

    # Credit the account
    print ('Crediting $25.00')
    account1.creditAccount(25.00)
    print ('Balance:  $' + str(account1.getBalance()) + '\n')


main()