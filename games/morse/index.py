import pygame
from utils.actions import Action
from utils.vector import Vector

speed = .1
RED = (255, 0, 0)

class MorseGame:
	pos: Vector = Vector(0, 0)

	def update(self, actions):
		if Action.DOWN in actions:
			self.pos.addY(speed)
		if Action.UP in actions:
			self.pos.add(Vector(0, -speed))
		if Action.LEFT in actions:
			self.pos.add(Vector(-speed, 0))
		if Action.RIGHT in actions:
			self.pos.add(Vector(speed, 0))

		return True

	def draw(self, screen):
		pygame.draw.circle(screen, RED, self.pos.getTuple(), 20);




