# 2.12 (7% Investment Return) Some investment advisors say that it’s reasonable to expect
# a 7% return over the long term in the stock market. Assuming that you begin with
# $1000 and leave your money invested, calculate and display how much money you’ll have
# after 10, 20 and 30 years. Use the following formula for determining these amounts:
# a = p(1 + r)n
# where
# p is the original amount invested (i.e., the principal of $1000),
# r is the annual rate of return (7%),
# n is the number of years (10, 20 or 30) and
# a is the amount on deposit at the end of the nth year.
import math

principal = int(1000)
rate = 0.07
a = principal + (principal*rate)

i = 0
j = 0
k = 0

for i in range(10):
    amount = principal * (1 + rate) ** i
    print("\tYear\tAmount")
    print("\t{}\t\t{:.2f}".format(i+1, amount))

print()

for j in range(20):
    amount = principal * (1 + rate) ** j
    print("\tYear\tAmount")
    print("\t{}\t\t{:.2f}".format(j+1, amount))

print()

for k in range(30):
    amount = principal * (1 + rate) ** k
    print("\tYear\tAmount")
    print("\t{}\t\t{:.2f}".format(k+1, amount))
