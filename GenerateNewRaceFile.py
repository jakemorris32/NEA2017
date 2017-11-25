import random

def genRace():

    names = ["Lanette","Stacy","Mitch","Ambrose","Leonardo","Al","Daisey","Lynda","Odessa","Carmelina","Sharleen","Donnette","Darnell","Mitzie","Liz","Zulema","Rhea","Thomas","Shawnta","Elfriede","Tera","Carlota","Nanette","Letha","Alaine","Oralee","Shelli","Melisa","Elliot","Graciela","Antione","Shiloh","Cliff","Dixie","Vonnie","Abigail","Luciano","Nga","Britteny","Marcela","Lynne","Tarra","Pamala","Dennis","Lorri","Roxane","Kori","Dorathy","Annemarie","Shea","Marylouise","Cheri","Lucrecia","Dixie","Shasta","Percy","Roy","Vina","Dorotha","Salvatore","Halley","Temeka","Khalilah","Laronda","Takako","Marlana","Eulalia","Clay","Margeret","Sherri","Damon","Laurinda","Margret","Chong","Maragret","Enid","Chae","Ria","Ezekiel","Eddy","Emilia","Luann","Pearlie","Arminda","Murray","Lizzette","Obdulia","Cristi","Novella","Muriel","Tad","Brook","Armida","Isis","Marylynn","Edda","Tuan","Dena","Rashad","Shane"]

    x = input("Enter race number to generate:")
    print("")

    with open("Race_Files/"+x+"_raceFile.txt" , "w") as file:
        for y in range (1,5):
            index = int(random.randint(0, 99))
            
            ID = str(random.randint(0,9999))
            ID = (((4 - len(ID)) * "0") + ID)
            
            file.write(names[index]+":"+str(random.randint(99, 450))+":"+str(random.randint(1,9))+":"+ID+"\n")


var = True
while var == True:
    genRace()
