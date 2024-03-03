from graphics import Window, Line, Point, Cell

def main():
    win = Window(800, 600)
    cell = Cell(100, 250, 100, 250, win)
    cell.draw()

    win.wait_for_close()

main()