# This program prompts a user to input the radius, height, and width, in that
# order, for a rectangular doughnut. The program will then calculate the
# surface area and volume of the doughnut. The program will next write to the
# screen the radius, height and width entered, as well as the surface area and
# volume of the doughnut.

import math

# This section asks the user to enter the radius, height, and width, in that
# order for a doughnut.
radius = float(input("Please enter the doughnut's radius ==> "))
print(radius)
height = float(input("Please enter the doughnut's height ==> "))
print(height)
width = float(input("Please enter the doughnut's width ==> "))
print(width)

# This section calculates the surface area and volume of the doughnut.
volume = math.pi * (2 * radius + width) * width * height
surface_area = 2 * math.pi * (height + width) * (2 * radius + width)

# This section writes to the screem the radius, height and width entered, as 
# well as the surface area and volume of the doughnut.
print("-"*40)
print()
print("   The doughnut's radius ={:>9.3f}".format(radius))
print("   The doughnut's height ={:>9.3f}".format(height))
print("   The doughnut's width  ={:>9.3f}".format(width))
print("   The doughnut's volume = {:>9.3f}".format(volume))
print("   Its surface area      = {:>9.3f}".format(surface_area))
print()
print("-"*40)