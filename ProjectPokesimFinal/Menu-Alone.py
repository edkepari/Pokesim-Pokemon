import pygame, math, sys
 
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
            return (0, 255, 125)
        else:
            return (100, 100, 100)
        
    def set_rect(self):
        self.set_rend()
        self.rect = self.rend.get_rect()
        self.rect.topleft = self.pos
 
pygame.init()

screen = pygame.display.set_mode((600, 400))
menu_font = pygame.font.Font(None, 25)
menuFinal = pygame.image.load('MainMenuFinal.png').convert_alpha()
options = [Option("NEW GAME", (250,150)), Option("Quit", (280, 200))]
switch = menuFinal
a= 1

screens= True
menuButtons= True

if a == 1:
    screens = True
def Main_Menu():
    while True:
            #Initial
        pygame.event.pump()
        if a == 1:
            screen.blit(switch, (0,0))
    
        for option in options:
            if option.rect.collidepoint(pygame.mouse.get_pos()):
                option.hovered = True
            else:
                option.hovered = False
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
                        #if mouseX >= 250 and mouseX <= 350:
                            #if mouseY >= 150 and mouseY <= 165:
                                #buttonChange = blank
                                #switch = mainMap
                                #characters = True          
                                #front = True
                                #walk = 'start'
                                #menuButtons = False
                    if mouseX >= 280 and mouseX <= 320:
                        if mouseY >= 200 and mouseY <= 215: 
                            pygame.quit()
                            sys.exit()            
        pygame.display.update()
         