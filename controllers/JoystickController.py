import pygame
from utils.actions import Action
from controllers.BaseController import BaseController

class JoystickController(BaseController):

	def __init__(self):
		self.joystick = pygame.joystick.Joystick(0)
		self.joystick2 = pygame.joystick.Joystick(1)
		self.p1b1 = self.joystick.get_button(0)
		self.p1b2 = self.joystick.get_button(1)
		self.p2b1 = self.joystick2.get_button(0)
		self.p2b2 = self.joystick2.get_button(1)
		self.joystick.init()
		self.joystick2.init()

	def getActions(self):

		pygame.event.pump()

		LR1 = self.joystick.get_axis(0)
		UD1 = self.joystick.get_axis(1)
		LR2 = self.joystick2.get_axis(0)
		UD2 = self.joystick2.get_axis(1)

		P1B1 = self.joystick.get_button(0)
		P1B2 = self.joystick.get_button(1)
		P2B1 = self.joystick2.get_button(0)
		P2B2 = self.joystick2.get_button(1)

		print(P1B1, P1B2, P2B1, P2B2, self.joystick.get_numbuttons())

		actions = set()
		if LR1 >= .9:
			actions.add(Action.LEFT)
		if LR1 <= -.9:
			actions.add(Action.RIGHT)
		if UD1 >= .9:
			actions.add(Action.UP)
		if UD1 <= -.9:
			actions.add(Action.DOWN)
		if P1B1 == 1:
			actions.add(Action.BUTTON_1)
		if P1B2 == 1:
			actions.add(Action.BUTTON_2)

		if LR2 >= .9:
			actions.add(Action.LEFT_P2)
		if LR2 <= -.9:
			actions.add(Action.RIGHT_P2)
		if UD2 >= .9:
			actions.add(Action.UP_P2)
		if UD2 <= -.9:
			actions.add(Action.DOWN_P2)
		if P2B1 == 1:
			actions.add(Action.BUTTON_1_P2)
		if P2B2 == 1:
			actions.add(Action.BUTTON_2_P2)

		return actions



