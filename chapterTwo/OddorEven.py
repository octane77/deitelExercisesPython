# 2.6 (Odd or Even) Use if statements to determine whether an integer is odd or even.
# [Hint: Use the remainder operator. An even number is a multiple of 2.
# Any multiple of 2 leaves a remainder of 0 when divided by 2.]

integer = int(input("Enter an integer: "))
if integer % 2 == 0:
    print("{} is an even number".format(integer))
else:
    print("{} is not an even number".format(integer))
