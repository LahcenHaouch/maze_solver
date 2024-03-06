from graphics import Window, Line, Point

class Cell():
    def __init__(self, x1: int, x2: int, y1: int, y2: int, win: Window = None):
        self.has_top_wall = True
        self.has_right_wall = True
        self.has_bottom_wall = True
        self.has_left_wall = True
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        self._win = win

    def draw(self):
        if self.has_top_wall:
            line = Line(Point(self._x1, self._y1), Point(self._x2, self._y1))
            line.draw(self._win.canvas, "black")
        if self.has_right_wall:
            line = Line(Point(self._x2, self._y1), Point(self._x2, self._y2))
            line.draw(self._win.canvas, "black")
        if self.has_bottom_wall:
            line = Line(Point(self._x1, self._y2), Point(self._x2, self._y2))
            line.draw(self._win.canvas, "black")        
        if self.has_left_wall:
            line = Line(Point(self._x1, self._y1), Point(self._x1, self._y2))
            line.draw(self._win.canvas, "black")

    def draw_move(self, to_cell, undo=False):
        color = "red"
        if undo:
            color = "gray"
        
        line = Line(Point((self._x2 + self._x1) / 2, (self._y2 + self._y1) / 2), Point((to_cell._x2 + to_cell._x1) / 2, (to_cell._y2 + to_cell._y1) / 2))
        line.draw(self._win.canvas, color)