import pygame, sys
#Center is at 165
#nuetral attacks should have a range of 170 (5)
#Forward and back should be around 180 (15)
hitbox = pygame.Rect(0,0,70,70)
Dmg = False
def Atk(Dir, x, y, foe, foex, foey):
    hit = foe.get_rect(center = (foex ,foey))
    if Dir == "Left":
        print("Attacking left")
        pygame.time.delay(100)
        hitbox.x = x - 20
        hitbox.y = y
        if hitbox.colliderect(hit) == True:
            print("HIT")
            Dmg = True
            return Dmg        
    elif Dir == "Nuet":
        print("Nuetral Attack")
        pygame.time.delay(100)
        hitbox.x = x + 5
        hitbox.y = y-70
    elif Dir == "Right":
        print("Attacking Right")
        pygame.time.delay(100)
        hitbox.x = x+20
        hitbox.y = y
        if hitbox.colliderect(hit) == True:
            print("HIT")
            Dmg = True
            return Dmg        
    elif Dir == "Up":
        print("Attacking up")
        pygame.time.delay(100)
        hitbox.x = x+20
        hitbox.y = y-70
    elif Dir == "Down":
        print("Crouttack")
        pygame.time.delay(100)
        hitbox.x = x + 10
        hitbox.y = 261
        #print(y)
        #print(x)
        #print(hit)
        #print(hitbox)
        if hitbox.colliderect(hit) == True:
            print("HIT")
            Dmg = True
            return Dmg 
        pygame.time.delay(100)
    

    

    
    
