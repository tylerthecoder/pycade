import pygame
import time
from retro import get_all_roms, run_rom
from games.games import PycadeGame
from utils.vector import Vector
from gameHolder import ALL_GAMES
from utils.actions import Action
from utils.colors import RED, BLACK

class TitleScreen(PycadeGame):
	def start(self):
	 self.selectedGame = 0
	 self.allRoms = get_all_roms()

	@staticmethod
	def get_name():
		return "Title Screen"

	def update(self):
		if Action.DOWN in self.newActions:
			self.selectedGame += 1

		if Action.UP in self.newActions:
			self.selectedGame -= 1

		if Action.BUTTON_1 in self.newActions:
			if self.selectedGame >= len(ALL_GAMES):
				rom = self.allRoms[self.selectedGame - len(ALL_GAMES)]
				self.navigate(rom=rom)
			else:
				self.navigate(game=ALL_GAMES[self.selectedGame])

		numOfGames = len(ALL_GAMES) + len(self.allRoms)

		self.selectedGame = (self.selectedGame + numOfGames) % numOfGames

		return True

	def draw(self):
		self.canvas.drawText(BLACK, "Pycade", Vector(10, 10))
		self.canvas.drawText(BLACK, "Choose A Game", Vector(10, 50))

		for gameIndex, game in enumerate(ALL_GAMES):
			self.canvas.drawText(
				BLACK,
				game.get_name(),
				Vector(10, 30 * gameIndex + 120)
			)

			if self.selectedGame == gameIndex:
				self.canvas.drawRect(
					RED,
					Vector(0, 30 * gameIndex + 115),
					Vector(self.screenSize.x, 30),
					2
				)

		for romIndex, rom in enumerate(self.allRoms):
			romIndex += len(ALL_GAMES)
			self.canvas.drawText(
				BLACK,
				rom,
				Vector(10, 30 * romIndex + 120)
			)

			if self.selectedGame == romIndex:
				self.canvas.drawRect(
					RED,
					Vector(0, 30 * romIndex + 115),
					Vector(self.screenSize.x, 30),
					2
				)





