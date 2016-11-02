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

class Colors:
	def __init__(self):
		self._blue = (0,0,255)
		self._red = (255,0,0)
		self._green = (0,255,0)
		self._white = (255,255,255)
		self._black =  (0,0,0)
		self._lightBlue = (0,0,100)
	def getRed(self): 
		return self._red
	def getBlue(self):
		return self._blue
	def getGreen(self): 
		return self._green
	def getWhite(self): 
		return self._white
	def getLightBlue(self):
		return self._lightBlue
	def getBlack(self):
		return self._black