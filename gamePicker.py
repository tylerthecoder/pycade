from screens.titleScreen import TitleScreen
from games.games import PycadeGame
from typing import List
from gameHolder import DEFAULT_GAME

class GamePicker:
    def __init__(self, screenSize, screen):
        self.screenSize = screenSize
        self.screen = screen

        initGame = DEFAULT_GAME if DEFAULT_GAME else TitleScreen

        self.startGame(initGame)

    def startGame(self, game: PycadeGame):
        def navigate(game: PycadeGame = TitleScreen):
            self.startGame(game)
        self.currentGame = game(self.screenSize, self.screen, navigate)
