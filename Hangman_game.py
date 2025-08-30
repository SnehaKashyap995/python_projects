import random
import emoji
print("!!!HANGMAN GAME!!!")
SomeWords=["mango","guava","banana","apple","cherry","watermelon","blackberry","pineapple"]
word=random.choice(SomeWords)       #chooses a random word from the list
ans=[]
for i in range(len(word)):
    ans.append("_")                 #creates blank spaces for the word
ansStr=''.join(ans)                 #converts the list into a string
print()
if word=="mango":
    print("Guess the word; Hint: It's the king of all fruits")
elif word=="guava":
    print("Guess the word; Hint: It's a green coloured round fruit!")
elif word=="banana":
    print("Guess the word; Hint: It's a yellow coloured fruit rich in iron")
if word=="apple":
    print("Guess the word; Hint: a fruit mostly harvested in cold regions")
elif word=="cherry":
    print("Guess the word; Hint: a small round fruit usually seen on cakes and desserts")
elif word=="watermelon":
    print("Guess the word; Hint: a huge green coloured watery fruit")
if word=="blackberry":
    print("Guess the word; Hint:a small dark purple fruit")
elif word=="pineapple":
    print("Guess the word; Hint: a huge fruit having thick peel and thorns on it")

letterGuessed=[]
chances=len(word)+2
correct=0
flag=0

print(ansStr)
print("You have",chances,"chances")
while (chances>0 and flag==0):
    guess=input("Enter a letter in lower case to guess the word:")
    if (len(guess)>1):
        print("Enter only a single letter")
        chances-=1
        continue
    elif guess in letterGuessed:
        print("You have already guessed that letter")
        chances-=1
        continue
    if guess in word:
        letterGuessed.append(guess)
        for i,c in enumerate(word):
            if c==guess:
                ans[i]=guess
        print(''.join(ans))
    else:
        chances-=1
        print(''.join(ans),"    chances left:",chances)
    if '_' not in ans:
        flag=1
        print("Woohoo! You Won.🥳🥳")
        break
if chances==0:
    print("You Lost! Try again...💔💔")
    print("The Word was",word)