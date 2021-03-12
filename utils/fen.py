from pieces import Piece

class Fen():
	def __init__(self, fen):
		self.pieces = [[Piece(), Piece(), Piece(), Piece(), Piece(), Piece(), Piece(), Piece()], 
					   [Piece(), Piece(), Piece(), Piece(), Piece(), Piece(), Piece(), Piece()], 
					   [Piece(), Piece(), Piece(), Piece(), Piece(), Piece(), Piece(), Piece()], 
					   [Piece(), Piece(), Piece(), Piece(), Piece(), Piece(), Piece(), Piece()], 
					   [Piece(), Piece(), Piece(), Piece(), Piece(), Piece(), Piece(), Piece()], 
					   [Piece(), Piece(), Piece(), Piece(), Piece(), Piece(), Piece(), Piece()], 
					   [Piece(), Piece(), Piece(), Piece(), Piece(), Piece(), Piece(), Piece()], 
					   [Piece(), Piece(), Piece(), Piece(), Piece(), Piece(), Piece(), Piece()]]
		typeLookup = {'k':"King",'p':"Pawn",'n':"Knight",'b':"Bishop",'r':"Rook",'q':"Queen"}
		fenBoard = fen.split(" ")[0]
		file = 0
		rank = 7

		for char in fenBoard:
			if char =="/":
				file = 0
				rank -=1
			else:
				if char.isdigit():
					file += int(char)
				else:
					pieceColor = "White" if char.isupper() else "Black"
					pieceType = typeLookup[char.lower()]
					self.pieces[file][rank] = Piece(pieceColor, pieceType)
					file+=1
