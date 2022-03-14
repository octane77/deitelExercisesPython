# 2.13 (How Big Can Python Integers Be?) We’ll answer this question later in the book.
# For now, use the exponentiation operator ** with large and very large exponents to produce
# some huge integers and assign those to the variable number to see if Python accepts
# them. Did you find any integer value that Python won’t accept?

n = 420
o = 6969
counter = 0

while counter <= 10:
    print(n ** o)
    counter += 1
    print()
