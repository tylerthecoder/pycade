from __future__ import annotations
from typing import Callable, Set, Type, List
from abc import ABC, abstractmethod, abstractproperty
import pygame
import time
from retro import get_all_roms, run_rom
from games.games import PycadeGame
from utils.vector import Vector
from gameHolder import ALL_GAMES
from utils.actions import Action
from utils.colors import RED, BLACK
import sys


class Menu(ABC):
	def __init__(
		self,
		game: PycadeGame,
		items: List[str] = [],
		onExit: Callable[[], None] = None,
	) -> None:
			self.game = game
			self.items = items
			self.onExit = onExit
			self.childMenu: Menu | None = None
			self.selectedItem = 0

	def update(self, newActions: Set[Action]) -> bool:
		if self.childMenu:
			return self.childMenu.update(newActions)

		if Action.DOWN in newActions:
			self.selectedItem += 1
			self.selectedItem = self.selectedItem % len(self.items)
			return True

		if Action.UP in newActions:
			self.selectedItem -= 1
			self.selectedItem = self.selectedItem % len(self.items)
			return True


		if Action.BUTTON_1 in newActions:
			self.onSelect(self.selectedItem)
			return True

		return False

	def draw(self, game: PycadeGame) -> None:
		if self.childMenu:
			self.childMenu.draw(game)
			return

		backgroundImg = TitleScreen.get_background_image(game)

		game.drawImage(backgroundImg, Vector(0, 0))

		game.canvas.drawText(BLACK, "Pycade" + str(self.selectedItem), Vector(game.screenSize.x / 2, 30), center=True, size=40)
		game.canvas.drawText(BLACK, self.getTitle(), Vector(game.screenSize.x / 2, 70), center=True, size=24)

		for i, item in enumerate(self.items):
			y = 160 + (i * 30)
			if i == self.selectedItem:
				game.canvas.drawText(RED, item, Vector(0, y), size = 22, center=True)
			else:
				game.canvas.drawText(BLACK, item, Vector(0, y), size = 20, center=True)


	def newMenu(self, menu: Type[Menu]) -> None:
		newMenu = menu(self.game, onExit = self.onChildMenuExit)
		self.childMenu = newMenu

	def onChildMenuExit(self) -> None:
		self.childMenu = None

	def exit(self) -> None:
		if self.onExit:
			self.onExit()

	@abstractmethod
	def getTitle(self) -> str:
		pass

	@abstractmethod
	def onSelect(self, index: int):
		pass

class MainMenu(Menu):
	def __init__(self, game: PycadeGame, onExit: Callable[[], None] = None) -> None:
		super().__init__(
			game,
			items = ["Play", "Settings", "Quit"],
			onExit = onExit,
		)

	def getTitle(self) -> str:
		return "Main Menu"

	def onSelect(self, index: int):
		print("Selected", index)
		if index == 0:
			self.newMenu(PlayMenu)
		elif index == 1:
			pass
		elif index == 2:
			self.exit()

class PlayMenu(Menu):
	def __init__(self, game: PycadeGame, onExit: Callable[[], None] = None) -> None:
		super().__init__(
			game,
			items = ["Community", "ROMs", "???", "Exit"],
			onExit=onExit,
		)

	def getTitle(self) -> str:
		return "Play"

	def onSelect(self, index: int):
		if index == 0:
			self.newMenu(CommunityMenu)
		elif index == 1:
			self.newMenu(RomMenu)
		elif index == 2:
			pass
		elif index == 3:
			self.exit()


class CommunityMenu(Menu):
	def __init__(self, game: PycadeGame, onExit: Callable[[], None] = None) -> None:
		# for gameIndex, game in enumerate(ALL_GAMES):
		gameNames = [game.get_name() for game in ALL_GAMES]
		gameNames.append("Exit")
		super().__init__(
			game,
			items = gameNames,
			onExit = onExit,
		)

	def getTitle(self) -> str:
		return "Community"

	def onSelect(self, index: int):
		if index ==  len(self.items)-1:
			self.exit()
			return

		game = ALL_GAMES[index]
		self.game.navigate(game=game)


class RomMenu(Menu):
	def __init__(self, game: PycadeGame, onExit: Callable[[], None] = None) -> None:
		self.roms = get_all_roms()
		romNames = list(map(self.getRomName, get_all_roms()))
		romNames.append("Exit")

		super().__init__(
			game,
			items = romNames,
			onExit = onExit,
		)

	def getRomName(self, rom: str) -> str:
		return rom.split("/")[-1]

	def getTitle(self) -> str:
		return "ROMs"

	def onSelect(self, index: int):
		if index ==  len(self.items)-1:
			self.exit()
			return

		rom = self.roms[index]
		self.game.navigate(rom=rom)

class TitleScreen(PycadeGame):

	backgroundImage: pygame.Surface | None = None

	@staticmethod
	def get_background_image(game: PycadeGame) -> pygame.Surface:
		if TitleScreen.backgroundImage is None:
			print("Loading background image", game.screenSize)
			TitleScreen.backgroundImage = PycadeGame.loadImage("assets/title-screen-background.jpg", game.screenSize)
		return TitleScreen.backgroundImage

	@staticmethod
	def get_name():
		return "Title Screen"

	def start(self):
		self.selectedGame = 0
		self.allRoms = get_all_roms()
		self.menu = MainMenu(self, onExit=self.exit)

	def update(self):
		return self.menu.update(self.newActions)

	def exit(self):
		sys.exit(0)

	def draw(self):
		self.menu.draw(self)






