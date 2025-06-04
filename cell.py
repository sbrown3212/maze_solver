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

    def draw(self, x1, y1, x2, y2):
        self.__x1 = x1
        self.__y1 = y1
        self.__x2 = x2
        self.__y2 = y2


        if self.has_left_wall:
            # create points
            p1 = Point(self.__x1, self.__y1)
            p2 = Point(self.__x1, self.__y2) 
            # create line
            line = Line(p1, p2)
            # draw line
            if self.__win:
                self.__win.draw_line(line, "black")

        if self.has_top_wall:
            # create points
            p1 = Point(self.__x1, self.__y1)
            p2 = Point(self.__x2, self.__y1) 
            # create line
            line = Line(p1, p2)
            # draw line
            if self.__win:
                self.__win.draw_line(line, "black")

        if self.has_right_wall:
            # create points
            p1 = Point(self.__x2, self.__y1)
            p2 = Point(self.__x2, self.__y2) 
            # create line
            line = Line(p1, p2)
            # draw line
            if self.__win:
                self.__win.draw_line(line, "black")

        if self.has_bottom_wall:
            # create points
            p1 = Point(self.__x1, self.__y2)
            p2 = Point(self.__x2, self.__y2) 
            # create line
            line = Line(p1, p2)
            # draw line
            if self.__win:
                self.__win.draw_line(line, "black")

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
