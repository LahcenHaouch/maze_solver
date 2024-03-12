from graphics import Window
from maze import Maze


def main():
    win = Window(800, 600)

    num_cols = 12
    num_rows = 10

    m1 = Maze(20, 20, num_rows, num_cols, 50, 50, win)
    m1._break_entrance_and_exit()
    m1._break_walls_r(1, 1)

    win.wait_for_close()


main()
