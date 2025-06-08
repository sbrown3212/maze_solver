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
        num_cols = 40
        num_rows = 40
        m1 = Maze(10, 10, num_cols, num_rows, 100, 100)
        self.assertEqual(
            len(m1._Maze__cells),
            num_cols
        )
        self.assertEqual(
            len(m1._Maze__cells[0]),
            num_rows
        )

    def test_break_entrance_and_exit(self):
        num_cols = 10
        num_rows = 10
        
        maze = Maze(0, 0, num_cols, num_rows, 10, 10)
        # maze.__break_entrance_and_exit()
        maze._Maze__break_entrance_and_exit()

        self.assertFalse(
            maze._Maze__cells[0][0].has_top_wall
        )
        self.assertFalse(
            maze._Maze__cells[num_cols - 1][num_rows - 1].has_bottom_wall
        )

    def test_reset_cells_visited(self):
        num_rows = 10
        num_cols = 10

        maze = Maze(0, 0, num_cols, num_rows, 10, 10)

        self.assertFalse(
            maze._Maze__cells[0][0].visited
        )
        self.assertFalse(
            maze._Maze__cells[num_cols - 1][num_rows - 1].visited
        )
        self.assertFalse(
            maze._Maze__cells[num_cols // 2][num_rows // 2].visited
        )

if __name__ == "__main__":
    unittest.main()

