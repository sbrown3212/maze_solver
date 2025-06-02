from graphics import Window, Point, Line
from cell import Cell

def main():
    win = Window(800, 600)

    c1 = Cell(win)
    c1.has_left_wall = False
    c1.draw(500,300, 600, 400)

    c2 = Cell(win)
    c2.has_top_wall = False
    c2.draw(100, 400, 200, 500)

    c1.draw_move(c2, undo=False)

    x1 = 100
    y1 = 100
    x2 = 200
    y2 = 200

    c3 = Cell(win)
    c3.draw(x1, y1, x2, y2)

    x1 = 250
    y1 = 250
    x2 = 350
    y2 = 350

    c4 = Cell(win).draw(x1, y1, x2, y2)

    c3.draw_move(c1, undo=True)

    win.wait_for_close()



if __name__ == '__main__':
    main()
