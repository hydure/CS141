# Colin Fox Lightfoot
# CFLightfoot@email.wm.edu
# (540)-538-2538
#
# 

def createDictionaryWithinDictionaryAndThreeListsForDataFile(inputedName):
    """Creates a list of data from an imported file."""
    
    # Creates an object out of the .csv stock file inputed by user.
    dataFile = open(inputedName, "r")
    dataDict = {}
    stockDict = {}
    increment = 0
    volumeList = []
    highList = []
    lowList = []
    tup = ()
    
    
    # Writes each line of the datafile onto a list that splits the data into a
    # dictionary within a dictionary, using a tuple that includes the year-month
    # as the key with an inner dictionary that includes each day as its keys and
    # the day's data as its values. Also creates three lists in the process.
    for line in dataFile:
        if line[0:7] == "Date" or "Close" in line:
            continue
        lineList = line.strip().split(',')
        date = lineList[0]
        lineList[0] = lineList[0].split("-")
        year = int(lineList[0][0])
        month = int(lineList[0][1])
        day = int(lineList[0][2])
        openValue = "{:.2f}".format(float(lineList[1]))
        highValue = "{:.2f}".format(float(lineList[2]))
        lowValue = "{:.2f}".format(float(lineList[3]))        
        closeValue = "{:.2f}".format(float(lineList[4]))
        volume = int(float(lineList[5]))
        adjCloseValue = "{:.2f}".format(float(lineList[6]))
        stockValues = [openValue, highValue, lowValue, closeValue, volume, \
                       adjCloseValue]
        
        if increment != 0:
            if month != tup[1]:
                dataDict[tup] = (stockDict)
                stockDict = {}
                tup = year, month
 
        stockDict[day] = stockValues
        tup = year, month
        
        tupl = int(volume), date
        volumeList.append(tupl)
        tupl = float(highValue), date
        highList.append(tupl)
        tupl = float(lowValue), date
        lowList.append(tupl)
        increment += 1
        
    dataFile.close()

    data = {'dataDict':dataDict, 'volumeList':volumeList, \
                    'highList':highList, 'lowList':lowList}    
    
    return data


###############################################################################
def getInfoAboutAParticularDay(dataDict, listOfMonths):
    
        
    year = int(input("Please enter the year you are interest in: "))
    print(year)
    actualYear = str(year)
    month = int(input("Please enter the month you are interested in: "))
    print(month)
    day = int(input("Please enter the day you are interested in: "))
    actualDay = str(day)
    print(day)
    
    try:
        for key, value in dataDict[year, month].items():
            if key == day or key == dataDict[year, month][day]:
                print(listOfMonths[month-1]+ " " + actualDay + ", " + \
                      actualYear)
                print("  {:10}{:10}{:10}{:9}{:13}{:10}".format("Open", "High", \
                "Low", "Close", "Volume", "Adj. Close"))
                print("  {:10}{:10}{:10}{:9}{:7,}{:>10}".format(value[0], \
                    value[1], value[2], value[3], value[4], value[5]))
                
    except KeyError:
        print("\nNo trading occurred on this day.")


###############################################################################
def getAveragePriceOfAParticularMonth(dataDict, listOfMonths):

    year = int(input("Please enter the year you are interest in: "))
    print(year)
    month = int(input("Please enter the month you are interested in: "))
    print(month)    
    
    totalSum = 0
    totalVolume = 0
    
    actualMonth = listOfMonths[month - 1]
    actualYear = str(year)
    
    try:
        for value in dataDict[year, month].values():
            totalSum += float(value[3]) * float(value[4])
            totalVolume += float(value[4])
        averagePrice = totalSum / totalVolume
        prettyPrice = "{:.2f}".format(averagePrice)
    
        print("\nThe average price for " + actualMonth + " " + actualYear + \
              " is " + prettyPrice + ".")
    
    except KeyError:
        print("\nNot a legal date")

    
###############################################################################
def printHighLowInformation(listOfMonths, volumeList, highList, \
                            lowList):
    
    volumeList.sort(reverse = True)
    maxVolume = volumeList[0][0]
    dateOccurs = volumeList[0][1].split("-")
    year = dateOccurs[0]
    month = listOfMonths[int(dateOccurs[1])-1]
    if int(dateOccurs[2]) < 10 :
            day = dateOccurs[2].replace("0", "")    
    day =  dateOccurs[2]
    print("The day with the highest trading volume was on " + month + " " + \
          day + ", " + year + " which was " "{:,}".format(maxVolume) + \
          " shares.")

    volumeList.sort()
    minVolume = volumeList[0][0]
    dateOccurs = volumeList[0][1].split("-")
    year = dateOccurs[0]
    month = listOfMonths[int(dateOccurs[1])-1]
    if int(dateOccurs[2]) < 10 :
            day = dateOccurs[2].replace("0", "")    
    day =  dateOccurs[2]
    print("The day with the lowest trading volume was on " + month + " " + \
              day + ", " + year + " which was " "{:,}".format(minVolume) + \
              " shares.")    

    highList.sort(reverse = True)
    maxValue = "{:.2f}".format(highList[0][0])
    dateOccurs = highList[0][1].split("-")
    year = dateOccurs[0]
    month = listOfMonths[int(dateOccurs[1])-1]
    if int(dateOccurs[2]) < 10 :
        day = dateOccurs[2].replace("0", "")
    print("The day with the highest value was on " + month + " " + day + ", " +\
          year + " which was " + maxValue + ".")
    
    lowList.sort()
    minValue = "{:.2f}".format(lowList[0][0])
    dateOccurs = lowList[0][1].split("-")
    year = dateOccurs[0]
    month = listOfMonths[int(dateOccurs[1])-1]
    if int(dateOccurs[2]) < 10 :
            day = dateOccurs[2].replace("0", "")    
    day = dateOccurs[2]
    print("The day with the lowest value was on " + month + " " + day + ", " +\
          year + " which was " + minValue + ".")    
    

###############################################################################
listOfMonths = ['January', 'February', 'March', 'April', 'May', 'June', 'July',\
                'August', 'September', 'October', 'November', 'December']

choice = ''

#Asks for the name of the file so it can be callable in above functions.
inputedName = input("Enter the name of the stock file: ")
print(inputedName)

data = createDictionaryWithinDictionaryAndThreeListsForDataFile(inputedName)

while choice != 'q':
    print("\na) Get information about a particular day of trading")
    print("b) Find average information about a particular month")
    print("c) Print high/low information")
    print("q) Quit\n")
    
    response = input("Enter choice: ")
    print(response + "\n")
    choice = response.lower()
    
    if choice == 'a':
        getInfoAboutAParticularDay(data['dataDict'], listOfMonths)
    elif choice == 'b':
        getAveragePriceOfAParticularMonth(data['dataDict'], listOfMonths)
    elif choice == 'c':
        printHighLowInformation(listOfMonths, data['volumeList'],\
                                data['highList'], data['lowList'])
    elif choice == 'q':
        print("Thanks for using my program")
    # If the user inputs any other input.    
    else:
        print("You've entered an incorrect choice. Try again")    