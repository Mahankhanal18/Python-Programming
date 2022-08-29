num = int(input("Enter the number of operation "))
total_sum = 0
for n in range(num):
    numbers = int(input("Enter your numbers "))
    total_sum = total_sum + numbers
print("Total sun ", total_sum)
average = total_sum/num
print("The average is %.2f" % average)
