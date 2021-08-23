from enum import Enum

class Action(Enum):
	UP = 0
	DOWN = 1
	LEFT = 2
	RIGHT = 3
	BUTTON_1 = 4
	BUTTON_2 = 11
	MENU = 5

	# Player 2's actions
	UP_P2 = 6
	DOWN_P2 = 7
	RIGHT_P2 = 8
	LEFT_P2 = 9
	BUTTON_1_P2 = 10
	BUTTON_2_P2 = 12