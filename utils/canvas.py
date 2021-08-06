from utils.vector import Vector
import pygame

class Canvas:
	def __init__(self, surface = None, size = None) -> None:
		if surface is None:
			self._surface = pygame.Surface(size)
		else:
			self._surface = surface

	def fill(self, color: tuple) -> None:
		self._surface.fill(color)

	def fillTransparent(self) -> None:
		self._surface.fill((0,0,0,0))

	def drawCircle(self, color, pos: Vector, radius: int) -> None:
		pygame.draw.circle(
			self._surface,
			color,
			pos.getTuple(),
			radius
		)






