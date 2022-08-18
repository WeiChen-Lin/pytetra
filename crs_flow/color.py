


def init_color(crs):

    crs.start_color()
    crs.use_default_colors()

    #Define colors
    if crs.can_change_color():
        crs.init_color(1, 1000, 0, 0)
        crs.init_color(2, 0, 1000, 0)
        crs.init_color(3, 1000, 1000, 0)
        crs.init_color(4, 0, 0, 1000)
        crs.init_color(5, 1000, 500, 1000)
        crs.init_color(6, 500, 500, 1000)
        crs.init_color(7, 862, 862, 862)
        
    crs.init_pair(1, -1, 1)
    crs.init_pair(2, -1, 2)
    crs.init_pair(3, -1, 3)
    crs.init_pair(4, -1, 4)
    crs.init_pair(5, -1, 5)
    crs.init_pair(6, -1, 6)
    crs.init_pair(7, -1, 7)