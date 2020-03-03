import pygame

challenges = [
    "Some1 asks for Trade",
    "Pre-flip goal",
    "3 Minute overtime",
    "Get into rule no.1",
    "Team pinch goal",
    "Score a Hat trick",
    "Low five",
    "PassingPlay goal",
    "Fake an opponent",
    "Get a lag indicator",
    "Opponent has anime PFP",
    "Someone own-goals",
    "FREEEEEEE",
    "Make an epic save",
    "Double tap goal",
    "Someone misses open net",
    "Flip reset goal",
    "Ceiling shot",
    "Musty flip goal",
    "You/teammate whiffs",
    "Toxicity in chat",
    "Opponent using weird car",
    "Opponents RageQuit(ff)",
    "Demo 2 in a row",
    "Bump/demo goal",
    "Comeback (3 points or more)",
    "Last second goal",
    "Score 120kmh+ goal",
    "PoolShot Goal",
    "Win with 7-1 score",
    "Turtle Goal",
    "AirDribble Goal",
    "Everyone miss the kickoff",
    "Score a Kick-off goal",
    "Score a reverse goal"
]

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
