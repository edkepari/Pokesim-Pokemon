#Imports
import pygame, math, sys
from pygame.locals import *

#Initialization
pygame.init()
screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption('PokeSim')

#Button Class
class Option:
 
    hovered = False
    
    def __init__(self, text, pos):
        self.text = text
        self.pos = pos
        self.set_rect()
        self.draw()
            
    def draw(self):
        self.set_rend()
        screen.blit(self.rend, self.rect)
        
    def set_rend(self):
        self.rend = menu_font.render(self.text, True, self.get_color())
        
    def get_color(self):
        if self.hovered:
            return (255, 0, 0)
        else:
            return (0, 0, 0)
        
    def set_rect(self):
        self.set_rend()
        self.rect = self.rend.get_rect()
        self.rect.topleft = self.pos
        
#MenuButtons
menu_font = pygame.font.Font(None, 25)
options = [Option("NEW GAME", (250,150)), Option("Quit", (280, 200))]
#BattleButtons
battleOptions = [Option("Fight", (320,310)), Option("Switch", (460,310))]
#FightButtons
fightOptions = [Option("Attack 1", (320,310)), Option("Attack 2", (460,310)), Option("Attack 3", (320,350)), Option("Attack 4", (460,350))]
#PokemonButtons
pokemonOptions = [Option("pokemon 1", (223,56)), Option("pokemon 2", (406,56)), Option("pokemon 3", (223,167)), Option("pokemon 4", (406,167))]


#Maps
menuFinal = pygame.image.load('MainMenuFinal.png').convert_alpha()
mainMap = pygame.image.load('FinalMap.png').convert_alpha()
arena = pygame.image.load('battleImage2.png').convert_alpha()
pokemonSwitch = pygame.image.load('pokebag2.png').convert_alpha()
switch = menuFinal

#Buttons
blank = []
buttonChange = options
menuButtons = True
actionButtons = False
attackButtons = False
pokemonButtons = False
actionChange = blank
fightChange = blank
pokemonChange = blank


#Character Sprites
#walk
char1_walk = pygame.image.load('char1_walk.png').convert_alpha()
char1_stop = pygame.image.load('char1_stop.png').convert_alpha()
char2_walk = pygame.image.load('char2_walk.png').convert_alpha()
char2_stop = pygame.image.load('char2_stop.png').convert_alpha()
#walk back
char1_back = pygame.image.load('char1_back.png').convert_alpha()
char1_back2 = pygame.image.load('char1_back2.png').convert_alpha()
char2_back = pygame.image.load('char2_back.png').convert_alpha()
char2_back2 = pygame.image.load('char2_back2.png').convert_alpha()
#stand still
char1_still = pygame.image.load('char1_front.png').convert_alpha()
char2_still = pygame.image.load('char2_front.png').convert_alpha()

#Sprite Initial
char1_switch = char1_still
char2_switch = char2_still
char1_x, char1_y = 15, 220
char2_x, char2_y = 550, 220
front = None
walk = ''

#Screen and Character Initial
screens = True
characters = False

#Transition Initial
switch_x, switch_y = 0, 401
change = False
direction = ''
colour = 0

#Timer
timer_event = pygame.USEREVENT + 1
pygame.time.set_timer(timer_event, 100)

#GAME!
while True:
    
    #Initial
    pygame.event.pump()
    #Screens
    if screens == True:
        screen.blit(switch, (0,0))
    #Characters
    if characters == True:
        pygame.time.delay(100)
        screen.blit(char1_switch, (char1_x, char1_y))
        screen.blit(char2_switch, (char2_x, char2_y))
    #Transition
    if change == True:    
        screen.blit(switch, (switch_x, switch_y))
        if colour == 0:
            direction = 'up'        
        if direction == 'up':
            switch_x += 10
            colour += 10
            if colour == 150:
                direction = 'down'
        elif direction == 'down':
            colour -= 10        
        if switch_x == 500:
            change = False
            switch = arena
            screens = True
            actionChange = battleOptions
            actionButtons = True
        pygame.time.delay(30)
        screen.fill((colour,colour,colour))    
        
    #Menu Options
    for option in buttonChange:
        if option.rect.collidepoint(pygame.mouse.get_pos()):
            option.hovered = True
        else:
            option.hovered = False
            pygame.quit
            sys.exit
        option.draw()    
        
    #Battle Options
    for option in actionChange:
        if option.rect.collidepoint(pygame.mouse.get_pos()):
            option.hovered = True
        else:
            option.hovered = False
            pygame.quit
            sys.exit
        option.draw()      
        
    #Fight Options
    for option in fightChange:
        if option.rect.collidepoint(pygame.mouse.get_pos()):
            option.hovered = True
        else:
            option.hovered = False
            pygame.quit
            sys.exit
        option.draw()  
        
    #Pokemon Switch Options
    for option in pokemonChange:
        if option.rect.collidepoint(pygame.mouse.get_pos()):
            option.hovered = True
        else:
            option.hovered = False
            pygame.quit
            sys.exit
        option.draw()     
        
        
        
    #Events
    mouseX, mouseY = 0,0
    for event in pygame.event.get():
        
        #Click Events
        if event.type == pygame.MOUSEBUTTONDOWN:
            (mouseX, mouseY) = pygame.mouse.get_pos()
            print (mouseX)
            print (mouseY)
        #Menu buttons
        if menuButtons == True:
            if mouseX >= 250 and mouseX <= 350:
                if mouseY >= 150 and mouseY <= 165:
                    buttonChange = blank
                    switch = mainMap
                    characters = True          
                    front = True
                    walk = 'start'
                    menuButtons = False
            if mouseX >= 280 and mouseX <= 320:
                if mouseY >= 200 and mouseY <= 215: 
                    pygame.quit()
                    sys.exit()            
        #Action buttons
        if actionButtons == True:
            if mouseX >= 320 and mouseX <= 455:
                if mouseY >= 305 and mouseY <= 340:
                    actionChange = blank
                    actionButtons = False
                    fightChange = fightOptions
                    attackButtons = True
                    break
            if mouseX >= 460 and mouseX <= 590:
                if mouseY >= 305 and mouseY <= 340:
                    switch = pokemonSwitch
                    pokemonChange = pokemonOptions
                    pokemonButtons = True
                    actionChange = blank
        #Attack buttons
        if attackButtons == True:
            if mouseX >= 320 and mouseX <= 455:
                if mouseY >= 310 and mouseY <= 340:
                    print('attack 1!')
            if mouseX >= 460 and mouseX <= 590:
                if mouseY >= 310 and mouseY <= 340:
                    print('attack 2!')
            if mouseX >= 320 and mouseX <= 455:
                if mouseY >= 350 and mouseY <= 390:
                    print('attack 3!')
            if mouseX >= 460 and mouseX <= 590:
                if mouseY >= 350 and mouseY <= 390:            
                    print('attack 4!')
                    
        if pokemonButtons == True:
            if mouseX >= 223 and mouseX <= 392:
                if mouseY >= 56 and mouseY <= 154:
                    print('pokemon 1!')
            if mouseX >= 406 and mouseX <= 572:
                if mouseY >= 56 and mouseY <= 154:
                    print('pokemon 2!')
            if mouseX >= 223 and mouseX <= 392:
                if mouseY >= 167 and mouseY <= 262:
                    print('pokemon 3!')
            if mouseX >= 406 and mouseX <= 572:
                if mouseY >= 167 and mouseY <= 262:            
                    print('pokemon 4!')        
                
        #Key Events
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
            if event.key == K_SPACE: # - use spacebar until battle system is put in - #
                actionChange = blank
                fightChange = blank
                front = False
                characters = True
                walk = 'back'
                char1_x, char1_y = 150, 220
                char2_x, char2_y = 410, 220
                switch = mainMap
            if event.key == K_m:
                walk = 'start'
                
        #Timer Events
        elif event.type == timer_event:
            
            if walk == 'start':
                front = True
                char1_x += 5
                char2_x -= 5
                if char1_x > 150:
                    characters = False
                    change = True
                    walk = 'stop'
            elif walk == 'back':
                char1_x -= 5
                char2_x += 5
                if char1_x < 15:
                    walk = 'stop'
                    front = None
                    char1_switch = char1_still
                    char2_switch = char2_still                    
            elif walk == 'stop':
                char1_x += 0
                char2_x -= 0
                
            #Sprite Animation
            if front == True:
                if char1_x % 10 == 0:
                    char1_switch = char1_stop
                else:
                    char1_switch = char1_walk
                if char2_x % 10 == 0:
                    char2_switch = char2_stop
                else: 
                    char2_switch = char2_walk
            elif front == False:
                if char1_x % 10 == 0:
                    char1_switch = char1_back
                else:
                    char1_switch = char1_back2
                if char2_x % 10 == 0:
                    char2_switch = char2_back
                else: 
                    char2_switch = char2_back2
                    
            #Update and Exit
            if event.type == QUIT:
                pygame.quit()
                sys.exit()        
                
        pygame.display.update()
