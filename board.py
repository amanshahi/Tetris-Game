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


class Board(Gameplay):
	def __init__(self):
		self._row = Row_no
		self._col = Col_no
		self._Matrix = [[0 for Xvar in range(Col_no)] for Yvar in range(Row_no)]
	def get_board(self):
		return self._Matrix
	def check_row_full(self,Enter):
		Full = []
		Enter_rev = list(zip(*Enter))
#		print len(Enter),len(Enter[0])
		for Xvar in range(len(Enter_rev)-1):
#			print Enter_rev[310].count(1)
			if Enter_rev[Xvar].count(1) == Row_no/10:
				Full.append(Xvar)
		return Full
	def check_row_empty(self,Enter):
		Full = []
		Enter_rev = list(zip(*Enter))
		for Xvar in xrange(len(Enter_rev)):
			if not Enter_rev[Xvar].count(0) == len(Enter_rev[Xvar]):
				Full.append(Xvar)
		return Full
	def bringDown(self,Full,Enter):
		Full_row = sorted(Full)

#		print Full_row
		c = Enter
		Enter_temp = list(zip(*Enter))
		for X_r in range(len(Enter_temp)): Enter_temp[X_r] = list(Enter_temp[X_r])
		for F_r in Full_row:
#			for X_r in range(F_r,-1,-1):
#				if X_r == 0: Enter_temp[0] = [0]*len(Enter_temp[0])
#				else : Enter_temp[X_r] = Enter_temp[X_r - 1]
			del(Enter_temp[F_r:F_r+Box_size])
			Enter_temp = [[0]*Row_no]*Box_size + Enter_temp
#		print Enter_temp
		Enter_new = list(zip(*Enter_temp))
#		print len(c),len(Enter_new)
		for Yr in range(len(Enter_new)): Enter_new[Yr] = list(Enter_new[Yr])
		return Enter_new
	
	def getCoor(self,Enter,shape):
		Coor,Coor1 = [], []
		for X in range(len(Enter)):
			for Y in range(len(Enter[0])):
				if Enter[X][Y] == 1: Coor.append([X,Y,shape])
					
		return Coor
