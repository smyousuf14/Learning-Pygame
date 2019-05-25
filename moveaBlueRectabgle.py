import pygame

#Initiate pygame
pygame.init()

#Create a display
gameDisplay = pygame.display.set_mode((500,500))
pygame.display.set_caption("A bit Racey")

clock = pygame.time.Clock()

isRunning = True

# Global Variables
RecX = 30
RecY = 30
pressedDown = False

#Main program
while isRunning:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning = False

    #Update the screen
    pygame.display.flip()

    #Draw a blue rectangle
    pygame.draw.rect(gameDisplay, (0, 128, 255), pygame.Rect(RecX,RecY,60,60))

    #Check if the right key was pressed.
    if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:

        # Move the rectangle to the right
        RecX += 2

        # Clear the screen
        gameDisplay.fill((0,0,0))

        # Update the screen
        pygame.display.flip()

        # Wait 1/60 of a second
        clock.tick(5)
