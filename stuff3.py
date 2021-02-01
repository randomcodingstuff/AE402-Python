score=input("What is your grade? ")
score=int(score)
if (not(score>0 and score<100)):
    print("Re-enter your grade! ")
elif score>=90 and score<=99:
    print("You got a A! ")
elif score>=80 and score<=89:
    print("You got a B! ")
elif score>=70 and score<=79:
    print("You got a C! ")
elif score>=60 and score<=69:
    print("You got a D! ")
elif score<60:
    print("You got a F! You failed! ")