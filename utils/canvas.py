from __future__ import annotations

from pygame.rect import Rect
from utils.vector import Vector
import pygame
from utils.font import PYCADE_FONT
from typing import Tuple

ColorType = Tuple[int, int, int] or Tuple[int, int, int, int]


class Canvas:
	def __init__(self, surface = None, size: Vector = None) -> None:
		if surface is None and size is not None:
			self._surface = pygame.Surface(size.getTuple(), pygame.SRCALPHA)
		else:
			self._surface = surface

	def fill(self, color: ColorType) -> None:
		self._surface.fill(color)

	def fillTransparent(self) -> None:
		self._surface.convert_alpha()
		self._surface.fill((0,0,0,0))

	def drawCircle(self, color: ColorType, pos: Vector, radius: int) -> None:
		pygame.draw.circle(
			self._surface,
			color,
			pos.getTuple(),
			radius
		)

	def drawLine(self, color: ColorType, startPos: Vector, endPos: Vector) -> None:
		pygame.draw.line(
			self._surface,
			color,
			startPos.getTuple(),
			endPos.getTuple()
		)

	def drawText(self, color: ColorType, text: str, pos: Vector, center: bool = False, size = 25) -> None:
		if center:
			fontRect = PYCADE_FONT.get_rect(text, size=size)
			fontRect.center = (self._surface.get_rect().center[0], int(pos.y))
			PYCADE_FONT.render_to(self._surface, fontRect, text, color, size=size)
			return

		PYCADE_FONT.render_to(
			self._surface,
			# Convert floats to ints
			tuple(map(int, pos.getTuple())),
			text,
			color
		)

	# Draw a rectangle to the screen
	# set thickness to 0 to fill the retangle with color
	def drawRect(self, color: ColorType, pos: Vector, size: Vector, thickness: int):
		pygame.draw.rect(
			self._surface,
			color,
			pygame.Rect(pos.x, pos.y, size.x, size.y),
			thickness
		)

	def drawCanvas(self, canvas: Canvas, pos: Vector) -> None:
		self._surface.blit(canvas._surface, pos.getTuple())





