math=input("What is your math grade? ")
english=input("What is your Englsih grade? ")
math=int(math)
english=int(english)
if math>=90 and english>=90 :
    print("You get a reward! ")
elif math>60 and english<60:
    print("Try harder! ")
elif math<60 and english>60:
    print ("Try harder! ")
else: 
    print("You get punishment! ")