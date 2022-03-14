# 3.4 (Fill in the Missing Code) In the code below
# for ***:
# for ***:
# print('@')
# print()
# replace the *** so that when you execute the code, it displays two rows, each containing
# seven @ symbols, as in:
# @@@@@@@
# @@@@@@@

rows = int(2)
columns = int(7)
symbol = "@"

for i in range(rows):
    for j in range(columns):
        print(symbol, end="")
    print()
