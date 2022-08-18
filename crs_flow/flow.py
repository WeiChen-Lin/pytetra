def init_screen(crs, screen):
    crs.noecho()
    crs.cbreak()
    screen.keypad(True)
    crs.curs_set(0)

def end_screen(crs, screen):
    crs.nocbreak()
    screen.keypad(False)
    crs.echo()
    crs.endwin()