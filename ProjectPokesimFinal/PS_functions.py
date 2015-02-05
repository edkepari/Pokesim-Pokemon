

#Sprite Initial
char1_switch = char1_still
char2_switch = char2_still
char1_x, char1_y = 15, 220
char2_x, char2_y = 550, 220  
def sprite_movement():  
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


#Sprite Initial
front = None
def Animation():
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


#Transition Initial
switch_x, switch_y = 0, 401
change = False
direction = ''
colour = 0
def transition():
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

