# 5.5 (IPython Session: Slicing) Create a string called alphabet containing 'abcdefghijklmnopqrstuvwxyz',
# then perform the following separate slice operations to obtain:
# a) The first half of the string using starting and ending indices.
# b) The first half of the string using only the ending index.
# c) The second half of the string using starting and ending indices.
# d) The second half of the string using only the starting index.
# e) Every second letter in the string starting with 'a'.
# f) The entire string in reverse.
# g) Every third letter of the string in reverse starting with 'z'.

alphabet = 'abcdefghijklmnopqrstuvwxyz'

# string[start:end:step]

print("The first half of the string using starting and ending indices.")
print(alphabet[0:13:])

print("The first half of the string using only the ending index")
print(alphabet[:13:])

print("The second half of the string using starting and ending indices.")
print(alphabet[13:26:])

print("The second half of the string using only the starting index")
print(alphabet[13::])

print("Every second letter in the string starting with 'a'.")
print(alphabet[::2])

print("The entire string in reverse")
print(alphabet[::-1])

print("Every third letter of the string in reverse starting with 'z'.")
print(alphabet[::-3])