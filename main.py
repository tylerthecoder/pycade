from time import sleep
import pygame
from games.snake.main import SnakeGame
from controllers.JoystickController import JoystickController

SCREEN_SIZE = (400, 400)
SPEED = 1


# define a main function
def main():
    pos = (20, 20)

    # initialize the pygame module
    pygame.init()
    # load and set the logo
    # logo = pygame.image.load("logo32x32.png")
    # pygame.display.set_icon(logo)
    pygame.display.set_caption("PYCADE")

    # create a surface on screen that has the size of 240 x 180
    screen = pygame.display.set_mode(SCREEN_SIZE)

    # define a variable to control the main loop
    running = True

    controller = JoystickController()

    lastActions = set()

    morseGame = SnakeGame(SCREEN_SIZE, screen)

    frameCount = 0


    # main loop
    while running:

        frameCount += 1

        actions = controller.getActions()
        morseGame.setActions(actions)

        shouldUpdateScreen = morseGame.update(frameCount)

        if shouldUpdateScreen:
            screen.fill((255, 255, 0))
            morseGame.draw(screen)
            pygame.display.update()

        # event handling, gets all event from the event queue
        for event in pygame.event.get():
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False


# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__=="__main__":
    # call the main function
    main()
