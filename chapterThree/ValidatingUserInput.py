# 3.1 (Validating User Input) Modify the script of Fig. 3.3 to validate its inputs. For any input, if the value
# entered is other than 1 or 2, keep looping until the user enters a correct value. Use one counter to keep track of
# the number of passes, then calculate the number of failures after all the user’s inputs have been received.

user_input = int(input("Enter a number: "))
counter = 0
while user_input != int(1) and user_input != int(2):
    print("Try again")
    counter += 1
    user_input = int(input("Enter a number: "))
if counter == 0:
    print("You got it right off the bat")
else:
    print("Took you {} tries but you finally got it".format(counter))
