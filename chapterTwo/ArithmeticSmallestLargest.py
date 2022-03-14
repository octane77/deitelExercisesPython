# 2.10 (Arithmetic, Smallest and Largest) Write a script that inputs three integers from
# the user. Display the sum, average, product, smallest and largest of the numbers. Note that
# each of these is a reduction in functional-style programming.

x = int(input("Input an Integer: "))
y = int(input("Input an Integer: "))
z = int(input("Input an Integer: "))

product = x * y * z
average = x + y + z / 3
summation = x + y + z
minimum = min(x, y, z)
maximum = max(x, y, z)

print("The product of these numbers is ", product)
print("The average of these numbers is ", average)
print("The sum of these numbers is ", summation)
print("The least of these numbers is", minimum)
print("The largest of these numbers is", maximum)
