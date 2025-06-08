from graphics import Window, Point, Line

class Cell:
    def __init__(self, window = None):
        # self.window = window
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.__x1 = -1
        self.__x2 = -1
        self.__y1 = -1
        self.__y2 = -1
        self.__win = window
        self.visited = False

    def draw(self, x1, y1, x2, y2):
        self.__x1 = x1
        self.__y1 = y1
        self.__x2 = x2
        self.__y2 = y2

        if self.__win:
            p_top_left = Point(x1, y1)
            p_top_right = Point(x2, y1)
            p_bottom_left = Point(x1, y2)
            p_bottom_right = Point(x2, y2)

            l_top = Line(p_top_left, p_top_right)
            l_right = Line(p_top_right, p_bottom_right)
            l_bottom = Line(p_bottom_left, p_bottom_right)
            l_left = Line(p_top_left,p_bottom_left)

            self.__win.draw_line(l_left, "black" if self.has_left_wall else "white")
            self.__win.draw_line(l_top, "black" if self.has_top_wall else "white")
            self.__win.draw_line(l_right, "black" if self.has_right_wall else "white")
            self.__win.draw_line(l_bottom, "black" if self.has_bottom_wall else "white")

    def draw_move(self, to_cell, undo=False):
        self_x = (self.__x1 + self.__x2) / 2
        self_y = (self.__y1 + self.__y2) / 2
        to_cell_x = (to_cell.__x1 + to_cell.__x2) / 2
        to_cell_y = (to_cell.__y1 + to_cell.__y2) / 2

        line = Line(Point(self_x, self_y), Point(to_cell_x, to_cell_y))
        # fill = undo == false ? "red" : "gray"
        fill = "red" if undo is False else "gray"

        if self.__win:
            self.__win.draw_line(line, fill)
