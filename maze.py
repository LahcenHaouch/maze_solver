from typing import List
from time import sleep
import random

from graphics import Window
from cell import Cell


class Maze:
    def __init__(
        self,
        x1: int,
        y1: int,
        num_rows: int,
        num_cols: int,
        cell_size_x: int,
        cell_size_y: int,
        win: Window = None,
        seed=None,
    ):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        if seed is not None:
            random.seed(seed)

        self.seed = seed
        self._create_cells()

    def _create_cells(self):
        self._cells: List[List[Cell]] = []
        for i in range(self.num_cols):
            col = []
            for j in range(self.num_rows):
                x1 = self.x1 + i * self.cell_size_x
                y1 = self.y1 + j * self.cell_size_y

                cell = Cell(
                    x1,
                    x1 + self.cell_size_x,
                    y1,
                    y1 + self.cell_size_y,
                    self.win,
                )
                col.append(cell)
                self._draw_cell_no_cd(cell)

            self._cells.append(col)

    def _draw_cell_no_cd(self, cell: Cell):
        if self.win is None:
            return

        cell.draw()
        self._animate()

    def _draw_cell(self, i: int, j: int):
        if self.win is None:
            return

        cell = self._cells[i][j]
        cell.draw()
        self._animate()

    def _animate(self):
        self.win.redraw()
        sleep(0.05)

    def _break_entrance_and_exit(self):
        start = self._cells[0][0]
        start.has_top_wall = False
        self._draw_cell_no_cd(start)

        exit = self._cells[self.num_cols - 1][self.num_rows - 1]
        exit.has_bottom_wall = False
        self._draw_cell_no_cd(exit)

    def _reset_cells_visited(self):
        for i in range(self.num_cols):
            for j in range(self.num_rows):
                self._cells[i][j].visited = False

    def _break_walls_r(self, i: int, j: int):
        cell = self._cells[i][j]
        cell.visited = True

        while True:
            possible_directions = []

            top = (
                self._cells[i][j - 1] if j - 1 >= 0 and j - 1 < self.num_rows else None
            )
            right = (
                self._cells[i + 1][j] if i + 1 >= 0 and i + 1 < self.num_cols else None
            )
            bottom = (
                self._cells[i][j + 1] if j + 1 >= 0 and j + 1 < self.num_rows else None
            )
            left = (
                self._cells[i - 1][j] if i - 1 >= 0 and i - 1 < self.num_cols else None
            )

            if top is not None and not top.visited:
                possible_directions.append(["top", i, j - 1])
            if right is not None and not right.visited:
                possible_directions.append(["right", i + 1, j])
            if bottom is not None and not bottom.visited:
                possible_directions.append(["bottom", i, j + 1])
            if left is not None and not left.visited:
                possible_directions.append(["left", i - 1, j])

            if len(possible_directions) == 0:
                cell.draw()
                return

            random_direction = possible_directions[
                random.randrange(0, len(possible_directions))
            ]

            direction = random_direction[0]

            if direction == "top":
                cell.has_top_wall = False
                top.has_bottom_wall = False
            elif direction == "right":
                cell.has_right_wall = False
                right.has_left_wall = False
            elif direction == "bottom":
                cell.has_bottom_wall = False
                bottom.has_top_wall = False
            else:
                cell.has_left_wall = False
                left.has_right_wall = False

            self._break_walls_r(random_direction[1], random_direction[2])

    def solve(self, i, j):
        self._solve_r(i, j)

    def _solve_r(self, i=0, j=0):
        self._animate()
        cell = self._cells[i][j]
        cell.visited = True
        print(i, j)

        if i == self.num_cols - 1 and j == self.num_rows - 1:
            return True

        top = self._cells[i][j - 1] if j - 1 >= 0 and j - 1 < self.num_rows else None
        right = self._cells[i + 1][j] if i + 1 >= 0 and i + 1 < self.num_cols else None
        bottom = self._cells[i][j + 1] if j + 1 >= 0 and j + 1 < self.num_rows else None
        left = self._cells[i - 1][j] if i - 1 >= 0 and i - 1 < self.num_cols else None

        print("top", top)
        print("right", right)
        print("bottom", bottom)
        print("left", left)

        if (
            top is not None
            and not top.visited
            and not cell.has_top_wall
            and not top.has_bottom_wall
        ):
            cell.draw_move(top)
            top_move = self._solve_r(i, j - 1)

            if top_move:
                return True
            else:
                cell.draw_move(top, True)
        if (
            right is not None
            and not right.visited
            and not cell.has_right_wall
            and not right.has_left_wall
        ):
            cell.draw_move(right)
            right_move = self._solve_r(i + 1, j)

            if right_move:
                return True
            else:
                cell.draw_move(right, True)
        if (
            bottom is not None
            and not bottom.visited
            and not cell.has_bottom_wall
            and not bottom.has_top_wall
        ):
            cell.draw_move(bottom)
            bottom_move = self._solve_r(i, j + 1)

            if bottom_move:
                return True
            else:
                cell.draw_move(bottom, True)
        if (
            left is not None
            and not left.visited
            and not cell.has_left_wall
            and not left.has_right_wall
        ):
            cell.draw_move(left)
            left_move = self._solve_r(i - 1, j)

            if left_move:
                return True
            else:
                cell.draw_move(left, True)

        return False
