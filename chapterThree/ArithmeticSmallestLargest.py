# 3.8 (Arithmetic, Smallest and Largest) In Exercise 2.10, you wrote a script that input
# three integers, then displayed the sum, average, product, smallest and largest of those values.
# Reimplement your script with a loop that inputs four integers.

for i in range(4):
    x = int(input("Input an Integer: "))
    product = x * x * x
    average = x + x + x + x / 3
    summation = x + x + x + x
    minimum = min(x, x, x, x)
    maximum = max(x, x, x, x)

print("The product of these numbers is", product)
print("The average of these numbers is {:.2f}".format(average))
print("The sum of these numbers is", summation)
print("The least of these numbers is", minimum)
print("The largest of these numbers is", maximum)