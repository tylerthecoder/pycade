from games.games import PycadeGame
from utils.vector import Vector
from gamePicker import GamePicker



class TitleScreen(PycadeGame):
	def __init__(self, windowSize, surface):
	 super().__init__(windowSize, surface)
	 self.gamePicker = GamePicker()

	def get_name(self):
		return "Title Screen"

	def update(self, frameCount):
		return True

	def draw(self):
		self.drawText("Pycade", Vector(10, 10))
		self.drawText("Choose A Game", Vector(10, 50))

		for game in self.gamePicker.games:
			self.drawText(game.get_name(), Vector(10, 60))


		pass





