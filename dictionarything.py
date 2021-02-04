d={}
print("#########################################################################################")
print("Welcome to the your words translator! ")
print("#########################################################################################")
print("Please enter the cooresponding number to the option you want to use! ")
print("#########################################################################################")
while True:
    print("1. Add words! ")
    print("2. List your words! ")
    print("3. English to Chinese! ")
    print("4. Chinese to English! ")
    print("5. Test yourself! ")
    print("6. ***Exit***")
    use=str(input("Enter the option (number)! "))
    if use=="1":
        while True:
            voc=input('Enter new English word! (enter 0 to exit) ')
            if voc=='0':
                break
            if voc not in d:
                    chinese=input("Enter Chinese translation! ")
                    d[voc]=chinese
            else: 
                print("Word already exists ")
    elif use=='2': 
        lk=sorted(d)
        for item in lk:
            print(item,'is', d[item])
    elif use=='3':
        voc=input('Enter English word you want to search! (enter 0 to exit) ')
        if voc=='0':
            break
        if voc in d:
            print(d[voc])
        else: 
            print("No matching word! ")
    elif use=='4':
        got=False
        ch=input('Enter Chinese word you want to search! (enter 0 to exit) ')
        if ch=='0':
            break
        for k,v in d.items():
            if ch==v:
                print(ch, "'s english is ",k)
                got=True
        if not got: 
            print('No matching word! ')
    elif use=='5':
        score=0
        print('The total score is',len(d),'points! ')
        for k,v in d.items():
            print(v,':')
            ans=input()
            if ans==k:
                score+=1
                print('Correct! You got ',score,'points now! ')
            else: 
                print('Wrong! You got ',score,' points now!　')
    elif use=='6':
        break
    else:
        print("Input invalid, try again! ")