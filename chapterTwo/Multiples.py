# 2.7 (Multiples) Use if statements to determine whether 1024 is a multiple of 4 and
# whether 2 is a multiple of 10. (Hint: Use the remainder operator.)

var = int(1024)
if var % 4 == 0:
    print("{} is a multiple of 4".format(var))
var = int(10)
if var % 2 == 0:
    print("{} is a multiple of 2".format(var))
