import re
#Giving the initial value 0
previousvalue = 0
#For the loop
run = True
#Defining the calculating function
def performMath():
    global run 
    global previousvalue
    equation = ""

    if previousvalue == 0:
       equation = input("Enter the equation ")

    else:
        equation = input(str(previousvalue))

    if equation == 'quit':
        print("Bye Hooman ")
        #This will terminate the loop
        run = False

    else:

        #re.sub is used to remove the letter and spaces from the equation
        equation = re.sub('[a-zA-Z,:()" "]' , '', equation)

        #(eval) is the built in function used for evaluation
        if previousvalue == 0:
            previousvalue = eval(equation)
        
        else:
            previousvalue = eval(str(previousvalue) + equation)

while run:
    performMath()