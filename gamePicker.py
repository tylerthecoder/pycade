from screens.titleScreen import TitleScreen
from games.games import PycadeGame
from typing import List

class GamePicker:
    def __init__(self, screenSize, screen):
        super().__init__()
        self.screenSize = screenSize
        self.screen = screen

        self.currentGame = TitleScreen(screenSize, screen, lambda game: self.startGame(game))

    def startGame(self, game: PycadeGame):
        def navigate(game: PycadeGame = TitleScreen):
            self.startGame(game)
        self.currentGame = game(self.screenSize, self.screen, navigate)
