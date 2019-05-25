import pygame

#Initiate pygame
pygame.init()

#Create a display
gameDisplay = pygame.display.set_mode((500,500))
pygame.display.set_caption("Animated Rectangle")

clock = pygame.time.Clock()

isRunning = True

# Global Variables
RecX = 30
RecY = 30
pressedDown = False

#Paint the screen.
def paint():
    gameDisplay.fill((0,0,0))
    pygame.draw.rect(gameDisplay, (0, 128, 255), pygame.Rect(RecX, RecY, 60, 60))
    pygame.display.flip()
    clock.tick(100)


#Main program
while isRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning = False

    # First paint the screen.
    paint()

    #If the right key is pressed.
    if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
        #Move to the right
        RecX += 3
        paint()

    elif event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
        #Move to the left
        RecX -= 3
        paint()

