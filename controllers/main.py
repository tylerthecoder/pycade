from config import IS_ARCADE
import pygame
from controllers.JoystickController import JoystickController
from controllers.KeyboardController import KeyboardController
from controllers.BaseController import BaseController
from controllers.ArcadeController import ArcadeController


def getMainController() -> BaseController:
	if pygame.joystick.get_count() > 0:
		return JoystickController()
	if IS_ARCADE:
		return ArcadeController()
	return KeyboardController()



