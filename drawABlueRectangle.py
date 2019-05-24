import pygame

#Initiate pygame
pygame.init()

gameDisplay = pygame.display.set_mode((500,500))
pygame.display.set_caption("A bit Racey")

clock = pygame.time.Clock()

isRunning = True

#Main program
while isRunning:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning = False

    #Update the screen
    pygame.display.flip()

    # Wait 1 / 60 of a second
    clock.tick(60)

    #Draw a blue rectangle
    pygame.draw.rect(gameDisplay, (0, 128, 255), pygame.Rect(30,30,60,60))
    
