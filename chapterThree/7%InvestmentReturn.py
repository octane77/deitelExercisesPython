principal = int(1000)
rate = 0.07

for i in range(30):
    amount = principal * (1 + rate) ** i
    print("\tYear\tAmount")
    print("\t{}\t\t{:.2f}".format(i+1, amount))
