stuff=[]
people=int(input("How many people?"))
for n in range(people):
    score=int(input("What are the scores? "))
    stuff.append(score)
    avg=(sum(stuff)/people)
print("Highest score is ",max(stuff)," Lowest score is ",min(stuff))
print("The average is ",avg)