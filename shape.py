import pygame
import random
import sys
import math
import time
from GamePlay import Gameplay

pygame.init()

Row_no = 300
Col_no = 320
Name = "Global Tetris"
FPS = 10
clock_used = pygame.time.Clock()
Box_size = 10
Coor = []
Score_displace = 250
Extension = 200
Start = 0
#BackgroundImage = 'rsz_45979918-cartoon-winter-landscape-with-iceberg-and-ice-snow-and-cloudy-sky-seamless-vector-nature-background--stock-vector.jpg'
#BackgroundImage2 = 'rsz_c29bf435b98b.jpg'
ShapeImage = 'rsz_158ba9c7c4de994225d55ac6d279813011428700689_full.jpg'
StartImage2 = 'rsz_258ba9c7c4de994225d55ac6d279813011428700689_full.jpg'
Gameover = 'rsz_38928790-abstract-cartoon-clouds-for-mobile-games-background-stock-vector(1).jpg'
InstructionScreen = 'rsz_c29bf435b98b3.jpg'

from GamePlay import Gameplay
class Shapes(Gameplay):
	def __init__(self,Sharray,image,size):
		self._shape = Sharray
		self._image = image
		self._xcoor = Row_no/2
		self._ycoor = 0
		self._width = len(Sharray)
		self._height = len(Sharray[0])
		self._size = size
	def move_left(self,Xor):
		return Xor - Box_size
	def move_right(self,Xor):
		return Xor + Box_size
	def down(self,Enter,Xcoor):
		flag = 0
		index = 0
		for Iter in Enter[Xcoor]:
			if Iter == 1:
				flag = 1
				break
			index = index + 1
#		print index
		if flag == 1: return index - Box_size
		else: return Col_no - Box_size
	def move_down(self,Yor):
		return Yor + Box_size
	def clockwise(self,New_shape):
		Shape = reversed(New_shape)
		Tr_shape = list(zip(*(Shape)))
		for Xvar in range(len(Tr_shape)):
			Tr_shape[Xvar] = list(Tr_shape[Xvar])
		return Tr_shape

