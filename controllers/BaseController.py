from utils.actions import Action
from typing import Set
from abc import ABC, abstractmethod


class BaseController(ABC):
	@abstractmethod
	def getActions(self) -> Set[Action]:
		pass

