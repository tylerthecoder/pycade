
from games.games import PycadeGame
from utils.vector import Vector
from utils.actions import Action
from utils.number import limitValue
import pygame
import math
import random


gravity = 2
maxFallingSpeed = 20
jumpBoostAmount = -40.0

pipeShaftWidth = 80
pipeShaftHeight = 100
pipeCapHeight = 60
pipeCapWidth = 110

pipeMoveSpeed = 10

pipeDistanceApart = 600

birdSize = Vector(100, 100)
pipeCapSize = Vector(pipeCapWidth, pipeCapHeight)
pipeShaftSize = Vector(pipeShaftWidth, pipeShaftHeight)

#Colors
SKY_COLOR = (32, 155, 155)
GRASS_COLOR = (0,255, 0)

class FlappyGame(PycadeGame):

	@staticmethod
	def get_name():
		return "Flappy Game"

	def __init__(self, screenSize, surface, navigate):
		PycadeGame.__init__(self, screenSize, surface, navigate)

		self.makeImages()

		self.isOver = False
		self.angle = 0
		self.birdPos = Vector(60, 10)
		self.birdVel = Vector(0, 0)
		self.score = 0

		# Make the default pipe
		self.pipes = [ Pipe(800, 230, 200, self) ]
		self.makePipe()

	def makeImages(self):
		self.flappyImg = self.loadImage("games/flappy/assets/flappy.png", birdSize)
		self.pipeTop = self.loadImage("games/flappy/assets/pipe-top.png", pipeCapSize)
		self.pipeMiddle = self.loadImage("games/flappy/assets/pipe-middle.png", pipeShaftSize)
		self.pipeBottom = pygame.transform.flip(self.pipeTop, False, True)

		# Make the backround image using pygame specific methods
		self.background = pygame.Surface(self.screenSize.getTuple())
		self.background.fill(SKY_COLOR)

	def update(self):
		if self.isOver:
			return

		self.birdPos = self.birdPos.add(self.birdVel)
		self.birdVel = self.birdVel.addY(gravity)


		self.birdVel.y = limitValue(self.birdVel.y, -maxFallingSpeed, maxFallingSpeed)

		if Action.BUTTON_1 in self.newActions:
			self.birdVel = self.birdVel.addY(jumpBoostAmount)

		for pipe in self.pipes:
			shouldDelete = pipe.update()
			if shouldDelete:
				self.makePipe()
				self.pipes.remove(pipe)
				self.score += 1

		# Check if the nearest pipe is colliding with the bird
		closestPipe = self.pipes[0]
		if closestPipe.checkCollision(self.birdPos):
			self.gameOver()

		return True

	def draw(self):
		self.drawImage(self.background, Vector(0, 0))

		if self.isOver:
			self.drawText("YOU SUCK", Vector(10, 10))
			self.drawText(f'Score Was {self.score}', Vector(10, 50))
			return

		self.drawImage(self.flappyImg, self.birdPos, angle=self.angle)

		for pipe in self.pipes:
			pipe.draw()

	def gameOver(self):
		self.isOver = True

	def makePipe(self):
		x = self.pipes[-1].holeX + pipeDistanceApart
		y = random.randint(0, self.screenSize.y)
		width = random.randint(200, 400)
		self.pipes.append(Pipe(x, y, width, self))

class Pipe():
	def __init__(self, holeX: int, holeY: int, holeSize: int, game: FlappyGame):
		self.holeX = holeX
		self.holeY = holeY
		self.holeSize = holeSize
		self.game = game

	def update(self):
		self.holeX -= pipeMoveSpeed
		# True if we should be deleted
		return self.holeX < -pipeCapWidth

	# returns True if the bird is hitting the pipe
	def checkCollision(self, birdPos: Vector):
		#check if the bird is in the hole
		isCollideX = abs(self.holeX - birdPos.x) < pipeCapWidth / 2
		isCollideY = abs(self.holeY - birdPos.y) < self.holeSize / 2
		return isCollideX and not isCollideY

	def draw(self):
		# draw from the top of the screen to the start of the hole
		self.drawPipeShaft(self.holeX, 0, self.holeY - self.holeSize / 2)
		self.drawPipeShaft(self.holeX, self.holeY + self.holeSize / 2, self.game.screenSize.y)

		topCapPos = Vector(self.holeX, self.holeY - (self.holeSize / 2 + pipeCapHeight))
		bottomCapPos = Vector(self.holeX, self.holeY + (self.holeSize / 2))

		self.game.drawImage(self.game.pipeBottom, topCapPos)
		self.game.drawImage(self.game.pipeTop, bottomCapPos)

	def drawPipeShaft(self, x: int, startY: int, endY: int):
		height = endY - startY
		numOfSections = math.ceil(height / pipeShaftHeight)
		for index in range(numOfSections):
			pipePos = Vector(x + 15, startY + index * pipeShaftHeight)
			# pipeSize = (80, pipeShaftHeight)
			pipeCrop = (0, 0, 80, math.floor(min(pipeShaftHeight, endY - pipePos.y)))
			self.game.drawImage(self.game.pipeMiddle, pipePos, crop=pipeCrop)