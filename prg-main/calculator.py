# Make a calculator
while True:
    # To choose the operation
    print(">>>>>>>>>>>>>......CALCULATOR.......<<<<<<<<<<<<<<<")
    print("Enter 1 for Addition ")
    print("Enter 2 for Subtradtion")
    print("Enter 3 for Multiplication ")
    print("Enter 4 for Divisin ")
    # To select the operation

    select = int(input("Enter from 1 to 4 \n"))
    # To enter the number
    num1 = int(input("Enter the first number "))
    num2 = int(input("Enter the second number "))
    if select == 1:
        print("The sum of two numbers is " , num1+num2)
    elif select == 2:
        print("The difference of two numbers is " + str(num1-num2))
    elif select == 3:
        print("The multiplication of two numbers is " + str(num1*num2))
    elif select == 4:
        print("The division of two numbers is " + str(num1/num2))

    res = input("Continue Y/N : ")
    if res == 'n' or res == 'N':
        break
