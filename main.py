from graphics import Window, Point, Line

def main():
    win = Window(800, 600)

    point_a = Point(100, 100)
    point_b = Point(100, 200)
    point_c = Point(200, 200)

    line_1 = Line(point_a, point_b)
    line_2 = Line(point_b, point_c)

    win.draw_line(line_1, "red")
    win.draw_line(line_2, "black")

    win.wait_for_close()



if __name__ == '__main__':
    main()
