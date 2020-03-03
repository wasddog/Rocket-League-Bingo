import pygame, random, webbrowser
from settings import *
from buttonClass import *

class App:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(title)
        self.window = pygame.display.set_mode((WIDTH, HEIGHT))
        self.running = True
        self.grid = cleanBoard
        self.selected = set()
        self.mousePos = None
        self.state = "waiting"
        self.beforeBingo = 1
        self.playingButtons = []
        self.font = pygame.font.SysFont("Comic Sans MS", 18)
        self.loadButtons()

    def run(self):
        while self.running:
            if self.state == "playing":
                self.playing_events()
                self.playing_update()
                self.playing_draw()
            if self.state == "waiting":
                self.waiting()
                self.playing_update()
                self.playing_draw()
        pygame.quit()
        #sys.exit()

    #### PLAYING STATE ####
    def playing_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                selected = self.mouseOnGrid()
                buttonClick = self.mouseOnButton()
                donateClick = self.mouseOnDonate()
                if selected:
                    self.selected.add(selected)
                    if self.beforeBingo == 1:
                        if self.findBingo(self.selected) == "BINGO":
                            self.bingoToScreen()
                            pygame.display.update()
                            pygame.time.wait(2000)
                            self.beforeBingo = 0
                if buttonClick:
                    self.state = "playing"
                    self.selected.clear()
                    self.grid = self.challengesGeneretor(challenges, cleanBoard)
                if donateClick:
                    webbrowser.open('https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=GABEG8C4PZ298&source=url')

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
                selected = self.mouseOnGrid()
                if selected:
                    try:
                        self.selected.remove(selected)
                    except:
                        pass
                else:
                    pass

    def waiting(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                buttonClick = self.mouseOnButton()
                donateClick = self.mouseOnDonate()
                if buttonClick:
                    self.state = "playing"
                    self.selected = set()
                    self.grid = self.challengesGeneretor(challenges, cleanBoard)
                if donateClick:
                    webbrowser.open('https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=GABEG8C4PZ298&source=url')

    def playing_update(self):
        self.mousePos = pygame.mouse.get_pos()
        for button in self.playingButtons:
            button.update(self.mousePos)

    def playing_draw(self):
        self.drawBackground(background, 0,0)
        self.drawGridBackground(self.window)

        for button in self.playingButtons:
            button.draw(self.window)

        if self.selected:
            for selected in self.selected:
                self.drawSelection(self.window, selected)

        self.drawText(self.window)
        self.drawGrid(self.window)
        self.donateB()
        pygame.display.update()

    #### HELPER FUNCTIONS #####
    def drawText(self, window):
        for yidx, row in enumerate(self.grid):
            for xidx, chlng in enumerate(row):
                if chlng != "":
                    pos = [(xidx * cellSizeW) + gridPos[0], (yidx * cellSizeH) + gridPos[1]]
                    self.textToScreen(window, str(chlng), pos)

    def drawSelection(self, window, pos):
        pygame.draw.rect(window, RED,
                         ((pos[0] * cellSizeW) + gridPos[0], (pos[1] * cellSizeH) + gridPos[1], cellSizeW, cellSizeH))

    def drawGridBackground(self, window):
        pygame.draw.rect(window, LIGHTBLUE,
                         (gridPos[0], gridPos[1], WIDTH - 154, HEIGHT - 150))

    def drawGrid(self, window):
        pygame.draw.rect(window, BLACK, (gridPos[0], gridPos[1], WIDTH - 154, HEIGHT - 150), 2)
        for x in range(5):
            # ||
            pygame.draw.line(window, BLACK,
                             (gridPos[0] + (x * cellSizeW), gridPos[1]),
                             (gridPos[0] + (x * cellSizeW), gridPos[1] + 570))
            # =
            pygame.draw.line(window, BLACK,
                             (gridPos[0], gridPos[1] + (x * cellSizeH)),
                             (gridPos[0] + 1125, gridPos[1] + (x * cellSizeH)))

    def mouseOnGrid(self):
        if self.mousePos[0] < gridPos[0] or self.mousePos[1] < gridPos[1]:
            return False
        if self.mousePos[0] > gridPos[0] + gridSizeW or self.mousePos[1] > gridPos[1] + gridSizeH:
            return False
        return ((self.mousePos[0] - gridPos[0]) // cellSizeW, (self.mousePos[1] - gridPos[1]) // cellSizeH)

    def mouseOnButton(self):
        if self.mousePos[0] < buttonPosition[0] or self.mousePos[1] < buttonPosition[1]:
            return False
        if self.mousePos[0] > buttonPosition[0] + bW or self.mousePos[1] > buttonPosition[1] + bH:
            return False
        return ((self.mousePos[0] - buttonPosition[0]), (self.mousePos[1] - buttonPosition[1]))

    def loadButtons(self):
        self.playingButtons.append(Button(WIDTH//2 - 100, 20, 200, 40, "Generate new bingo!"))

    def textToScreen(self, window, text, pos):
        font = self.font.render(text, True, BLACK)
        fontWidth = font.get_width()
        fontHeight = font.get_height()
        pos[0] += (cellSizeW-fontWidth)//2
        pos[1] += (cellSizeH - fontHeight) // 2
        window.blit(font, pos)

    def challengesGeneretor(self, challenges, board):
        challenges1 = challenges[:]
        for n, i in enumerate(board):
            for j in range(len(i)):
                x = random.randint(0, len(challenges1) - 1)
                board[n][j] = challenges1[x]
                challenges1.remove(challenges1[x])
        return board

    def drawBackground(self, background, xpos, ypos):
        self.window.blit(pygame.transform.scale(background, (WIDTH,HEIGHT)), [xpos, ypos])

    def donateB(self):
        self.window.blit(pygame.transform.scale(donateIMG, (donateW,donateH)), donateP)

    def mouseOnDonate(self):
        if self.mousePos[0] < donateP[0] or self.mousePos[1] < donateP[1]:
            return False
        if self.mousePos[0] > donateP[0] + donateW or self.mousePos[1] > donateP[1] + donateH:
            return False
        return ((self.mousePos[0] - donateP[0]), (self.mousePos[1] - donateP[1]))

    def findBingo(self, set):
        selected = list(set.copy())
        countX0, countX1, countX2, countX3, countX4, countY0, countY1, countY2, countY3, countY4 = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
        for i in selected:
            if i[0] == 0: countX0 += 1
            if i[0] == 1: countX1 += 1
            if i[0] == 2: countX2 += 1
            if i[0] == 3: countX3 += 1
            if i[0] == 4: countX4 += 1
        for i in selected:
            if i[1] == 0: countY0 += 1
            if i[1] == 1: countY1 += 1
            if i[1] == 2: countY2 += 1
            if i[1] == 3: countY3 += 1
            if i[1] == 4: countY4 += 1
        if countX0 == 5 or countX1 == 5 or countX2 == 5 or countX3 == 5 or countX4 == 5 or countY0 == 5 or countY1 == 5 or countY2 == 5 or countY3 == 5 or countY4 == 5:
            return "BINGO"
        if (0,0) in set and (1,1) in set and (2,2) in set and (3,3) in set and (4,4) in set or (0,4) in set and (1,3) in set and (2,2) in set and (3,1) in set and (4,0) in set:
            return "BINGO"

    def bingoToScreen(self):
        self.window.blit(pygame.transform.scale(bingoIMG, (WIDTH,HEIGHT)), [0,0])

