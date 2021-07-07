import pygame
from utils.actions import Action
from utils.vector import Vector
from games.games import PycadeGame

speed = .1
RED = (255, 0, 0)

class MorseGame(PycadeGame):
	pos: Vector = Vector(0, 0)

	@staticmethod
	def get_name():
		return "Morse Mayhem"

	def update(self, frameCount):
		if Action.DOWN in self.newActions:
			self.pos.addY(speed)
		if Action.UP in self.newActions:
			self.pos.add(Vector(0, -speed))
		if Action.LEFT in self.newActions:
			self.pos.add(Vector(-speed, 0))
		if Action.RIGHT in self.newActions:
			self.pos.add(Vector(speed, 0))

		return True

	def draw(self):
		pass




