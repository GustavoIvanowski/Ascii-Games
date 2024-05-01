class Board:
    def __init__(self, dimension=17, obs=False):
        self.matrix = []
        self.fruitSpace = []
        if obs: self.obsSpace = [(99,99)]
        else: self.obsSpace = False
        self.score = 0

        for i in range(dimension):
            self.matrix.append([0]*dimension)
            for j in range(dimension):
                self.fruitSpace.append((i,j))
                if self.obsSpace: self.obsSpace.append((i,j))
        if self.obsSpace: self.obsSpace.remove((99,99))

    def render(self):
        dim = len(self.matrix)
        screen = ''

        screen += '+' + '- ' * dim + '+ \n'
        for i in range(dim):
            screen += '|'
            for j in range(dim):
                if self.matrix[i][j] == 0: screen += '  '
                elif self.matrix[i][j] == 1: screen += 'x '
                elif self.matrix[i][j] == 2: screen += 'o '
                elif self.matrix[i][j] == 3: screen += '# '
            screen += '| \n'
        screen += '+' + '- ' * dim + '+ \n'

        return screen

class Snake:
    def __init__(self, board):

        if len(board.matrix) == 10:
            self.coords = [(5,1),(5,2),(5,3)]
            board.matrix[5][7] = 2
            board.fruitSpace.remove((5,7))
            if board.obsSpace: board.obsSpace.remove((5,7))
        elif len(board.matrix) == 17:
            self.coords = [(8,1),(8,2),(8,3)]
            board.matrix[8][12] = 2
            board.fruitSpace.remove((8,12))
            if board.obsSpace: board.obsSpace.remove((8,12))
        else:
            self.coords = [(12,1),(12,2),(12,3)]
            board.matrix[12][18] = 2
            board.fruitSpace.remove((12,18))
            if board.obsSpace: board.obsSpace.remove((12,18))

        for i in self.coords:
            if board.obsSpace: board.obsSpace.remove(i)
            board.fruitSpace.remove(i)
            temp = list(i)
            board.matrix[temp[0]][temp[1]] = 1

    def advance(self, direction, board):

        new = list(self.coords[-1])
        if direction == 'w': new[0] -= 1
        elif direction == 'a': new[1] -= 1
        elif direction == 's': new[0] += 1
        elif direction == 'd': new[1] += 1

        if new[0] < 0 or new[1] < 0: return False
        
        try: 
            if board.matrix[new[0]][new[1]] == 2: 
                generateFruit(board)
            else:
                if board.obsSpace: board.obsSpace.remove(tuple(new))
                back = list(self.coords.pop(0))
                board.matrix[back[0]][back[1]] = 0
                board.fruitSpace.append(tuple(back))
                if board.obsSpace: board.obsSpace.append(tuple(back))

            if tuple(new) in self.coords: return False
            if board.matrix[new[0]][new[1]] == 3: return False
            self.coords.append(tuple(new))
            board.matrix[new[0]][new[1]] = 1
            if tuple(new) in board.fruitSpace: board.fruitSpace.remove(tuple(new))
        except: return False

        return True
        
from random import choice
def generateFruit(board):
    new = choice(board.fruitSpace)
    board.fruitSpace.remove(new)
    new = list(new)
    board.matrix[new[0]][new[1]] = 2
    board.score += 1
    if board.score % 2 == 1 and board.obsSpace: generateObs(board)

def generateObs(board):
    new = choice(board.obsSpace)
    board.obsSpace.remove(new)
    new = list(new)
    board.matrix[new[0]][new[1]] = 3

import curses
from time import sleep
from threading import Thread
from snakeMenu import snakeMenu, gameOver

def main(stdscr, settings=False):
    if not settings: settings = snakeMenu(stdscr)

    if settings[0] == 0: b = Board(dimension=10, obs=settings[1])
    elif settings[0] == 1: b = Board(dimension=17, obs=settings[1])
    elif settings[0] == 2: b = Board(dimension=25, obs=settings[1])

    if settings[2] == 0: speed = 0.18
    elif settings[2] == 1: speed = 0.13
    elif settings[2] == 2: speed = 0.08

    stdscr.clear()
    stdscr.addstr(9,13,'SNAKE',curses.A_BOLD)
    stdscr.refresh()
    sleep(2)
    stdscr.clear()
    s = Snake(b)
    dQueue = ['d']
    stdscr.addstr(b.render())

    def game():
        global playing
        playing = True
        while True:
            sleep(speed)
            if len(dQueue) > 1: dQueue.pop(0)
            if not s.advance(dQueue[0], b):playing = False; break
            stdscr.clear()
            stdscr.addstr(b.render())
            stdscr.addstr("Score: "+str(b.score))
            stdscr.refresh()

    Thread(target=game).start()

    while playing:
        inp = stdscr.getkey()
        if (inp == 'w' or inp == 'KEY_UP') and dQueue[-1] in 'adKEY_LEFTKEY_RIGHT': dQueue.append('w')
        elif (inp == 'a' or inp == 'KEY_LEFT') and dQueue[-1] in 'wsKEY_UPKEY_DOWN': dQueue.append('a')
        elif (inp == 's' or inp == 'KEY_DOWN') and dQueue[-1] in 'adKEY_LEFTKEY_RIGHT': dQueue.append('s')
        elif (inp == 'd' or inp == 'KEY_RIGHT') and dQueue[-1] in 'wsKEY_UPKEY_DOWN': dQueue.append('d')

    stdscr.clear()
    gameOver(stdscr, settings, b.score, main)
    
curses.wrapper(main)
