from enum import Enum

class Action(Enum):
	UP = 0
	DOWN = 1
	LEFT = 2
	RIGHT = 3
	BUTTON_1 = 4
	MENU = 5

	# Player 2's actions
	UP_P2 = 6
	DOWN_P2 = 7
	RIGHT_P2 = 8
	LEFT_P2 = 9
	Button_1_P2 = 10