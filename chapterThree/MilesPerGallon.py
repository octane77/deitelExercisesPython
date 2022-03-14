# 3.11 (Miles Per Gallon) Drivers are concerned with the mileage obtained by their automobiles.
# One driver has kept track of several tankfuls of gasoline by recording miles driven
# and gallons used for each tankful. Develop a sentinel-controlled-repetition script that
# prompts the user to input the miles driven and gallons used for each tankful. The script
# should calculate and display the miles per gallon obtained for each tankful. After processing
# all input information, the script should calculate and display the combined miles per
# gallon obtained for all tankfuls (that is, total miles driven divided by total gallons used).

totalNumberOfMiles = int(0)
totalNumberOfGallons = int(0)

milesDriven = float(input("How many miles did you drive? (-1 to end): "))
while milesDriven != int(-1):
    gallonsUsed = float(input("Enter the gallons used (-1 to end): "))

    totalNumberOfMiles += milesDriven
    totalNumberOfGallons += gallonsUsed

    if gallonsUsed != 0:
        numberOfMilesPerGallon = float(milesDriven // gallonsUsed)
        print("Miles per gallon per tank: {:.2f}".format(numberOfMilesPerGallon))

    if totalNumberOfGallons != 0:
        combinedNumberOfMilesPerGallon = float(totalNumberOfMiles // totalNumberOfGallons)
        print("Total MPG: {:.2f}".format(combinedNumberOfMilesPerGallon))

    milesDriven = float(input("How many miles did you drive? (-1 to end): "))
