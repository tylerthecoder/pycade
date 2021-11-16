from typing import List, Type
from games.games import PycadeGame
from games.snake import SnakeGame
from games.flappy import FlappyGame
from games.streetFigher import StreetFighter
from games.Oorbitz import Oorbitz

from games.dieZombie import DieZombie

ALL_GAMES: List[Type[PycadeGame]] = [
	Oorbitz,
	SnakeGame,
	FlappyGame,
	StreetFighter,
	DieZombie
]

# Set this to the game you are working on to skip the title screen

DEFAULT_GAME = None
