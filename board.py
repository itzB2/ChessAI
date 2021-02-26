#Libraries
import pygame

#Own Modules
from pieces import Piece
from utils.fen import Fen

class Move:
	def __init__(self, ss, ts):
		self.StartSquare = int(ss)
		self.TargetSquare = int(ts)

class Board:
	def __init__(self, size, darkCol, lightCol, slectedCol, fen = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"):
		self.surface = pygame.Surface((size,size))
		self.squares = [[{'color': '', 'piece': '', 'selected': False}, 
						 {'color': '', 'piece': '', 'selected': False}, 
						 {'color': '', 'piece': '', 'selected': False}, 
						 {'color': '', 'piece': '', 'selected': False}, 
						 {'color': '', 'piece': '', 'selected': False}, 
						 {'color': '', 'piece': '', 'selected': False}, 
						 {'color': '', 'piece': '', 'selected': False}, 
						 {'color': '', 'piece': '', 'selected': False}], 
						 [{'color': '', 'piece': '', 'selected': False}, 
						 {'color': '', 'piece': '', 'selected': False}, 
						 {'color': '', 'piece': '', 'selected': False}, 
						 {'color': '', 'piece': '', 'selected': False}, 
						 {'color': '', 'piece': '', 'selected': False}, 
						 {'color': '', 'piece': '', 'selected': False},
						 {'color': '', 'piece': '', 'selected': False}, 
						 {'color': '', 'piece': '', 'selected': False}], 
						 [{'color': '', 'piece': '', 'selected': False}, 
						 {'color': '', 'piece': '', 'selected': False}, 
						 {'color': '', 'piece': '', 'selected': False}, 
						 {'color': '', 'piece': '', 'selected': False}, 
						 {'color': '', 'piece': '', 'selected': False}, 
						 {'color': '', 'piece': '', 'selected': False}, 
						 {'color': '', 'piece': '', 'selected': False}, 
						 {'color': '', 'piece': '', 'selected': False}], 
						 [{'color': '', 'piece': '', 'selected': False}, 
						 {'color': '', 'piece': '', 'selected': False}, 
						 {'color': '', 'piece': '', 'selected': False}, 
						 {'color': '', 'piece': '', 'selected': False}, 
						 {'color': '', 'piece': '', 'selected': False}, 
						 {'color': '', 'piece': '', 'selected': False}, 
						 {'color': '', 'piece': '', 'selected': False}, 
						 {'color': '', 'piece': '', 'selected': False}], 
						 [{'color': '', 'piece': '', 'selected': False}, 
						 {'color': '', 'piece': '', 'selected': False}, 
						 {'color': '', 'piece': '', 'selected': False}, 
						 {'color': '', 'piece': '', 'selected': False}, 
						 {'color': '', 'piece': '', 'selected': False}, 
						 {'color': '', 'piece': '', 'selected': False}, 
						 {'color': '', 'piece': '', 'selected': False}, 
						 {'color': '', 'piece': '', 'selected': False}], 
						 [{'color': '', 'piece': '', 'selected': False}, 
						 {'color': '', 'piece': '', 'selected': False}, 
						 {'color': '', 'piece': '', 'selected': False}, 
						 {'color': '', 'piece': '', 'selected': False}, 
						 {'color': '', 'piece': '', 'selected': False}, 
						 {'color': '', 'piece': '', 'selected': False}, 
						 {'color': '', 'piece': '', 'selected': False}, 
						 {'color': '', 'piece': '', 'selected': False}], 
						 [{'color': '', 'piece': '', 'selected': False}, 
						 {'color': '', 'piece': '', 'selected': False}, 
						 {'color': '', 'piece': '', 'selected': False}, 
						 {'color': '', 'piece': '', 'selected': False}, 
						 {'color': '', 'piece': '', 'selected': False}, 
						 {'color': '', 'piece': '', 'selected': False}, 
						 {'color': '', 'piece': '', 'selected': False}, 
						 {'color': '', 'piece': '', 'selected': False}], 
						 [{'color': '', 'piece': '', 'selected': False}, 
						 {'color': '', 'piece': '', 'selected': False}, 
						 {'color': '', 'piece': '', 'selected': False}, 
						 {'color': '', 'piece': '', 'selected': False}, 
						 {'color': '', 'piece': '', 'selected': False}, 
						 {'color': '', 'piece': '', 'selected': False}, 
						 {'color': '', 'piece': '', 'selected': False}, 
						 {'color': '', 'piece': '', 'selected': False}]]
		self.sqSize = size/8
		self.drawSquares(lightCol, darkCol)
		self.currentfen = fen
		self.slectedCol = slectedCol
		self.lightCol = lightCol
		self.darkCol = darkCol
		self.canSelect = True
		self.ColourToMove = "White"

	def drawSquares(self, lightCol, darkCol):
		file = 0
		while file<8:
			rank = 0
			while rank<8:
				isLightSquare = (file + rank) % 2 != 0

				squareColor = lightCol if isLightSquare else darkCol
				position = (file*self.sqSize, rank*self.sqSize)
				self.squares[file][rank]["color"] = squareColor
				pygame.draw.rect(self.surface, self.squares[file][rank]["color"], pygame.Rect(position[0],position[1],self.sqSize,self.sqSize)) 
				rank+=1
			file+=1

	def drawPieces(self):
		pieces = Fen(self.currentfen).pieces
		file = 0
		while file<8:
			rank = 0
			while rank<8:
				self.squares[file][rank]["piece"] = pieces[file][rank]
				sprite = pieces[file][rank].sprite
				sprite = pygame.transform.smoothscale(sprite, (int(self.sqSize),int(self.sqSize)))
				pos = (int(file*self.sqSize), int(rank*self.sqSize))
				self.surface.blit(sprite, pos)
				rank+=1
			file+=1

	def getSquare(self, mPos):
		square = [0,0]
		file = 0
		while file<8:
			startPos = int(file*self.sqSize)
			endPos = int((file+1)*self.sqSize)
			# print(file, startPos, endPos, mPos[1])
			if mPos[0] <= endPos and mPos[0] >= startPos:
				square[0] = file
				break
			file+=1
		rank = 0
		while rank<8:
			startPos = int(rank*self.sqSize)
			endPos = int((rank+1)*self.sqSize)
			# print(file, startPos, endPos, mPos[0])
			if mPos[1] <= endPos and mPos[1] >= startPos:
				square[1] = rank
				break
			rank+=1
		return square

	def selectSquare(self, mPos):
		index = self.getSquare(mPos)
		isLightSquare = (index[0] + index[1]) % 2 != 0
		squareColor = self.lightCol if isLightSquare else self.darkCol

		if self.canSelect == True and self.squares[index[0]][index[1]]["selected"] == False:

			self.squares[index[0]][index[1]]["selected"] = True
			self.drawSquare(index,self.slectedCol)
			self.canSelect = False
		elif self.canSelect == False and self.squares[index[0]][index[1]]["selected"] == True:

			self.squares[index[0]][index[1]]["selected"] = False
			self.drawSquare(index, squareColor)
			self.canSelect = True

		if self.squares[index[0]][index[1]]["selected"] == True and self.squares[index[0]][index[1]]["piece"].key != "Blank":
			selectedPiece = self.squares[index[0]][index[1]]["piece"].key
			print(f"{selectedPiece} is selected")
			print(self.squares[index[0]][index[1]]["piece"].isSlidingPiece)
			self.movePiece(index)

	def drawSquare(self, index, col):
		position = (index[0]*self.sqSize, index[1]*self.sqSize)
		pygame.draw.rect(self.surface, col, pygame.Rect(position[0],position[1],self.sqSize,self.sqSize)) 

	def movePiece(self, index):
		piece = self.squares[index[0]][index[1]]["piece"]

	def draw(self,surface):
		self.drawPieces()
		surface.blit(self.surface, (0,0))

