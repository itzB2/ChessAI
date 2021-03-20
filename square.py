from pieces import Piece

class square():
	def __init__(self, pos=(-1,-1), index=(0,0), color=(0,0,0), piece = Piece(), selected=False, sqSize = 25):
		self.index = index
		self.color = color
		self.pos = pos
		self.piece = piece
		self.selected = selected
		self.sqSize = sqSize

	def update(self):
		self.piece.file = self.index[0]
		self.piece.rank = self.index[1]

	def __str__(self):
		return f"Selected: {self.selected}, Index: {self.index}, Position: {self.pos}, Piece: {str(self.piece)}"