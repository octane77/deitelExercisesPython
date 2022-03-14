# 4.11 (Guess-the-Number Modification) Modify the previous exercise to count the number
# of guesses the player makes. If the number is 10 or fewer, display "Either you know the
# secret or you got lucky!" If the player makes more than 10 guesses, display "You should
# be able to do better!" Why should it take no more than 10 guesses? Well, with each “good
# guess,” the player should be able to eliminate half of the numbers, then half of the remaining
# numbers, and so on. Doing this 10 times narrows down the possibilities to a single number.
# This kind of “halving” appears in many computer science applications. For example, in the
# “Computer Science Thinking: Recursion, Searching, Sorting and Big O” chapter, we’ll present
# the high-speed binary search and merge sort algorithms, and you’ll attempt the quicksort
# exercise—each of these cleverly uses halving to achieve high performance.

import random

user_input = 0
lucky_number = 1
counter = 0
while user_input != lucky_number:
    user_input = int(input("Guess my number between 1 and 1000 with the fewest guesses: "))
    lucky_number = random.randint(1, 1000)
    if user_input > lucky_number:
        print("Too high. Try again")
    elif user_input < lucky_number:
        print("Too low. Try again")
    counter += 1

else:
    print("Congratulations. You guessed the number! and it took you {} try(ies).".format(counter))

if counter < 10:
    print("Either you know the secret or you got lucky!")

if counter > 10:
    print("You should be able to do better!")
