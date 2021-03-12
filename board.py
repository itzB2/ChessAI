#Libraries
import pygame

#Own Modules
from pieces import Piece
from utils.fen import Fen

class Move:
	def __init__(self, ss, ts, piece):
		self.StartSquare = ss
		self.TargetSquare = ts
		self.piece = piece

def generateMovesForSlidingPieceLOL(piece):
	pass

class Board:
	def __init__(self, size, darkCol, lightCol, slectedCol, fen = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"):
		self.surface = pygame.Surface((size,size))
		self.squares = [[{'color': '', 'piece': '', 'selected': False, "pos": ()}, 
						 {'color': '', 'piece': '', 'selected': False, "pos": ()}, 
						 {'color': '', 'piece': '', 'selected': False, "pos": ()}, 
						 {'color': '', 'piece': '', 'selected': False, "pos": ()}, 
						 {'color': '', 'piece': '', 'selected': False, "pos": ()}, 
						 {'color': '', 'piece': '', 'selected': False, "pos": ()}, 
						 {'color': '', 'piece': '', 'selected': False, "pos": ()}, 
						 {'color': '', 'piece': '', 'selected': False, "pos": ()}], 
						 [{'color': '', 'piece': '', 'selected': False, "pos": ()}, 
						 {'color': '', 'piece': '', 'selected': False, "pos": ()}, 
						 {'color': '', 'piece': '', 'selected': False, "pos": ()}, 
						 {'color': '', 'piece': '', 'selected': False, "pos": ()}, 
						 {'color': '', 'piece': '', 'selected': False, "pos": ()}, 
						 {'color': '', 'piece': '', 'selected': False, "pos": ()},
						 {'color': '', 'piece': '', 'selected': False, "pos": ()}, 
						 {'color': '', 'piece': '', 'selected': False, "pos": ()}], 
						 [{'color': '', 'piece': '', 'selected': False, "pos": ()}, 
						 {'color': '', 'piece': '', 'selected': False, "pos": ()}, 
						 {'color': '', 'piece': '', 'selected': False, "pos": ()}, 
						 {'color': '', 'piece': '', 'selected': False, "pos": ()}, 
						 {'color': '', 'piece': '', 'selected': False, "pos": ()}, 
						 {'color': '', 'piece': '', 'selected': False, "pos": ()}, 
						 {'color': '', 'piece': '', 'selected': False, "pos": ()}, 
						 {'color': '', 'piece': '', 'selected': False, "pos": ()}], 
						 [{'color': '', 'piece': '', 'selected': False, "pos": ()}, 
						 {'color': '', 'piece': '', 'selected': False, "pos": ()}, 
						 {'color': '', 'piece': '', 'selected': False, "pos": ()}, 
						 {'color': '', 'piece': '', 'selected': False, "pos": ()}, 
						 {'color': '', 'piece': '', 'selected': False, "pos": ()}, 
						 {'color': '', 'piece': '', 'selected': False, "pos": ()}, 
						 {'color': '', 'piece': '', 'selected': False, "pos": ()}, 
						 {'color': '', 'piece': '', 'selected': False, "pos": ()}], 
						 [{'color': '', 'piece': '', 'selected': False, "pos": ()}, 
						 {'color': '', 'piece': '', 'selected': False, "pos": ()}, 
						 {'color': '', 'piece': '', 'selected': False, "pos": ()}, 
						 {'color': '', 'piece': '', 'selected': False, "pos": ()}, 
						 {'color': '', 'piece': '', 'selected': False, "pos": ()}, 
						 {'color': '', 'piece': '', 'selected': False, "pos": ()}, 
						 {'color': '', 'piece': '', 'selected': False, "pos": ()}, 
						 {'color': '', 'piece': '', 'selected': False, "pos": ()}], 
						 [{'color': '', 'piece': '', 'selected': False, "pos": ()}, 
						 {'color': '', 'piece': '', 'selected': False, "pos": ()}, 
						 {'color': '', 'piece': '', 'selected': False, "pos": ()}, 
						 {'color': '', 'piece': '', 'selected': False, "pos": ()}, 
						 {'color': '', 'piece': '', 'selected': False, "pos": ()}, 
						 {'color': '', 'piece': '', 'selected': False, "pos": ()}, 
						 {'color': '', 'piece': '', 'selected': False, "pos": ()}, 
						 {'color': '', 'piece': '', 'selected': False, "pos": ()}], 
						 [{'color': '', 'piece': '', 'selected': False, "pos": ()}, 
						 {'color': '', 'piece': '', 'selected': False, "pos": ()}, 
						 {'color': '', 'piece': '', 'selected': False, "pos": ()}, 
						 {'color': '', 'piece': '', 'selected': False, "pos": ()}, 
						 {'color': '', 'piece': '', 'selected': False, "pos": ()}, 
						 {'color': '', 'piece': '', 'selected': False, "pos": ()}, 
						 {'color': '', 'piece': '', 'selected': False, "pos": ()}, 
						 {'color': '', 'piece': '', 'selected': False, "pos": ()}], 
						 [{'color': '', 'piece': '', 'selected': False, "pos": ()}, 
						 {'color': '', 'piece': '', 'selected': False, "pos": ()}, 
						 {'color': '', 'piece': '', 'selected': False, "pos": ()}, 
						 {'color': '', 'piece': '', 'selected': False, "pos": ()}, 
						 {'color': '', 'piece': '', 'selected': False, "pos": ()}, 
						 {'color': '', 'piece': '', 'selected': False, "pos": ()}, 
						 {'color': '', 'piece': '', 'selected': False, "pos": ()}, 
						 {'color': '', 'piece': '', 'selected': False, "pos": ()}]]
		self.sqSize = size/8
		self.currentfen = fen
		self.slectedCol = slectedCol
		self.lightCol = lightCol
		self.darkCol = darkCol
		self.canSelect = True
		self.ColourToMove = "White"
		self.selectedSquare = [-1,-1]

	def InitSquares(self, lightCol, darkCol):
		file = 0
		while file<8:
			rank = 0
			while rank<8:
				isLightSquare = (file + rank) % 2 != 0

				squareColor = lightCol if isLightSquare else darkCol
				position = (file*self.sqSize, rank*self.sqSize)
				self.squares[file][rank]["color"] = squareColor
				self.squares[file][rank]["pos"] = position
				pygame.draw.rect(self.surface, self.squares[file][rank]["color"], pygame.Rect(position[0],position[1],self.sqSize,self.sqSize)) 
				rank+=1
			file+=1

	def InitPieces(self):
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
			self.selectedSquare = index
			self.canSelect = False

		elif self.canSelect == False and self.squares[index[0]][index[1]]["selected"] == True:

			self.squares[index[0]][index[1]]["selected"] = False
			self.selectedSquare = [-1,-1]
			self.canSelect = True

		if self.canSelect == False and self.squares[index[0]][index[1]]["selected"] == False and self.squares[index[0]][index[1]]["piece"].key == "Blank":
			move = Move(self.selectedSquare, index, self.squares[self.selectedSquare[0]][self.selectedSquare[1]]["piece"])
			self.movePiece(move)
			self.selectedSquare = [-1,-1]
			self.canSelect = True

	def drawPieces(self):
		pieces = self.squares
		file = 0
		while file<8:
			rank = 0
			while rank<8:
				sprite = pieces[file][rank]["piece"].sprite
				sprite = pygame.transform.smoothscale(sprite, (int(self.sqSize),int(self.sqSize)))
				pos = (int(file*self.sqSize), int(rank*self.sqSize))
				self.surface.blit(sprite, pos)
				rank+=1
			file+=1

	def drawSquare(self, index, col):
		position = (index[0]*self.sqSize, index[1]*self.sqSize)
		pygame.draw.rect(self.surface, col, pygame.Rect(position[0],position[1],self.sqSize,self.sqSize)) 

	def drawSquares(self):
		for row in self.squares:
			for square in row:
				# color = self.slectedCol if square["selected"] else square["color"]
				color = square["color"]
				pygame.draw.rect(self.surface, color, pygame.Rect(square["pos"][0],square["pos"][1],self.sqSize,self.sqSize)) 

	def clearSquare(self, index):
		file = index[0]
		rank = index[1]
		position = (file*self.sqSize, rank*self.sqSize)
		pygame.draw.rect(self.surface, self.squares[file][rank]["color"], pygame.Rect(position[0],position[1],self.sqSize,self.sqSize)) 

	def movePiece(self, moveObject):
		index = moveObject.StartSquare
		piece = moveObject.piece
		def move(move):
			self.clearSquare(index)
			self.squares[index[0]][index[1]]["selected"] = False
			self.squares[index[0]][index[1]]["piece"] = Piece()
			self.squares[moveObject.TargetSquare[0]][moveObject.TargetSquare[1]]["piece"] = piece

		if piece.color == self.ColourToMove:
			move(moveObject)
			self.ColourToMove = "Black" if piece.color == "White" else "White"

	def draw(self,surface):
		self.drawSquares()
		self.drawPieces()
		surface.blit(self.surface, (0,0))

