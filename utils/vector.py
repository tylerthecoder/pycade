from __future__ import annotations


class Vector:
	x = 0
	y = 0

	def __init__(self, x, y):
		self.x = x
		self.y = y

	def add(self, val: Vector):
		self.x += val.x
		self.y += val.y

	def addX(self, val: Vector):
		self.x += val

	def addY(self, val: Vector):
		self.y += val

	def sub(self, val: Vector):
		self.x -= val.x
		self.y -= val.y

	def getTuple(self):
		return (self.x, self.y)











