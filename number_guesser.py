import random               #random module is imported

# r= random.randrange(5,11)
# s=random.randint(5,11)           #randint includes 11 too
# print(r)
# print(s)


top_of_range=input("Enter a number:")
if top_of_range.isdigit():
    top_of_range=int(top_of_range)
    if top_of_range<0:
        print("Please type a number greater than 0 next time.")
        quit()
else:
    print("Enter a number next time!")
    quit()

random_num=random.randint(0,top_of_range)

num_of_guess=0
while True:
    num_of_guess+=1
    guess=input("Make a guess:")
    if guess.isdigit():
        guess=int(guess)
    else:
        print("Please enter a number next time.")
        continue

    if guess==random_num:
        print("You got it!")
        break
    elif guess<random_num:
        print("Your guess was too low.")
    else:
        print("Your guess was too high.")
print(f"You got it in {num_of_guess} guesses.")