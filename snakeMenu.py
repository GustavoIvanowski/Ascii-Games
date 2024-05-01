import curses

def snakeMenu(stdscr):
    stdscr.clear()
    size = 1
    while True:
        stdscr.addstr(7,11,'BOARD SIZE',curses.A_BOLD)
        if size == 0:
            stdscr.addstr(9,6,'SMALL', curses.A_BOLD)
            stdscr.addstr(9,13,'normal')
            stdscr.addstr(9,21,'large')
            stdscr.addstr(12,12, '<-   ->')
            stdscr.addstr(13,12, 'a     d')
            stdscr.addstr(15,8, 'ENTER TO CONFIRM')
        elif size == 1:
            stdscr.addstr(9,6,'small')
            stdscr.addstr(9,13,'NORMAL', curses.A_BOLD)
            stdscr.addstr(9,21,'large')
        elif size == 2:
            stdscr.addstr(9,6,'small')
            stdscr.addstr(9,13,'normal')
            stdscr.addstr(9,21,'LARGE', curses.A_BOLD)
        stdscr.addstr(12,12, '<-   ->')
        stdscr.addstr(13,12, 'a     d')
        stdscr.addstr(15,8, 'ENTER TO CONFIRM')

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
        stdscr.addstr(7,12,'OBSTACLES',curses.A_BOLD)
        if obstacles:
            stdscr.addstr(9,8,'off')
            stdscr.addstr(9,21,'ON', curses.A_BOLD)
        else:
            stdscr.addstr(9,8,'OFF', curses.A_BOLD)
            stdscr.addstr(9,21,'on')
        stdscr.addstr(12,12, '<-   ->')
        stdscr.addstr(13,12, 'a     d')
        stdscr.addstr(15,8, 'ENTER TO CONFIRM')

        stdscr.refresh()
        inp = stdscr.getkey()

        if inp == '\n': break
        elif inp in 'adKEY_LEFTKEY_RIGHT':
            obstacles = not obstacles
        stdscr.clear()

    stdscr.clear()
    speed = 1

    while True:
        stdscr.addstr(7,13,'SPEED',curses.A_BOLD)
        if speed == 0:
            stdscr.addstr(9,6,'SLOW', curses.A_BOLD)
            stdscr.addstr(9,13,'normal')
            stdscr.addstr(9,22,'fast')
            stdscr.addstr(12,12, '<-   ->')
            stdscr.addstr(13,12, 'a     d')
            stdscr.addstr(15,8, 'ENTER TO CONFIRM')
        elif speed == 1:
            stdscr.addstr(9,6,'slow')
            stdscr.addstr(9,13,'NORMAL', curses.A_BOLD)
            stdscr.addstr(9,21,'fast')
        elif speed == 2:
            stdscr.addstr(9,6,'slow')
            stdscr.addstr(9,13,'normal')
            stdscr.addstr(9,21,'FAST', curses.A_BOLD)
        stdscr.addstr(12,12, '<-   ->')
        stdscr.addstr(13,12, 'a     d')
        stdscr.addstr(15,8, 'ENTER TO CONFIRM')

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