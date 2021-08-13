import pygame
from utils.actions import Action
from controllers.BaseController import BaseController
from  typing import Optional

class KeyboardController(BaseController):

	def __init__(self):
		self.currentKeys = set()

	def getActionFromKey(self, key: int) -> Optional[Action]:
		if key == pygame.K_w or key == pygame.K_UP:
			return Action.UP
		if key == pygame.K_d or key== pygame.K_RIGHT:
			return Action.RIGHT
		if key == pygame.K_a or key== pygame.K_LEFT:
			return Action.LEFT
		if key == pygame.K_s or key == pygame.K_DOWN:
			return Action.DOWN
		if key == pygame.K_SPACE:
			return Action.BUTTON_1
		if key == pygame.K_LALT:
			return Action.BUTTON_2

		# Wasd for player two (ijkl)
		if key == pygame.K_j:
			return Action.LEFT_P2
		if key == pygame.K_k:
			return Action.DOWN_P2
		if key == pygame.K_l:
			return Action.RIGHT_P2
		if key == pygame.K_i:
			return Action.UP_P2
		if key == pygame.K_RETURN:
			return Action.BUTTON_1_P2

		if key == pygame.K_ESCAPE:
			return Action.MENU

	def getActions(self):
		for event in pygame.event.get((pygame.KEYDOWN, pygame.KEYUP)):
			if event.type == pygame.KEYDOWN:
				self.currentKeys.add(event.key)
			if event.type == pygame.KEYUP:
				self.currentKeys.remove(event.key)

		return set(map(self.getActionFromKey, self.currentKeys))







