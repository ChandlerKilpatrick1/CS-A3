"""
*Program 2 : Five_Expressions
*Programmer: Chandler Kilpatrick
*Due: 10/7/19
*CS 3A, Fall 2019
*Description: This program will compute and display five values/equations.
"""

# This prints the required information.
print("My family name is Kilpatrick \n"
      + "My Student ID is 20407711 \n"
      + "The number of characters in my first name is 8 \n"
)
# The variable is representing my ID number.
myId = 20407711

# The number of letters in my last name.
numLet = 10

# This will calculate and print expression one:
expression_answer = myId % 17
print("Expression #1 ---------- :" + str(expression_answer)+ "\n")

# This will calculate and print expression two:
expression_answer = (numLet + 17) % 11
print("Expression #2 ---------- :" + str(expression_answer)+ "\n")

# This will calculate and print expression three:
expression_answer = myId/(numLet + 800)
print("Expression #3 ---------- :" + str(expression_answer)+ "\n")

# This will calculate and print expression four:
expression_answer = 1+2+3+4+5+6+7+8+9+10
print("Expression #4 ---------- :" + str(expression_answer)+ "\n")

# This will calculate and print expression five:
# Function without the parentheses: 5000/80 +myId-123456/numLet+20*numLet+20
# expression_answer = 15000/(80 +((myId-123456)/(numLet+20)**2))

expression_answer = 15000/(80 +((myId-123456)/((numLet+20)*(numLet+20))))
print("Expression #5 ---------- :" + str(expression_answer)+ "\n")


""" --------------- RUN -----------------
My family name is Kilpatrick 
My Student ID is 20407711 
The number of characters in my first name is 8 

Expression #1 ---------- :10

Expression #2 ---------- :5

Expression #3 ---------- :25194.704938271603

Expression #4 ---------- :55

Expression #5 ---------- :0.6631868189900353

-------------------------------------- """
