"""
*Program 4 : Chocolate Coupons
*Programmer: Chandler Kilpatrick
*Due: 10/21/19
*CS 3A, Fall 2019
*Description: This program will simulate a transaction of selling chocolate bars.
"""

mainmenu_input = " "
num_credits = 0

while mainmenu_input[0].lower() != 's':
    print("Menu:\n\tP (process Purchase)\n\tS (Shut down)\n\n")
    mainmenu_input = input("Your Choice:")
    # This if is directs for input P
    if mainmenu_input[0].lower() == 'p':
        # This if is ensures that you qualify for a free bar.
        if num_credits >= 7:
            print("You qualify for a free chocolate bar. " 
                  + "Would you like to use your credits?")
            use_coupon = input("(Y or N)")

            # This if is directs for input Yes
            if use_coupon.lower() == 'y':
                
                num_credits -= 7
                print("You have just used 7 credits and have "
                      + str(num_credits) + " left.")
                print("Enjoy your free chocolate bar.")
            # This if is directs for input No    
            elif use_coupon.lower() == 'n':
                
                new_num_credits = int(input("How many chocolate bars would you like to buy?"))

                # This if is ensures that inputs are greater than 0.
                if new_num_credits < 0:
                    
                    print("\nPlease enter a valid number of chocolate bars to purchase.\n")
                else:

                    num_credits += new_num_credits
                    # num_credits += int(input("How many chocolate bars would you like to buy?"))
                    print("You just earned " + str(new_num_credits)
                        + " coupons and have a total of " + str(num_credits) + " to use.")
                    
            else:
                
                print("*** Invalid response ***")
                
        else:
            new_num_credits = int(input("How many chocolate bars would you like to buy?"))
            num_credits += new_num_credits
            # num_credits += int(input("How many chocolate bars would you like to buy?"))
            print("You just earned " + str(new_num_credits)
            + " coupons and have a total of " + str(num_credits) + " to use.")
            
    elif mainmenu_input[0].lower() == 's':
        break
        
    else:
        print("\n\n*** Use P or S, please. ***\n\n")
    
# End of While Loop    
    
print("System shutting down.\nGood bye")









"""                         MY RUNS

##################################################################

Menu:
	P (process Purchase)
	S (Shut down)


Your Choice:d


*** Use P or S, please. ***


Menu:
	P (process Purchase)
	S (Shut down)


Your Choice:push
How many chocolate bars would you like to buy?14
You just earned 14 coupons and have a total of 14 to use.
Menu:
	P (process Purchase)
	S (Shut down)


Your Choice:p
You qualify for a free chocolate bar. Would you like to use your credits?
(Y or N)n
How many chocolate bars would you like to buy?21
You just earned 21 coupons and have a total of 35 to use.
Menu:
	P (process Purchase)
	S (Shut down)


Your Choice:p
You qualify for a free chocolate bar. Would you like to use your credits?
(Y or N)j
*** Invalid response ***
Menu:
	P (process Purchase)
	S (Shut down)


Your Choice:p
You qualify for a free chocolate bar. Would you like to use your credits?
(Y or N)n
How many chocolate bars would you like to buy?2
You just earned 2 coupons and have a total of 37 to use.
Menu:
	P (process Purchase)
	S (Shut down)


Your Choice:proc
You qualify for a free chocolate bar. Would you like to use your credits?
(Y or N)y
You have just used 7 credits and have 30 left.
Enjoy your free chocolate bar.
Menu:
	P (process Purchase)
	S (Shut down)


Your Choice:s
System shutting down.
Good bye

##################################################################

Menu:
	P (process Purchase)
	S (Shut down)


Your Choice:p
How many chocolate bars would you like to buy?3
You just earned 3 coupons and have a total of 3 to use.
Menu:
	P (process Purchase)
	S (Shut down)


Your Choice:PUSH
How many chocolate bars would you like to buy?7
You just earned 7 coupons and have a total of 10 to use.
Menu:
	P (process Purchase)
	S (Shut down)


Your Choice:PPPPP
You qualify for a free chocolate bar. Would you like to use your credits?
(Y or N)n
How many chocolate bars would you like to buy?5
You just earned 5 coupons and have a total of 15 to use.
Menu:
	P (process Purchase)
	S (Shut down)


Your Choice:PULLLLLL
You qualify for a free chocolate bar. Would you like to use your credits?
(Y or N)n
How many chocolate bars would you like to buy?10
You just earned 10 coupons and have a total of 25 to use.
Menu:
	P (process Purchase)
	S (Shut down)


Your Choice:PARKING
You qualify for a free chocolate bar. Would you like to use your credits?
(Y or N)n
How many chocolate bars would you like to buy?7
You just earned 7 coupons and have a total of 32 to use.
Menu:
	P (process Purchase)
	S (Shut down)


Your Choice:Poor
You qualify for a free chocolate bar. Would you like to use your credits?
(Y or N)n
How many chocolate bars would you like to buy?5
You just earned 5 coupons and have a total of 37 to use.
Menu:
	P (process Purchase)
	S (Shut down)


Your Choice:p
You qualify for a free chocolate bar. Would you like to use your credits?
(Y or N)y
You have just used 7 credits and have 30 left.
Enjoy your free chocolate bar.
Menu:
	P (process Purchase)
	S (Shut down)


Your Choice:PaCk
You qualify for a free chocolate bar. Would you like to use your credits?
(Y or N)YESSSS
*** Invalid response ***
Menu:
	P (process Purchase)
	S (Shut down)


Your Choice:PACK
You qualify for a free chocolate bar. Would you like to use your credits?
(Y or N)y
You have just used 7 credits and have 23 left.
Enjoy your free chocolate bar.
Menu:
	P (process Purchase)
	S (Shut down)


Your Choice:g


*** Use P or S, please. ***


Menu:
	P (process Purchase)
	S (Shut down)


Your Choice:p
You qualify for a free chocolate bar. Would you like to use your credits?
(Y or N)f
*** Invalid response ***
Menu:
	P (process Purchase)
	S (Shut down)


Your Choice:s
System shutting down.
Good bye

##################################################################


"""

