def advstats(char, rolllist, statlist, stat1, stat2):
    statinput(char, stat1, rolllist[-1])
    del rolllist[-1]
    statlist.remove(stat1)
    statinput(char, stat2, rolllist[-1])
    del rolllist[-1]
    statlist.remove(stat2)
    char = whichstat(char, rolllist, statlist)
    return char

def alignlist():
    alignlist = ["lawful good", "lawful neutral", "lawful evil"]
    alignlist.extend(["neutral good", "true neutral", "neutral evil"])
    alignlist.extend(["chaotic good", "chaotic neutral", "chaotic evil"])
    return alignlist

def backgroundlist():
    backgroundlist = ["acolyte", "criminal", "spy", "folk hero"]
    backgroundlist.extend(["haunted one", "noble", "sage", "soldier"])
    return backgroundlist

def classlist():
    classlist = ["barbarian", "bard", "cleric", "druid", "fighter", "monk"]
    classlist.extend(["paladin", "ranger", "rogue", "sorcerer", "warlock", "wizard"])
    return classlist

def fixword(word):
    word = word.replace('.', '')
    word = word.replace(':', '')
    word = word.replace(';', '')
    word = word.replace('!', '')
    word = word.replace('?', '')
    # word = word.replace(' ', '')
    word = word.lower()
    return word

def indivstat(char, stat):
    while True:
        statnum = input("What do you want your " + stat + " to be? ")
        if str(statnum) == "random":
            char = statinput(char, stat, roll(6, 3))
            break
        elif 6 <= int(statnum) <= 18:
            char = statinput(char, stat, int(statnum))
            break
        else:
            print(stat + " must be random or an int between 6 and 18")
    return char

def lifestylelist():
    lifestylelist = ["wretched", "squalid", "poor", "modest"]
    lifestylelist.extend(["comfortable", "wealthy", "aristocratic"])
    return lifestylelist

def printallstats(char):
    print("\n")
    print("Character sheet: ")
    print(char.race, char.classtype)
    print("    name: " + char.name)
    print("base stats:")
    print("    strength: " + str(char.strength))
    print("    dexterity: " + str(char.dex))
    print("    constitution: " + str(char.con))
    print("    intelligence: " + str(char.intelligence))
    print("    wisdom: " + str(char.wis))
    print("    charisma: " + str(char.charisma))
    try:
        print("background: " + char.background)
        print("alignment: " + char.alignment)
        print("lifestyle: " + char.lifestyle)
        printracialtraits(char)
        printbackgroundstats(char)
        printmoney(char)
    except:
        printracialtraits(char)
    print("\n")

def printbackgroundstats(char):
    print("Traits gained by having a " + char.background + " background: ")
    if char.background == "acolyte":
        print("    skill proficiencies: insight, religion")
        print("    knows two extra languages")
    if char.background == "criminal" or char.background == "spy":
        print("    skill proficiencies: deception, stealth")
        print("    proficient with thieves tools and a gaming set")
    if char.background == "folk hero":
        print("    skill proficiencies: animal handling, survival")
        print("    proficient with land vehicles and an artisan's tool")
    if char.background == "haunted one":
        print("    skill proficiencies: two of these four: arcana, investigation, religion, or survival")
        print("    knows one extra exotic language")
    if char.background == "noble":
        print("    skill proficiencies: history, persuasion")
        print("    proficient in a gaming set and knows an extra language")
    if char.background == "sage":
        print("    skill proficiencies: arcana, history")
        print("    knows two extra languages")
    if char.background == "soldier":
        print("    skill proficiencies: athletics, intimidation")
        print("    proficient in land vehicles and one gaming set")

def printmoney(char):
    print("Money gained by living a " + char.lifestyle + " lifestyle: ", end="")
    if char.lifestyle == "wretched":
        print("none")
    elif char.lifestyle == "squalid":
        print("1 sp")
    elif char.lifestyle == "poor":
        print("2 sp")
    elif char.lifestyle == "modest":
        print("1 gp")
    elif char.lifestyle == "comfortable":
        print("2 gp")
    elif char.lifestyle == "wealthy":
        print("4 gp")
    elif char.lifestyle == "aristocratic":
        print("10+ gp")

def printracialtraits(char):
    print("Traits gained by being a " + char.race + ": ")
    if "dragonborn" in char.race:
        print("    +2 strength, +1 charisma, draconic ancestry, breath weapon, damage resistance")
    elif "dwarf" in char.race:
        print("    +2 constitution, darkvision, dwarven resilience, dwarven combat training, stonecunning")
    elif "elf" in char.race:
        print("    +2 dexterity, darkvision, keen senses, fey ancestry, trance")
    elif "gnome" in char.race:
        print("    +2 intelligence, darkvision, gnome cunning")
    elif "goliath" in char.race:
        print("    +2 strength, +1 constitution, natural athlete, stone's endurance, powerful build, mountain born")
    elif "half-elf" in char.race:
        print("    +2 charisma, +1 to two other ability scores, darkvision, fey ancestry, skill versatility")
    elif "half-orc" in char.race:
        print("    +2 strength, +1 constitution, darkvision, menacing, relentless endurance, savage attacks")
    elif "halfling" in char.race:
        print("    +2 dexterity, lucky, brave, halfling nimbleness")
    elif "human" in char.race:
        print("    +1 to all ability scores, extra language")
    return

def racelist():
    racelist = ["dragonborn", "dwarf", "elf", "gnome", "goliath"]
    racelist.extend(["half-elf", "half-orc", "halfling", "human"])
    return racelist

def racespecs(race, method):
    import random
    if method == "rand":
        if race == "dwarf":
            race = (random.choice(["hill", "mountain"])) + " dwarf"
        elif race == "elf":
            race = (random.choice(["eladrin", "high", "wood"])) + " elf"
        elif race == "gnome":
            race = (random.choice(["deep", "rock"])) + " gnome"
        elif race == "halfling":
            race = (random.choice(["lightfoot", "stout"])) + " halfling"
    elif method == "choice":
        if race == "dwarf":
            while True:
                info = str(input("Hill or mountain dwarf? "))
                info = fixword(info)
                if info not in ["hill", "mountain"]:
                    print("Must be one of these options")
                else:
                    break
            race = info + " dwarf"
        elif race == "elf":
            while True:
                info = str(input("Eladrin, high, or wood elf? "))
                info = fixword(info)
                if info not in ["eladrin", "high", "wood"]:
                    print("Must be one of these options")
                else:
                    break
            race = info + " elf"
        elif race == "gnome":
            while True:
                info = str(input("Deep or rock gnome? "))
                info = fixword(info)
                if info not in ["deep", "rock"]:
                    print("Must be one of these options")
                else:
                    break
            race = info + " gnome"
        elif race == "halfling":
            while True:
                info = str(input("Lightfoot or Stout halfling? "))
                info = fixword(info)
                if info not in ["lightfoot", "stout"]:
                    print("Must be one of these options")
                else:
                    break
            race = info + " halfling"
    return race

def randclass():
    import random
    charclass = random.choice(classlist())
    return charclass

def randrace():
    import random
    race = random.choice(racelist())
    race = racespecs(race, "rand")
    return race
        
def roll(dice, times):
    import random
    total = 0
    while times > 0:
        number = random.randint(1, dice)
        if number == 1:
            number = random.randint(1, dice)
        total += number
        times -= 1
    return total

def randstats(char):
    char.strength = roll(6, 3)
    char.dex = roll(6, 3)
    char.con = roll(6, 3)
    char.intelligence = roll(6, 3)
    char.wis = roll(6, 3)
    char.charisma = roll(6, 3)
    return char

def statassign(char, rolllist):
    import random
    statlist = ["strength", "dex", "con", "intelligence", "wis", "charisma"]
    rolllist.sort()
    if char.classtype == "barbarian":
        char = advstats(char, rolllist, statlist, "strength", "con")
    elif char.classtype == "bard":
        char = advstats(char, rolllist, statlist, "charisma", "dex")
    elif char.classtype == "cleric":
        char = advstats(char, rolllist, statlist, "wis", "charisma")
    elif char.classtype == "druid":
        char = advstats(char, rolllist, statlist, "wis", "intelligence")
    elif char.classtype == "fighter":
        char = advstats(char, rolllist, statlist, "dex", "strength")
    elif char.classtype == "monk":
        char = advstats(char, rolllist, statlist, "dex", "strength")
    elif char.classtype == "paladin":
        char = advstats(char, rolllist, statlist, "intelligence", "con")
    elif char.classtype == "ranger":
        char = advstats(char, rolllist, statlist, "strength", "wis")
    elif char.classtype == "rogue":
        char = advstats(char, rolllist, statlist, "dex", "wis")
    elif char.classtype == "sorcerer":
        char = advstats(char, rolllist, statlist, "charisma", "con")
    elif char.classtype == "warlock":
        char = advstats(char, rolllist, statlist, "charisma", "wis")
    elif char.classtype == "wizard":
        char = advstats(char, rolllist, statlist, "intelligence", "wis")
    return char

def statinput(char, stat, statinput):
    if stat == "strength":
        char.strength = statinput
    elif stat == "dex":
        char.dex = statinput
    elif stat == "con":
        char.con = statinput
    elif stat == "intelligence":
        char.intelligence = statinput
    elif stat == "wis":
        char.wis = statinput
    elif stat == "charisma":
        char.charisma = statinput
    return char

def whichstat(char, rolllist, statlist):
    from random import choice
    i = 0
    while i<4:
        stat = choice(statlist)
        char = statinput(char, stat, rolllist[-1])
        del rolllist[-1]
        statlist.remove(stat)
        i += 1
    return char