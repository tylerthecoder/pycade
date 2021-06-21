from gpiozero import Button
import RPi.GPIO as GPIO
from time import sleep
import pygame

button = Button(17)
button2 = Button(27)

GPIO.setup(5, GPIO.OUT)
GPIO.setup(6, GPIO.OUT)


SCREEN_SIZE = (400, 400)
SPEED = 1


# while True:

    # import the pygame module, so you can use it

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

    screen.fill((255, 255, 0))
    pygame.draw.circle(screen, (255, 0, 0), pos, 20)
    pygame.display.update()

    # define a variable to control the main loop
    running = True



    # main loop
    while running:
        Up = GPIO.input(5)
        Down = GPIO.input(6)
        Right = not button.is_pressed
        Left = not button2.is_pressed

        if Left:
            pos = (pos[0] - SPEED, pos[1])
        if Right:
            pos = (pos[0] + SPEED, pos[1])
        if Up:
            pos = (pos[0], pos[1] - SPEED)
        if Down:
            pos = (pos[0], pos[1] + SPEED)

        if pos[0] < 0:
            pos = (0, pos[1])

        if pos[1] < 0:
            pos = (pos[0], 0)

        if pos[0] > SCREEN_SIZE[0]:
          pos = (SCREEN_SIZE[0], pos[1])

        if pos[1] > SCREEN_SIZE[1]:
          pos = (pos[0], SCREEN_SIZE[1])

        if Left or Right or Up or Down:
            screen.fill((255, 255, 0))
            pygame.draw.circle(screen, (255, 0, 0), pos, 20)
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
