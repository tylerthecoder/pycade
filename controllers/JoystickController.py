import pygame
from utils.actions import Action
from controllers.BaseController import BaseController

class JoystickController(BaseController):

	def __init__(self):
		pygame.joystick.Joystick(0).init()
		pygame.joystick.Joystick(1).init()

	def getActions(self):
		LR1 = pygame.joystick.Joystick(0).get_axis(0)
		UD1 = pygame.joystick.Joystick(0).get_axis(1)
		LR2 = pygame.joystick.Joystick(1).get_axis(0)
		UD2 = pygame.joystick.Joystick(1).get_axis(1)


		actions = set()
		if LR1 >= .9:
			actions.add(Action.LEFT)
		if LR1 <= -.9:
			actions.add(Action.RIGHT)
		if UD1 >= .9:
			actions.add(Action.UP)
		if UD1 <= -.9:
			actions.add(Action.DOWN)

		if LR2 >= .9:
			actions.add(Action.LEFT_P2)
		if LR2 <= -.9:
			actions.add(Action.RIGHT_P2)




		return actions



