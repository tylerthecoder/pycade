import pygame
from enum import Enum
from utils.vector import Vector
from utils.actions import Action
from games.games import PycadeGame
from utils.colors import RED, GREEN,ORANGE
import random
import math

# Constants
speedDelta = .01
maxSpeed = 3

class SnakeGame(PycadeGame):
	def start(self):
		self.moveDir = Vector(1, 0)
		self.lastMoveDir = self.moveDir
		self.boardSize = 10
		self.snakeSize = 4
		self.speed = .1
		self.isOver = False
		self.cellSize = min(self.screenSize.x, self.screenSize.y) / self.boardSize
		headPos = Vector(4, 4)
		# The head is the first body part
		self.bodyPos = [headPos]
		self.placeFruit()

	@staticmethod
	def get_name():
		return "Snake"

	def update(self):
		if Action.DOWN in self.newActions and not self.lastMoveDir == Vector(0, 1):
			self.moveDir = Vector(0, 1)
		elif Action.UP in self.newActions and not self.lastMoveDir == Vector(0, -1):
			self.moveDir = Vector(0, -1)
		elif Action.RIGHT in self.newActions and not self.lastMoveDir == Vector(1, 0):
			self.moveDir = Vector(1, 0)
		elif Action.LEFT in self.newActions and not self.lastMoveDir == Vector(-1, 0):
			self.moveDir = Vector(-1, 0)

		if self.frameCount % math.floor(1 / self.speed) == 0:
			self.moveHead()
			self.lastMoveDir = self.moveDir.copy()
			return True

		# Nothing position was changed so we don't need to redraw
		return False

	def draw(self):
		if self.isOver:
			self.drawText("YOU SUCK", Vector(10, 10))
			self.drawText(f'Score Was {self.snakeSize}', Vector(10, 50))
			return

		# Draw the grid
		for rowIndex in range(self.boardSize):
			for colIndex in range(self.boardSize):
				x = colIndex * self.cellSize
				y = rowIndex * self.cellSize

				self.drawRect(
					RED,
					Vector(x, y),
					Vector(self.cellSize, self.cellSize),
					1
				)

		# Draw the body
		for index, bodyPartPos in enumerate(self.bodyPos):
			newBodyPartPos = self.toScreenPos(bodyPartPos)
			# The color of the head should be Red.
			color = RED if index == 0 else GREEN
			self.drawCircle(color, newBodyPartPos, self.cellSize * .4)

		# Draw the fruit
		fruitScreenPos = self.toScreenPos(self.fruitPos)
		self.drawCircle(ORANGE, fruitScreenPos, self.cellSize * .4)

		return True

	def moveHead(self):
		# Move the head
		currentHeadPos = self.bodyPos[0].add(self.moveDir)

		# Append new position
		self.bodyPos.insert(0,currentHeadPos)

		# Delete the tail if we are too long
		if len(self.bodyPos) > self.snakeSize:
			del self.bodyPos[-1]

		# see if the new head is on the fruit
		if currentHeadPos == self.fruitPos:
			self.placeFruit()
			self.snakeSize += 1
			self.speed += speedDelta
			if self.speed > maxSpeed:
				self.speed = maxSpeed

		# see if the new head is off the screen
		if currentHeadPos.x > self.boardSize-1 or currentHeadPos.x < 0 or currentHeadPos.y > self.boardSize - 1 or currentHeadPos.y < 0:
			self.lose()

		# see if the snake intersects itself
		for index, bodyPos in enumerate(self.bodyPos):
			# Head always intersects your self
			if index == 0:
				continue
			if currentHeadPos == bodyPos:
				self.lose()

	def placeFruit(self):
		# Create an array of all the spots where the fruit could be placed
		potSpots = []
		for rowIndex in range(self.boardSize):
			for colIndex in range(self.boardSize):
				loc = Vector(rowIndex, colIndex)
				if not loc in self.bodyPos:
					potSpots.append(loc)

		# There are no more spots, so we lose
		if len(potSpots) == 0:
			self.win()

		self.fruitPos = random.choice(potSpots)

	# Converts a position on the grid to a position on the screen
	def toScreenPos(self, pos: Vector):
		newPos = pos \
			.scalarMultiply(self.cellSize) \
			.add(Vector(self.cellSize / 2, self.cellSize / 2))

		return newPos

	def lose(self):
		self.isOver = True



