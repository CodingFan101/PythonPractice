import math
radius = int(input("What is the radius of the cylinder in meters? "))
height = int(input("What is the height of the cylinder in meters? "))
volume = math.pi * (radius**2) * height
print("The volume of the cylinder in meters is: " + str(volume))