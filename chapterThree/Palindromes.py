# 3.12 (Palindromes) A palindrome is a number, word or text phrase that reads the same
# backwards or forwards. For example, each of the following five-digit integers is a palindrome:
# 12321, 55555, 45554 and 11611. Write a script that reads in a five-digit integer
# and determines whether it’s a palindrome. [Hint: Use the // and % operators to separate
# the number into its digits.]

palindrome = False
while palindrome == False:
    integer = int(input("Enter a five digit integer: "))
    int1 = integer // 10_000
    int2 = integer % 10_000 // 1000
    int3 = integer % 10_000 % 1000 // 100
    int4 = integer % 10_000 % 1000 % 100 // 10
    int5 = integer % 10_000 % 1000 % 100 % 10

    if int1 == int5 and int2 == int4:
        print("{} is a palindrome".format(integer))
        palindrome = True
    else:
        print("{} isn't a palindrome".format(integer))
