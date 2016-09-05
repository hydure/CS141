#Player.py
# Colin Fox Lightfoot
# CFLightfoot@email.wm.edu
# (540)-538-2538
#
# Defines the Player class.

class Player (object):
    
    def __init__ (self, first, last):
        '''The constructor for a player.'''
        
        self.first = first
        self.last = last
        self.rating = 0
        self.info = []


###############################################################################
    def update(self, year, team, pos, att, yards, tds, fumbles):
        '''Creates a list of information for this player for this year and 
        append it to the info field. Then calls calcrating.'''
        
        # Appends a player's season to the player's information and calculates
        # the player's new overall rusher rating.
        newStats = [year, team, pos, att, yards, tds, fumbles]
        self.info.append(newStats)
        self.calcrating()


###############################################################################
    def calcrating(self):
        '''Goes through all sub-lists in info adding up totals for touchdowns, 
        attempts, etc. Then calculates the overall rating for this player.
        Stores it in the instance variable "rating".  If the player's total
        attempts is 0, the rating is set to 0. '''
        
        totalTouchdown = 0
        totalYards = 0
        totalAttempts = 0
        totalFumbles = 0
        
        # Iterates through each year the player played and adds up specific
        # information accordingly.
        for yearStat in self.info:
            totalTouchdown += int(yearStat[5])
            totalYards += int(yearStat[4])
            totalAttempts += int(yearStat[3])
            totalFumbles += int(yearStat[6])
        
        # If the player never attempted to rush, his rating is set to 0.
        if totalAttempts == 0:
            self.rating = 0        
        # Calculates the player's rating based on his overall information.
        else:
            yds = (totalYards/(4.05 * totalAttempts))
        
            if yds > 2.375:
                yds = 2.375
        
            perTDs = ((39.5 * totalTouchdown) / totalAttempts)
        
            if perTDs > 2.375:
                perTDs = 2.375
        
            perFumbles = (2.375 - ((21.5 * totalFumbles) / totalAttempts))
        
            self.rating = ((yds + perTDs + perFumbles) * (100 / 4.5))
        
        
        

###############################################################################
    def returnName(self):
        '''Returns the name of the player first last.'''
        
        return "{} {}".format(self.first, self.last)


###############################################################################
    def returnReverseName(self):
        '''Returns the name of the player as last, first.'''
        
        return "{}, {}".format(self.last, self.first)


###############################################################################
    def __eq__ (self, other):
        '''Determines if this person's name is the same as the other person's
        name.'''
        
        return self.first == other.first and self.last == other.last


###############################################################################
    def __lt__(self,other):
        '''Determines if this person's name is less than the other person's
        name alphabetically.'''
    
        if self.last == other.last:
            return self.first < other.first
        else:
            return self.last < other.last
            

###############################################################################
    def __gt__ (self, other):
        '''Determines if this person's name is greater than the other person's
        name alphabetically.'''

        if self.last == other.last:
            return self.first > other.first
        else:
            return self.last > other.last        


###############################################################################
    def __str__(self):
        '''Returns a string of the person's name and their rating in a nice
        format.'''
        
        name = "{} {}".format(self.first, self.last)

        return "{:28s}{:.2f}".format(name, self.rating)


###############################################################################
    def calc(self, sublist):
        '''Calculates a rusher rating for one sub-list year in  the info list'''

        # Calculates the information for only a specific year for a player.
        stats = self.info[sublist]
        yds = int(stats[4])/(4.05 * int(stats[3]))
        perTDs = (39.5 * int(stats[5])) / int(stats[3])
        perFumbles = 2.375 - ((21.5 * int(stats[6])) / int(stats[3]))
        
        # If the player never attempted to rush, his rating is set to 0.
        if int(stats[3]) == 0:
            rating = 0        
        # Calculates the player's rating based on only one year's information.
        else:
            if yds > 2.375:
                yds = 2.375        
        
            if perTDs > 2.375:
                perTDs = 2.375
        
            rating = (yds + perTDs + perFumbles) * (100 / 4.5)
        
        return rating


###############################################################################
    def printInfo(self):
        '''Prints the individual year information about this player, including
        each year's rusher rating. The list should be in year order. Uses calc
        to assist.'''
        
        increment = 0
        name = "{} {}".format(self.first, self.last)
        
        # Sorts every season of a player in chronological order
        self.info.sort()
        
        # Prints out information from each season a player played football.
        for season in self.info:
            yearRating = self.calc(increment)
            year = self.info[increment][0]
            team = self.info[increment][1]
            
            print("{} in {} played for {} - {:.2f}".format\
                  (name, year, team, yearRating))
            
            increment += 1
            
            
###############################################################################