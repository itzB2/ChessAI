#Libraries
import pygame

#Own Modules
from pieces import Piece
from utils.fen import Fen
from square import square

def clamp(num, min_value, max_value):
	return max(min(num, max_value), min_value)

directionOffsets = [8,-8,-1,1,7,-7,9,-9]
numSquaresToEdge = []
numSquaresToEdge = [i*0 for i in range(0,72)]

for file in range(8):
	for rank in range(8):
		numNorth = 7 - rank
		numSouth = rank
		numWest = file
		numEast = 7 - file

		squareIndex = rank*8+file

		numSquaresToEdge[squareIndex] = [numNorth, numSouth, numWest, numEast, min(numNorth, numWest), min(numSouth, numEast), min(numNorth, numEast),  min(numNorth, numEast), min(numSouth, numWest)]


class Move:
	def __init__(self, ss, ts, piece):
		self.StartSquare = ss
		self.TargetSquare = ts
		self.piece = piece

	def __repr__(self):
		return f"Start Square: {self.StartSquare}, End Square: {self.TargetSquare}, Piece: {str(self.piece)},"

class Board:
	def __init__(self, size, darkCol, lightCol, slectedCol, overlayCol1, overlayCol2, fen = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"):
		self.surface = pygame.Surface((size,size))
		self.sqSize = size/8
		self.squares = [[square(sqSize=self.sqSize) if j==0 else square(sqSize=self.sqSize) for j in range(0,8)] for i in range(0,8)]
		self.currentfen = fen
		self.slectedCol = slectedCol
		self.lightCol = lightCol
		self.darkCol = darkCol
		self.overlayCol1 = overlayCol1
		self.overlayCol2 = overlayCol2
		self.canSelect = True
		self.ColourToMove = "White"
		self.selectedSquare = None

	def InitSquares(self, lightCol, darkCol):
		file = 0
		while file<8:
			rank = 0
			while rank<8:
				isLightSquare = (file + rank) % 2 != 0

				squareColor = lightCol if isLightSquare else darkCol
				position = (file*self.sqSize, rank*self.sqSize)
				self.squares[file][rank].color = squareColor
				self.squares[file][rank].pos = position
				pygame.draw.rect(self.surface, self.squares[file][rank].color, pygame.Rect(position[0],position[1],self.sqSize,self.sqSize)) 
				rank+=1
			file+=1

	def InitPieces(self):
		pieces = Fen(self.currentfen).pieces
		file = 0
		while file<8:
			rank = 0
			while rank<8:
				self.squares[file][rank].piece = pieces[file][rank]
				self.squares[file][rank].piece.generateMoves()
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
		overlayColor = self.overlayCol2 if isLightSquare else self.overlayCol1
		square = self.squares[index[0]][index[1]]
		MOVES = self.GenerateMoves(index[0]*8+index[1])
		try:
			selectedSquare = self.squares[self.selectedSquare[0]][self.selectedSquare[1]]
		except:
			pass

		if self.canSelect == True and square.selected == False:
			if square.piece.color == self.ColourToMove:
				square.selected = True
				self.selectedSquare = index
				self.canSelect = False
				for move in MOVES:
					ts = move.TargetSquare
					SquareHighlight = self.squares[ts[0]][ts[1]]
					SquareHighlight.color = overlayColor

		elif self.canSelect == False and square.selected == True:

			square.selected = False
			self.selectedSquare = [-1,-1]
			self.canSelect = True

		elif self.canSelect == False and self.squares[index[0]][index[1]].selected == False and self.squares[index[0]][index[1]].piece.key == "Blank":
			move = Move(self.selectedSquare, index, self.squares[self.selectedSquare[0]][self.selectedSquare[1]].piece)
			self.movePiece(move, MOVES)
			self.selectedSquare = [-1,-1]
			self.canSelect = True


	def drawPieces(self):
		pieces = self.squares
		file = 0
		while file<8:
			rank = 0
			while rank<8:
				sprite = pieces[file][rank].piece.sprite
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
				color = self.slectedCol if square.selected else square.color
				pygame.draw.rect(self.surface, color, pygame.Rect(square.pos[0],square.pos[1],self.sqSize,self.sqSize)) 

	def clearSquare(self, index):
		file = index[0]
		rank = index[1]
		position = (file*self.sqSize, rank*self.sqSize)
		pygame.draw.rect(self.surface, self.squares[file][rank].color, pygame.Rect(position[0],position[1],self.sqSize,self.sqSize)) 

	def movePiece(self, moveObject, moves):
		print("Moving in progress")
		index = moveObject.StartSquare
		piece = moveObject.piece
		def move(move, moves):
			for i in moves:
				# print(i)
				print(i.TargetSquare[0], moveObject.TargetSquare[0], i.TargetSquare[1], moveObject.TargetSquare[1])
				if i.TargetSquare[0] == moveObject.TargetSquare[0] and i.TargetSquare[1] == moveObject.TargetSquare[1]:
					self.clearSquare(index)
					self.squares[index[0]][index[1]].selected = False
					self.squares[index[0]][index[1]].piece = Piece()
					self.squares[moveObject.TargetSquare[0]][moveObject.TargetSquare[1]].piece = piece

		if piece.color == self.ColourToMove:
			move(moveObject, moves)
			self.ColourToMove = "Black" if piece.color == "White" else "White"

	def GenerateMoves(self, index):
		moves = []
		# for startSquare in range(64):
		# 	piece = self.squares[int(startSquare/8)][int(startSquare%8)].piece
		# 	if piece.color == self.ColourToMove:
		# 		if piece.isSlidingPiece:
		# 			moves = self.GenerateSlidingMoves(startSquare, piece)
		startSquare = index
		piece = self.squares[int(startSquare/8)][int(startSquare%8)].piece
		if piece.color == self.ColourToMove:
			if piece.isSlidingPiece:
				moves = self.GenerateSlidingMoves(startSquare, piece)

		return moves

	def GenerateSlidingMoves(self, startSquare, piece):
		moves = []
		StartDirIndex = 4 if piece.type == "Bishop" else 0
		EndDirIndex   = 4 if piece.type == "Rook" else 8
		for directionIndex in range(StartDirIndex, EndDirIndex):
			for n in range(numSquaresToEdge[startSquare][directionIndex]):
				targetSquare = startSquare+directionOffsets[directionIndex]*(n+1)
				pieceOnTargetSquare = self.squares[int(targetSquare/8)][int(targetSquare%8)].piece

				if piece.color == pieceOnTargetSquare.color and piece.key == pieceOnTargetSquare.key:
					break

				# print(int(startSquare/8), int(startSquare%8))
				moves.append(Move([int(startSquare/8), int(startSquare%8)], [int(targetSquare/8), int(targetSquare%8)], piece))

				if piece.color != pieceOnTargetSquare.color and piece.key == pieceOnTargetSquare.key:
					#TODO: ADD POINTS
					break
		return moves

	def draw(self,surface):
		self.drawSquares()
		self.drawPieces()
		surface.blit(self.surface, (0,0))

