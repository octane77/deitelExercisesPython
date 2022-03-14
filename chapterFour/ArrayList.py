a = ["Banana", "Orange", "Mango"]
b = ["Bread", "Eggs", "Tomatoes"]
c = ["Rice", "Beans", "Yam"]

print("{}. {}\n{}. {}\n{}. {}".format(1, a[0], 2, b[0], 3, c[0]))
print("{}. {}\n{}. {}\n{}. {}".format(4, a[1], 5, b[1], 6, c[1]))
print("{}. {}\n{}. {}\n{}. {}".format(7, a[2], 8, b[2], 9, c[2]))
print()
print("{}. {}\n{}. {}\n{}. {}".format(1, a[0], 2, a[1], 3, a[2]))
print("{}. {}\n{}. {}\n{}. {}".format(4, b[0], 5, b[1], 6, b[2]))
print("{}. {}\n{}. {}\n{}. {}".format(7, c[0], 8, c[1], 9, c[2]))
print()

sn = 1
for x in a:
    print("{}. {}".format(sn, x))
    sn += 1
for y in b:
    print("{}. {}".format(sn, y))
    sn += 1
for z in c:
    print("{}. {}".format(sn, z))
    sn += 1

print()

sn = 1
items = [a, b, c]
print("S/N\tObject\tPosition")
for column in range(3):
    for row in range(3):
        print("{}.\t{}\t{}".format(sn, items[column][row], [column, row]))
        sn += 1
        # print(items[column][row], end="\n")
print()

sn = 1
print("S/N\tObject\tPosition")
for column in range(2, -1, -1):
    for row in range(2, -1, -1):
        # print("{}.\t{}\t{}".format(sn, items[column][row], [column, row]))
        print(f'{sn}. {items[column][row]:>6}\t\t{[column, row]}')
        sn += 1
