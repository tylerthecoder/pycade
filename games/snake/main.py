import pygame
from enum import Enum
from utils.vector import Vector
from utils.actions import Action
from games.games import PycadeGame


size = 10

BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

class GameItem(Enum):
	NONE = 0
	FRUIT = 1
	HEAD = 2
	TAIL = 3


class SnakeGame(PycadeGame):

	def __init__(self, screenSize, surface):
		PycadeGame.__init__(self, screenSize, surface)
		self.cellSize = screenSize[0] / size
		self.headPos = Vector(4,4)
		self.moveDir = Vector(1, 0)
		self.grid = []
		for i in range(size):
			self.grid.append([])
			for j in range(size):
				self.grid[i].append(GameItem.NONE)


	def update(self, frameCount):
		if Action.DOWN in self.newActions:
			self.moveDir = Vector(0, -1)
		elif Action.UP in self.newActions:
			self.moveDir = Vector(0, 1)
		elif Action.LEFT in self.newActions:
			self.moveDir = Vector(-1, 0)
		elif Action.RIGHT in self.newActions:
			self.moveDir = Vector(1, 0)

		if frameCount % 500 == 0:
			self.grid[self.headPos.x][self.headPos.y] = GameItem.NONE
			self.headPos.add(self.moveDir)

		self.grid[self.headPos.x][self.headPos.y] = GameItem.FRUIT

		return True

	def draw(self, surface):
		for rowIndex, row in enumerate(self.grid):
			for colIndex, col in enumerate(row):
				x = colIndex * self.cellSize
				y = rowIndex * self.cellSize

				self.drawRect(
					RED,
					Vector(x, y),
					Vector(self.cellSize, self.cellSize),
					1
				)

				gameItem = self.grid[rowIndex][colIndex]

				pos = Vector(x, y)
				pos.add(Vector(self.cellSize / 2, self.cellSize / 2))

				if gameItem is GameItem.FRUIT:
					pygame.draw.circle(surface, GREEN, pos.getTuple(), self.cellSize * .4)


		return True




