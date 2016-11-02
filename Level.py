import pygame
import random
import sys
import math
import time

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

class level:
	def __init__(self,Level,Img,FPS,Bar):
		self._level = Level
		self._img = Img
		self._fps = FPS
		self._bar = Bar
	def RandomShape(self,Enter):
		Random = self._fps
		for Xrandom in range(Random):
			X = random.randint(Start,Row_no/10)
			Y = random.randint(Row_no/10,Row_no/10 + 1)
			Enter[X*10][Y*10] = 1
		return Enter