run = True 
def reverse():
    global run
    string=input("Enter the string ")
    reverse=string[::-1]
    print("The reverse of your string is %s"%reverse)
    if string == 'quit':
        run = False
    elif (reverse==string):
        print('It is palindrome')
    else:
        print("It is not palindrome")
    
    print("\n\n\n")
while run:
    reverse()

    
