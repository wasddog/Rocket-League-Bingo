import pygame

challenges = open('challenges.txt').read().split("\n")

title = "Rocket-League Bingo"
background = pygame.image.load('img.jpg')
donateIMG = pygame.image.load('donate.png')
bingoIMG = pygame.image.load('bingo.png')

# Colors
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (178,34,34)
LIGHTBLUE = (224,255,255)

# boards
cleanBoard = [
        ["", "", "", "", ""],
        ["", "", "", "", ""],
        ["", "", "", "", ""],
        ["", "", "", "", ""],
        ["", "", "", "", ""]
    ]

# posiotons and sizes
WIDTH = 1280
HEIGHT = 720

gridPos = (75,100)

cellSizeW = 225
cellSizeH = 114

gridSizeW = cellSizeW*5
gridSizeH = cellSizeH*5

buttonPosition = (WIDTH//2 - 100, 20)
bW = 200
bH = 40

donateP = [1100, 650]
donateW = 100
donateH = 100
