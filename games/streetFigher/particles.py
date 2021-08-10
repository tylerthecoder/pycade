from games.games import PycadeGame
from utils.canvas import Canvas
from utils.vector import Vector

class Particals:

	frameIndex = 0

	def __init__(self):
		self.particles = []
		self.frame1 = Canvas(size=Vector(30, 30))
		self.frame2 = Canvas(size=Vector(30, 30))
		self.make()

	def make(self):
		self.frame1.fillTransparent()
		self.frame1.drawCircle(
			(255, 0 , 0),
			Vector(15, 15),
			10,
		)
		self.frame2.fillTransparent()
		self.frame2.drawCircle(
			(0,0,255),
			Vector(15, 15),
			10
		)
		pass

	def draw(self, game: PycadeGame, pos: Vector):
		self.frameIndex += 1
		img = self.frame1 if self.frameIndex % 2 == 0 else self.frame2
		game.drawImage(
			img._surface,
			pos
		)







