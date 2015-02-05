import random, math
from ClassesPokemon import *

def Battle(Player, Computer):
    PlayerParty=Player.Party[:]
    ComputerParty=Computer.Party[:]
    while True:
        if len(PlayerParty)==0:
            return Computer
        elif len(ComputerParty)==0:
            return Player
        while True:
            temp1=0
            activePokemon1=PlayerParty[0]
            activePokemon2=ComputerParty[0]
            choice=input("What will " + activePokemon1.Name + " do? ")
            if choice=="Switch":
                if len(PlayerParty)>1:
                    choice=input("Which Pokemon do u want to switch to? ")
                    tempPokemon=activePokemon1
                    activePokemon1=PlayerParty[int(choice)]
                    PlayerParty[int(choice)]=tempPokemon
                    PlayerParty[0]=activePokemon1
                    temp1=1
                    break
                else:
                    print("You only have one pokemon left!")
                    continue
            else:
                activePokemon1.Move=getMove(activePokemon1.MoveSet[int(choice)])
                break
        activePokemon2.Move=getMove(random.choice(activePokemon2.MoveSet))
        if temp1==0:
            FirstPokemon, SecondPokemon, num=WhoGoesFirst(activePokemon1, activePokemon2)
            SecondPokemon.HP=int(SecondPokemon.HP)-DamageCalculator(FirstPokemon, SecondPokemon, FirstPokemon.Move)
            if SecondPokemon.HP<=0:
                if num==1:
                    print(activePokemon2.Name + " fainted!")
                    ComputerParty.remove(activePokemon2)
                    continue
                else:
                    print(activePokemon1.Name + " fainted!")
                    PlayerParty.remove(activePokemon1)
                    if len(PlayerParty)>=1:
                        choice=input("Which pokemon would you like to send out next? ")
                        tempPokemon=PlayerParty[int(choice)]
                        PlayerParty[int(choice)]=PlayerParty[0]
                        PlayerParty[0]=tempPokemon
                    continue
            if num==1:
                ComputerParty[0]=SecondPokemon
            else:
                PlayerParty[0]=SecondPokemon
            FirstPokemon.HP=int(FirstPokemon.HP)-DamageCalculator(SecondPokemon, FirstPokemon, SecondPokemon.Move)
            if FirstPokemon.HP<=0:
                if num==1:
                    print(activePokemon1.Name + " fainted!")
                    PlayerParty.remove(activePokemon1)
                    if len(PlayerParty)>=1:
                        choice=input("Which pokemon would you like to send out next? ")
                        tempPokemon=PlayerParty[int(choice)]
                        PlayerParty[int(choice)]=PlayerParty[0]
                        PlayerParty[0]=tempPokemon
                    continue
                else:
                    print(activePokemon2.Name + " fainted!")
                    ComputerParty.remove(activePokemon2)
                    continue
            if num==1:
                PlayerParty[0]=FirstPokemon
            else:
                ComputerParty[0]=FirstPokemon
        else:
            FirstPokemon, SecondPokemon=activePokemon2, activePokemon1
            SecondPokemon.HP=int(SecondPokemon.HP)-DamageCalculator(FirstPokemon, SecondPokemon, FirstPokemon.Move)
            if SecondPokemon.HP<=0:
                print(activePokemon1.Name + " fainted!")
                PlayerParty.remove(activePokemon1)
                if len(PlayerParty)>=1:
                    choice=input("Which pokemon would you like to send out next? ")
                    tempPokemon=PlayerParty[int(choice)]
                    PlayerParty[int(choice)]=PlayerParty[0]
                    PlayerParty[0]=tempPokemon
                continue
            PlayerParty[0]=SecondPokemon

def WhoGoesFirst(Pokemon1, Pokemon2):
    if Pokemon1.Speed>Pokemon2.Speed:
        return Pokemon1, Pokemon2, 1
    elif Pokemon1.Speed<Pokemon2.Speed:
        return Pokemon2, Pokemon1, 2
    else:
        blah=[Pokemon1,Pokemon2]
        LuckyPokemon=random.choice(blah)
        if LuckyPokemon==Pokemon1:
            return LuckyPokemon, Pokemon2, 1
        else:
            return LuckyPokemon, Pokemon1, 2

def DamageCalculator(Attacker, Defender, Move):
    print(Attacker.Name + " used " + Move.Name + "!")
    RandomNumber = random.random() * 100
    if RandomNumber<=100 - int(Move.Accuracy):
        print(Attacker.Name + " missed!")
        return 0
    if Move.Catagory=="Physical":
        damage = (((42 * int(Attacker.Attack) * int(Move.Power))/int(Defender.Defense))/50) + 2
    elif Move.Catagory=="Special":
        damage = (((42 * int(Attacker.SpAttack) * int(Move.Power))/int(Defender.SpDefense))/50) + 2
    damage = STAB(damage, Attacker, Move)
    effect = effectiveness(Defender, Move, TypeAdvantagesObjects)
    damage = damage * effect
    RandomNumber = random.randint(84,100)
    damage = damage * (RandomNumber / 100)
    if effect!=0:
        damage = criticalHit(damage)
    if effect==0:
        print("It does not affect " + Defender.Name + "!")
    elif effect > 1:
        print("It's supereffective!")
    elif effect < 1:
        print("It's not very effective.")
    return math.floor(damage)

def STAB(damage, Attacker, Move):
    if Attacker.Type1==Move.Type or Attacker.Type2==Move.Type:
        return damage*1.5
    return damage

def effectiveness(Defender, Move, TypeObjects):
    effect = 1
    for i in range(0,len(TypeObjects)):
        if Move.Type==TypeObjects[i].MoveType:
            for j in range(0,len(TypeObjects[i].ImmuneAgainst)):
                if Defender.Type1==(TypeObjects[i].ImmuneAgainst)[j] or Defender.Type2==(TypeObjects[i].ImmuneAgainst)[j]:
                    return 0
            for j in range(0,len(TypeObjects[i].StrongAgainst)):
                if Defender.Type1==(TypeObjects[i].StrongAgainst)[j] or Defender.Type2==(TypeObjects[i].StrongAgainst)[j]:
                    effect = effect * 2
            for j in range(0,len(TypeObjects[i].WeakAgainst)):
                if Defender.Type1==(TypeObjects[i].WeakAgainst)[j] or Defender.Type2==(TypeObjects[i].WeakAgainst)[j]:
                    effect = effect / 2
            return effect
    return effect

def criticalHit(damage):
    crit = False
    RandomNumber = random.random() * 100
    if RandomNumber<=6.25:
        crit = True
    if crit==True:
        print("A critical hit!")
        return damage * 2
    return damage
"""
def getPokemon(string):
    for i in range(0,len(PokemonObjects)):
        if string==PokemonObjects[i].Name:
            return PokemonObjects[i]
    return ("There is no such Pokemon as " + string + ".")
"""
def getMove(string):
    for i in range(0,len(MoveObjects)):
        if string==MoveObjects[i].Name:
            return MoveObjects[i]
    return ("There is no such move as " + string + ".")

def generatePokemon():
    randomPokemonName = random.choice(PokemonNames)
    with open('PokesimPokemon.txt', 'r') as in_file:
        PokemonStats = in_file.readlines()
        for i in range(0,len(PokemonStats)):
            PokemonStats[i] = PokemonStats[i].replace('\n', '')
    with open('PokemonMovepools.txt', 'r') as in_file:
        PokemonMovepools = in_file.readlines()
        for i in range(0,len(PokemonMovepools)):
            PokemonMovepools[i] = PokemonMovepools[i].replace('\n', '')
    randomPokemonMovepool=[]
    for i in range(0,len(PokemonMovepools)):
        if randomPokemonName==PokemonMovepools[i]:
            for j in range(i,len(PokemonMovepools)):
                if PokemonMovepools[j]=="****":
                    break
                randomPokemonMovepool.append(PokemonMovepools[j])
    for i in range(0,len(PokemonStats)):
        if randomPokemonName==PokemonStats[i]:
            randomPokemon = Pokemon(PokemonStats[i], PokemonStats[i+1], PokemonStats[i+2], PokemonStats[i+3], PokemonStats[i+4], PokemonStats[i+5], PokemonStats[i+6], PokemonStats[i+7], PokemonStats[i+8], randomPokemonMovepool)
            return randomPokemon

def generateTrainer():
    PartyPokemon=[]
    for i in range(0,4):
        PartyPokemon.append(generatePokemon())
    Names = ["Parimal", "Adithya", "Taimour", "Adnan"]
    RandomTrainer = Trainer(random.choice(Names), PartyPokemon)
    return RandomTrainer
"""
def SwitchPokemon(Player, Computer):
    choice1=input("Which pokemon do you want to exchange? ")
    choice2=input("Which pokemon do you want in return? ")
    Player.Party[int(choice1)]=Computer.Party[int(choice2)]
    return Player
"""
with open('PokesimPokemon.txt', 'r') as in_file:
    PokemonStats = in_file.readlines()
    for i in range(0,len(PokemonStats)):
        PokemonStats[i] = PokemonStats[i].replace('\n' , '')
        
with open('PokemonMoves.txt', 'r') as in_file:
    MoveStats = in_file.readlines()
    for i in range(0,len(MoveStats)):
        MoveStats[i] = MoveStats[i].replace('\n', '')
        
with open('MatchTypes.txt', 'r') as in_file:
    MoveEffectiveness = in_file.readlines()
    for i in range(0,len(MoveEffectiveness)):
        MoveEffectiveness[i] = MoveEffectiveness[i].replace('\n', '')
        
PokemonNames=[]
for i in range(10,len(PokemonStats),10):
    PokemonNames.append(PokemonStats[i])
del PokemonStats
        
MoveObjects=[]
for i in range(0,len(MoveStats)):
    if MoveStats[i]=="****":
        tempObject = Moves(MoveStats[i+1], MoveStats[i+2], MoveStats[i+3], MoveStats[i+4], MoveStats[i+5], MoveStats[i+6])
        MoveObjects.append(tempObject)
del MoveStats

TypeAdvantagesObjects=[]
tempStrong=[]
tempWeak=[]
tempImmune=[]
for i in range(0,len(MoveEffectiveness)):
    if MoveEffectiveness[i]=="****":
        for j in range(i+3,len(MoveEffectiveness)):
            if MoveEffectiveness[j]=="-":
                tempStrong.append(MoveEffectiveness[j])
                temp = j+2
                break
            tempStrong.append(MoveEffectiveness[j])
        for j in range(temp,len(MoveEffectiveness)):
            if MoveEffectiveness[j]=="-":
                tempWeak.append(MoveEffectiveness[j])
                temp = j+2
                break
            tempWeak.append(MoveEffectiveness[j])
        for j in range(temp,len(MoveEffectiveness)):
            if MoveEffectiveness[j]=="-":
                tempImmune.append(MoveEffectiveness[j])
                break
            tempImmune.append(MoveEffectiveness[j])
        tempObject = TypeAdvantages(MoveEffectiveness[i+1], tempStrong, tempWeak, tempImmune)
        tempStrong, tempWeak, tempImmune = [], [], []
        TypeAdvantagesObjects.append(tempObject)
del MoveEffectiveness

"""
RandomTrainer=generateTrainer()
print(RandomTrainer.Name)
for i in range(0,len(RandomTrainer.Party)):
    print(RandomTrainer.Party[i].Name)
    print(RandomTrainer.Party[i].MoveSet)
"""

"""
temp=0
while temp==0:
    attacker=input("Attacking Pokemon: ")
    for i in range(0,len(PokemonObjects)):
        if attacker==PokemonObjects[i].Name:
            attacker=PokemonObjects[i]
            temp=1
while temp==1:
    defender=input("Defending Pokemon: ")
    for i in range(0,len(PokemonObjects)):
        if defender==PokemonObjects[i].Name:
            defender=PokemonObjects[i]
            temp=0
while temp==0:
    move=input("Attacking Move: ")
    for i in range(0,len(MoveObjects)):
        if move==MoveObjects[i].Name:
            move=MoveObjects[i]
            temp=1
print(DamageCalculator(attacker, defender, move))
"""

"""

tempFile = open("TemporaryFile.txt", 'w')
tempFile.write("Physical\n")
tempFile.close()
tempFile = open("TemporaryFile.txt", 'a')
for i in range(0,len(MoveObjects)):
    if MoveObjects[i].Catagory=="Physical":
        tempFile.write(MoveObjects[i].Name + "\n")
tempFile.write("-\n")
tempFile.write("Special\n")
for i in range(0,len(MoveObjects)):
    if MoveObjects[i].Catagory=="Special":
        tempFile.write(MoveObjects[i].Name + "\n")
tempFile.write("-\n")
tempFile.close()
"""



roundnum=1
while roundnum<=3:
    Parimal=generateTrainer()
    print(Parimal.Name)
    for i in range(0,len(Parimal.Party)):
        print(Parimal.Party[i].Name)
        print(Parimal.Party[i])
        print(Parimal.Party[i].MoveSet)
    Comp=generateTrainer()
    print(Comp.Name)
    for i in range(0,len(Comp.Party)):
        print(Comp.Party[i].Name)
        print(Comp.Party[i])
        print(Comp.Party[i].MoveSet)
    Winner=Battle(Parimal, Comp)
    if Winner==Parimal:
        print("You Won!!!")
        if roundnum==3:
            break
        roundnum+=1
        continue
    else:
        print("You Lost.")
        roundnum=10
        break


if roundnum==3:
    print("You are now the ultimate pokemon master!!!")
else:
    print("You Lost!!!")