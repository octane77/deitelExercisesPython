# 2.5 (Circle Area, Diameter and Circumference) For a circle of radius 2, display the diameter,
# circumference and area. Use the value 3.14159 for π. Use the following formulas
# (r is the radius): diameter = 2r, circumference = 2πr and area = πr2. [In a later chapter, we’ll
# introduce Python’s math module which contains a higher-precision representation of π.]

pi = 3.14159
radius = float(input("Enter the radius of this circle: "))
circumference = 2 * pi * radius
area = pi * radius ** 2
print("The area of this circle is {:.2f}".format(area))
print("The circumference of this circle is {:.2f}".format(circumference))
