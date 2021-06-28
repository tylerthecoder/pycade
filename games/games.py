from abc import ABC, abstractmethod
import pygame
from utils.vector import Vector
from utils.actions import Action
from typing import Set

class PycadeGame(ABC):

	def __init__(self, windowSize, surface):
		self.surface = surface
		self.windowSize = windowSize
		self.lastActions = set()
		self.newActions = set()


	@abstractmethod
	def update(self, frameCount):
		pass

	@abstractmethod
	def draw(self):
		pass


	def drawCircle(self):
		pass

	def setActions(self, actions: Set[Action]):
		self.newActions = self.lastActions - actions
		self.lastActions = actions

	def drawRect(self, color, pos: Vector, size: Vector, thickness: int):
		pygame.draw.rect(
			self.surface,
			color,
			pygame.Rect(pos.x, pos.y, size.x, size.y),
			thickness
		)