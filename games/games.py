from abc import ABC, abstractmethod, abstractproperty
import pygame
from utils.vector import Vector
from utils.actions import Action
from typing import Set
from utils.font import PYCADE_FONT
from collections.abc import Callable

class PycadeGame(ABC):
	def __init__(self, screenSize, surface, navigate):
		self.navigate = navigate
		self.surface = surface
		self.screenSize = Vector(screenSize[0], screenSize[1])
		self.lastActions = set()
		self.newActions = set()

		self.start()


	# This method is called when the the game is started
	@abstractmethod
	def start(self):
		pass

	@staticmethod
	@abstractmethod
	def get_name(self):
		pass

	@abstractmethod
	def update(self):
		pass

	@abstractmethod
	def draw(self):
		pass

	# Makes a pygame surface and returns it
	def loadImage(self, url: str, size: Vector):
		img = pygame.image.load(url).convert_alpha()
		img = pygame.transform.scale(img, size.getTuple())
		return img


	# Draws an image to the screen
	# You shouldn't set angle or size all the time because pygame is slow and resizing images
	def drawImage(self, img, position: Vector, angle = 0, size: Vector = None, crop= None):
		if not size is None:
			img = pygame.transform.scale(img, size)

		if angle != 0:
			img = pygame.transform.rotate(img, angle)
			position = img.get_rect(topleft = img.get_rect(topleft = position.getTuple()).topleft)
			self.surface.blit(img, position)
			return

		if crop is None:
			self.surface.blit(img, position.getTuple())
		else:
			self.surface.blit(img, position.getTuple(), crop)


	def setActions(self, actions: Set[Action]):
		self.newActions = self.lastActions - actions
		self.lastActions = actions
		if Action.MENU in actions:
			self.navigate()

	def setTimes(self, frameCount, msSinceLastFrame, totalMs):
		self.frameCount = frameCount
		self.msSinceLastFrame = msSinceLastFrame
		self.totalMs = totalMs

	# Draw a rectangle to the screen
	# set thickness to 0 to fill the retangle with color
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
		PYCADE_FONT.render_to(
			self.surface,
			pos.getTuple(),
			text,
			(0, 0, 0)
		)


