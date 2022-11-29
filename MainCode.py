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
x = 500
y = 300
width = 40
height = 40
vel = 20
clock = pygame.time.Clock()
#Testing
#rectangle= pygame.Rect(x,y,width,height)
rectangle= pygame.Rect(0,400,40,40)
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
    rectangle.x += (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * vel
    #rectangle.y += (keys[pygame.K_DOWN] - keys[pygame.K_UP]) * vel
        
    rectangle.centerx = rectangle.centerx % screen.get_width()
    rectangle.centery = rectangle.centery % screen.get_height()
        
        #"""if keys[pygame.K_LEFT] and x > 0:
         #   x -= 20
                    #pygame.time.delay(20)
        #if keys[pygame.K_RIGHT] and x< 1500 - width:
         #   x += 20
        #if keys[pygame.K_UP] and y > 0:
         #   y -= 20
        #if keys[pygame.K_DOWN] and y<800-height:
         #   y += 20
          #  """
    screen.fill("BLACK")
        #pygame.draw.rect(screen, "BLUE", (x,y, width, height))
    pygame.draw.rect(screen, (255, 0, 0), rectangle)
        #pygame.display.update()
    pygame.display.flip()
            
