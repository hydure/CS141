# Proj3.py
#
# Colin Fox Lightfoot
# CFLightfoot@email.wm.edu
# (540)-538-2538
#
# This program allows you to choose one of five games labeled a through e. This
# program reads through a dictionary.txt file for the respective games.
# Game a finds all the words of a particular length containging just a single
# vowel that does not have a particualr letter in it. Game b finds all the 
# words containing all the letters of a particular word in no particualr order.
# Game c finds all the words that contain all but one of the letters of a
# string of unique characters. Game d finds finds all the words that use i, j,
# t and x exactly once. Game e finds all the palindromes of a particular length.
# If the user is done playing games and wants to quit, any case of 'q' is
# pressed, the dataFile is closed, and then the program closes.


def cleanWord(word):
    """Returns word in lowercase stripped of whitespace."""
    
    return word.strip().lower()


##############################################################################
def findWordofLengthSingleVowel(dataFile):
    """Finds all the words of a particular length containing a single vowel \
    that does not have a particular letter in it."""
    
    # Gets and prints input.
    lengthInput = input("\nPlease enter the word length you are looking for: ")
    wordLength = int(lengthInput)
    print(wordLength)
    excludeLetter = input("Please enter the letter you'd like to exclude: ")
    print(excludeLetter+"\n")
    
    #Assigns the values to compare words to.
    vowels = 'aeiou'
    vowelsInWord = ""
    nothing = ""
    
    # Looks at each word in the dataFile, cleans it, then checks to see
    # if the word matches the parameters and restrictions.
    for word in dataFile:
        word = cleanWord(word)
        count = 0
        
        # Looks at each character in each word & prints the words that have only
        # one vowel, are the inputed length, and do not include the particular
        # letter to exclude.
        for char in word:
            if char in vowels:
                count += 1
            if char in excludeLetter:
                count = (count + 1) * 2
        if count <= 1 and wordLength == len(word):
            print(word)
            nothing = nothing + "a"
    
    # If no words match the function and are printed.    
    if nothing == "":
        print("There are no words that fit this criteria.")                

    
#############################################################################
def findWordContainingAllLetters(dataFile):
    """Finds all the words containing all the letters of a particular word \
    (in no particular order)."""

    #Gets and prints input.
    userInput = input("\nEnter word: ")
    print(userInput)
    maxLength = int(input("What is the maximum length of the words you want: "))
    print(maxLength)
    print()
    
    # Tells program how many words fit the parameters and restrictions.
    anotherCount = 0   
    
    # Looks at each word in the dataFile, cleans it, then checks to see
    # if the word matches the parameters and restrictions.    
    for word in dataFile:
        word = cleanWord(word)
        count = 0  
        newWord = word

        # If all the characters of the userInput are in the word, and all of the
        # repeated characters in the userInput are found in the word, and the
        # word is less than or equal to the length desired then the word is
        #printed.
        for char in userInput:
            if char in newWord:
                newWord = newWord.replace(char, "", 1)
                count += 1 
        if count == len(userInput) and len(word) <= maxLength:
            print(word)
            anotherCount += 1
            
    # If no words match the function and are printed.    
    if anotherCount == 0:
        print("\nThere are no words that fit this criteria.")            


###############################################################################
def findWordWithAllButOneLetter(dataFile):
    """Finds all the words that contain all but one of the letters of a \
    string of unique characters."""

    userInput = input("\nPlease enter the string of unique characters: ")
    print(userInput+"\n")

    anotherCount = 0       
    
    # Looks at each word in the dataFile, cleans it, then checks to see
    # if the word matches the parameters and restrictions.    
    for word in dataFile:
        word = cleanWord(word)
        count = 0
        nothing = ""
        
        # If all but one character of a unique string is in the word,
        # then the word is printed.
        for char in userInput:
            if char in word:
                count += 1 
        if count == len(userInput) - 1:
            print(word)
            anotherCount += 1

    # If no words match the function and are printed.    
    if anotherCount == 0:
        print("\nThere are no words that fit this criteria.")                        


###############################################################################
def findWordContainingIJTAndX(dataFile):
    """Find all words that use i, j, t and x exactly once."""

    #Declares the string to be searched for in each word of dictionary.
    string = "ijtx"
    print()
    
    # Looks at each word in the dataFile, cleans it, then checks to see
    # if the word matches the parameters and restrictions.    
    for word in dataFile:
            word = cleanWord(word)
            count = 0
            newWord = word

            # If the word has i, j, t, and x in it in no particular order, and
            # does not have more than one i, j, t, and x, the word is
            # printed.
            for char in string:
                if char in newWord:
                    newWord = newWord.replace(char, '' , 1)
                    count += 1
                if char in newWord:
                    count -= 1
            if count == len(string):
                print(word)    
        
                    
###############################################################################
def findPalindromesOfParticularLength(dataFile):
    """Find all the palindromes of a particular length"""
    
    # Asks the user for how long they want the palindromes the user is
    # searching for to be.
    maxLength = int(input("\nEnter the length of the palindromes you desire: "))
    print(maxLength)
    print()

    # Sets a variable to tell if no words fit the criteria of the function.
    nothing = ""
    
    # Looks at each word in the dataFile, cleans it, then checks to see
    # if the reversed word equals the word that has the inputed length and
    # prints word if the two versions of the word are equal.    
    for word in dataFile:
        word = cleanWord(word)
        if len(word) == maxLength and word == word[::-1]:
            print(word)
            nothing = nothing + "a"

    # If no words match the function and are printed.    
    if nothing == "":
        print("There are no words that fit this criteria.")


###############################################################################
# Opens dictionary so each word in it can be checked during each word game.
dataFile = open("dictionary.txt", 'r')
        
# Allows while loop to run as until user enters any case of 'q'.
choice = ""
        
print("Let's play a game")
        
while choice != 'q':
            
    # Resets the index to 0 in the dictionary so the whole file can be searched
    # through again when the next game is called.
    dataFile.seek(0)
            
    # The menu that appears for users to determine what game to play.
    print("\nChoose which game you want to play")
    print("a) Find words with only one vowel and excluding a specific letter")
    print("b) Find words containing all the letters of another word with "\
          "a maximum length")
    print("c) Find words containing all characters but one of a given length")
    print("d) Find words containing i, j, t and x")
    print("e) Find all the palindromes of a particular length")
    print("q) quit\n")
            
    # Gets user input and lowers the case so games can be called in either
    # upper or lower case in the user input.
    inputChoice = input("Enter a choice: ")
    print(inputChoice)
    choice = inputChoice.lower()
        
    # Calls a game depending on the input.
    if choice == 'a':
        findWordofLengthSingleVowel(dataFile)
    elif choice == 'b':
        findWordContainingAllLetters(dataFile)
    elif choice == 'c':
        findWordWithAllButOneLetter(dataFile)
    elif choice == 'd':
        findWordContainingIJTAndX(dataFile)
    elif choice == 'e':
        findPalindromesOfParticularLength(dataFile)
    elif choice == 'q':
        print("\nThanks for playing")
        dataFile.close()
    # If the user inputs any other input.    
    else:
        print("\nYou've entered an incorrect choice. Try again")