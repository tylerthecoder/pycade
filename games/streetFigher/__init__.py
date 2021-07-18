import pygame
from games.games import PycadeGame
from utils.vector import Vector

streetFighterSize = Vector(200, 300)

class StreetFighter(PycadeGame):
	def start(self):
		self.fighter1Pos = Vector(100, 100)
		self.makeImages()
		self.imgIndex = 0

	def makeImages(self):
		self.streetFigherImg = self.loadImage(
			"games/streetFigher/assets/Fighter1.png", streetFighterSize
		)
		self.streetFigherImg2 = self.loadImage(
			"games/streetFigher/assets/Fighter1a.png", streetFighterSize
		)

	@staticmethod
	def get_name():
		return "Street Fighter"

	def update(self):

		if self.frameCount % 10 == 0:
			self.imgIndex = (self.imgIndex + 1) % 2

		return True

	def draw(self):
		img = self.streetFigherImg if self.imgIndex == 0 else self.streetFigherImg2

		self.drawImage(
			img,
			self.fighter1Pos,
		)


