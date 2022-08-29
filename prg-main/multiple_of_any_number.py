multiple_number=int(input("Whose multiple "))
multiple_upto=int(input("upto where "))
for multiple_upto in range(1,multiple_upto+1):
    multiple=multiple_number*multiple_upto
    print(str(multiple_number) + " * " + str(multiple_upto) + " = " + str(multiple))