from typing import Optional
import pygame
from utils.actions import Action
from controllers.BaseController import BaseController



# This file has the keymapping for my specific arcade controller.

class ArcadeController(BaseController):

	def __init__(self):
		self.currentKeys = set()

	def getActionFromKey(self, key: int) -> Optional[Action]:
		if key == pygame.K_UP:
			return Action.UP
		if key== pygame.K_RIGHT:
			return Action.RIGHT
		if key== pygame.K_LEFT:
			return Action.LEFT
		if key == pygame.K_DOWN:
			return Action.DOWN
		if key == pygame.K_LCTRL:
			return Action.BUTTON_1
		if key == pygame.K_LALT:
			return Action.BUTTON_2

		if key == pygame.K_d:
			return Action.LEFT_P2
		if key == pygame.K_f:
			return Action.DOWN_P2
		if key == pygame.K_g:
			return Action.RIGHT_P2
		if key == pygame.K_r:
			return Action.UP_P2
		if key == pygame.K_a:
			return Action.BUTTON_1_P2
		if key == pygame.K_s:
			return Action.BUTTON_2_P2

		if key == pygame.K_5:
			return Action.MENU

	def getActions(self):
		for event in pygame.event.get((pygame.KEYDOWN, pygame.KEYUP)):
			if event.type == pygame.KEYDOWN:
				self.currentKeys.add(event.key)
			if event.type == pygame.KEYUP and event.key in self.currentKeys:
				self.currentKeys.remove(event.key)

		return set(map(self.getActionFromKey, self.currentKeys))