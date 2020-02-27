import pygame, sys, random
from settings import *
from buttonClass import *


class App:

    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((WIDTH, HEIGHT))
        self.running = True
        self.grid = testboard
        self.selected = set()
        self.mousePos = None
        self.state = "playing"
        self.playingButtons = []
        self.endButtons = []
        self.font = pygame.font.SysFont("arial", cellSize // 2)
        self.loadButtons()

    def run(self):
        while self.running:
            if self.state == "playing":
                self.playing_events()
                self.playing_update()
                self.playing_draw()
        pygame.quit()
        sys.exit()

    #### PLAYING STATE ####

    def playing_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                selected = self.mouseOnGrid()
                if selected:
                    self.selected.add(selected)
                else:
                    print("not on board")
                    # self.selected = None

    def playing_update(self):
        self.mousePos = pygame.mouse.get_pos()
        for button in self.playingButtons:
            button.update(self.mousePos)

    def playing_draw(self):
        self.window.fill(WHITE)

        for button in self.playingButtons:
            button.draw(self.window)

        if self.selected:
            for selected in self.selected:
                self.drawSelection(self.window, selected)

        self.drawText(self.window)

        self.drawGrid(self.window)
        pygame.display.update()

    #### HELPER FUNCTIONS #####
    def drawText(self, window):
        for yidx, row in enumerate(self.grid):
            for xidx, chlng in enumerate(row):
                if chlng != "":
                    pos = [(xidx * cellSize) + gridPos[0], (yidx * cellSize) + gridPos[1]]
                    self.textToScreen(window, chlng, pos)

    def drawSelection(self, window, pos):
        pygame.draw.rect(window, RED,
                         ((pos[0] * cellSize) + gridPos[0], (pos[1] * cellSize) + gridPos[1], cellSize, cellSize))

    def drawGrid(self, window):
        pygame.draw.rect(window, BLACK, (gridPos[0], gridPos[1], WIDTH - 150, HEIGHT - 150), 2)
        for x in range(5):
            pygame.draw.line(window, BLACK, (gridPos[0] + (x * cellSize), gridPos[1]),
                             (gridPos[0] + (x * cellSize), gridPos[1] + 450))
            pygame.draw.line(window, BLACK, (gridPos[0], gridPos[1] + (x * cellSize)),
                             (gridPos[0] + 450, gridPos[1] + (x * cellSize)))

    def mouseOnGrid(self):
        if self.mousePos[0] < gridPos[0] or self.mousePos[1] < gridPos[1]:
            return False
        if self.mousePos[0] > gridPos[0] + gridSize or self.mousePos[1] > gridPos[1] + gridSize:
            return False
        return ((self.mousePos[0] - gridPos[0]) // cellSize, (self.mousePos[1] - gridPos[1]) // cellSize)

    def loadButtons(self):
        self.playingButtons.append(Button(20, 40, 100, 40))

    def textToScreen(self, window, text, pos):
        font = self.font.render(text, False, BLACK)
        window.blit(font, pos)

    def challengesGeneretor(self, challenges, board):
        for n,i in enumerate(board):
            for idx,j in enumerate(i):
                x = random.randrange(0, len(challenges))
                board[n][idx] = challenges[x]
                challenges.remove(challenges[x])
