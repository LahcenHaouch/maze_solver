from graphics import Window, Line, Point, Cell

def main():
    win = Window(800, 600)
    first_cell = Cell(100, 250, 100, 250, win)
    first_cell.draw()

    second_cell = Cell(300, 550, 300, 500, win)
    second_cell.draw()

    first_cell.draw_move(second_cell, True)

    win.wait_for_close()

main()