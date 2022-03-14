# 4.14 (Computer-Assisted Instruction) Computer-assisted instruction (CAI) refers to the
# use of computers in education. Write a script to help an elementary school student learn
# multiplication.
# Create a function that randomly generates and returns a tuple of two positive one-digit integers.
# Use that function’s result in your script to prompt the user with a question, such as How much is 6 times 7?
# For a correct answer, display the message "Very good!" and ask another multiplication
# question. For an incorrect answer, display the message "No. Please try again." and let
# the student try the same question repeatedly until the student finally gets it right.

import random
operand_1 = 0
operand_2 = 0
operand_3 = 0
user_input = 1

while user_input != operand_3:
    operand_1 = random.randint(1, 100)
    operand_2 = random.randint(1, 100)
    operand_3 = operand_1 * operand_2
    user_input = input("How much is {} * {}?: ".format(operand_1, operand_2))
