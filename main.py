from graphics import Window, Line, Point

def main():
    win = Window(800, 600)

    first_line = Line(Point(0, 0), Point(800, 300))
    first_line.draw(win.canvas, "red")
    second_line = Line(Point(6, 6), Point(700, 500))
    second_line.draw(win.canvas, "black")

    win.wait_for_close()

main()