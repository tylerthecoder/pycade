from utils.canvas import Canvas
from utils.font import PYCADE_FONT
from retro import run_rom
from screens.titleScreen import TitleScreen
import time
from games.games import PycadeGame
from gameHolder import DEFAULT_GAME
from utils.colors import YELLOW
import pygame
from config import FULLSCREEN, SCREEN_SIZE
from typing import Union, Type, Tuple

class GamePicker:
    def __init__(self, screenSize: Tuple[int, int]):
        self.screenSize = screenSize
        self.currentGame: Union[PycadeGame, None] = None
        self.quitDisplay = False

        initGame = DEFAULT_GAME if DEFAULT_GAME else TitleScreen

        self.makeScreen()

        self.startGame(initGame)

    def makeScreen(self):
        global SCREEN_SIZE
        if FULLSCREEN:
            infoObject = pygame.display.Info()
            SCREEN_SIZE = (infoObject.current_w, infoObject.current_h)

        self.screenSize = SCREEN_SIZE

        self.screen = pygame.display.set_mode(SCREEN_SIZE)
        if self.currentGame:
            self.currentGame.surface = self.screen
            self.currentGame.canvas = Canvas(self.screen)

    def draw(self):
        if self.quitDisplay:
            pass
        self.screen.fill(YELLOW)
        if self.currentGame:
            self.currentGame.draw()

    def startGame(self, game: Type[PycadeGame]):
        def navigate(game: Type[PycadeGame] = None, rom: str = None):
            if game is not None:
                self.startGame(game)
            elif rom is not None:
                self.startRom(rom)
        print(self.screenSize)
        self.currentGame = game(self.screenSize, self.screen, navigate)

    def startRom(self, rom: str):
        # We need to quit the display so the arcade can launch
        self.quitDisplay = True
        pygame.display.quit()

        run_rom("nes", rom)
        pygame.display.init()
        self.makeScreen()

