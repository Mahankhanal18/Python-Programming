import random
while True:
    number=random.randint(100000,999999)
    print(int(number))
    otp=int(input("Enter the OTP that is sent to your mobile "))
    if otp==number:
        print("You are Welcome ")
        break
    else:
        print("Sorry the OTP is Wrong")
        
    res = input("Continue Y/N : ")
    if res == 'n' or res == 'N':
        break
