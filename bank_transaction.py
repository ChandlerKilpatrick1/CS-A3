"""
*Program 3 : Bank Transaction
*Programmer: Chandler Kilpatrick
*Due: 10/14/19
*CS 3A, Fall 2019
*Description: This program will simulate a bank transaction.
"""

import sys

# This asks for the user's checking account balance.
checking_amount = float(input("Enter the initial balance for checking: " ))
# This asks for the user's checking account balance.
savings_amount = float(input("Enter the initial balance for savings: "))



# This if checks to make sure that the input is a valid account balance.
if (checking_amount) < 0 :
    print(' [ERROR] Please enter a positive balance for your checking account')
    sys.exit()

# This if checks to make sure that the input is a valid account balance.    
if (savings_amount) < 0 :
    print(" [ERROR] Please enter a positive balance for your savings account")
    sys.exit()
    
# This asks for the user to decide on an action. 
action_taken = input("Do you want to Deposit, Withdraw or Transfer?")

# This if statement deposits money into either account.
if action_taken == "Deposit":
    
    action_location = input("Deposit to (C)hecking or (S)avings?")
    action_amount = float(input("Deposit how much? "))
    if action_amount < 0:
        # This function appears when a negative amount is entered.
        print(" [ERROR] Deposit amount must be positive")
        sys.exit()
    # This if statement adds the deposit amount to the checking account.
    if action_location == "C":
        checking_amount += action_amount
    # This if statement adds the deposit amount to the savings account.
    elif action_location == "S":
        savings_amount += action_amount

    else:
        print("Please enter a 'C' or an 'S' ")
        sys.exit()       
       
# This elif statement withdraws money into either account.  
elif action_taken == "Withdraw":
    
    action_location = input("Withdraw from (C)hecking or (S)avings?")
    action_amount = float(input("Withdraw how much? "))
    if action_amount < 0:
        # This function appears when a negative amount is entered.
        print(" [ERROR] Withdrawal amount must be positive")
        sys.exit()
    # This if statement subtracts the withdrawal amount from the checking account.
    if action_location == "C":
        checking_amount -= action_amount
        # Checks to make sure balance amount is zero or greater.
        if checking_amount < 0:
            print("Balance cannot be less than zero")
            sys.exit()
        
    # This if statement subtracts the withdrawal amount from the savings account.
    elif action_location == "S":
        savings_amount -= action_amount
        # Checks to make sure balance amount is zero or greater.
        if checking_amount < 0:
            print("Balance cannot be less than zero")
            sys.exit()

    else:
        print("Please enter a 'C' or an 'S' ")
        sys.exit()  
# This elif statement transfers money into either account.  
elif action_taken == "Transfer":
    
    action_location = input("Transfer to (C)hecking or (S)avings?")
    action_amount = float(input("Transfer how much? "))
    # This function appears when a negative amount is entered.
    if action_amount < 0:
        print(" [ERROR] Transfer amount must be positive")
        sys.exit()
    
    if action_location == "C":
        checking_amount += action_amount
        savings_amount -= action_amount
        if savings_amount < 0:
            print("Balance cannot be less than zero")
            sys.exit()

    elif action_location == "S":
        savings_amount += action_amount
        checking_amount -= action_amount
        if checking_amount < 0:
            print("Balance cannot be less than zero")
            sys.exit()

    else:
        print("Please enter a 'C' or an 'S' ")
        sys.exit()

# This else statement appears if the user inputs none of the appropriate actions. 
else:
    print("Please enter a Valid Action")
    sys.exit()

# This prints the final account balances.
print("After the transaction:")
print(" Savings balance: " + str(savings_amount))
print(" Checking balance: " + str(checking_amount))


"""                         MY RUNS

##################################################################

Enter the initial balance for checking: 3000
Enter the initial balance for savings: 2000
Do you want to Deposit, Withdraw or Transfer?Deposit
Deposit to (C)hecking or (S)avings?C
Deposit how much?200
After the transaction:
 Savings balance: 2000.0
 Checking balance: 3200.0

##################################################################

Enter the initial balance for checking: 4000
Enter the initial balance for savings: 5000
Do you want to Deposit, Withdraw or Transfer?Transfer
Transfer to (C)hecking or (S)avings?S
Transfer how much? 400
After the transaction:
 Savings balance: 5400.0
 Checking balance: 3600.0

##################################################################

Enter the initial balance for checking: 4000
Enter the initial balance for savings: -3000
 [ERROR] Please enter a positive balance for your savings account

##################################################################

Enter the initial balance for checking: 4000
Enter the initial balance for savings: 3000
Do you want to Deposit, Withdraw or Transfer?withdrw
Please enter a Valid Action

"""
