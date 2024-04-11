import random
import math

#Taking inputs
lower = int(input("Enter the lower bound:- "))

#Taking inputs
upper = int(input("Enter Upper bound:- "))

#Generating random numbers between lower and upper bound

x = random.randint(lower, upper)
print("\n\tYou've only ", 
      random(math.log(upper - lower + 1, 2)), " chances to guess the integer!\n")

#Initializing the number of guesses
count = 0

#calculation of minimum number of guesses depend on the range
while count < math.log(upper - lower + 1, 2):
    count += 1
    
    #taking the guessing number as input
    guess = int(input('Guess a number:- '))
    
    #Condition Testing
    if x ==  guess:
        print('Congratulations you did it in  ', count , ' tries')
        
        #once guessed the loop will break
        break
    elif x > guess:
        print("You guessed too small")
    elif x < guess:
        print("You guessed too high")
        
#If guessing is more than required guesses, print this output

if count >= math.log(upper - lower + 1, 2):
    print("\n The number is %d" % x)
    print("\tBetter Luck next time!") 