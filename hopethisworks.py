names=list()
scores=list()
def average(scores):
    total=0
    n=len(scores)
    for item in scores:
        total=total+item
    average=total/n
    return average
def highestscore(scores):
    highest=0
    n=len(scores)
    for i in range(n):
        if scores[i]>highest:
            highest=scores[i]
            highestname=names[i]
    person=list()
    person.append(highestname)
    person.append(highest)
    return person
def lowestscore(scores):
    lowest=100
    n=len(scores)
    for i in range(n):
        if scores[i]<lowest:
            lowest=scores[i]
            lowestname=names[i]
            person=list()
    person.append(lowestname)
    person.append(lowest)
    return person
n=input("How many people? ")
n=int(n)
for i in range(n):
    name=input("Input name: ")
    names.append(name)
    score=int(input("Input score: "))
    scores.append(score)
    print(scores)
    print(names)
    ave=average(scores)
    high=highestscore(scores)
    low=lowestscore(scores)
print("The average is ",ave)
print(high[0],'got the highest score',high[1])
print(low[0],'got the lowest score',low[1])