from tkinter import Tk, BOTH, Canvas

class Window():
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.__root = Tk()
        self.__root.title("Maze Solver")
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
        self.canvas = Canvas(self.__root, bg="white", height=height, width=width)
        self.canvas.pack(fill=BOTH, expand=1)
        self.running = False
    
    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.running = True
        
        while self.running:
            self.redraw()

    def close(self):
        self.running = False


class Point():
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

class Line():
    def __init__(self, a: Point, b: Point):
        self.a = a
        self.b = b

    def draw(self, canvas: Canvas, fill_color: str):
        canvas.create_line(self.a.x, self.a.y, self.b.x, self.b.y, fill=fill_color, width=2)
        canvas.pack(fill=BOTH, expand=1)

class Cell():
    def __init__(self, x1: int, x2: int, y1: int, y2: int, win: Window):
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
