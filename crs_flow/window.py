class Window:
    def __init__(
        self,
        crs,
        height=0,
        width=0,
        begin_y=0,
        begin_x=0,
        border=False,
        text=None,
        bkgd= (False, ''),
    ):
        self.height = height
        self.width = width
        self.begin_y = begin_y
        self.begin_x = begin_x
        self.border = border
        self.crs = crs
        self.bkgd = bkgd
        self.draw()

    def _window(self):
        return self.crs.newwin(self.height, self.width, self.begin_y, self.begin_x)

    def draw(self):

        window = self._window()
        
        bkgd, color = self.bkgd

        if bkgd:
            window.bkgd(' ', self.crs.color_pair(color) | self.crs.A_BLINK)

        if self.border:
            window.border()

        window.refresh()
