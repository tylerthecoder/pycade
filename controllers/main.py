import pygame
from controllers.JoystickController import JoystickController
from controllers.KeyboardController import KeyboardController

def getMainController():
	if pygame.joystick.get_count() > 0:
		return JoystickController()
	return KeyboardController()




