import random
number=random.randint(1,9)
guess=0
count=0

while guess!=number and guess!="exit":
    guess=input("Whats the guess ")

    if guess=="exit":
        break
    guess=int(guess)
    count += 1
    
    if guess<number:
        print("Too LOW")
    elif guess>number:
        print("Too HIgh")
    else:
        print("Yeah thats the number")
        print("And it only took you %d time "%count)