# 3.13 (Factorials) Factorial calculations are common in probability. The factorial of a
# non-negative integer n is written n! (pronounced “n factorial”) and is defined as follows:
# n! = n · (n - 1) · (n - 2) · … · 1
# for values of n greater than or equal to 1, with 0! defined to be 1. So,
# 5! = 5 · 4 · 3 · 2 · 1
# which is 120. Factorials increase in size very rapidly. Write a script that inputs a non-negative
# integer and computes and displays its factorial. Try your script on the integers 10, 20,

factorial = 1
number = int(input("Enter a positive integer: "))
if number < 0:
    print("Enter a positive integer fool")
else:
    for i in range(1, number + 1):
        factorial = factorial * i
    print("The factorial of", number, "is", factorial)

# from math import factorial
# factorial(25)
# print(factorial(25))
#
