#ETGG 1801
#Eli Vaudrin
#Lab04 Flow Control
#9/26/20

import random
import pygame
import time

pygame.display.init()
window = pygame.display.set_mode((700, 500))

myColors = (102, 255, 0), (102, 204, 255), (51, 255, 51), (210, 123, 211), (0,255, 255)

for num in range(0, 101):
    print(num)

x = random.randint(0, 700)
y = random.randint(0,500)

pygame.draw.circle(window, random.choice(myColors), (x, y), 100)

pygame.draw.polygon(window, random.choice(myColors), ((x, y), (x, y), (x, y), (x, y), (x, y)))

pygame.draw.rect(window, random.choice(myColors), (x, y, x, y))

pygame.draw.ellipse(window, random.choice(myColors), (x, y, x, y))

pygame.display.update()

time.sleep(5)

pygame.quit()

input("Press enter to exit the program")