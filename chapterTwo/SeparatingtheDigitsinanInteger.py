# 2.11 (Separating the Digits in an Integer) Write a script that inputs a five-digit integer
# from the user. Separate the number into its individual digits. Print them separated by three
# spaces each. For example, if the user types in the number 42339, the script should print
# 4 2 3 3 9
# Assume that the user enters the correct number of digits. Use both the floor division and
# remainder operations to “pick off ” each digit.

integer = int(input("Enter a five digit integer: "))
int1 = integer//10_000
int2 = integer % 10_000//1000
int3 = integer % 10_000 % 1000//100
int4 = integer % 10_000 % 1000 % 100//10
int5 = integer % 10_000 % 1000 % 100 % 10
print("{} {} {} {} {}".format(int1, int2, int3, int4, int5))
