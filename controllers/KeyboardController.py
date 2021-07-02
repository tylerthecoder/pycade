import pygame
from pynput.keyboard import Key, Listener
from utils.actions import Action

class KeyboardController:
	def getActionFromKey(self, key: str):
		print(key)
		if key == "w":
			return Action.UP
		if key == "a":
			return Action.LEFT
		if key == "d":
			return Action.RIGHT
		if key == "s":
			return Action.DOWN

	def getActions(self):
		actions = set()
		events = pygame.event.get()

		for event in events:
			if event.type == pygame.KEYDOWN:
				action = self.getActionFromKey(event.key)
				actions.add(action)

		return actions







