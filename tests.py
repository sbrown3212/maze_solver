import unittest
from maze import Maze

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._Maze__cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._Maze__cells[0]),
            num_rows,
        )

    def test_maze_create_cells_small(self):
        num_cols = 1
        num_rows = 1
        m1 = Maze(0, 0, num_cols, num_rows, 1, 1)
        self.assertEqual(
            len(m1._Maze__cells),
            num_cols
        )
        self.assertEqual(
            len(m1._Maze__cells[0]),
            num_rows
        )

    def test_maze_create_cells_large(self):
        num_cols = 100
        num_rows = 100
        m1 = Maze(10, 10, num_cols, num_rows, 100, 100)
        self.assertEqual(
            len(m1._Maze__cells),
            num_cols
        )
        self.assertEqual(
            len(m1._Maze__cells[0]),
            num_rows
        )

if __name__ == "__main__":
    unittest.main()

