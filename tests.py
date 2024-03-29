import unittest

from maze import Maze


class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10

        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(len(m1._cells), num_cols)
        self.assertEqual(len(m1._cells[0]), num_rows)

    def test_maze_start_exit_cells(self):
        num_cols = 12
        num_rows = 10

        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)

        m1._break_entrance_and_exit()

        start = m1._cells[0][0]
        self.assertFalse(start.has_top_wall)

        exit = m1._cells[num_cols - 1][num_rows - 1]
        self.assertFalse(exit.has_bottom_wall)

    def test_reset_visited_cells(self):
        num_cols = 12
        num_rows = 10

        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)

        m1._break_entrance_and_exit()
        m1._break_walls_r(0, 0)

        start = m1._cells[0][0]

        self.assertTrue(start.visited)

        m1._reset_cells_visited()
        self.assertFalse(start.visited)


if __name__ == "__main__":
    unittest.main()
