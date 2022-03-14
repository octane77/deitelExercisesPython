# 2.15 (Sort in Ascending Order) Write a script that inputs three different floating-point
# numbers from the user. Display the numbers in increasing order. Recall that an if statement’s
# suite can contain more than one statement. Prove that your script works by running
# it on all six possible orderings of the numbers. Does your script work with duplicate
# numbers? [This is challenging. In later chapters you’ll do this more conveniently and with
# many more numbers.]

firstNumber = float(input("Enter an Integer: "))
secondNumber = float(input("Enter an Integer: "))
thirdNumber = float(input("Enter an Integer: "))

smallest = firstNumber
largest = firstNumber

if secondNumber < smallest:
    smallest = secondNumber

if secondNumber > largest:
    largest = secondNumber

if thirdNumber < smallest:
    smallest = thirdNumber

if thirdNumber > largest:
    largest = thirdNumber

print("Numbers input: {:.2f}, {:.2f}, {:.2f}".format(firstNumber, secondNumber, thirdNumber))
print("Smallest number is: {:.2f}".format(smallest))
print("Largest number is: {:.2f}".format(largest))
