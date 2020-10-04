# This is to create a fully random character
# pylint: disable=no-member
# pylint: disable=unused-wildcard-import

from CharFunctions import *
import random

class Player:
    def __init__(self, name, race, classtype, strength, dex, con, intelligence, wis, charisma, background):
        self.name = name
        self.race = race
        self.classtype = classtype
        self.strength = strength
        self.dex = dex
        self.con = con
        self.intelligence = intelligence
        self.wis = wis
        self.charisma = charisma

genform = input("Would you like to \n  1. Fully randomize \n  2. Randomize with class/stat bias \n  3. Partially randomize \n  ")
while True:
    char = Player
    try:
        choice = int(genform)
    except:
        print("Not a valid input")
        continue
    name = str(input("What do you want your character's name to be? "))
    char.name = name
    if choice == 1:
        char.race = randrace()
        char.classtype = randclass()
        char = randstats(char)
        while(char.strength + char.dex + char.con + char.intelligence + char.wis + char.charisma)<60:
            randstats(char)
        break
    elif choice == 2:
        char.race = randrace()
        char.classtype = randclass()
        rolllist = []
        i = 0
        while i < 6:
            rolllist.append(roll(6, 3))
            i += 1
        char = statassign(char, rolllist)
        break
    elif choice == 3:
        while True:
            race = str(input("Race: "))
            race = fixword(race)
            if race == "random":
                char.race = randrace()
                print(char.race)
                break
            elif race in racelist():
                race = racespecs(race, "choice")
                char.race = race
                break
            else:
                print("Not a valid race")
        while True:
            classtype = str(input("Class: "))
            classtype = fixword(classtype)
            if classtype == "random":
                char.classtype = randclass()
                print(char.classtype)
                break
            elif classtype in classlist():
                char.classtype = classtype
                break
            else:
                print("Not a valid class")
        while True:
            method = str(input("Choose some stats or fully randomize? "))
            if "choose" in method and "random" in method:
                print("Pick one, coward")
            elif "random" in method:
                char = randstats(char)
                break
            elif "choose" in method:
                char = indivstat(char, "strength")
                char = indivstat(char, "dex")
                char = indivstat(char, "con")
                char = indivstat(char, "intelligence")
                char = indivstat(char, "wis")
                char = indivstat(char, "charisma")
                break
        break            
    else:
        print("Not a valid choice")
while True:
    moreinfo = str(input("Do you want to add any extra info (background, alignment, lifestyle): "))
    moreinfo = fixword(moreinfo)
    if "y" in moreinfo and "n" in moreinfo:
        print("Choose one coward")
    elif "y" in moreinfo:
        if genform == "1" or genform == "2":
            char.background = random.choice(backgroundlist())
            char.alignment = random.choice(alignlist())
            char.lifestyle = random.choice(lifestylelist())
            printallstats(char)
            break
        while True:
            backgrnd = str(input("What would you like your background to be? "))
            backgrnd = fixword(backgrnd)
            if backgrnd == "random":
                char.background = random.choice(backgroundlist())
                break
            elif backgrnd in backgroundlist():
                char.background = backgrnd
                break
            elif backgrnd not in backgroundlist():
                print("Must be random or one of these options: " + ", ".join(backgroundlist()))
        while True:
            alignment = str(input("What would you like your alignment to be? "))
            alignment = fixword(alignment)
            if alignment == "random":
                char.alignment = random.choice(alignlist())
                break
            elif alignment in alignlist():
                char.alignment = alignment
                break
            elif alignment not in alignlist():
                print("Must be random or one of these options: " + ", ".join(alignlist()))
        while True:
            lifestyle = str(input("What would you like your lifestyle to be? "))
            lifestyle = fixword(lifestyle)
            if lifestyle == "random":
                char.lifestyle = random.choice(lifestylelist())
                break
            elif lifestyle in lifestylelist():
                char.lifestyle = lifestyle
                break
            elif lifestyle not in lifestylelist():
                print("Must be random or one of these options: " + ", ".join(lifestylelist()))
        printallstats(char)
        break
    elif "n" in moreinfo:
        printallstats(char)
        break