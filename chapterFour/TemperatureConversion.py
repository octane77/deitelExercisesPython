# 4.9 (Temperature Conversion) Implement a fahrenheit function that returns the
# Fahrenheit equivalent of a Celsius temperature. Use the following formula:
# F = (9 / 5) * C + 32
# Use this function to print a chart showing the Fahrenheit equivalents of all Celsius temperatures
# in the range 0–100 degrees. Use one digit of precision for the results. Print the
# outputs in a neat tabular format.

def fahrenheit():
    print("Celsius Fahrenheit")
    for var in range(0, 101):
        conversion = (var * 9 / 5) + 32

        print("{} \t\t{:.1f}".format(var, conversion))
        # print(f'{var: > 6} {var ** 2: > 7} {var ** 3: > 5}')


fahrenheit()
