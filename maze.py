from cell import Cell
import time

class Maze:
    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win = None,
    ):
        self.__x1 = x1
        self.__y1 = y1
        self.__num_rows = num_rows
        self.__num_cols = num_cols
        self.__cell_size_x = cell_size_x
        self.__cell_size_y = cell_size_y
        self.__win = win
        self.__cells = []

        self.__create_cells()
        self.__break_entrance_and_exit()

    def __create_cells(self):
        for i in range(self.__num_cols):
            self.__cells.append([])

            for j in range(self.__num_rows):
                self.__cells[i].append(Cell(self.__win))
                # when testing (when no window is provided), skip drawing cells
                if self.__win:
                    self.__draw_cell(i, j)

    def __draw_cell(self, i, j):
        x1 = self.__x1 + (i * self.__cell_size_x)
        y1 = self.__y1 + (j * self.__cell_size_y)
        x2 = x1 + self.__cell_size_x
        y2 = y1 + self.__cell_size_y

        cell = self.__cells[i][j]
        cell.draw(x1, y1, x2, y2)
        self.animate()

    def animate(self):
        if not self.__win:
            return
        self.__win.redraw()
        time.sleep(0.02)

    def __break_entrance_and_exit(self):
        x1 = 0
        y1 = 0
        x2 = self.__num_cols - 1
        y2 = self.__num_rows - 1

        self.__cells[x1][y1].has_top_wall = False
        self.__draw_cell(x1, y1)

        self.__cells[x2][y2].has_bottom_wall = False
        self.__draw_cell(x2, y2)

