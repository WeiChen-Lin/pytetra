import time
import curses as crs
from turtle import color
from crs_flow.window import Window
from crs_flow.color import init_color
from crs_flow.flow import init_screen, end_screen

# m1 mac terminal => 158, 44
# https://blog.csdn.net/Rong_Toa/article/details/80766592
# http://slav0nic.org.ua/static/books/python/curses_module/curses_howto.html

screen = crs.initscr()

init_screen(crs, screen)

init_color(crs)

LINES, COLS = crs.LINES, crs.COLS

# border_left = Window(crs, height=LINES, width=2, begin_y=0, begin_x=0, bkgd=(True, 7))
# border_top = Window(crs, height=1, width=COLS, begin_y=0, begin_x=0, bkgd=(True, 7))
# border_right = Window(crs, height=LINES, width=2, begin_y=0, begin_x=156, bkgd=(True, 7))
# border_bottom = Window(crs, height=1, width=COLS, begin_y=LINES - 1, begin_x=0, bkgd=(True, 7))

game_site = Window(crs, height=44, width=90, begin_y=0, begin_x=34, border=True)

time.sleep(60)

end_screen(crs, screen)
