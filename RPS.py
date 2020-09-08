import random
items=["rock","scissor","paper"]
print()
print("start the game:")
chance=10
i=1
while chance>0:
    print("--------------------------------------")
    print("your turn:\n1)rock for press 1:"
          "\n2)scissor for press 2:"
          "\n3)paper for press 3:")
    print("Enter {} time".format(i))
    a = int(input())
    user=items[a-1]
    computer = random.choice(items)
    print(user)
    print("computer choice:", computer)
    print(user, "vs" ,computer)
    if user==computer:
        print("Tie!")

    if user!=computer:
        if(user=="rock"):
            if(computer=="scissor"):
                print("you won!", user , "smashed", computer)
            elif(computer=="paper"):
                print("you lost!", computer,"covered", user)

        if (user=="scissor"):
            if(computer=="rock"):
                print("you lost!", computer , "smashed",user)
            elif(computer=="paper"):
                print("you won!", user,  "cut" , computer)

        if(user=="paper"):
            if(computer=="rock"):
                print(" you won! ",user ,"cover" , computer)
            elif(computer=="scissor"):
                print("you lost!scissor cut the paper")

    chance-=1
    i+=1





