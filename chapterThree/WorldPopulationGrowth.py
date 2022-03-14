# 3.27 (World Population Growth) World population has grown considerably over the centuries. Continued growth could
# eventually challenge the limits of breathable air, drinkable water, arable land and other limited resources.
# There’s evidence that growth has been slowing in recent years and that world population could peak some time this
# century, then start to decline. For this exercise, research world population growth issues. This is a controversial
# topic, so be sure to investigate various viewpoints. Get estimates for the current world population and its growth
# rate. Write a script that calculates world population growth each year for the next 100 years, using the
# simplifying assumption that the current growth rate will stay constant. Print the results in a table. The first
# column should display the year from 1 to 100. The second column should display the anticipated world population at
# the end of that year. The third column should display the numerical increase in the world population that would
# occur that year. Using your results, determine the years in which the population would be double and eventually
# quadruple what it is today.

worldPopulation = int(input("Whats the current world population?: "))
worldPopulationGrowthRate = float(input("Whats the current world population growth rate?: "))
worldPopulationGrowthRate = worldPopulationGrowthRate/100
for year in range(0, 100):
    currentWorldPopulation = int(worldPopulation + (worldPopulation * worldPopulationGrowthRate) * year)
    print("\tYear\tWorld Population")
    print("\t{}\t\t{:.2f}".format(year+1, currentWorldPopulation))
