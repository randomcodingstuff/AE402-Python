import random 
num=random.randint(1,10)
guess=int(input("Guess a number form 1 to 10! "))
if not(guess>=0 and guess<=10):
    print("Re-enter a number from 1 to 10! ")
elif (guess==num):
    print("You guessed it correct! ")
else :
    print("You guessed it wrong! ")
    print("The answer is ",num)