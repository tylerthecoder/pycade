import pygame
from games.games import PycadeGame
from utils.vector import Vector
from utils.actions import Action
from .fighter import Fighter

streetFighterSize = Vector(200, 300)

class StreetFighter(PycadeGame):
	def start(self):
		fight1Img1 = self.loadImage(
				"games/streetFigher/assets/Fighter1.png", streetFighterSize
		)
		fight1Img2 = self.loadImage(
			"games/streetFigher/assets/Fighter1a.png", streetFighterSize
		)
		self.fighter1 = Fighter([fight1Img1, fight1Img2])

		fight2Img1 = self.loadImage(
			"games/streetFigher/assets/sarge.png", streetFighterSize
		)
		fight2Img2 = self.loadImage(
			"games/streetFigher/assets/sarge2.png", streetFighterSize
		)
		fight2Img1 = pygame.transform.flip(fight2Img1, True, False)
		fight2Img2 = pygame.transform.flip(fight2Img2, True, False)
		self.fighter2 = Fighter([fight2Img1, fight2Img2])

		self.background = pygame.Surface(self.screenSize.getTuple())
		self.background.fill((40, 40, 20))

	@staticmethod
	def get_name():
		return "Street Fighter"

	def update(self):
		if Action.LEFT in self.currentActions:
			self.fighter1.walkLeft()
		elif Action.RIGHT in self.currentActions:
			self.fighter1.walkRight()
		else:
			self.fighter1.stopWalking()

		if Action.LEFT_P2 in self.currentActions:
			self.fighter2.walkLeft()
		elif Action.RIGHT_P2 in self.currentActions:
			self.fighter2.walkRight()
		else:
			self.fighter2.stopWalking()


		self.fighter1.update(self.frameCount)
		self.fighter2.update(self.frameCount)

		return True


	def draw(self):
		self.drawImage(self.background, Vector(0, 0))
		self.fighter1.draw(self)
		self.fighter2.draw(self)


