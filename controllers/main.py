import pygame
from controllers.JoystickController import JoystickController
from controllers.KeyboardController import KeyboardController
from controllers.BaseController import BaseController


def getMainController() -> BaseController:
	if pygame.joystick.get_count() > 0:
		return JoystickController()
	return KeyboardController()



