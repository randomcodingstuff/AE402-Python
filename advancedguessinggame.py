import random 
condition=True
count=0
num=random.randint(1,20)
while count<5 and condition==True: 
    guess=int(input("Guess a number form 1 to 20! "))
    count=count+1
    if not(guess>=0 and guess<=20):
        print("Re-enter a number from 1 to 20! ")
    elif (guess==num):
        print("You guessed it correct! ")
        print("You guessed ",count,"times! ")
        condition=False
    else :
        if guess>num: 
            print("You guessed it wrong! ") 
            print("Your answer was too large" )
        elif num>guess: 
            print("You guessed it wrong! ") 
            print("Your answer was too small" )
        else: 
            print("You failed, you used 5 times already! ")