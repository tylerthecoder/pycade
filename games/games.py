from abc import ABC, abstractmethod, abstractproperty
import pygame
from utils.vector import Vector
from utils.actions import Action
from typing import Set
from utils.font import PYCADE_FONT

class PycadeGame(ABC):

	def __init__(self, windowSize, surface):
		self.surface = surface
		self.windowSize = windowSize
		self.lastActions = set()
		self.newActions = set()

	@abstractmethod
	def get_name(self):
		pass

	@abstractmethod
	def update(self, frameCount):
		pass

	@abstractmethod
	def draw(self):
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

	def drawCircle(self, color, pos: Vector, radius: int):
		pygame.draw.circle(
			self.surface,
			color,
			pos.getTuple(),
			radius
		)

	def drawText(self, text: str, pos: Vector):
		# text_surface, rect = PYCADE_FONT.render("Hello World!", (0, 0, 0))

		# rect = PYCADE_FONT.get_rect(

		# )


    # screen.blit(text_surface, (40, 250))

		PYCADE_FONT.render_to(
			self.surface,
			pos.getTuple(),
			text,
			(0, 0, 0)
		)


