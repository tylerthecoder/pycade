import pygame
from pynput.keyboard import Key, Listener
from utils.actions import Action

class KeyboardController:
	def getActionFromKey(self, key: int) -> Action:
		if key == pygame.K_w or key == pygame.K_UP:
			return Action.UP
		if key == pygame.K_d or key== pygame.K_RIGHT:
			return Action.RIGHT
		if key == pygame.K_a or key== pygame.K_LEFT:
			return Action.LEFT
		if key == pygame.K_s or key == pygame.K_DOWN:
			return Action.DOWN
		if key == pygame.K_SPACE or key == pygame.K_RETURN:
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







