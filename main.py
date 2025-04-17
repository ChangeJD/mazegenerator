from graphics import Window, Point, Line
from maze import Maze
from cell import Cell
def main():
    win = Window(800, 600)

    m1 = Maze(30, 30, 15, 20, 30, 30, win)
    m1._break_entrance_and_exit()
    m1._break_walls_r(0, 0)
    m1._reset_cells_visited()
    m1.solve()
    win.wait_for_close()

main()