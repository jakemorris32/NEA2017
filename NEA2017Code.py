                                                                                                                    
 #-----------------#
 #----FUNCTIONS----#
 #-----------------#

# FUCTION: LIST PRINT (lPrint)

def lPrint(myList , name):
    print (name + " =")
    for item in myList: print (item)
    
# FUNCTION: IMPORT A NEW FILE (importFile)

def importFile(fileName):
    with open((fileName) , "r") as file: 
        # 'word.strip' - removes \n from each line
        # 'line.split(":")' - defines a word as each item separated by a colon
        # 'for line in file' - repeats this process for each line
        list = [[word.strip() for word in line.split(":")] for line in file]
        print("")
    return (list)

# FUNCTION: DISPLAY THE LEADERBOARD (displayLB)

def displayLB():
    lbList = importFile("lbFile.txt")
    print ("\t      LEADERBOARD")
    print("")
    print (40 * "=")
    print ("NAME    \tDRIVER ID\tPOINTS")
    print (40 * "=")
    for item in lbList:
        fItem = ""
        for subitem in item:
            # Ensures the tabs are even
            subitem = (subitem + (" " * ( 8 - len(subitem))))
            # Prints each subitem with a tab in the middle
            fItem += (subitem  + "\t")
        print(fItem)
        

# FUNCTION: IMPORT A NEW RACE (raceImport)

def raceImport():
    print ("Importing race...")
    raceNo = input("Enter race number: ")
    raceFile = ("Race_Files/" + raceNo + "_raceFile.txt")

    driverInfo = importFile(raceFile)
    for item in driverInfo:
        item.append(0) # Appends a new points variable to the end of each sublist

    print("Race import completed")


    # 'key=lambda' is an argument used to instruct driverInfo to be sorted by time
    driverInfo = sorted(driverInfo, key=lambda x: x[1])
    driverInfo[0][4] += 10 # Gives the correct amount of points to the top 3 drivers
    driverInfo[1][4] += 6
    driverInfo[2][4] += 3

    return driverInfo

# FUNCTION: COMBINE POINTS (combinePoints)

def combinePoints():
    fileList = importFile("lbFile.txt")
    lPrint(fileList ,"fileList")
    with open(("lbFile.txt") , "w") as file :
        # Find drivers with matching driverIDs
        for fileItem in fileList:
            for infoItem in driverInfo:
                if infoItem[3] == fileItem[1]:
                    print("Combining " , fileItem , "with" , infoItem)
                    fileItem[2] = int(infoItem[4]) + int(fileItem[2])
                    driverInfo.remove(infoItem)
        print("")
        file.writelines(":".join(str(word) for word in line) + "\n" for line in fileList)

        
        
# FUNCTION: SORT LEADERBOARD FILE (sortLB)

def sortLB():

    with open("lbFile.txt" , "r") as file:
        combinePoints()

    with open("lbFile.txt" , "a") as file:
        for item in driverInfo:
            del(item[1])
            del(item[1])
            for subitem in item:
                file.write(str(subitem))
                if subitem != item[2]:
                    file.write(":")
            file.write("\n")
            
    lbList = importFile("lbFile.txt")

    # Make the last item an interger so it can be sorted
    for item in lbList:
        item[2] = int(item[2])
        
    # lbList is sorted by the 4th value (points)
    lbList = sorted(lbList , key=lambda x: x[2])
    lbList = list(reversed(lbList))
    print("lbList sorted")

    
    with open("lbFile.txt" , "w") as file:

        for item in lbList:
            for subitem in item:
                file.write(str(subitem))
                if subitem != item[2]:
                    file.write(":")
            file.write("\n")
    print("lbList written")
                
        


 #-----------------#
 #----MAIN-CODE----#
 #-----------------#


# USER MENU
print ("================================================================")
print ("==                                                            ==")
print ("==                    NEA PYTHON CODE 2017                    ==")
print ("==                                                            ==")
print ("================================================================")
print("")
print("")
print("Welcome")
print("")
# Displays a list of options and asks user to choose one
print("Would you like to:") 
print("   - Import a new race (a)")
print("   - Sort the leaderboard (b)")
print("   - Display the leaderboard (c)")
print("   - Erase lbFile.txt (d)")
print("   - Exit the program (exit)")


chosen = False
# Will continue asking for an input until answer is valid
while chosen == False:
    print("")
    answer = input("Input: ")

    if answer == "a": # Import race
        driverInfo = raceImport()

    elif answer == "b": # Sort leaderboard
        sortLB()

    elif answer == "c": # Display leaderboard
        displayLB()

    elif answer == "d":
        sure = input("Are you sure? (y/n): ")
        if sure == "y":
            print("Erasing lbFile.txt")
            with open("lbFile.txt" , "w") as file:
               file.write("")
        else:
            print ("lbFile.txt will not be erased")
        
        
    elif answer == "exit": # Exit the program
        print("")
        print("Exiting NEA2016Code.py")
        quit() # Built in function to exit

    else: # If answer is invalid
        print ("")
        print ("ERROR INVALID OPTION")
        print ("PLEASE CHOOSE AGAIN")
        print ("")
