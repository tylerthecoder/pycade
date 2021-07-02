from time import sleep
import pygame
from games.snake.main import SnakeGame
from screens.titleScreen import TitleScreen
from controllers.KeyboardController import KeyboardController
from controllers.JoystickController import JoystickController
from utils.colors import YELLOW

SCREEN_SIZE = (400, 400)
SPEED = 1

screens = []


# define a main function
def main():
    pos = (20, 20)

    # initialize the pygame module
    pygame.init()
    pygame.display.set_caption("PYCADE")

    # create a surface on screen
    screen = pygame.display.set_mode(SCREEN_SIZE)

    # define a variable to control the main loop
    running = True

    controller = JoystickController()
    morseGame = SnakeGame(SCREEN_SIZE, screen)

    frameCount = 0
    lastActions = set()

    # main loop
    while running:

        frameCount += 1

        actions = controller.getActions()
        morseGame.setActions(actions)

        shouldUpdateScreen = morseGame.update(frameCount)

        if shouldUpdateScreen:
            screen.fill(YELLOW)
            morseGame.draw()
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
