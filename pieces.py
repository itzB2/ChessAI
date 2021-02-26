#Libraries
import pygame as pg
import os

p = {"White King":pg.image.load(os.path.join("Sprites", "White King.png")).convert_alpha(),
	 "White Queen":pg.image.load(os.path.join("Sprites", "White Queen.png")).convert_alpha(),
	 "White Bishop":pg.image.load(os.path.join("Sprites", "White Bishop.png")).convert_alpha(),
	 "White Knight":pg.image.load(os.path.join("Sprites", "White Knight.png")).convert_alpha(),
	 "White Rook":pg.image.load(os.path.join("Sprites", "White Rook.png")).convert_alpha(),
	 "White Pawn":pg.image.load(os.path.join("Sprites", "White Pawn.png")).convert_alpha(),
	 "Black King":pg.image.load(os.path.join("Sprites", "Black King.png")).convert_alpha(),
	 "Black Queen":pg.image.load(os.path.join("Sprites", "Black Queen.png")).convert_alpha(),
	 "Black Bishop":pg.image.load(os.path.join("Sprites", "Black Bishop.png")).convert_alpha(),
	 "Black Knight":pg.image.load(os.path.join("Sprites", "Black Knight.png")).convert_alpha(),
	 "Black Rook":pg.image.load(os.path.join("Sprites", "Black Rook.png")).convert_alpha(),
	 "Black Pawn":pg.image.load(os.path.join("Sprites", "Black Pawn.png")).convert_alpha(),
	 "Blank":pg.image.load(os.path.join("Sprites", "blank.png")).convert_alpha()
	}

class Piece:
	def __init__(self, color, pType):
		key = ""

		self.color = color
		self.type = pType
		self.isSlidingPiece = True if pType == "Queen" or pType == "Rook" or pType == "Bishop" else False

		if color == "White":
			key = key+"White "
		elif color == "Black":
			key = key+"Black "

		if pType == "King":
			key = key+"King"
		elif pType == "Queen":
			key = key+"Queen"
		elif pType == "Bishop":
			key = key+"Bishop"
		elif pType == "Knight":
			key = key+"Knight"
		elif pType == "Rook":
			key = key+"Rook"
		elif pType == "Pawn":
			key = key+"Pawn"

		if color == "" and pType == "":
			key = "Blank"

		self.key = key
		self.sprite = p[key]
