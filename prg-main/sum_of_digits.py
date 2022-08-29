num=int(input("Enter any 3 or more digit number "))
sum=0
for digit in str(num):
    sum+=int(digit)
#print should not be indented
print(sum)