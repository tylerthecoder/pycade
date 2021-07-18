from games.games import PycadeGame
from utils.vector import Vector
from gameHolder import ALL_GAMES
from utils.actions import Action
from utils.colors import RED



class TitleScreen(PycadeGame):
	def start(self):
	 self.selectedGame = 0

	@staticmethod
	def get_name():
		return "Title Screen"

	def update(self):
		if Action.DOWN in self.newActions:
			self.selectedGame += 1

		if Action.UP in self.newActions:
			self.selectedGame -= 1

		if Action.BUTTON_1 in self.newActions:
			self.navigate(ALL_GAMES[self.selectedGame])

		self.selectedGame = (self.selectedGame + len(ALL_GAMES)) % len(ALL_GAMES)

		return True

	def draw(self):
		self.drawText("Pycade", Vector(10, 10))
		self.drawText("Choose A Game", Vector(10, 50))

		for gameIndex, game in enumerate(ALL_GAMES):
			self.drawText(
				game.get_name(),
				Vector(10, 30 * gameIndex + 120)
			)

			if self.selectedGame == gameIndex:
				self.drawRect(
					RED,
					Vector(0, 30 * gameIndex + 115),
					Vector(self.screenSize.x, 30),
					2
				)





