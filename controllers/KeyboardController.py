import pygame
from pynput.keyboard import Key, Listener
from utils.actions import Action

class KeyboardController:
	def getActionFromKey(self, key: int) -> Action:
		if key == pygame.K_w:
			return Action.UP
		if key == pygame.K_d:
			return Action.RIGHT
		if key == pygame.K_a:
			return Action.LEFT
		if key == pygame.K_s:
			return Action.DOWN
		if key == pygame.K_SPACE:
			return Action.BUTTON_1
		if key == pygame.K_ESCAPE:
			return Action.MENU


	def getActions(self):
		actions = set()

		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				action = self.getActionFromKey(event.key)
				actions.add(action)

		return actions







