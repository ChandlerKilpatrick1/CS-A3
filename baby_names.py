"""
*Program 6 : Baby Names
*Programmer: Chandler Kilpatrick
*Due: 11/4/19
*CS 3A, Fall 2019
*Description: This program will ask for and show the statistics behind a baby name.
"""

# This function calls and saves the return values of other functions.
def main():
    name_to_search = beginning()
    line_found = finding(name_to_search)
    formatted_print(line_found)


# This function will prompt the user for a baby name.
def beginning():
    print("This program allows you to search through the data " 
          + "from the Social Security Administration "
          + "to see how popular a particular name has been since 1900.")
    name = input("Type a name: ")
    print("Popularity ranking of name " + '"'+ name + '"' )
    return name

# This function will find the request baby name in the name.txt
def finding(name):
    CONST_file_name = "names.txt"
    open_file = open(CONST_file_name, 'r')
    str_holder = ""
    for line in open_file:
        for character in line:
            if character == " ":
                if str(str_holder).lower() == str(name).lower():
                    return line
                else:
                    str_holder = ""
                    break
                
            str_holder += character


    not_found = '"' + name + '"' + ' not found.'
    return not_found


# This function will print out the required format for the name statistics.
def formatted_print(line_found):
    CONST_starting_year = 1900
    if line_found.__contains__("not found"):
        print(line_found)
    else:
        str_holder = ""
        starting_year = CONST_starting_year
        line_found = line_found.lstrip() + " "
        name_flag = False
        
        for character in line_found:
            str_holder += character
            if character == " ":
                if name_flag == False:
                    name_flag = True
                    str_holder = ""
                else:    
                    print(str(starting_year) + ": " + str_holder)
                    str_holder = ""
                    starting_year += 10
    

    
main()
        


"""                         MY RUNS

##################################################################

This program allows you to search through the data from the Social Security Admi
nistration to see how popular a particular name has been since 1900.
Type a name: Lisa
Popularity ranking of name "Lisa"
1900: 0 
1910: 0 
1920: 0 
1930: 0 
1940: 464 
1950: 38 
1960: 1 
1970: 6 
1980: 31 
1990: 113 
2000: 298

##################################################################

This program allows you to search through the data from the Social Security Admi
nistration to see how popular a particular name has been since 1900.
Type a name: hksjdhf
Popularity ranking of name "hksjdhf"
"hksjdhf" not found.

##################################################################
"""
    
            
