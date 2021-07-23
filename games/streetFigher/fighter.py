from __future__ import annotations # So we can use the Fighter class as a type
import pygame
from utils.vector import Vector
from games.games import PycadeGame
from utils.actions import Action

moveSpeed = 10
gravity = 1.5
maxFallSpeed = 20
jumpSpeed = 20

class Fighter():
	def __init__(self, name: str, walkImg1: pygame.Surface, walkImg2: pygame.Surface, punchImg: pygame.Surface, blockImg: pygame.Surface, isPlayer1: bool, screenSize: Vector):
		self.name = name
		self.punchImg = punchImg
		self.punchTimeLeft = 0
		self.blockImg = blockImg
		self.blockTimeLeft = 0
		self.imgIndex = 0
		self.imgs = [walkImg1, walkImg2]
		self.isPlayer1 = isPlayer1
		self.screenSize = screenSize
		self.size = Vector(200, 300)

		startingPos = Vector(100, 100) if isPlayer1 else Vector(screenSize.x - self.size.x, 100)
		self.pos = startingPos

		self.vel = Vector(0,0)
		self.health = 100
		self.facingDirection = 1
		self.isPunching = False
		self.hitPlayer = False
		self.isBlocking = False

	def update(self, frameCount):
		self.vel.y += gravity

		if self.vel.y > maxFallSpeed:
			self.vel.y = maxFallSpeed

		self.pos = self.pos.add(self.vel)

		# Don't let player go through floor
		if self.pos.y > self.screenSize.y - self.size.y:
			self.pos.y = self.screenSize.y - self.size.y

		if self.punchTimeLeft > 0:
			self.punchTimeLeft -= 1
			if self.punchTimeLeft == 0:
				self.isPunching = False
				self.hitPlayer = False

		if frameCount % 10 == 0:
			self.imgIndex = (self.imgIndex + 1) % len(self.imgs)

	def walkLeft(self):
		self.vel.x = -moveSpeed
		self.faceWalkingDirection()

	def walkRight(self):
		self.vel.x = moveSpeed
		self.faceWalkingDirection()

	def stopWalking(self):
		self.vel.x = 0
		self.faceWalkingDirection()

	def jump(self):
		self.vel.y = -jumpSpeed

	def punch(self):
		# Can't punch if you're blocking or already punching
		if self.isBlocking or self.isPunching:
			return
		self.isPunching = True
		self.punchTimeLeft = 8
		pass

	def block(self):
		self.isBlocking = True

	def unblock(self):
		self.isBlocking = False


	def takeDamage(self, amount: int):
		self.health -= amount

	def tryPunching(self, fighter: Fighter):
		punchPos = self.pos if self.facingDirection == 1 else self.pos.addX(self.size.x)
		punchPos = punchPos.addY(self.size.y /2)
		if self.isPunching and not self.hitPlayer:
			# If the punch pos is inside the fighter's rect, and the fighter is not blocking
			if fighter.pos.x - 10 < punchPos.x < fighter.pos.x + fighter.size.x + 10 and \
				fighter.pos.y - 10  < punchPos.y < fighter.pos.y + fighter.size.y + 10 and \
				not fighter.isBlocking:
				self.hitPlayer = True
				fighter.takeDamage(5)
				return True
		return False

	def faceWalkingDirection(self):
		# If the fighter is moving a different direction flip the image
		if self.vel.x > 0 and self.facingDirection == 1 or \
			self.vel.x < 0 and self.facingDirection == -1:
			self.imgs[0] = pygame.transform.flip(self.imgs[0], True, False)
			self.imgs[1] = pygame.transform.flip(self.imgs[1], True, False)
			self.punchImg = pygame.transform.flip(self.punchImg, True, False)
			self.facingDirection = -self.facingDirection

	def draw(self, game: PycadeGame):

		# Draw health bar
		barX = 10 if self.isPlayer1 else self.screenSize.x - self.size.x - 10
		barY = 10
		barWidth = self.health
		barHeight = 10
		barPos = Vector(barX, barY)
		barSize = Vector(barWidth, barHeight)
		barColor = (0, 255, 0) if self.health > 50 else (255, 0, 0)
		game.drawRect(barColor, barPos, barSize, 0)

		imgToDraw = self.punchImg if self.isPunching else self.blockImg if self.isBlocking else self.imgs[self.imgIndex]

		game.drawImage(
			imgToDraw,
			self.pos
		)
		pass






