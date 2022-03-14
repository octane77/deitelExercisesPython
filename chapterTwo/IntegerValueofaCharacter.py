# 2.9 (Integer Value of a Character) Here’s a peek ahead. In this chapter, you learned
# about strings. Each of a string’s characters has an integer representation. The set of characters
# a computer uses together with the characters’ integer representations is called that
# computer’s character set. You can indicate a character value in a program by enclosing that
# character in quotes, as in 'A'. To determine a character’s integer value, call the built-in
# function ord:
# In [1]: ord('A')
# Out[1]: 65
# Display the integer equivalents of B C D b c d 0 1 2 $ * + and the space character.

print("The character B has the value", ord("B"))
print("The character C has the value", ord("C"))
print("The character D has the value", ord("D"))
print("The character b has the value", ord("b"))
print("The character c has the value", ord("c"))
print("The character d has the value", ord("d"))
print("The character 0 has the value", ord("0"))
print("The character 1 has the value", ord("1"))
print("The character 2 has the value", ord("2"))
print("The character $ has the value", ord("$"))
print("The character * has the value", ord("*"))
print("The character + has the value", ord("+"))
print("The character  has the value", ord(" "))
