'''
Links used:
http://inventwithpython.com/blog/2012/10/30/creating-a-button-ui-module-for-pygame/comment-page-1/
http://www.pygame.org/docs/ref/display.html
https://www.youtube.com/watch?v=IG2WidpYUY8
http://stackoverflow.com/questions/16636250/python-pygame-how-do-i-know-if-a-mouse-clicked-on-an-image
https://www.youtube.com/watch?v=1RxjbltPCVw
'''
import random, math
from FinalClassesPokemon import *
import pygame, sys
from pygame.locals import *

pygame.init()
pygame.font.init()

width = 600
height = 400
centreX = width/2-150
centreY = height/2
PlayerX = 100
PlayerY = 150
CompX = 400
CompY = 50
YouHPX = 300
YouHPY = 150
CompHPX = 50
CompHPY = 50
MessageX = 100
MessageY = 250
lenHPbar = 200
depthHPbar = 15
numRounds = 3
FPS = 30
Wait = 1000
yellow = (255, 255, 0)
green = (102, 204, 0)
black = (0, 0, 0)
red = (255, 0, 0)
blue = (0, 0, 255)
white = (255, 255, 255)
testfont = pygame.font.SysFont( "Arial", 20)
clock = pygame.time.Clock()
textRect = pygame.Rect(MessageX, MessageY, 400, 150)
hitSound = pygame.mixer.Sound('Critical.ogg')

button1X = 320
button1Y = 310
button1XR = button1X+135
button1YD = button1Y+30
button2X = 460
button2Y = 310
button2XR = button2X+135
button2YD = button2Y+30
button3X = 320
button3Y = 350
button3XR = button3X+135
button3YD = button3Y+30
button4X = 460
button4Y = 350
button4XR = button4X+135
button4YD = button4Y+30

moveRect = pygame.Rect(button1X, button1Y, width-button1X, height-button1Y)

Poke1BarX = 50
Poke1BarY = 50
Poke1X = 125
Poke1Y = 80
Poke2BarX = 350
Poke2BarY = 50
Poke2X = 425
Poke2Y = 80
Poke3BarX = 50
Poke3BarY = 200
Poke3X = 125
Poke3Y = 230
Poke4BarX = 350
Poke4BarY = 200
Poke4X = 425
Poke4Y = 230

def mainGame():
    #Inits:
    tempRounds = 1
    global screen
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Project PokeSim')
    pygame.mixer.music.load('127-battle-vs-gym-leader-.mp3')
    pygame.mixer.music.play(-1, 0.0)
    while tempRounds<=numRounds: 
        screen.fill(black)
        pygame.draw.rect(screen, black, textRect)
        pygame.display.update()
        Player = generateTrainer()
        Comp = generateTrainer()
        Winner = Battle(Player, Comp)
        if Winner==Player:
            screen.fill(black)
            label = testfont.render("You Won!!!", 0, green)
            screen.blit(label, (centreX, centreY))
            pygame.display.update()
            pygame.time.wait(Wait)
            tempRounds+=1
        else:
            screen.fill(black)
            label = testfont.render("You Lost.", 0, green)
            screen.blit(label, (centreX, centreY))
            pygame.display.update()
            pygame.time.wait(Wait)
            screen.fill(black)
            label = testfont.render("You Suck.", 0, green)
            screen.blit(label, (centreX, centreY))
            pygame.display.update()
            pygame.time.wait(Wait)
            pygame.mixer.music.stop()
            pygame.quit()
            sys.exit()
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.mixer.music.stop()
                pygame.quit()
                sys.exit()
        if tempRounds==4:
            screen.fill(black)
            label = testfont.render("You are the Ultimate Pokemon Champion!!!", 0, green)
            screen.blit(label, (centreX, centreY))
            pygame.display.update()
            pygame.time.wait(Wait)
            pygame.mixer.music.stop()
            pygame.quit()
            sys.exit()            
        pygame.display.update()
        clock.tick(FPS)

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
            screen.fill(black)
            screen.blit(activePokemon1.Back, (PlayerX, PlayerY))
            screen.blit(activePokemon2.Front, (CompX, CompY))
            label = testfont.render("What will " + activePokemon1.Name + " do?", 0, green)
            screen.blit(label, (MessageX, MessageY))
            displayHPbar(activePokemon1, 1)
            displayHPbar(activePokemon2, 0)
            pygame.display.update()
            choice = 0
            condition = True
            while condition == True:
                label = testfont.render("Fight", 0, white)
                screen.blit(label, (button1X, button1Y))
                label = testfont.render("Switch", 0, white)
                screen.blit(label, (button2X, button2Y))
                mouseX, mouseY = pygame.mouse.get_pos()
                if mouseX>=button1X and mouseX<=button1XR and mouseY>=button1Y and mouseY<=button1YD:
                    label = testfont.render("Fight", 0, red)
                    screen.blit(label, (button1X, button1Y))
                elif mouseX>=button2X and mouseX<=button2XR and mouseY>=button2Y and mouseY<=button2YD:
                    label = testfont.render("Switch", 0, red)
                    screen.blit(label, (button2X, button2Y))
                for event in pygame.event.get():
                    if event.type==MOUSEBUTTONDOWN:
                        if mouseX>=button1X and mouseX<=button1XR and mouseY>=button1Y and mouseY<=button1YD:
                            condition = False
                            break
                        elif mouseX>=button2X and mouseX<=button2XR and mouseY>=button2Y and mouseY<=button2YD:
                            choice = "Switch"
                            condition = False
                            break
                pygame.display.update()
                clock.tick(FPS)
            if choice!="Switch":
                condition = True
                pygame.draw.rect(screen, black, moveRect)
            while condition == True:
                label = testfont.render(activePokemon1.MoveSet[0], 0, white)
                screen.blit(label, (button1X, button1Y))
                label = testfont.render(activePokemon1.MoveSet[1], 0, white)
                screen.blit(label, (button2X, button2Y))
                label = testfont.render(activePokemon1.MoveSet[2], 0, white)
                screen.blit(label, (button3X, button3Y))
                label = testfont.render(activePokemon1.MoveSet[3], 0, white)
                screen.blit(label, (button4X, button4Y))
                mouseX, mouseY = pygame.mouse.get_pos()
                if mouseX>=button1X and mouseX<=button1XR and mouseY>=button1Y and mouseY<=button1YD:
                    label = testfont.render(activePokemon1.MoveSet[0], 0, red)
                    screen.blit(label, (button1X, button1Y))
                elif mouseX>=button2X and mouseX<=button2XR and mouseY>=button2Y and mouseY<=button2YD:
                    label = testfont.render(activePokemon1.MoveSet[1], 0, red)
                    screen.blit(label, (button2X, button2Y))
                elif mouseX>=button3X and mouseX<=button3XR and mouseY>=button3Y and mouseY<=button3YD:
                    label = testfont.render(activePokemon1.MoveSet[2], 0, red)
                    screen.blit(label, (button3X, button3Y))
                elif mouseX>=button4X and mouseX<=button4XR and mouseY>=button4Y and mouseY<=button4YD:
                    label = testfont.render(activePokemon1.MoveSet[3], 0, red)
                    screen.blit(label, (button4X, button4Y))
                for event in pygame.event.get():
                    if event.type == KEYDOWN:
                        if event.key == K_q:
                            choice = 0
                            pygame.draw.rect(screen, black, moveRect)
                            condition = False
                            break
                        elif event.key == K_w:
                            choice = 1
                            pygame.draw.rect(screen, black, moveRect)
                            condition = False
                            break
                        elif event.key == K_e:
                            choice = 2
                            pygame.draw.rect(screen, black, moveRect)
                            condition = False
                            break
                        elif event.key == K_r:
                            choice = 3
                            pygame.draw.rect(screen, black, moveRect)
                            condition = False
                            break
                        elif event.key == K_s:
                            choice = "Switch"
                            pygame.draw.rect(screen, black, moveRect)
                            condition = False
                            break
                    elif event.type==MOUSEBUTTONDOWN:
                        if mouseX>=button1X and mouseX<=button1XR and mouseY>=button1Y and mouseY<=button1YD:
                            choice = 0
                            pygame.draw.rect(screen, black, moveRect)
                            condition = False
                            break
                        elif mouseX>=button2X and mouseX<=button2XR and mouseY>=button2Y and mouseY<=button2YD:
                            choice = 1
                            pygame.draw.rect(screen, black, moveRect)
                            condition = False
                            break
                        elif mouseX>=button3X and mouseX<=button3XR and mouseY>=button3Y and mouseY<=button3YD:
                            choice = 2
                            pygame.draw.rect(screen, black, moveRect)
                            condition = False
                            break
                        elif mouseX>=button4X and mouseX<=button4XR and mouseY>=button4Y and mouseY<=button4YD:
                            choice = 3
                            pygame.draw.rect(screen, black, moveRect)
                            condition = False
                            break
                pygame.display.update()
                clock.tick(FPS)
            if choice=="Switch":
                if len(PlayerParty)>1:
                    label = testfont.render("Which Pokemon do u want to switch to?", 0, green)
                    pygame.draw.rect(screen, black, textRect)
                    screen.fill(black)
                    screen.blit(label, (MessageX, MessageY+100))
                    pygame.display.update()
                    choice = SwitchScreen(PlayerParty)
                    condition = False
                    while condition == True:
                        for event in pygame.event.get():
                            if event.type == KEYDOWN:
                                if event.key == K_2:
                                    choice = 1
                                    condition = False
                                    break
                                elif event.key == K_3:
                                    if len(PlayerParty)>=3:
                                        choice = 2
                                        condition = False
                                        break
                                    break
                                elif event.key == K_4:
                                    if len(PlayerParty)==4:
                                        choice = 3
                                        condition = False
                                        break
                                    break
                                elif event.key == K_1:
                                    choice = 0
                                    condition = False
                                    break
                        pygame.display.update()
                        clock.tick(FPS)
                    if choice == 0:
                        continue
                    tempPokemon=activePokemon1
                    activePokemon1=PlayerParty[int(choice)]
                    PlayerParty[int(choice)]=tempPokemon
                    PlayerParty[0]=activePokemon1
                    screen.fill(black)
                    screen.blit(activePokemon1.Back, (PlayerX, PlayerY))
                    displayHPbar(activePokemon1, 1)
                    screen.blit(activePokemon2.Front, (CompX, CompY))
                    displayHPbar(activePokemon2, 0)
                    label = testfont.render("Your foe is weak. Go get him " + activePokemon1.Name + "!", 0, green)
                    screen.blit(label, (MessageX, MessageY))
                    pygame.display.update()
                    pygame.time.wait(Wait)
                    temp1=1
                    break
                else:
                    label = testfont.render("You only have one Pokemon left!", 0,green)
                    pygame.draw.rect(screen, black, textRect)
                    screen.blit(label, (MessageX, MessageY))
                    pygame.display.update()
                    pygame.time.wait(Wait)
                    continue
            else:
                activePokemon1.Move=getMove(activePokemon1.MoveSet[int(choice)])
                break
        activePokemon2.Move=getMove(random.choice(activePokemon2.MoveSet))
        if temp1==0:
            FirstPokemon, SecondPokemon, num=WhoGoesFirst(activePokemon1, activePokemon2)
            tempHP = SecondPokemon.HP
            SecondPokemon.HP=int(SecondPokemon.HP)-DamageCalculator(FirstPokemon, SecondPokemon, FirstPokemon.Move)
            if SecondPokemon==activePokemon1:
                HPbarAnimation(SecondPokemon, tempHP, SecondPokemon.HP, 1)
            elif SecondPokemon==activePokemon2:
                HPbarAnimation(SecondPokemon, tempHP, SecondPokemon.HP, 0)
            if SecondPokemon.HP<=0:
                if num==1:
                    label = testfont.render(activePokemon2.Name + " fainted!", 0, green)
                    pygame.draw.rect(screen, black, textRect)
                    screen.blit(label, (MessageX, MessageY))
                    pygame.display.update()
                    pygame.time.wait(Wait)
                    ComputerParty.remove(activePokemon2)
                    continue
                else:
                    label = testfont.render(activePokemon1.Name + " fainted!", 0, green)
                    pygame.draw.rect(screen, black, textRect)
                    screen.blit(label, (MessageX, MessageY))
                    pygame.display.update()
                    pygame.time.wait(Wait)
                    PlayerParty.remove(activePokemon1)
                    if len(PlayerParty)>=1:
                        label = testfont.render("Which pokemon would you like to send out next?", 0, green)
                        pygame.draw.rect(screen, black, textRect)
                        screen.fill(black)
                        screen.blit(label, (MessageX, MessageY+100))
                        pygame.display.update()
                        choice = SwitchScreen(PlayerParty)
                        condition = False
                        while condition == True:
                            for event in pygame.event.get():
                                if event.type == KEYDOWN:
                                    if event.key == K_1:
                                        choice = 0
                                        condition = False
                                        break
                                    elif event.key == K_2:
                                        if len(PlayerParty)>=2:
                                            choice = 1
                                            condition = False
                                            break
                                        break
                                    elif event.key == K_3:
                                        if len(PlayerParty)==3:
                                            choice = 2
                                            condition = False
                                            break
                                        break
                            pygame.display.update()
                            clock.tick(FPS)
                        tempPokemon=PlayerParty[int(choice)]
                        PlayerParty[int(choice)]=PlayerParty[0]
                        PlayerParty[0]=tempPokemon
                    continue
            if num==1:
                ComputerParty[0]=SecondPokemon
            else:
                PlayerParty[0]=SecondPokemon
            tempHP = FirstPokemon.HP
            FirstPokemon.HP=int(FirstPokemon.HP)-DamageCalculator(SecondPokemon, FirstPokemon, SecondPokemon.Move)
            if FirstPokemon==activePokemon1:
                HPbarAnimation(FirstPokemon, tempHP, FirstPokemon.HP, 1)
            elif FirstPokemon==activePokemon2:
                HPbarAnimation(FirstPokemon, tempHP, FirstPokemon.HP, 0)
            if FirstPokemon.HP<=0:
                if num==1:
                    label = testfont.render(activePokemon1.Name + " fainted!", 0, green)
                    pygame.draw.rect(screen, black, textRect)
                    screen.blit(label, (MessageX, MessageY))
                    pygame.display.update()
                    pygame.time.wait(Wait)
                    PlayerParty.remove(activePokemon1)
                    if len(PlayerParty)>=1:
                        label = testfont.render("Which pokemon would you like to send out next?", 0, green)
                        pygame.draw.rect(screen, black, textRect)
                        screen.fill(black)
                        screen.blit(label, (MessageX, MessageY))
                        pygame.display.update()
                        choice = SwitchScreen(PlayerParty)
                        condition = False
                        while condition == True:
                            for event in pygame.event.get():
                                if event.type == KEYDOWN:
                                    if event.key == K_1:
                                        choice = 0
                                        condition = False
                                        break
                                    elif event.key == K_2:
                                        if len(PlayerParty)>=2:
                                            choice = 1
                                            condition = False
                                            break
                                        break
                                    elif event.key == K_3:
                                        if len(PlayerParty)==3:
                                            choice = 2
                                            condition = False
                                            break
                                        break
                            pygame.display.update()
                            clock.tick(FPS)
                        tempPokemon=PlayerParty[int(choice)]
                        PlayerParty[int(choice)]=PlayerParty[0]
                        PlayerParty[0]=tempPokemon
                    continue
                else:
                    label = testfont.render(activePokemon2.Name + " fainted!", 0, green)
                    pygame.draw.rect(screen, black, textRect)
                    screen.blit (label, (MessageX, MessageY))
                    pygame.display.update()
                    pygame.time.wait(Wait)
                    ComputerParty.remove(activePokemon2)
                    continue
            if num==1:
                PlayerParty[0]=FirstPokemon
            else:
                ComputerParty[0]=FirstPokemon
        else:
            FirstPokemon, SecondPokemon=activePokemon2, activePokemon1
            tempHP = SecondPokemon.HP
            SecondPokemon.HP=int(SecondPokemon.HP)-DamageCalculator(FirstPokemon, SecondPokemon, FirstPokemon.Move)
            HPbarAnimation(SecondPokemon, tempHP, SecondPokemon.HP, 1)
            if SecondPokemon.HP<=0:
                label = testfont.render(activePokemon1.Name + " fainted!", 0, green)
                pygame.draw.rect(screen, black, textRect)
                screen.blit(label, (MessageX, MessageY))
                pygame.display.update()
                pygame.time.wait(Wait)
                PlayerParty.remove(activePokemon1)
                if len(PlayerParty)>=1:
                    label = testfont.render("Which pokemon would you like to send out next?", 0, green)
                    pygame.draw.rect(screen, black, textRect)
                    screen.fill(black)
                    screen.blit(label, (MessageX, MessageY))
                    pygame.display.update()
                    choice = SwitchScreen(PlayerParty)
                    condition = False
                    while condition == True:
                        for event in pygame.event.get():
                            if event.type == KEYDOWN:
                                if event.key == K_1:
                                    choice = 0
                                    condition = False
                                    break
                                elif event.key == K_2:
                                    if len(PlayerParty)>=2:
                                        choice = 1
                                        condition = False
                                        break
                                    break
                                elif event.key == K_3:
                                    if len(PlayerParty) == 3:
                                        choice = 2
                                        condition = False
                                        break
                                    break
                        pygame.display.update()
                        clock.tick(FPS)
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
    label = testfont.render(Attacker.Name + " used " + Move.Name + "!", 1, green)
    pygame.draw.rect(screen, black, textRect)
    screen.blit(label, (MessageX, MessageY))
    pygame.display.update()
    pygame.time.wait(Wait)
    RandomNumber = random.random() * 100
    if RandomNumber<=100 - int(Move.Accuracy):
        label = testfont.render(Attacker.Name + " missed!", 1, green)
        pygame.draw.rect(screen, black, textRect)
        screen.blit(label, (MessageX, MessageY))
        pygame.display.update()
        pygame.time.wait(Wait)
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
        hitSound.play()
        pygame.time.wait(Wait)
        damage = criticalHit(damage)
    if effect==0:
        label = testfont.render("It does not affect " + Defender.Name + "!", 0, green)
        pygame.draw.rect(screen, black, textRect)
        screen.blit(label, (MessageX, MessageY))
        pygame.display.update()
        pygame.time.wait(Wait)
    elif effect > 1:
        label = testfont.render("It's supereffective!", 0, green)
        pygame.draw.rect(screen, black, textRect)
        screen.blit(label, (MessageX, MessageY))
        pygame.display.update()
        pygame.time.wait(Wait)
    elif effect < 1:
        label = testfont.render("It's not very effective.", 0, green)
        pygame.draw.rect(screen, black, textRect)
        screen.blit(label, (MessageX, MessageY))
        pygame.display.update()
        pygame.time.wait(Wait)
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
        label = testfont.render("A critical hit!", 0, green)
        pygame.draw.rect(screen, black, textRect)
        screen.blit(label, (MessageX, MessageY))
        pygame.display.update()
        pygame.time.wait(Wait)
        return damage * 2
    return damage

def getMove(string):
    for i in range(0,len(MoveObjects)):
        if string==MoveObjects[i].Name:
            return MoveObjects[i]
    return ("There is no such move as " + string + ".")

def generatePokemon():
    randomPokemonName = random.choice(PokemonNames)
    front = pygame.image.load(randomPokemonName + 'F.png')
    back = pygame.image.load(randomPokemonName + 'B.png')
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
            randomPokemon = Pokemon(PokemonStats[i], PokemonStats[i+1], PokemonStats[i+2], PokemonStats[i+3], PokemonStats[i+4], PokemonStats[i+5], PokemonStats[i+6], PokemonStats[i+7], PokemonStats[i+8], randomPokemonMovepool, front, back)
            return randomPokemon

def generateTrainer():
    PartyPokemon=[]
    for i in range(0,4):
        PartyPokemon.append(generatePokemon())
    Names = ["Parimal", "Adithya", "Taimour", "Adnan"]
    RandomTrainer = Trainer(random.choice(Names), PartyPokemon)
    return RandomTrainer

def HPbarAnimation(Monster, Initial, Final, Who):
    start = (int(Initial)/int(Monster.OriginalHP))*100
    startLen = math.floor((start/100)*lenHPbar)
    end = (int(Final)/int(Monster.OriginalHP))*100
    endLen = math.floor((end/100)*lenHPbar)
    if Who==0:
        while True:
            pygame.draw.rect(screen, black, (CompHPX, CompHPY, lenHPbar, depthHPbar))
            if startLen>=(lenHPbar/2):
                pygame.draw.rect(screen, green, (CompHPX, CompHPY, startLen, depthHPbar))
            elif startLen==0:
                pygame.display.update()
                return None
            elif startLen<(lenHPbar/4):
                pygame.draw.rect(screen, red, (CompHPX, CompHPY, startLen, depthHPbar))
            elif startLen>=(lenHPbar/4):
                pygame.draw.rect(screen, yellow, (CompHPX, CompHPY, startLen, depthHPbar))
            if startLen>endLen and startLen>0:
                startLen-=1
            else:
                pygame.display.update()
                return None
            pygame.display.update()
            clock.tick(FPS)        
    while True:
        pygame.draw.rect(screen, black, (YouHPX, YouHPY, lenHPbar, depthHPbar))
        if startLen>=(lenHPbar/2):
            pygame.draw.rect(screen, green, (YouHPX, YouHPY, startLen, depthHPbar))
        elif startLen==0:
            pygame.display.update()
            return None
        elif startLen>=(lenHPbar/4):
            pygame.draw.rect(screen, yellow, (YouHPX, YouHPY, startLen, depthHPbar))
        elif startLen<(lenHPbar/4):
            pygame.draw.rect(screen, red, (YouHPX, YouHPY, startLen, depthHPbar))
        if startLen>endLen and startLen>0:
            startLen-=1
        else:
            pygame.display.update()
            return None
        pygame.display.update()
        clock.tick(FPS)

def displayHPbar(Monster, Who):
    percentage = (int(Monster.HP)/int(Monster.OriginalHP))*100
    length = (percentage/100)*lenHPbar
    if Who==0:
        pygame.draw.rect(screen, black, (CompHPX, CompHPY, lenHPbar, depthHPbar))
        if length>=(lenHPbar/2):
            pygame.draw.rect(screen, green, (CompHPX, CompHPY, length, depthHPbar))
        elif length>=(lenHPbar/4):
            pygame.draw.rect(screen, yellow, (CompHPX, CompHPY, length, depthHPbar))
        elif length<(lenHPbar/4):
            pygame.draw.rect(screen, red, (CompHPX, CompHPY, length, depthHPbar))
        pygame.display.update()
        return None
    elif Who==5:
        pygame.draw.rect(screen, black, (Poke1BarX, Poke1BarY, lenHPbar, depthHPbar))
        if length>=(lenHPbar/2):
            pygame.draw.rect(screen, green, (Poke1BarX, Poke1BarY, length, depthHPbar))
        elif length>=(lenHPbar/4):
            pygame.draw.rect(screen, yellow, (Poke1BarX, Poke1BarY, length, depthHPbar))
        elif length<(lenHPbar/4):
            pygame.draw.rect(screen, red, (Poke1BarX, Poke1BarY, length, depthHPbar))
        pygame.display.update()
        return None
    elif Who==6:
        pygame.draw.rect(screen, black, (Poke2BarX, Poke2BarY, lenHPbar, depthHPbar))
        if length>=(lenHPbar/2):
            pygame.draw.rect(screen, green, (Poke2BarX, Poke2BarY, length, depthHPbar))
        elif length>=(lenHPbar/4):
            pygame.draw.rect(screen, yellow, (Poke2BarX, Poke2BarY, length, depthHPbar))
        elif length<(lenHPbar/4):
            pygame.draw.rect(screen, red, (Poke2BarX, Poke2BarY, length, depthHPbar))
        pygame.display.update()
        return None
    elif Who==7:
        pygame.draw.rect(screen, black, (Poke3BarX, Poke3BarY, lenHPbar, depthHPbar))
        if length>=(lenHPbar/2):
            pygame.draw.rect(screen, green, (Poke3BarX, Poke3BarY, length, depthHPbar))
        elif length>=(lenHPbar/4):
            pygame.draw.rect(screen, yellow, (Poke3BarX, Poke3BarY, length, depthHPbar))
        elif length<(lenHPbar/4):
            pygame.draw.rect(screen, red, (Poke3BarX, Poke3BarY, length, depthHPbar))
        pygame.display.update()
        return None
    elif Who==8:
        pygame.draw.rect(screen, black, (Poke4BarX, Poke4BarY, lenHPbar, depthHPbar))
        if length>=(lenHPbar/2):
            pygame.draw.rect(screen, green, (Poke4BarX, Poke4BarY, length, depthHPbar))
        elif length>=(lenHPbar/4):
            pygame.draw.rect(screen, yellow, (Poke4BarX, Poke4BarY, length, depthHPbar))
        elif length<(lenHPbar/4):
            pygame.draw.rect(screen, red, (Poke4BarX, Poke4BarY, length, depthHPbar))
        pygame.display.update()
        return None
    pygame.draw.rect(screen, black, (YouHPX, YouHPY, lenHPbar, depthHPbar))
    if length>=(lenHPbar/2):
        pygame.draw.rect(screen, green, (YouHPX, YouHPY, length, depthHPbar))
    elif length>=(lenHPbar/4):
        pygame.draw.rect(screen, yellow, (YouHPX, YouHPY, length, depthHPbar))
    elif length<(lenHPbar/4):
        pygame.draw.rect(screen, red, (YouHPX, YouHPY, length, depthHPbar))
    pygame.display.update()    
    return None

def SwitchScreen(PlayerParty):
    while True:
        pygame.draw.rect(screen, black, (0, 0, 600, 320))
        screen.blit(PlayerParty[0].Front, (Poke1X, Poke1Y))
        displayHPbar(PlayerParty[0], 5)
        if len(PlayerParty)>=2:
            screen.blit(PlayerParty[1].Front, (Poke2X, Poke2Y))
            displayHPbar(PlayerParty[1], 6)
        if len(PlayerParty)>=3:
            screen.blit(PlayerParty[2].Front, (Poke3X, Poke3Y))
            displayHPbar(PlayerParty[2], 7)
        if len(PlayerParty)==4:
            screen.blit(PlayerParty[3].Front, (Poke4X, Poke4Y))
            displayHPbar(PlayerParty[3], 8)
        mouseX, mouseY = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type==MOUSEBUTTONDOWN:
                if mouseX>=0 and mouseX<300 and mouseY>=0 and mouseY<150:
                    return 0
                elif mouseX>=300 and mouseX<600 and mouseY>=0 and mouseY<150 and len(PlayerParty)>=2:
                    return 1
                elif mouseX>=0 and mouseX<300 and mouseY>=150 and mouseY<300 and len(PlayerParty)>=3:
                    return 2
                elif mouseX>=300 and mouseX<600 and mouseY>=150 and mouseY<300 and len(PlayerParty)==4:
                    return 3
        pygame.display.update()
        clock.tick(FPS/3)

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

if __name__ == "__main__":
    mainGame()