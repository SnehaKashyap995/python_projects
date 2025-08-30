import random
while True:
    my_list=["stone","paper","scissor","thread"]
    val=random.choice(my_list)
    print("1.stone"," 2.paper"," 3.scissor"," 4.thread")
    p=int(input(("Enter your choice:")))
    if p>4:
        print("Invalid input")
    print("computer:",val)
    if val=="stone":
        if p==1:
            print("Draw")
        if p==2:
            print("You Win")
        if p==3:
            print("You lose")
        if p==4:
            print("You Win")
    elif val=="paper":
        if p==1:
            print("You Lose")
        if p==2:
            print("Draw")
        if p==3:
            print("You Win")
        if p==4:
            print("You Win")
    elif val=="scissor":
        if p==1:
            print("You win")
        if p==2:
            print("You Lose")
        if p==3:
            print("Draw")
        if p==4:
            print("You Lose")
    elif val=="thread":
        if p==1:
            print("You lose")
        if p==2:
            print("You lose")
        if p==3:
            print("You Win")
        if p==4:
            print("Draw")
    print("\n")