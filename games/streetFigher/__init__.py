import pygame
from games.games import PycadeGame
from utils.vector import Vector
from utils.actions import Action
from .fighters.sarge import Sarge
from .fighters.kodo import Kodo


class StreetFighter(PycadeGame):
	def start(self):
		self.fighter1 = Sarge(True, self.screenSize)
		self.fighter2 = Kodo(False, self.screenSize)
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

		if Action.UP in self.newActions:
			self.fighter1.jump()
		if Action.UP_P2 in self.newActions:
			self.fighter2.jump()

		if Action.DOWN in self.currentActions:
			self.fighter1.block()
		else:
			self.fighter1.unblock()

		if Action.DOWN_P2 in self.currentActions:
			self.fighter2.block()
		else:
			self.fighter2.unblock()


		if Action.BUTTON_1 in self.newActions:
			self.fighter1.punch()
		if Action.BUTTON_1_P2 in self.newActions:
			self.fighter2.punch()


		# Do damage
		self.fighter1.tryPunching(self.fighter2)
		self.fighter2.tryPunching(self.fighter1)

		self.fighter1.update(self.frameCount)
		self.fighter2.update(self.frameCount)

		return True

	def draw(self):
		self.drawImage(self.background, Vector(0, 0))
		self.fighter1.draw(self)
		self.fighter2.draw(self)


