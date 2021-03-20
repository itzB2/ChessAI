#Libraries
import pygame

pygame.init()

DISPLAY = pygame.display.set_mode((720,720))

#Own Modules
from board import Board
from utils.fen import Fen

size = DISPLAY.get_width()
dC = (255, 137, 94)
lC = (200,200,200)
sC = (247, 58, 45)
oC1 = (0, 0, 0)
oC2 = (255, 0, 0)

board = Board(size,dC,lC,sC,oC1,oC2, fen="Qq")
board.InitPieces()
board.InitSquares(lC, dC)

running = False
while not running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = True
		elif event.type == pygame.MOUSEBUTTONDOWN:
			mPos = pygame.mouse.get_pos()
			if pygame.mouse.get_pressed()[0] == 1:
				board.selectSquare(mPos)
			elif pygame.mouse.get_pressed()[1] == 1:
				#MIDDLE
				pass
			elif pygame.mouse.get_pressed()[2] == 1:
				#RMB
				pass

	board.draw(DISPLAY)
	pygame.display.update()