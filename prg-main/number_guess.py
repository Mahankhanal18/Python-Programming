import random
number = random.randint( 0 , 9 )
count = 0
guess = 0

while guess!=number and guess!="exit":
    guess=input("Enter the number ")

    if guess=="exit":
        break
    guess=int(guess)
    count+=1

    if guess<number:
        print("Think a higher number than this one ")
    elif guess>number:
        print("Think a lower number than this one ")

    else:
        print("Yay! you got the number ")
        print("And it only took you %s tries"%count)