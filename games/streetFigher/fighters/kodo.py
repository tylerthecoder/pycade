from ..fighter import Fighter
from games.games import PycadeGame
from utils.vector import Vector

streetFighterSize = Vector(200, 300)

class Kodo(Fighter):
	def __init__(self, isPlayer1: bool, screenSize: Vector):
		img1 = PycadeGame.loadImage(
			"games/streetFigher/assets/kodo.png", streetFighterSize
		)
		img2 = PycadeGame.loadImage(
			"games/streetFigher/assets/kodo2.png", streetFighterSize
		)
		punchImg = PycadeGame.loadImage(
			"games/streetFigher/assets/kodo-punch.png", streetFighterSize
		)
		blockImg = PycadeGame.loadImage(
			"games/streetFigher/assets/kodo-block.png", streetFighterSize
		)
		super().__init__("Kodo", img1, img2, punchImg, blockImg, isPlayer1, screenSize)

