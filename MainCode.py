"""from tkinter import *

Window = Tk()
Window.title("CreativeName")
Window.configure(width=1000, height=600, bg = "lightgray")
window.mainloop()
"""
import pygame, sys
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
#x = 500
#y = 300
width = 330
height = 330
vel = 20
clock = pygame.time.Clock()
hitstun = 500
inf = True
Lockout = False
#Testing
#Characters should be made on a 330 x 330 canvas
#rectangle= pygame.Rect(x,y,width,height)
rectangle= pygame.Rect(0,400,40,40)
Fighter1 = pygame.image.load("1.png")
Stage = pygame.image.load("Stage.png")
Fighter1 = pygame.Surface.convert_alpha(Fighter1)

#rectangle= pygame.Rect(500,300,200,300)
#                       x  y     width  height
#pygame.draw.rect(screen, "BLACK", rectangle)

run = True
while run:
    #pygame.time.delay(10)
    clock.tick(60)
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

        
    if keys[pygame.K_LEFT] and x > 0 and Lockout == False:
        x -= 5
        
    if keys[pygame.K_RIGHT] and x< 1500 - width and Lockout == False:
        x += 5
    if keys[pygame.K_UP] and y > 0 and Lockout == False:
        #y -= 5 Disabled for jumping code
        #Jumping is locked
        pass
    if keys[pygame.K_DOWN] and y<800-height and Lockout == False:
        #y += 5 He shouldn't go down beyond this y coord
        #instead show image of your character crouching
        screen.blit(pygame.image.load(("2.png")), (x,y))
        Lockout = True
        pygame.time.delay(100)
        Lockout = False
        pygame.display.flip()

        

        #inf = True
          
    #screen.fill("BLACK")
    screen.blit(Stage, (0,0))
    screen.blit(Fighter1, (x,y))
        #pygame.draw.rect(screen, "BLUE", (x,y, width, height))
    #pygame.draw.rect(screen, (255, 0, 0), rectangle)
        #pygame.display.update()
    pygame.display.flip()
            
