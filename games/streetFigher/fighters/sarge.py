import pygame
from ..fighter import Fighter
from games.games import PycadeGame
from utils.vector import Vector

streetFighterSize = Vector(200, 300)

class Sarge(Fighter):
	def __init__(self, isPlayer1: bool, screenSize: Vector):
		img1 = PycadeGame.loadImage(
			"games/streetFigher/assets/sarge.png", streetFighterSize
		)
		img2 = PycadeGame.loadImage(
			"games/streetFigher/assets/sarge2.png", streetFighterSize
		)
		img1 = pygame.transform.flip(img1, True, False)
		img2 = pygame.transform.flip(img2, True, False)
		punchImg = PycadeGame.loadImage(
			"games/streetFigher/assets/sarge-punch.png", streetFighterSize
		)
		punchImg = pygame.transform.flip(punchImg, True, False)
		super().__init__("Sarge", img1, img2, punchImg, img1, isPlayer1, screenSize)
		self.armHeight = (0.5 * self.size.y) + 20






