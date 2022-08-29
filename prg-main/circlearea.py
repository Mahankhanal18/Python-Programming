#Write a Python program which accepts the radius of a circle from the user and compute the area
radius=float(input("Enter the radius of the circle : "))
area=3.14*radius**2
print("The area of circle with radius " + str(radius) +" is %.2f" %area)