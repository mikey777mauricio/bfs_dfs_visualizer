#  Author: Mikey Mauricio
#  Date: Thursday, June 3rd 2021
#  Purpose: Lab 4

from cs1lib import *

RADIUS = 5
EDGE_WIDTH = 2
FONT_SIZE = 15

class Vertex:
    def __init__(self, name, x, y):
        self.name = name
        self.x = int(x)
        self.y = int(y)
        self.adj_list = []

    def __str__(self):
        str_adj = f'{self.adj_list[0]}'
        for i in range(1, len(self.adj_list)):
            str_adj += f', {self.adj_list[i]}'
        return f'{self.name}; Location: {self.x}, {self.y}; Adjacent vertices: {str_adj}'

    def draw_vertex(self, r, g, b):
        set_stroke_color(r, g, b)
        set_fill_color(r, g, b)
        draw_circle(self.x, self.y, RADIUS)

    def draw_edges(self, other, r, g, b):
        set_stroke_color(r, g, b)
        set_fill_color(r, g, b)
        set_stroke_width(EDGE_WIDTH)
        draw_line(self.x, self.y, other.x, other.y)

    def is_clicked(self, mousex, mousey):
        if mousex in range(self.x - RADIUS, self.x + RADIUS) and mousey in range(self.y - RADIUS, self.y + RADIUS):
            return True
        else:
            return False

    def highlight(self, r, g, b):
        for adj in self.adj_list:
            self.draw_edges(adj, r, g, b)

    def display_text(self):
        set_font_size(FONT_SIZE)
        set_stroke_color(0, 0, 0)
        set_font_bold()
        draw_text(f'{self.name}', self.x, self.y - FONT_SIZE)