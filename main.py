from graphics import Window, Point, Line
from cell import Cell
from maze import Maze

def main():
    win = Window(800, 600)

    Maze(100, 100, 10, 10, 25, 25, win)

    win.wait_for_close()



if __name__ == '__main__':
    main()
