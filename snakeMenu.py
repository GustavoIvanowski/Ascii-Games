import curses

def snakeMenu(stdscr):
    stdscr.clear()
    size = 1
    while True:
        stdscr.addstr(5,13,'BOARD SIZE',curses.A_BOLD)
        if size == 0:
            stdscr.addstr(7,8,'SMALL', curses.A_BOLD)
            stdscr.addstr(7,15,'normal')
            stdscr.addstr(7,23,'large')
        elif size == 1:
            stdscr.addstr(7,8,'small')
            stdscr.addstr(7,15,'NORMAL', curses.A_BOLD)
            stdscr.addstr(7,23,'large')
        elif size == 2:
            stdscr.addstr(7,8,'small')
            stdscr.addstr(7,15,'normal')
            stdscr.addstr(7,23,'LARGE', curses.A_BOLD)
        stdscr.addstr(10,14, '<-   ->')
        stdscr.addstr(11,14, 'a     d')
        stdscr.addstr(13,10, 'ENTER TO CONFIRM')

        stdscr.refresh()
        inp = stdscr.getkey()

        if inp == '\n': break
        elif inp == 'a' or inp == 'KEY_LEFT':
            if size == 0: size = 2
            else: size -= 1
        elif inp == 'd' or inp == 'KEY_RIGHT':
            if size == 2: size = 0
            else: size += 1
        stdscr.clear()

    stdscr.clear()
    obstacles = False

    while True:
        stdscr.addstr(5,13,'OBSTACLES',curses.A_BOLD) # 7,12
        if obstacles:
            stdscr.addstr(7,9,'off')
            stdscr.addstr(7,23,'ON', curses.A_BOLD)
        else:
            stdscr.addstr(7,9,'OFF', curses.A_BOLD)
            stdscr.addstr(7,23,'on')
        stdscr.addstr(10,14, '<-   ->')
        stdscr.addstr(11,14, 'a     d')
        stdscr.addstr(13,10, 'ENTER TO CONFIRM')

        stdscr.refresh()
        inp = stdscr.getkey()

        if inp == '\n': break
        elif inp in 'adKEY_LEFTKEY_RIGHT':
            obstacles = not obstacles
        stdscr.clear()

    stdscr.clear()
    speed = 1

    while True:
        stdscr.addstr(5,15,'SPEED',curses.A_BOLD)
        if speed == 0:
            stdscr.addstr(7,7,'SLOW', curses.A_BOLD)
            stdscr.addstr(7,14,'normal')
            stdscr.addstr(7,22,'fast')
        elif speed == 1:
            stdscr.addstr(7,7,'slow')
            stdscr.addstr(7,14,'NORMAL', curses.A_BOLD)
            stdscr.addstr(7,22,'fast')
        elif speed == 2:
            stdscr.addstr(7,7,'slow')
            stdscr.addstr(7,14,'normal')
            stdscr.addstr(7,22,'FAST', curses.A_BOLD)
        stdscr.addstr(10,14, '<-   ->')
        stdscr.addstr(11,14, 'a     d')
        stdscr.addstr(13,10, 'ENTER TO CONFIRM')

        stdscr.refresh()
        inp = stdscr.getkey()

        if inp == '\n': break
        elif inp == 'a' or inp == 'KEY_LEFT':
            if speed == 0: speed = 2
            else: speed -= 1
        elif inp == 'd' or inp == 'KEY_RIGHT':
            if speed == 2: speed = 0
            else: speed += 1
        stdscr.clear()
    
    stdscr.clear()
    return [size, obstacles, speed]


def gameOver(stdscr, settings, score, game):
    stdscr.addstr(9,9, 'GAME OVER')
    stdscr.addstr(11,9, 'Score: '+str(score))
    stdscr.addstr(12,2, 'Q to quit, Enter to Try Again')
    while True:
        inp = stdscr.getkey()
        if inp == '\n':
            curses.wrapper(game, settings)
        elif inp == 'Q' or inp == 'q': break