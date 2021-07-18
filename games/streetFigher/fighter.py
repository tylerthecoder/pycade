import pygame
from utils.vector import Vector
from games.games import PycadeGame
from utils.actions import Action

moveSpeed = 5

class Fighter():
	def __init__(self, imgs):
		self.imgs = imgs
		self.imgIndex = 0
		self.pos = Vector(0,0)
		self.vel = Vector(0,0)
		self.facingDirection = 1

	def walkLeft(self):
		self.vel.x = -moveSpeed
		self.faceWalkingDirection()

	def walkRight(self):
		self.vel.x = moveSpeed
		self.faceWalkingDirection()

	def stopWalking(self):
		self.vel.x = 0
		self.faceWalkingDirection()

	def update(self, frameCount):
		self.pos = self.pos.add(self.vel)
		if frameCount % 10 == 0:
			self.imgIndex = (self.imgIndex + 1) % len(self.imgs)

	def faceWalkingDirection(self):
		# If the fighter is moving a different direction flip the image
		if self.vel.x > 0 and self.facingDirection == 1 or \
			self.vel.x < 0 and self.facingDirection == -1:
			self.imgs[0] = pygame.transform.flip(self.imgs[0], True, False)
			self.imgs[1] = pygame.transform.flip(self.imgs[1], True, False)
			self.facingDirection = -self.facingDirection


	def draw(self, game: PycadeGame):
		game.drawImage(
			self.imgs[self.imgIndex],
			self.pos
		)
		pass






