import random
def hangman():
 
    words=random.choice(["apple", "banana", "hero", "dictionary", "studio", "code", "python", "untitled",
    "human", "being", "clandestino", "despacito", "mosquito"])
    validletters='abcdefghijklmnopqrstuvwxyz'
    turns = 10
    guessmade = ''
    
    while len(words) > 0:
        main = ""
        missed = 0
        
        for letter in words:
            if letter in guessmade:
                main=main+letter
            else:
                main=main+ "_" + " "
        if main == words:
            print(main)
            print("You Win! Hurrah!")
            break
        print("Guess the word",main)
        guess=input()


        if guess in validletters:
            guessmade = guessmade + guess
        else:
            print("Enter the valid character ")
            guess=input()
        if guess not in words:
            turns = turns - 1
           

            if turns==9:
                print("9 turns left")
                print(" --------- ")

            if turns==8:
                print("8 turns left")
                print(" --------- ")
                print("     O     ")

            if turns==7:
                print("7 turns left")
                print(" --------- ")
                print("     O     ")
                print("     |     ")

            if turns==6:
                print("6 turns left")
                print(" --------- ")
                print("     O     ")
                print("     |     ")
                print("    /      ")

            if turns==5:
                print("5 turns left")
                print(" --------- ")
                print("     O     ")
                print("     |     ")
                print("    / \    ")

            if turns==4:
                print("4 turns left")
                print(" --------- ")
                print("   \ O     ")
                print("     |     ")
                print("    / \    ")

            if turns==3:
                print("3 turns left")
                print(" --------- ")
                print("   \ O /   ")
                print("     |     ")
                print("    / \    ")

            if turns==2:
                print("2 turns left")
                print(" --------- ")
                print("   \ O /__ ")
                print("     |     ")
                print("    / \    ")

            if turns==1:
                print("1 turn left")
                print("Its your only chance")
                print(" --------- ")
                print("   \ O /__|")
                print("     |     ")
                print("    / \    ")

            if turns==0:
                print("You couldn't make it ")

                res = input("Continue Y/N : ")
                if res == 'n' or res == 'N':
                   break
          
           

name=input("Enter your name: ")
print("Welcome", name)
print("......................;;,.........................")
print("Try your best to win less than 10 tries")
hangman()
print()