import pygame
from controllers.main import getMainController
from gamePicker import GamePicker
from config import SCREEN_SIZE

# define a main function
def main():
    global SCREEN_SIZE

    # initialize the pygame module
    pygame.init()
    pygame.joystick.init()
    pygame.display.set_caption("PYCADE")
    pygame.mouse.set_visible(False)

    clock = pygame.time.Clock()

    running = True
    controller = getMainController()
    gameHolder = GamePicker(SCREEN_SIZE)
    frameCount = 0
    lastDrawTime = 0
    # init to true so the screen draws the initial contents
    shouldUpdateScreen = True

    print("Using Controller", controller)

    # main loop
    while running:

        # Pause for next frame
        deltaTime = clock.tick(30)
        deltaTime = 0
        totalTimeLapsed = pygame.time.get_ticks()
        frameCount += 1
        gameHolder.currentGame.setTimes(frameCount, deltaTime, totalTimeLapsed)

        # If set, can't be unset
        shouldUpdateScreen = gameHolder.currentGame.update() or shouldUpdateScreen

        timeSinceLastDraw = pygame.time.get_ticks() - lastDrawTime

        # 60 frames a second
        if timeSinceLastDraw > 1000 / 60 and shouldUpdateScreen:
            lastDrawTime = pygame.time.get_ticks()
            shouldUpdateScreen = False
            gameHolder.draw()
            # Temp fix for pi. The screen wont update on pi
            # Unless you call the update function twice
            # Still get a weird glitching effect
            pygame.display.flip()
            pygame.display.flip()

        actions = controller.getActions()
        gameHolder.currentGame.setActions(actions)


        for event in pygame.event.get((pygame.QUIT)):
            if event.type == pygame.QUIT:
                running = False


if __name__=="__main__":
    main()
