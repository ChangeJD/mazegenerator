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
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        random.seed(seed)


        self._create_cells()

    def _create_cells(self):
        self._cells = []
        for i in range(self.num_cols):
            self._cells.append([])
            for j in range(self.num_rows):
                self._cells[i].append(Cell(self.win))
        for i in range(self.num_cols):
            for j in range(self.num_rows):
                self._draw_cell(i, j)
    
    def _draw_cell(self, i, j):
        if self.win is None:
            return
        x1 = self.x1 + i * self.cell_size_x
        x2 = x1 + self.cell_size_x
        y1 = self.y1 + j * self.cell_size_y
        y2 = y1 + self.cell_size_y
        self._cells[i][j].draw(x1, y1, x2, y2)
        self._animate()

    def _animate(self):
        if self.win is None:
            return
        self.win.redraw()
        time.sleep(0.05)

    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0, 0)
        self._cells[self.num_cols-1][self.num_rows-1].has_bottom_wall = False
        self._draw_cell(self.num_cols - 1, self.num_rows - 1)

    def _break_walls_r(self, i, j):
        current = self._cells[i][j]
        current.visited = True
        while True:
            to_visit = []
            if j != 0:
                if self._cells[i][j-1].visited == False:
                    to_visit.append([i, j-1])
            if j != self.num_rows-1:
                if self._cells[i][j+1].visited == False:
                    to_visit.append([i, j+1])
            if i != 0:
                if self._cells[i-1][j].visited == False:
                    to_visit.append([i-1, j])
            if i != self.num_cols-1:
                if self._cells[i+1][j].visited == False:
                    to_visit.append([i+1, j])

            if len(to_visit) == 0:
                self._draw_cell(i, j)
                return
            
            else:
                n = random.randrange(0, len(to_visit))
                k, l = to_visit[n]
                if k > i:
                    #remove right wall of original, left wall of new
                    self._cells[i][j].has_right_wall = False
                    self._cells[k][l].has_left_wall = False
                elif k < i:
                    self._cells[i][j].has_left_wall = False
                    self._cells[k][l].has_right_wall = False                 
                    #remove left wall of original, right wall of new
                elif l > j:
                    self._cells[i][j].has_bottom_wall = False
                    self._cells[k][l].has_top_wall = False
                    #remove bottom wall of original, top wall of new
                elif l < j:
                    self._cells[i][j].has_top_wall = False
                    self._cells[k][l].has_bottom_wall = False
                    #remove top wall of original, bottom wall of new
                self._draw_cell(i,j)
                self._draw_cell(k,l)

                self._break_walls_r(k,l)

    def _reset_cells_visited(self):
        for column in self._cells:
            for cell in column:
                cell.visited = False

    def solve(self):
        return self._solve_r(0, 0)
    
    def _solve_r(self, i, j):
        self._animate()
        current = self._cells[i][j]
        current.visited = True
        if i == self.num_cols - 1 and j == self.num_rows - 1:
            return True
        #right
        if i < self.num_cols - 1 and current.has_right_wall == False:
            if self._cells[i+1][j].visited == False:
                to_cell = self._cells[i+1][j]
                current.draw_move(to_cell)
                if self._solve_r(i+1, j) == True:
                    return True
                else:
                    current.draw_move(to_cell, undo=True)
        #down
        if j < self.num_rows - 1 and current.has_bottom_wall == False:
            if self._cells[i][j+1].visited == False:
                to_cell = self._cells[i][j+1]
                current.draw_move(to_cell)
                if self._solve_r(i, j+1) == True:
                    return True
                else:
                    current.draw_move(to_cell, undo=True)
        #left
        if i > 0 and current.has_left_wall == False:
            if self._cells[i-1][j].visited == False:
                to_cell = self._cells[i-1][j]
                current.draw_move(to_cell)
                if self._solve_r(i-1, j) == True:
                    return True
                else:
                    current.draw_move(to_cell, undo=True)
        #up
        if j > 0 and current.has_top_wall == False:
            if self._cells[i][j-1].visited == False:
                to_cell = self._cells[i][j-1]
                current.draw_move(to_cell)
                if self._solve_r(i, j-1) == True:
                    return True
                else:
                    current.draw_move(to_cell, undo=True)
        return False
