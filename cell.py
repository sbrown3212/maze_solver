from graphics import Window, Point, Line

class Cell:
    def __init__(self, window):
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
            self.__win.draw_line(line, "black")

        if self.has_top_wall:
            # create points
            p1 = Point(self.__x1, self.__y1)
            p2 = Point(self.__x2, self.__y1) 
            # create line
            line = Line(p1, p2)
            # draw line
            self.__win.draw_line(line, "black")

        if self.has_right_wall:
            # create points
            p1 = Point(self.__x2, self.__y1)
            p2 = Point(self.__x2, self.__y2) 
            # create line
            line = Line(p1, p2)
            # draw line
            self.__win.draw_line(line, "black")

        if self.has_bottom_wall:
            # create points
            p1 = Point(self.__x1, self.__y2)
            p2 = Point(self.__x2, self.__y2) 
            # create line
            line = Line(p1, p2)
            # draw line
            self.__win.draw_line(line, "black")
