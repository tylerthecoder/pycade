import pygame
from utils.actions import Action


class JoystickController:

	def __init__(self):
		pygame.joystick.init();
		self.joystick = pygame.joystick.Joystick(0)
		self.joystick.init()


	def getActions(self):
		LR = self.joystick.get_axis(0)
		UD = self.joystick.get_axis(1)

		actions = set()
		if LR >= .9:
			actions.add(Action.LEFT)
		if LR <= -.9:
			actions.add(Action.RIGHT)
		if UD >= .9:
			actions.add(Action.UP)
		if UD <= -.9:
			actions.add(Action.DOWN)

		return actions



