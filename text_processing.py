"""
*Program 5 : Text Processing
*Programmer: Chandler Kilpatrick
*Due: 10/28/19
*CS 3A, Fall 2019
*Description: This program will search for and interact with a specific character.
"""



# This function requests a key character from the user.
def getKeyCharacter():
    keyCharacter = ''
    while len(keyCharacter) != 1 :
        keyCharacter = input("Please enter a SINGLE character to act as key: ")
    return keyCharacter

# This function requests a string from the user.
def getString():
    theString = ''
    while len(theString) < 4 :
        theString = input("Please enter a phrase or sentence >= 4 and <= 500 characters: ")
    return theString

# This function returns the string with all key character replaced with '*'.
def maskCharacter(theString, keyCharacter):
    new_word = ''
    for letter in theString:
        if letter == keyCharacter:
            new_word += '*'
        else:
            new_word += letter

    return new_word
        
# This function returns the string with all key character removed.
def removeCharacter(theString, keyCharacter):
    new_word = ''
    for letter in theString:
        if letter == keyCharacter:
            new_word += ''
        else:
            new_word += letter
    return new_word

# This function returns the number of times a key character appears.
def countKey(theString, keyCharacter):
    letter_count = 0
    for letter in theString:
        if letter == keyCharacter:
            letter_count += 1

    return letter_count

   
keyCharacter = getKeyCharacter()
theString = getString()
print("String with key character, '" + keyCharacter
      + "' masked: " + maskCharacter(theString, keyCharacter))
print("String with '" + keyCharacter + "' removed: "
      + removeCharacter(theString, keyCharacter))
print("# of occurrences of key character, '" + keyCharacter + "' : "
      + str(countKey(theString, keyCharacter)))




"""                         MY RUNS

##################################################################

Please enter a SINGLE character to act as key: e
Please enter a phrase or sentence >= 4 and <= 500 characters: hello
String with key character, 'e' masked: h*llo
String with 'e' removed: hllo
# of occurrences of key character, 'e' : 1
>>> 


##################################################################

Please enter a SINGLE character to act as key: eeeeeeeeee
Please enter a SINGLE character to act as key: ffffffff
Please enter a SINGLE character to act as key: e
Please enter a phrase or sentence >= 4 and <= 500 characters: h
Please enter a phrase or sentence >= 4 and <= 500 characters: hh
Please enter a phrase or sentence >= 4 and <= 500 characters: hhhheeeelllllllloooo
String with key character, 'e' masked: hhhh****lllllllloooo
String with 'e' removed: hhhhlllllllloooo
# of occurrences of key character, 'e' : 4

##################################################################

Please enter a SINGLE character to act as key: o
Please enter a phrase or sentence >= 4 and <= 500 characters: google
String with key character, 'o' masked: g**gle
String with 'o' removed: ggle
# of occurrences of key character, 'o' : 2

##################################################################

Please enter a SINGLE character to act as key: r
Please enter a phrase or sentence >= 4 and <= 500 characters: The Rat ran rapidly
String with key character, 'r' masked: The Rat *an *apidly
String with 'r' removed: The Rat an apidly
# of occurrences of key character, 'r' : 2

"""
