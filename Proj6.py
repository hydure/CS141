# Proj6.py
# Colin Fox Lightfoot
# CFLightfoot@email.wm.edu
# (540)-538-2538
#
# Creates a dictionary with each player and his associated values. Then prints
# an alphabetical list, by last name, then first if necessary, of each player
# and his associated rusher rating. Then allows the user to continually look up
# a player's overall rusher rating or individual years and each year's rusher
# rating, if the player is in the dictionary. 

from Player import Player

def createPlayerDictionary(fileName):
    """Creates a dictionary entry for each player in a data file, adding each
    of their season's associated values to the dictionary."""
    
    players = {}    
    
    # Opens the data file and skips the first line.
    dataFile = open(fileName, "r")
    dataFile.readline()
    
    # Iterates through every line in the data file and adds a player and his
    # information, or adds information to a player already in the dictionary.
    for line in dataFile:
        lineList = line.strip().split(',')
        name = "{} {}".format(lineList[0], lineList[1])
        player = Player(lineList[0], lineList[1])
        if name not in players:
            players[name] = player
        players[name].update(lineList[13], lineList[3], lineList[2], \
                        lineList[5], lineList[6], lineList[7], lineList[10])
    
    dataFile.close()
    
    return players
    
###############################################################################
def printAlphaPlayerList(players):
    """Prints a dictionary of players alphabetically and their overal rusher
    ratings."""
    
    playerList = []
    
    # Adds the player and his overall rusher rating to a list.
    for val in players.values():
        playerList.append(val)
    
    #Sorts the list alphabetically by last name and then first name if 
    # necessary.
    playerList.sort()
    
    # Prints each player's name and rusher rating from the list.
    for player in playerList:
        print(player)


###############################################################################
def lookUpIndividualPlayerInformation(players):
    """Looks up individual player information about a specific player."""
    
    #Prompts the user if they want a particualr player's information.
    response = input("\n\nDo you want information about a particular player? ")
    print(response)
    answer = response.lower()
    
    # While the user wants a particular player's information the program runs.
    while answer == 'y':
        
        # Works if the player the use ris looking for is in the dictionary.
        try:
            name = input("Enter player's name: ")
            print(name)
            
            # Finds the player in the dictionary and gets his information.
            player = players[name]
            
            #Prompts the user to pick the player's overall rusher rating or the
            # player's individual years and their associated rusher ratings.
            response = input("\nPick one\na) Overall rusher rating\n" \
                "b) Individual years and ratings\n\nEnter choice: ")
            choice = response.lower()
            print(choice + "\n")
            
            if choice == 'a':
                print(player)
            elif choice == 'b':
                player.printInfo()
            else:
                print("You've entered an illegal choice")
                
        # Tells the user that the player is not in the dictionary if the player
        # is not in the dictionary.
        except KeyError:
            print("This player is not in the system.")
        
        response = input("\nAre you interested in another player? ")
        print(response)
        answer = response.lower()
        
        
###############################################################################
# Main program that runs each of the above procedures and functions.
fileName = "rushers.csv"
players = createPlayerDictionary(fileName)
printAlphaPlayerList(players)
lookUpIndividualPlayerInformation(players)