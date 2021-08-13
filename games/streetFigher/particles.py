from games.games import PycadeGame
from utils.canvas import Canvas
from utils.vector import Vector
import math
from random import randint

PARTICAL_CANVAS_SIZE = 30

class Particals:

	frameIndex = 0

	def __init__(self):
		self.particles = []
		self.frame1 = Canvas(size=Vector(PARTICAL_CANVAS_SIZE, PARTICAL_CANVAS_SIZE))
		self.frame2 = Canvas(size=Vector(PARTICAL_CANVAS_SIZE, PARTICAL_CANVAS_SIZE))
		self.make()

	def make(self):
		# start with random pixels near to each other
		spreadDist1 = int(0.2 * PARTICAL_CANVAS_SIZE)
		mid = Vector(PARTICAL_CANVAS_SIZE/2, PARTICAL_CANVAS_SIZE/2)
		self.frame1.fillTransparent()
		for _ in range(10):
			x = int(mid.x + randint(-spreadDist1, spreadDist1))
			y = int(mid.y + randint(-spreadDist1, spreadDist1))
			self.frame1.drawRect((255, 0, 0), Vector(x, y), Vector(3, 3), 0)

		spreadDist2 = int(0.5 * PARTICAL_CANVAS_SIZE)
		mid = Vector(PARTICAL_CANVAS_SIZE/2, PARTICAL_CANVAS_SIZE/2)
		self.frame2.fillTransparent()
		for _ in range(10):
			x = int(mid.x + randint(-spreadDist2, spreadDist2))
			y = int(mid.y + randint(-spreadDist2, spreadDist2))
			self.frame2.drawRect((255, 0, 0), Vector(x, y), Vector(3, 3), 0)

	def draw(self, game: PycadeGame, pos: Vector):
		self.frameIndex += 1
		img = self.frame1 if math.floor(self.frameIndex/5) % 2 == 0 else self.frame2
		game.drawImage(
			img._surface,
			pos
		)







