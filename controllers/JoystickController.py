import pygame
from utils.actions import Action
from controllers.BaseController import BaseController

class JoystickController(BaseController):

	def __init__(self):
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



