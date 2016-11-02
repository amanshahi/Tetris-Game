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

class Gameplay:
	def __init__(self,row,col,title):
		self._score = 0
		self._row = row
		self._col = col
		self._pcInc = 10
		self._rwInc = 100
		self._gameSurface = pygame.display.set_mode((row,col+200))
		self.set_caption(title)
		self._font = pygame.font.SysFont(None,25)
		self.update()
		self._quit = False
	def get_gameSurface(self):
		return self._gameSurface
	def pc_update_score(self,score):
		score += self._pcInc
		return score
	def rw_update_score(self,score):
		score += self._rwInc
		return score
	def getQuit(self):
		return self._quit
	def set_caption(self,title):
		pygame.display.set_caption(title)
	def update(self):
		pygame.display.update()
	def getSurface(self): 
		return self._gameSurface
	def changeColor(self,color):
	 	self._gameSurface.fill(color)
	 	self.update()
	def out_message_centered(self,text,color,displace = 0):
		out_msg = self._font.render(text,True,color)
		display_at = out_msg.get_rect()
		display_at.center = (self._row/2, self._col/2 + displace)
		self._gameSurface.blit(out_msg,display_at)
	def image(self,name):
		return pygame.image.load(name)
	def project(self,Image,Xcoor,Ycoor,Sharray):
		Image_Load = pygame.image.load(Image)
		for i in range(len(Sharray)):
			for j in range(len(Sharray[0])):
				if Sharray[i][j] == 1:
					self._gameSurface.blit(Image_Load,(Xcoor + j*Box_size,Ycoor + i*Box_size))
				if Sharray[i][j] == -1:
					self._gameSurface.blit(Image_Load,(Xcoor - j*Box_size,Ycoor - i*Box_size))
	def display(self,Image,Xcoor,Ycoor):
		Image_load = pygame.image.load(Image)
		self._gameSurface.blit(Image_load,(Xcoor,Ycoor))
	
	def Draw_rect(self,Xcoor,Ycoor,Length,Bredth,Color):
		pygame.draw.rect(self._gameSurface,Color,(Xcoor,Ycoor,Length,Bredth))
	def changeEnter(self,Sharray,Xcoor,Ycoor,Box_size,Enter):
		New_enter = Enter
		Xrange = len(Sharray)
		Yrange = len(Sharray[0])
		for Xvar in range(Xrange):
			for Yvar in range(Yrange):
				if Sharray[Xvar][Yvar] == 1:
					if Xcoor + Yvar*Box_size < Row_no and Ycoor + Xvar*Box_size < Col_no:
						New_enter[Xcoor + Yvar*Box_size][Ycoor + Xvar*Box_size] = 1
#				if Sharray[Xvar][Yvar] == -1:
#					if Xcoor + Yvar*Box_size <=Col_no and Ycoor + Xvar*Box_size <= Row_no:
#						New_enter[Xcoor - Yvar*Box_size][Ycoor - Xvar*Box_size] = 1
		return New_enter	
	def pause(self,Quit,color1,color2,score):
		while not Quit:
			for event in pygame.event.get():
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_p:
						Quit = True
						return 0
					elif event.key == pygame.K_q:
						Quit = True
						quit()
			self.Draw_rect(Start,Start,Row_no,Col_no + Extension,color1)
			self.out_message_centered("Paused! press 'p' to resume ..",color2,0)
			self.out_message_centered("Your score is : " + str(score) + " ..",color2,30)
			self.out_message_centered("Press 'q' to quit ..",color2,60)
			self.update()
	
