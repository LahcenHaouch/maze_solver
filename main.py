from graphics import Window
from maze import Maze


def main():
    win = Window(800, 600)
    # first_cell = Cell(100, 250, 100, 250, win)
    # first_cell.draw()

    # second_cell = Cell(300, 550, 300, 500, win)
    # second_cell.draw()

    # first_cell.draw_move(second_cell, True)
    num_cols = 12
    num_rows = 10

    m1 = Maze(20, 20, num_rows, num_cols, 50, 50, win)
    m1._break_entrance_and_exit()

    win.wait_for_close()


main()
