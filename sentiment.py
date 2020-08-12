"""
*Program 9 : Sentiment
*Programmer: Chandler Kilpatrick
*Due: 12/2/19
*CS 3A, Fall 2019
*Description: This program will create a score for each word using a dictionary.
"""



# This function prints out the possible answers.
def print_prompt():
    print("What would you like to do?\n")
    print("1: Get the score of a word\n")
    print("2: Get the average score of words in a file\n")
    print("3: Find the highest / lowest scoring words in a file\n")
    print("4: Sort the words into positive.txt and negative.txt\n")
    print("5: Exit the program\n")
    action = input("Enter a number 1 - 5: ")
    return action



# This function set all letters to lowercase and ensure that letters are left. 
def no_punc(lines):
    new_string_list = []
    for line in lines:
        line = line.lower()
        line = line.strip()
        new_string = ""
        for char in line:
            if char in "abcdefghijklmnopqrstuvwxyz0123456789 ":
                new_string += char
        new_string_list.append(new_string)
    return new_string_list



# This function creates the dictionaries for a given file.
def create_dicts():
    file_name = input("file name? ")
    open_file = open(file_name, "r")
    word_rating = {} # sentiments
    word_count = {} # counts
    
    updated_file = no_punc(open_file)
    for line in updated_file:
        line = line.strip()
        line = line.lower()
        for word in line.split():
        
            if word not in word_rating:
                word_count[word] = 1
                word_rating[word] = int(line[0])/word_count[word]
            else:
                word_count[word] += 1
                word_rating[word] += int(line[0])/word_count[word]
    #print(word_count, word_rating)
    return(word_count, word_rating)



# This function finds the average of the sentiments.
def file_avg(sentiments):
    sentiments = float(sentiments)
    if sentiments > 2.01:
        print("is positive")
    elif sentiments <= 1.99 and sentiments >= 2.01:
        print("is neutral")
    elif sentiments < 1.99:
        print("is negative")       
        

# This function outputs a word as positive or negative.
def print_category(score):
    
    n_file = open("negative.txt", "w")
    p_file = open("positive.txt", "w")
    
    #sort into pos and neg 
    for k,v in score.items():
        if int(v) <= 1.99:
            n_file.write(str(k)+ '\n' + str(v) + '\n')

        elif int(v) >= 2.01:
            p_file.write(str(k)+ '\n' + str(v) + '\n')
    n_file.close()
    p_file.close()



# This function find the average of the specified file.
def avg_score_file(sentiments, counts):
    
    file_score = 0
    word_count = 0
    for k,v in counts.items():
        file_score += float(sentiments[k]) * int(counts[k])
        word_count += int(counts[k])
    print("score = " + str(file_score/word_count))
    return (str(file_score/word_count))



# This function add to the word count.
def add(score, words, sentiments, counts):
    for word in words.split():
        sentiments[word] = int(score)/counts[word]
        counts[word] += 1
        
    return (sentiments, counts)



# This function finds and prints the min and max of score of the given words.
def min_max():
    (word_count, word_rating) = create_dicts()
    sorted_word_rating = sorted(word_rating.items(), key=lambda x: x[1], reverse=True)
    print("Maximum Score is " + str(sorted_word_rating[0][1]) + " for "
          + str(sorted_word_rating[0][0]))
    print("Minimum Score is " + str(sorted_word_rating[-1][1]) + " for "
          + str(sorted_word_rating[-1][0]))   
    


# This main function runs the code.          
def main():
    (word_count, word_rating) = create_dicts()
    action = '0'
    while action != '5':
        action = print_prompt()
        
        if action == '1':
            word = input("which word? ")
            print("score = " + str(word_rating[word]))
            print(word, end = " ")
            file_avg(word_rating[word])

        elif action == '2':
            (word_count_one, word_rating_one) = create_dicts()
            score = avg_score_file(word_rating_one, word_count_one)
            file_avg(score)
            correctness = input("Am I right (yes/no)? ")
            if correctness == 'no':
                updates_score = input("What score should this sentence " + 
                                 "have (0 - 4 where 4 is the most positive)?")

        elif action == '3':
            min_max()

        elif action == '4':
            print_category(word_rating)

main()

"""                         MY RUNS

##################################################################

file name? training.txt
What would you like to do?

1: Get the score of a word

2: Get the average score of words in a file

3: Find the highest / lowest scoring words in a file

4: Sort the words into positive.txt and negative.txt

5: Exit the program

Enter a number 1 - 5: 1
which word? the
score = 18.179715422566407
the is positive
What would you like to do?

1: Get the score of a word

2: Get the average score of words in a file

3: Find the highest / lowest scoring words in a file

4: Sort the words into positive.txt and negative.txt

5: Exit the program

Enter a number 1 - 5: 2
file name? training.txt
score = 11.350787608757438
is positive
Am I right (yes/no)? yes
What would you like to do?

1: Get the score of a word

2: Get the average score of words in a file

3: Find the highest / lowest scoring words in a file

4: Sort the words into positive.txt and negative.txt

5: Exit the program

Enter a number 1 - 5: 2
file name? training.txt
score = 11.350787608757438
is positive
Am I right (yes/no)? no
What score should this sentence have (0 - 4 where 4 is the most positive)?4
What would you like to do?

1: Get the score of a word

2: Get the average score of words in a file

3: Find the highest / lowest scoring words in a file

4: Sort the words into positive.txt and negative.txt

5: Exit the program

Enter a number 1 - 5: 3
file name? training.txt
Maximum Score is 30.931917269407226 for 4
Minimum Score is 0.0 for conceivable
What would you like to do?

1: Get the score of a word

2: Get the average score of words in a file

3: Find the highest / lowest scoring words in a file

4: Sort the words into positive.txt and negative.txt

5: Exit the program

Enter a number 1 - 5: 4
What would you like to do?

1: Get the score of a word

2: Get the average score of words in a file

3: Find the highest / lowest scoring words in a file

4: Sort the words into positive.txt and negative.txt

5: Exit the program

Enter a number 1 - 5: 5
>>> 

##################################################################



##################################################################
"""
