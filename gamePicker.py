from games.morse.index import MorseGame
from games.snake.main import SnakeGame
from games.games import PycadeGame
from typing import List

class GamePicker:

	def __init__(self):
	 super().__init__()

	 self.games: List[PycadeGame] = [
		 MorseGame,
		 SnakeGame,
	 ]
	 self.currentGame = MorseGame;

	def pickGame(self, game: PycadeGame):
		self.currentGame = game

