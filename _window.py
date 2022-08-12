import curses

from os import get_terminal_size

lines, cols = get_terminal_size()
# m1 mac terminal => 158, 44 
# target for 150, 40
print(lines, cols)