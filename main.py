from graphics import Window, Point, Line
from cell import Cell

def main():
    win = Window(800, 600)

    x1 = 100
    y1 = 100
    x2 = 200
    y2 = 200

    cell = Cell(win).draw(x1, y1, x2, y2)

    x1 = 250
    y1 = 250
    x2 = 350
    y2 = 350

    cell = Cell(win).draw(x1, y1, x2, y2)

    c = Cell(win)
    c.has_left_wall = False
    c.draw(500,300, 600, 400)

    c = Cell(win)
    c.has_top_wall = False
    c.draw(100, 400, 200, 500)

    win.wait_for_close()



if __name__ == '__main__':
    main()
