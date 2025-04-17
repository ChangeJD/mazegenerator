from graphics import Line, Point

class Cell:
    def __init__(self, win=None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.x1 = None
        self.y1 = None
        self.x2 = None
        self.y2 = None
        self.win = win
        self.visited = False

    def draw(self, x1, y1, x2, y2):
        if self.win is None:
            return
        walls_to_draw_black = []
        walls_to_draw_white = []
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        
        if self.has_left_wall:
            walls_to_draw_black.append(Line(Point(self.x1, self.y1), Point(self.x1, self.y2)))
        else:
            walls_to_draw_white.append(Line(Point(self.x1, self.y1), Point(self.x1, self.y2)))

        if self.has_right_wall:
            walls_to_draw_black.append(Line(Point(self.x2, self.y1), Point(self.x2, self.y2)))
        else:
            walls_to_draw_white.append(Line(Point(self.x2, self.y1), Point(self.x2, self.y2)))

        if self.has_top_wall:
            walls_to_draw_black.append(Line(Point(self.x1, self.y1), Point(self.x2, self.y1)))
        else:
            walls_to_draw_white.append(Line(Point(self.x1, self.y1), Point(self.x2, self.y1)))

        if self.has_bottom_wall:
            walls_to_draw_black.append(Line(Point(self.x1, self.y2), Point(self.x2, self.y2)))
        else:
            walls_to_draw_white.append(Line(Point(self.x1, self.y2), Point(self.x2, self.y2)))

        for wall in walls_to_draw_black:
            self.win.draw_line(wall, "black")
        for wall in walls_to_draw_white:
            self.win.draw_line(wall, "white")

    def draw_move(self, to_cell, undo=False):
        line = Line(Point((self.x1+self.x2)/2, (self.y1+self.y2)/2), Point((to_cell.x1+to_cell.x2)/2, (to_cell.y1+to_cell.y2)/2))
        if undo:
            self.win.draw_line(line, "gray")
        else:
            self.win.draw_line(line, "blue")