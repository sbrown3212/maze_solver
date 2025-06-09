from cell import Cell
import time
import random

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
        seed = None
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
        if seed:
            random.seed(seed)
        self.__break_walls_r(0, 0)
        self.__reset_cells_visited()

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
        time.sleep(0.001)

    def __break_entrance_and_exit(self):
        x1 = 0
        y1 = 0
        x2 = self.__num_cols - 1
        y2 = self.__num_rows - 1

        self.__cells[x1][y1].has_top_wall = False
        self.__draw_cell(x1, y1)

        self.__cells[x2][y2].has_bottom_wall = False
        self.__draw_cell(x2, y2)

    def __break_walls_r(self, i, j):
        # 'i' represents x axis or columns ('i + 1' refers to the next column to the right)
        # 'j' represents y axis or rows ('j + 1' refers to the next row below)
        #
        # compass:
        #       [j-1]
        # [i-1] [cur] [i+1]
        #       [j+1]

        current_cell = self.__cells[i][j]
        current_cell.visited = True

        possible_directions = []

        # Determine possible directions
        # if cell to right of current exists and has not been visited
        if i+1 <= self.__num_cols-1 and self.__cells[i+1][j].visited == False:
            possible_directions.append([i+1, j])

        # if cell to left of current exists and has not been visited
        if i-1 >= 0 and self.__cells[i-1][j].visited == False:
            possible_directions.append([i-1, j])

        # if cell below current exists and has not been visited
        if j+1 <= self.__num_rows-1 and self.__cells[i][j+1].visited == False:
            possible_directions.append([i, j+1])

        # if cell above current exists and has not been visited
        if j-1 >= 0 and self.__cells[i][j-1].visited == False:
            possible_directions.append([i, j-1])

        # Draw current cell and return if all neighboring cells have been visited
        if len(possible_directions) == 0:
            self.__draw_cell(i, j)
            return

        # Shuffle possible_directions
        random.shuffle(possible_directions)

        # while possible_directions has elements
        while possible_directions:
            # pop last item from possible_directions and use as next cell
            [next_x, next_y] = possible_directions.pop()
            next_cell = self.__cells[next_x][next_y]

            # Double check that next cell has not been visited
            if next_cell.visited == True:
                continue
            
            # Erase walls between current and next cells
            dx = next_x - i
            dy = next_y - j

            if dx == -1: # moving left
                current_cell.has_left_wall = False
                next_cell.has_right_wall = False
            elif dx == 1: # moving right
                current_cell.has_right_wall = False
                next_cell.has_left_wall = False
            elif dy == 1: # moving down
                current_cell.has_bottom_wall = False
                next_cell.has_top_wall = False
            elif dy == -1: # moving up
                current_cell.has_top_wall = False
                next_cell.has_bottom_wall = False

            # Redraw current and next cells
            self.__draw_cell(i, j)
            self.__draw_cell(next_x, next_y)

            # Recursively call '__break_walls_r' on 'next' cell
            self.__break_walls_r(next_x, next_y)

    def __reset_cells_visited(self):
        for i in range(self.__num_cols):
            for j in range(self.__num_rows):
                self.__cells[i][j].visited = False

    def solve(self):
        self.__solve_r(0, 0)

    def __solve_r(self, i, j):
        self.animate()

        # Set current cell 'visited' to 'True'
        current_cell = self.__cells[i][j]
        current_cell.visited = True

        # Return 'True' if end cell is found
        if i == self.__num_cols - 1 and j == self.__num_rows-1:
            return True

        # Save value for neighboring cells
        n_left = self.__cells[i-1][j] if i-1 >= 0 else None
        n_right = self.__cells[i+1][j] if i+1 <= self.__num_cols - 1 else None
        n_above = self.__cells[i][j-1] if j-1 >= 0 else None
        n_below = self.__cells[i][j+1] if j+1 <= self.__num_rows - 1 else None
        
        # for each direction:
        # left
        # Check if neighboring cell exists
        if n_left:
            # if no walls are blocking, and if neighboring cell has not been visited
            if current_cell.has_left_wall == False and n_left.has_right_wall == False and n_left.visited == False:
                # Draw red line to neighboring cell
                current_cell.draw_move(n_left)
                # Get result from recursive call on neighboring cell
                result = self.__solve_r(i-1, j)
                # Return true neighboring cell returns true (end was found)
                if result:
                    return True
                # Undo line (redraw as gray) if reslut returns false
                current_cell.draw_move(n_left, undo=True)
        # right
        if n_right:
            if current_cell.has_right_wall == False and n_right.has_left_wall == False and n_right.visited == False:
                current_cell.draw_move(n_right)
                result = self.__solve_r(i+1, j)
                if result:
                    return True
                current_cell.draw_move(n_right, undo=True)
        # above
        if n_above:
            if current_cell.has_top_wall == False and n_above.has_bottom_wall == False and n_above.visited == False:
                current_cell.draw_move(n_above)
                result = self.__solve_r(i, j-1)
                if result:
                    return True
                current_cell.draw_move(n_above, undo=True)
        # below
        if n_below:
            if current_cell.has_bottom_wall == False and n_below.has_top_wall == False and n_below.visited == False:
                current_cell.draw_move(n_below)
                result = self.__solve_r(i, j+1)
                if result:
                    return True
                current_cell.draw_move(n_below, undo=True)

        return False
