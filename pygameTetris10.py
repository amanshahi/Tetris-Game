import pygame
import random
import sys
import math
import time
from board import Board
from GamePlay import Gameplay
from shape import Shapes
from Color import Colors
from Level import level

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
ShapeImage = 'rsz_158ba9c7c4de994225d55ac6d279813011428700689_full.jpg'
ShapeImage2 = 'rsz_258ba9c7c4de994225d55ac6d279813011428700689_full.jpg'
StartImage = 'rsz_images1.jpg'
Gameover = 'rsz_38928790-abstract-cartoon-clouds-for-mobile-games-background-stock-vector(1).jpg'
InstructionScreen = 'rsz_c29bf435b98b3.jpg'

def restart(quit,MainGame,Color,Shape,Game_board,Level):
	Main_Game(quit,MainGame,Color,Shape,Game_board,Level)
	
def M_screen(quit,MainGame,Color,Shape,Game_board,Level):
	StartScreen(quit,MainGame,Color,Shape,Game_board,Level)
		

def instruction(Quit,MainGame,color,Shape,Game_board,level):
#	MainGame.changeColor(Color.getRed())
	MainGame.display(InstructionScreen,Start,Start)
	while not Quit:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				Quit = True
				quit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_b:
					MainGame.changeColor(Color.getRed())
					return 0
				if event.key == pygame.K_q:
					quit()
				if event.key == pygame.K_c:
					Main_Game(Quit,MainGame,Color,Shape,Game_board,Level)
		MainGame.out_message_centered("Welcome To Global Tetris Game",Color.getGreen(),-Row_no/3 - 20)
		MainGame.out_message_centered("Instructions : ",Color.getBlack(),-Row_no/12 - 40)
		MainGame.out_message_centered("Press 'p' to pause/resume .. ",Color.getBlack(),-Row_no/12 - 10)
		MainGame.out_message_centered("Press 'r' to restart .. ",Color.getBlack(),-Row_no/12 + 20)
		MainGame.out_message_centered("Press 'a' to move the block left ..",Color.getBlack(),30)
		MainGame.out_message_centered("Press 'd' to move the block right ..",Color.getBlack(),Row_no/12 + 40)
		MainGame.out_message_centered("Press 's' to rotate the",Color.getBlack(),Col_no/8 + 60)
		MainGame.out_message_centered(" block clockwise ..",Color.getBlack(),Col_no/8 + 80)
		MainGame.out_message_centered("Press space to move",Color.getBlack(),Row_no/5 + 90)
		MainGame.out_message_centered("the block down ..",Color.getBlack(),Row_no/5 + 110)
		MainGame.out_message_centered("Press 'b' to go back ..",Color.getBlack(),Row_no/5  + 170)
		MainGame.out_message_centered("Press 'c' to play ..",Color.getBlack(),(Col_no+10)/3 + 160)
		MainGame.out_message_centered("Press 'q' to quit ..",Color.getBlack(),Row_no/2 - 15 + 170)
		MainGame.update()

def check_special(Shape):
	if Shape._shape == [[1]]:
		return True
	return False

def StartScreen(quit,MainGame,Color,Shape,Game_board,Level):
	while not quit:
		for events in pygame.event.get():
			if events.type == pygame.QUIT:
				quit()
				quit = True
			if events.type == pygame.KEYDOWN:
				if events.key == pygame.K_i:
					instruction(quit,MainGame,Color,Shape,Game_board,Level)
				elif events.key == pygame.K_c:
					Main_Game(quit,MainGame,Color,Shape,Game_board,Level)
				elif events.key == pygame.K_q:
					quit = True
		MainGame.display(StartImage,Start,Start)
		MainGame.out_message_centered("Welcome To Global Tetris Game",Color.getBlue(),-Row_no/3)
		MainGame.out_message_centered("Press 'i' for quick instructions .. ",Color.getGreen(),-Row_no/12)
		MainGame.out_message_centered("Press 'c' to play .. ",Color.getGreen(),Row_no/10)
		MainGame.out_message_centered("Press 'q' to quit .. ",Color.getGreen(),Row_no/4 - Row_no/60)
		MainGame.out_message_centered("Press 'm' to goto main screen .. ",Color.getGreen(),Row_no/4 - Row_no/60 + 35)
		MainGame.out_message_centered("Your score will be displayed here .. ",Color.getBlack(),Col_no/2)
		MainGame.out_message_centered("You get +10 points ",Color.getBlack(),Row_no/2 + 55)
		MainGame.out_message_centered("for dropping a block ..",Color.getBlack(),Row_no/2 + 85)
		MainGame.out_message_centered("You get +50 points ",Color.getBlack(),Row_no/2 + 115)
		MainGame.out_message_centered("for using special block ( 1x1 ) ..",Color.getBlack(),Row_no - 15)
		MainGame.out_message_centered("You get +100 points ",Color.getBlack(),Row_no/2 + 165)
		MainGame.out_message_centered("for clearing a row .. ",Color.getBlack(),Row_no + 45)
		MainGame.update()


def get_random(size):
	return random.randint(0,size)
def Check_box(shape,Enter,Xcoor,Ycoor):
	for Xvar in range(len(shape)):
		for Yvar in range(len(shape[0])):
			if shape[Xvar][Yvar] != 0:
				if Xcoor + Yvar*Box_size<Row_no and Ycoor + Xvar*Box_size<Col_no:
					if Enter[Xcoor + Yvar*Box_size][Ycoor + Xvar*Box_size] != 0:
						return list(zip(*shape[Xvar:]))[Yvar].count(1)
	return 0
def GameOver(Quit,MainGame,Color,Shape,Game_board,score,Level,Curr_level):
	quit_ms = False
	MainGame.display(Gameover,Start,Start)
	while not quit_ms:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				quit_ms = True
				quit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_c:
					Main_Game(Quit,MainGame,Color,Shape,Game_board,Level)
				if event.key == pygame.K_q:
					quit_ms = True
					quit()
		MainGame.out_message_centered("Game Over!",Color.getRed(),-Row_no/6)
		MainGame.out_message_centered("Press 'c' to play again .. ",Color.getBlack(),0)
		MainGame.out_message_centered("Press 'q' to quit .. ",Color.getBlack(),Row_no/15)
		MainGame.out_message_centered("Your final score was " + str(score) + " ..",Color.getBlack(),(Row_no*2)/3)
		MainGame.out_message_centered("Your reached upto level : " + str(Level[Curr_level]._level) + " ..",Color.getBlack(),(Row_no*2)/3 + 30)
		MainGame.out_message_centered("Well played.. ",Color.getBlack(),Row_no - 40)
		MainGame.update()
		clock_used.tick(FPS)
def change(Enter,Xcoor,Ycoor):
	New_enter = list(zip(*Enter))
	for Xvar in range(len(New_enter)): New_enter[Xvar] = list(New_enter[Xvar])
	del(New_enter[Ycoor:Ycoor + Box_size + 1])
	New_enter = [0]*len(New_enter[0]) + New_enter
	New = list(zip(*New_enter))
	for Xvar in range(len(New)): New[Xvar] = list(New[Xvar])
	return New
def Main_Game(Quit,MainGame,Color,Shape,Game_board,Level):
	Coor,Coor1 = [],[]
	Enter = [[0 for Xrow in range(Col_no+1)] for Yrow in range(Row_no+1)]
	Score_now = 0
	Curr_level = 0
	No_blocks = 0
	while not Quit:
		Present = 0
		getRandomShape = Shape[get_random(len(Shape) - 1)]
		Ycoor = getRandomShape._ycoor
		Xcoor = getRandomShape._xcoor
		New_shape = getRandomShape._shape
		Xc = Xcoor
		Yc = Ycoor
		prev = False
		Level_object = Level[Curr_level]
		Lev = Level[Curr_level]._level
		FPS = Level[Curr_level]._fps
		BackGroundImage = Level[Curr_level]._img
		Score_barrier = Level[Curr_level]._bar
		Flag = 0
		while not prev:
			if not Flag:
				for events in pygame.event.get():
					if events.type == pygame.QUIT:
						quit()
					elif events.type == pygame.KEYDOWN:
						if events.key == pygame.K_a or events.key == pygame.K_LEFT:
							Xcoor = getRandomShape.move_left(Xcoor)
							if Check_box(New_shape,Enter,Xcoor,Ycoor):
								Xcoor = Xcoor + Box_size
							Xcoor = max(Xcoor,0)
						elif events.key == pygame.K_q:
						  	Quit = True
						  	quit()
						elif events.key == pygame.K_m:
						  	M_screen(Quit,MainGame,Color,Shape,Game_board,Level)
						elif events.key == pygame.K_r:
						  	restart(Quit,MainGame,Color,Shape,Game_board,Level)
						elif events.key == pygame.K_p:
						  	MainGame.pause(False,Color.getWhite(),Color.getBlack(),Score_now)
						elif events.key == pygame.K_d or events.key == pygame.K_RIGHT:
							Xcoor = getRandomShape.move_right(Xcoor)
							if Check_box(New_shape,Enter,Xcoor,Ycoor):
								Xcoor = Xcoor - Box_size
							Xcoor = min(Xcoor,Row_no - len(New_shape[0])*Box_size)
						elif events.key == pygame.K_s:
							New_shape = getRandomShape.clockwise(New_shape)
							if Check_box(New_shape,Enter,Xcoor,Ycoor):
								Ycoor = Ycoor - Box_size
						elif events.key == pygame.K_SPACE:
						  	Flag = 1
					  		FPS = 1000
			if prev == 1: break
			Ycoor = getRandomShape.move_down(Ycoor)
			if Check_box(New_shape,Enter,Xcoor,Ycoor):
				Ycoor = Ycoor - Box_size*Check_box(New_shape,Enter,Xcoor,Ycoor)
				prev = True
			if Ycoor + Box_size*(len(New_shape)) >= Col_no: 
			 	Ycoor = Ycoor - (Ycoor + Box_size*(len(New_shape))) + Col_no
				prev = True
			MainGame.display(BackGroundImage,Start,Start)
			MainGame.Draw_rect(Start,Col_no,Row_no,Box_size,Color.getGreen())
			MainGame.out_message_centered("Your score is : "+str(Score_now),Color.getBlack(),Score_displace)
			MainGame.out_message_centered("Level : "+str(Curr_level+1),Color.getBlack(),Score_displace+30)
			MainGame.out_message_centered("Score to cross : "+str(Score_barrier),Color.getBlack(),Score_displace+60)
			MainGame.project(getRandomShape._image,Xcoor,Ycoor,New_shape)
			for coor in Coor:
				MainGame.display(getRandomShape._image,coor[0],coor[1])
			clock_used.tick(FPS)
			MainGame.update()
			if Xcoor == Xc and Ycoor == Yc:
			  	GameOver(Quit,MainGame,Color,Shape,Game_board,Score_now,Level,Curr_level)

		Sharray = New_shape
		Score_now = MainGame.pc_update_score(Score_now)
		Enter = MainGame.changeEnter(Sharray,Xcoor,Ycoor,Box_size,Enter)
		
		Fixed = Game_board.check_row_full(Enter)
		if len(Fixed) != 0: Score_now = MainGame.rw_update_score(Score_now)
		if Score_now > Score_barrier: 
			Score_now = 0
			Curr_level += 1
			Enter = [[0 for Xrow in range(Col_no+1)] for Yrow in range(Row_no+1)]
			Enter = Level_object.RandomShape(Enter)
		
		if check_special(getRandomShape):
			Enter = Game_board.bringDown([Ycoor]+Fixed,Enter)
			Score_now += 50
		else:
			Enter = Game_board.bringDown(Fixed,Enter)
		Coor = Game_board.getCoor(Enter,New_shape)
		MainGame.update()
MainGame = Gameplay(Row_no,Col_no,Name)
Color = Colors()
Shape =	[
		Shapes([[1,1,1,1]],ShapeImage,1),
		Shapes([[1,1],[1,1]],ShapeImage,1),
		Shapes([[0,1,0],[1,1,1]],ShapeImage,1),
		Shapes([[0,0,1],[1,1,1]],ShapeImage,1),
		Shapes([[1,0],[1,1],[0,1]],ShapeImage,1),
		Shapes([[1,1]],ShapeImage,1),
		Shapes([[1,1,1],[0,1,0],[0,1,0]],ShapeImage,1),
		Shapes([[0,1,0],[1,1,1],[0,1,0]],ShapeImage,1),
		Shapes([[1]],ShapeImage,1)
		]
Level = [
		level(1,'rsz_45979918-cartoon-winter-landscape-with-iceberg-and-ice-snow-and-cloudy-sky-seamless-vector-nature-background--stock-vector.jpg',10,200),
		level(2,'rsz_stock-vector-seamless-cartoon-volcano-desert-landscape-separated-layers-for-game-design-320153378.jpg',15,500),
		level(3,'rsz_stock-vector-vector-cartoon-landscape-arcade-game-world-wooden-fence-on-the-abstract-background-of-a-summer-127760576.jpg',20,1000),
		level(4,'rsz_z6gcfaz.png',30,1500),
		level(5,'rsz_bg_icy_feature.jpg',50,2000),
		]
Enter = []
Game_board = Board()
Enter = Game_board.get_board()
StartScreen(MainGame.getQuit(),MainGame,Color,Shape,Game_board,Level)
quit()
