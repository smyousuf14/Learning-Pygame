import pygame

#Initiate pygame
pygame.init()

gameDisplay = pygame.display.set_mode((500,500))
pygame.display.set_caption("A bit Racey")

clock = pygame.time.Clock()

isRunning = True

#Load an image.
carImage = pygame.image.load("car.png")

#Main program
while isRunning:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning = False
