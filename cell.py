from graphics import Window, Line, Point


class Cell:
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
        top_wall = Line(
            Point(self._x1, self._y1), Point(self._x2, self._y1), self._win.canvas
        )
        if self.has_top_wall:
            top_wall.draw("black")
        else:
            top_wall.draw("#d9d9d9")

        right_wall = Line(
            Point(self._x2, self._y1), Point(self._x2, self._y2), self._win.canvas
        )
        if self.has_right_wall:
            right_wall.draw("black")
        else:
            right_wall.draw("#d9d9d9")

        bottom_wall = Line(
            Point(self._x1, self._y2), Point(self._x2, self._y2), self._win.canvas
        )
        if self.has_bottom_wall:
            bottom_wall.draw("black")
        else:
            bottom_wall.draw("#d9d9d9")

        left_wall = Line(
            Point(self._x1, self._y1), Point(self._x1, self._y2), self._win.canvas
        )
        if self.has_left_wall:
            left_wall.draw("black")
        else:
            left_wall.draw("#d9d9d9")

    def draw_move(self, to_cell, undo=False):
        color = "red"
        if undo:
            color = "gray"

        line = Line(
            Point((self._x2 + self._x1) / 2, (self._y2 + self._y1) / 2),
            Point((to_cell._x2 + to_cell._x1) / 2, (to_cell._y2 + to_cell._y1) / 2),
        )
        line.draw(self._win.canvas, color)
