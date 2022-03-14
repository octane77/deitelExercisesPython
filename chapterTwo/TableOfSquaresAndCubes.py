# 2.8 (Table of Squares and Cubes) Write a script that calculates the squares and cubes
# of the numbers from 0 to 5. Print the resulting values in table format, as shown below. Use
# the tab escape sequence to achieve the three-column output.
# number square cube
# 0 0 0
# 1 1 1
# 2 4 8
# 3 9 27
# 4 16 64
# 5 25 125
# print('f{i: >2}{}')

x = int(0)
print("\tNumber\tSquare\tCube\t")
print("\t{}\t \t{}\t \t{}\t ".format(x, (x * x), (x * x * x)))
x = int(1)
print("\t{}\t \t{}\t \t{}\t ".format(x, (x * x), (x * x * x)))
x = int(2)
print("\t{}\t \t{}\t \t{}\t ".format(x, (x * x), (x * x * x)))
x = int(3)
print("\t{}\t \t{}\t \t{}\t ".format(x, (x * x), (x * x * x)))
x = int(4)
print("\t{}\t \t{}\t \t{}\t ".format(x, (x * x), (x * x * x)))
x = int(5)
print("\t{}\t \t{}\t \t{}\t ".format(x, (x * x), (x * x * x)))
print()
x = 0
print("Number\tSquare\tCube ")
for var in range(6):
    print(f'{var: > 6} {var ** 2: > 7} {var ** 3: > 5}')
