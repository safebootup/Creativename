"""from tkinter import *

Window = Tk()
Window.title("CreativeName")
Window.configure(width=1000, height=600, bg = "lightgray")
window.mainloop()
"""
def refresh(P1state, P2state):
        screen.blit(pygame.image.load((P1state)), (x,y))
        screen.blit(pygame.image.load((P2state)), (x2, y2))
        pygame.draw.rect(screen, "RED", Hurt1)
        pygame.draw.rect(screen, "RED", Hurt2)
        pygame.draw.rect(screen, "GREEN", Health1)
        pygame.draw.rect(screen, "GREEN", Health2)
    
import pygame, sys
import Attacks
#Display
background_color = ("BLUE")
screen = pygame.display.set_mode((1500, 800))
pygame.display.set_caption("CreativeName")
screen.fill(background_color)
pygame.display.flip()
#Y should be around 800 - numbers shown in stage (Its flipped for some reason)
#X should be around 250 for P1 and 1150 for p2
x = 250
y = 237
x2 = 1150
y2 = 237
#x = 500
#y = 300
width = 330
height = 330
vel = 20
clock = pygame.time.Clock()
hitstun = 500
inf = True
Lockout = False
JLock = False
Crouching = False
Lockout2 = False
Attack = Attacks
dmg = False
Health1 = pygame.Rect(0,0,500,40)
Hurt1 = pygame.Rect(0,0,500,40)
Health2 = pygame.Rect(1000,0,500,40)
Hurt2 = pygame.Rect(1000,0,500,40)
#Testing
#Characters should be made on a 330 x 330 canvas center at 165
#rectangle= pygame.Rect(x,y,width,height)
#rectangle= pygame.Rect(1150,330,40,40)
Fighter1 = pygame.image.load("P1Idle.png")
Stage = pygame.image.load("Stage.png")
Fighter1 = pygame.Surface.convert_alpha(Fighter1)
Fighter2 = pygame.image.load("P2Idle.png")
Fighter2 = pygame.Surface.convert_alpha(Fighter2)
Left = pygame.image.load("P1Dir.png")
Left2 = pygame.image.load("P2Dir.png")
#rectangle= pygame.Rect(500,300,200,300)
#                       x  y     width  height
#pygame.draw.rect(screen, "BLACK", rectangle)

run = True
while run:
    if Health2.w < 0 or Health1.w < 0:
        run = False
        pygame.time.delay(20000)
        pygame.display.quit()
    #pygame.time.delay(10)
    #clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.display.quit()
        if event.type == pygame.KEYDOWN:
            pygame.key.name(event.key)
    keys = pygame.key.get_pressed()
    #rectangle.x += (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * vel
    #rectangle.y += (keys[pygame.K_DOWN] - keys[pygame.K_UP]) * vel
        
    #rectangle.centerx = rectangle.centerx % screen.get_width()
    #rectangle.centery = rectangle.centery % screen.get_height()


    if keys[pygame.K_a] and x > 0 and Lockout == False and JLock == False:
        x -= 10
        if keys[pygame.K_c]:
            #refresh("P1Dir.png", Fighter2)
            screen.blit(pygame.transform.flip(Left, True, False), (x,y))
            screen.blit(Fighter2, (x2, y2))
            pygame.draw.rect(screen, "RED", Hurt1)
            pygame.draw.rect(screen, "RED", Hurt2)
            pygame.draw.rect(screen, "GREEN", Health1)
            pygame.draw.rect(screen, "GREEN", Health2)
            pygame.display.flip()
            dmg = Attack.Atk("Left", x, y,Fighter2, x2, y2)
            pygame.time.delay(200)
            if dmg == True:
                Health2.w -= 15
            pygame.time.delay(200)
        #refresh("P1Walk.png","P2Idle.png")
            
        
    if keys[pygame.K_d] and x< 1500 - width and Lockout == False and JLock == False:
        x += 10
        
        if keys[pygame.K_c]:
            refresh("P1Dir.png", "P2Idle.png")
            pygame.display.flip()
            dmg = Attack.Atk("Right", x, y,Fighter2, x2, y2)
            pygame.time.delay(200)
            if dmg == True:
                Health2.w -= 15
        #refresh("P1Walk.png","P2Idle.png")

            
    if keys[pygame.K_w] and y > 5 and Lockout == False:
        #y -= 5 Disabled for jumping code
        #Jumping is locked
        for i in range(10):
                if i <=5:
                        y -= 50
                        pygame.display.flip()
                        refresh("3.png" ,"P2Idle.png")
                        pygame.display.flip()
                        pygame.time.delay(100)
                else:
                        y += 50
                        refresh("3.png" ,"P2Idle.png")
                        pygame.display.flip()
                        pygame.time.delay(100)
        y = 237
        JLock = True
        jump = True

        pygame.display.flip()
    else:
        JLock = False
        jump = False
        
    if keys[pygame.K_s] and y<800-height and JLock == False:
        #y += 5 He shouldn't go down beyond this y coord
        #instead show image of your character crouching

        #screen.blit(pygame.image.load(("2.png")), (x,y))
        #screen.blit(Fighter2, (1150, 237))
        #pygame.draw.rect(screen, "GREEN", Health1)
        #pygame.draw.rect(screen, "GREEN", Health2)
        Lockout = True
        Crouching = True
        #pygame.time.delay(100)
        #Lockout = False
        if keys[pygame.K_c]:
            refresh("P1Crouttack.png", "P2Idle.png")
            pygame.display.flip()
            dmg = Attack.Atk("Down", x, y,Fighter2, x2, y2)
            pygame.time.delay(100)
            if dmg == True:
                Health2.w -= 10
        refresh("P1Crouch.png", "P2Idle.png")
        pygame.display.flip()
                
                
    else:
        Lockout = False
        Crouching = False

    dmg = False
    if keys[pygame.K_LEFT] and x2 > 0 and Lockout2 == False:
            x2 -=10
            if keys[pygame.K_m]:
                    screen.blit(pygame.transform.flip(Left2, True, False), (x2,y2))
                    screen.blit(Fighter1, (x, y))
                    pygame.draw.rect(screen, "RED", Hurt1)
                    pygame.draw.rect(screen, "RED", Hurt2)
                    pygame.draw.rect(screen, "GREEN", Health1)
                    pygame.draw.rect(screen, "GREEN", Health2)
                    pygame.display.flip()
                    dmg = Attack.Atk("Left", x2,y2, Fighter1, x, y)
                    if dmg == True:
                            Health1.w -= 10
    if keys[pygame.K_RIGHT] and x2 < 1500 - width and Lockout2 == False:
            x2 += 10
            if keys[pygame.K_m]:
                    refresh("P1Dir.png","P2Dir.png")
                    pygame.display.flip()
                    dmg = Attack.Atk("Right", x2,y2, Fighter1, x, y)
                    if dmg == True:
                            Health1.w -= 10            
    if keys[pygame.K_DOWN]:
            Lockout2 = True
            refresh("P1Crouch.png", "P2Crouch.png")
            #Crouching = True
            if keys[pygame.K_m]:
                    refresh("P1Crouttack.png", "P2Crouttack.png")
                    pygame.display.flip()
                    dmg = Attack.Atk("Down", x2,y2, Fighter1, x, y)
                    if dmg == True:
                            Health1.w -= 10
            pygame.display.flip()
    else:
            Lockout2 = False
            #Crouching = False
            
            
            
            
        #inf = True
          
    #screen.fill("BLACK")
    screen.blit(Stage, (0,0))
    if Crouching == False and jump == False  and keys[pygame.K_c] == False:
        refresh("P1Idle.png", "P2Idle.png")
        #screen.blit(Fighter1, (x,y))
        #screen.blit(Fighter2, (1150, 237))
        #pygame.draw.rect(screen, "GREEN", Health1)
        #pygame.draw.rect(screen, "GREEN", Health2)
        #pygame.draw.rect(screen, "BLUE", (x,y, width, height))
        #pygame.draw.rect(screen, (255, 0, 0), rectangle)
        #pygame.display.update()
        pygame.display.flip()
            
