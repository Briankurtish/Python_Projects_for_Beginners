import random
#the library is used in order to choose random words from a list of words

name  = input("What is your name? ")
#The user is asked to enter the name first

print("Good luck! ", name)

words = ['rainbow', 'computer', 'science', 'programming', 'python', 'mathematics', 'player',
         'condition', 'reverse', 'water', 'board', 'cipher']


#The random function will choose a random word from the list of words above
word = random.choice(words)

print("Guess the Characters")

guesses = ''

#any of number of turns can be used here
turns = 12

while turns > 0:
    #count the number of times a user fails
    failed = 0
    
    #looping through all the characters from input word one at a time
    for char in word:
        
        #comparing that character with the character in guesses
        if char in guesses:
            print(char, end=" ")
        
        else:
            print("_")
            
            #for every failure, 1 will be incremented on the failure
            failed += 1
            
    if failed == 0:
        
        #user will win the game if failure is 0 and "you win will be printed out"
        print("You Win")
        
        print("The word is: ", word)
        break
    
    #if the user enters the wrong character, it will prompt the user to enter another character 
    print()
    guess = input("Guess a character: ")
    
    #Every input will be stored in guesses
    guesses += guess
    
    #check input with character in word
    if guess not in word:
        turns -= 1
        
        #if character does not match the word the wrong will be given as output
        print("Wrong")
        
        # this will print the number of
        # turns left for the user
        print("You have", + turns, 'more guesses')
 
        if turns == 0:
            print("You Loose")
