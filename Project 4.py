# Colin Fox Lightfoot
# CFLightfoot@email.wm.edu
# (540)-538-2538
#
# This program asks for the name of a datafile in order to find out its six 
# best months, its six worst months, the day where the datafile's stock reached
# its highest value, the day where the datafile's stock reached its lowest
# value, the day where the stock had its highest volume and the total value
# of all those shares, and the day where the stock had its lowest volume and
# the total value of all those shares.


def createListForDataFile(inputedName):
    """Creates a list of data from an imported file."""
    
    # Creates an object out of the .csv stock file inputed by user.
    dataFile = open(inputedName, "r")
    dataList = []
    
    # Writes each line of the datafile onto a list that is then written onto 
    # another list, so it can be manipulated later.
    for line in dataFile:
        if line[0:7] == "Date" or "Close" in line:
            continue
        lineList = line.strip().split(',')
        stockList = [lineList[0], float(lineList[4]), int(lineList[5]), \
                                      float(lineList[2]), float(lineList[3])]
        dataList.append(stockList)
    
    dataFile.close()
    
    return dataList
        
        
###############################################################################
def getMonthlyAverages(dataList):
    """Gets the monthly average of each stock and puts that, plus dates \
    into a new list of data."""
    
    refinedStockList = []
    
    # Splits up the portions of each date in the data so it can be manipulated.
    for stockList in dataList:
        stockList[0] = stockList[0].split("-")
        stockList[0][0] = int(stockList[0][0])
        stockList[0][1] = int(stockList[0][1])
        stockList[0][2] = int(stockList[0][2])
        refinedStockList += stockList

    # Declaring variables for the next step.
    totalSum = 0
    dailyNumber = 0
    totalVolume = 0
    monthlyAveragePrice = 0
    increment = 0
    monthlyAverages = []
    
    # Goes through each line of data and adds up the daily prices and volumes
    # for each month of each of the years to determine the monthly averages
    # in regards to stock price.
    for line in dataList:
        month = dataList[increment-1][0][1]
        year = dataList[increment-1][0][0]        
        
        dailyNumber = line[1] * line[2]
        totalSum += dailyNumber
        totalVolume += line[2]
        
        # If the month on the current line does not match the month on the
        # previous line, then the monthly average is computed for the previous
        # line and every other line with the previous line's month and year, 
        # and the process is repeated starting with the current line.
        if increment != 0:
            if line[0][1] != dataList[increment-1][0][1]:
                totalSum -= dailyNumber
                totalVolume -= line[2]
                averagePrice = totalSum/totalVolume
                monthlyAverages += [[averagePrice, (month, year)]]
                dailyNumber = line[1] * line[2]
                totalVolume = line[2]
                totalSum = dailyNumber        
        increment += 1
    
    averagePrice = totalSum/totalVolume
    monthlyAverages += [[averagePrice, (month, year)]]    
    
        
    return monthlyAverages


###############################################################################
def printInfo(monthlyAverages, name):
    """Prints a list of the six worst and best monthly averages plus dates."""
    
    # Sorts the monthly average stock prices from high to low and then takes\
    # the first six averages.
    monthlyAverages.sort(reverse = True)
    sixBestAverages = monthlyAverages[0:6]
    print("The six best months for", name, "stock are:")
    
    rep = 0
    
    # Changes the dates into a yyyy-mm format and prints them along with each
    # of the six months' particular average stock price.
    while rep < 6:
        year = str(monthlyAverages[rep][1][1])
        month = str(monthlyAverages[rep][1][0])
        if len(month) < 2:
            month = "0" + month
        print(year + '-' + month + '   {:0.3f}'.format(monthlyAverages[rep][0]))
        rep += 1
    
    print()
    
    # Sorts the monthly average stock prices from low to high and then takes\
    # the first six averages.
    monthlyAverages.sort()
    sixWorstAverages = monthlyAverages[0:6]
    print("The six worst months for", name, "stock are:")
    
    rep = 0
    
    # Changes the dates into a yyyy-mm format and prints them along with each
    # of the six months' particular average stock price.
    while rep < 6:
        year = str(monthlyAverages[rep][1][1])
        month = str(monthlyAverages[rep][1][0])
        if len(month) < 2:
            month = "0" + month
        print(year + '-' + month + \
              '    {:0.3f}'.format(monthlyAverages[rep][0]))
        rep += 1    
    
    print()

###############################################################################
def getHighestStockInfo(dataList):
    """Finds and prints the date and price of when the stock was the highest \
    in terms of value."""
    
    # Finds the day with the highest stock price and converts the date into
    # strings that can be manipulated.
    for line in dataList:
        line[0], line[3] = line[3], line[0] 
    
    bestDay = max(dataList)    
    highestValue = str("{:.2f}".format(bestDay[0]))
    day = str(bestDay[3][2])
    month = str(bestDay[3][1])
    year = str(bestDay[3][0])
    
    # Adds zeros to days and months less than 10 to make the print pretty.
    if len(day) < 2:
            day = "0" + day
    if len(month) < 2:
        month = "0" + month  
        
    # Prints the date of the highest stock price and its value.
    date = year + "-" + month + "-" + day
    print("The day where the stock reached its highest point is", date, \
          "with a value of", highestValue+'.')


###############################################################################
def getLowestStockInfo(dataList):        
    """Finds and prints the date and price of when the stock was the lowest\
    in terms of value."""
    
    # Finds the day with the lowest stock price and converts the date into
    # strings that can be manipulated.    
    for line in dataList:
        line[0], line[4] = line[4], line[0]    
    
    worstDay = min(dataList)    
    lowestValue = str(worstDay[0])
    day = str(worstDay[3][2])
    month = str(worstDay[3][1])
    year = str(worstDay[3][0])
    
    
    # Adds zeros to days and months less than 10 to make the print pretty.
    if len(day) < 2:
        day = "0" + day
    if len(month) < 2:
        month = "0" + month
    
    # Prints the date of the lowest stock price and its value.
    date = year + "-" + month + "-" + day
    print("The day where the stock reached its lowest point is", date, \
              "with a value of", lowestValue+".")    

    
###############################################################################
def getHighestVolume(dataList):
    """Finds and prints the date of when the stock had the highest volume \
    and the stocks cumulative value."""
    
    # Finds the day with the highest stock volume and converts the date into
    # strings that can be manipulated.    
    for line in dataList:
            line[0], line[2] = line[2], line[0]
    
    highestVolumeDay = max(dataList)
    highestVolume = int(highestVolumeDay[0])
    day = str(highestVolumeDay[3][2])
    month = str(highestVolumeDay[3][1])
    year = str(highestVolumeDay[3][0])    
    
    # Adds zeros to days and months less than 10 to make the print pretty.
    if len(day) < 2:
        day = "0" + day
    if len(month) < 2:
        month = "0" + month
        
    # Prints the date of the highest stock volume and its volume.    
    date = year + "-" + month + "-" + day    
    print("The day with the highest volume is", date, \
                  "with a volume of", "{:,}".format(highestVolume), "shares.")    
            
            
###############################################################################
def getLowestVolume(dataList):
    """Finds and prints the date of when the stock had the lowest volume \
        and the stocks cumulative value."""        
    
    # Finds the day with the lowest stock volume and converts the date into
    # strings that can be manipulated.     
    lowestVolumeDay = min(dataList)
    lowestVolume = int(lowestVolumeDay[0])
    day = str(lowestVolumeDay[3][2])
    month = str(lowestVolumeDay[3][1])
    year = str(lowestVolumeDay[3][0])    
        
    # Adds zeros to days and months less than 10 to make the print pretty.    
    if len(day) < 2:
        day = "0" + day
    if len(month) < 2:
        month = "0" + month
            
    # Prints the date of the lowest stock volume and its volume.  
    date = year + "-" + month + "-" + day    
    print("The day with the lowest volume is", date, \
                    "with a volume of", "{:,}".format(lowestVolume), "shares.")    
                
                
###############################################################################    
#Asks for the name of the file so it can be callable in above functions.
inputedName = input("Enter the name of the data file: ")
print(inputedName+"\n")
name = inputedName.replace(".csv", "'s")

#Runs each of the above procedures and functions.
dataList = createListForDataFile(inputedName)
monthlyAverages = getMonthlyAverages(dataList)
printInfo(monthlyAverages, name)
getHighestStockInfo(dataList)
getLowestStockInfo(dataList)
getHighestVolume(dataList)
getLowestVolume(dataList)