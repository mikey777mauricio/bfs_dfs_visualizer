from cs1lib import *
from vertex import *
from load_graphEC import vert_dict
from bfsfuncEC import *
from dfsFun import *

# load img
img = load_image("dartmouth_map.png")

# window constants
HEIGHT = 811
WIDTH = 1012

# color constants
r = 0
g = 0
b = 1
OFF = 0
HIGHLIGHT = 1

# path selection variables
start_selected = False
start_vert = None
goal_vert = None


# start selection function
def mouse_click(mx, my):
    global start_vert, start_selected
    for key in vert_dict:
        #  if vertex is clicked
        if vert_dict[key].is_clicked(mx, my):
            start_selected = True  # selection = true
            start_vert = vert_dict[key]  # set start to selected vertex
            start_vert.draw_vertex(HIGHLIGHT, r, b)  # highlight selected vertex


# goal selection function
def mouse_hover(mx, my):
    global goal_vert
    if start_selected:  # if start has been selected
        for vert in vert_dict:
            if vert_dict[vert].is_clicked(mx, my):  # if mouse hovers over a vertex
                goal_vert = vert_dict[vert]  # set goal to hovered vertex


# highlight path function
def highlight_points():
    if goal_vert is not None:
        list_frontier, backpointer, path = bfs(start_vert, goal_vert)  # call BFS function with start and goal
        #  iterate through each vertex in path
        for point in backpointer:
            if backpointer[point] is not None:
                point.draw_edges(backpointer[point], OFF, HIGHLIGHT, HIGHLIGHT)
        for i in range(1, len(list_frontier)):
            if list_frontier[i] not in path:
                list_frontier[i].draw_vertex(HIGHLIGHT, OFF, HIGHLIGHT)
            else:
                list_frontier[i].draw_vertex(HIGHLIGHT, OFF, OFF)
            # display names of start and goal vertex
        start_vert.draw_vertex(OFF, HIGHLIGHT, OFF)
        goal_vert.draw_vertex(HIGHLIGHT, HIGHLIGHT, OFF)
        start_vert.display_text()
        goal_vert.display_text()

def highlight_dfs():
    if goal_vert is not None:
        paths = dfs(start_vert, goal_vert)
        for path in paths:
            for vert in path:
                if vert is not None:
                    vert.draw_edges(vert, HIGHLIGHT, HIGHLIGHT, HIGHLIGHT)



#  draw each vertex function
def draw_all():
    for vert in vert_dict:  # iterate through each vertices
        vert_dict[vert].draw_vertex(r, g, b)  # draw each vertices
        vert_dict[vert].highlight(r, g, b)  # draw edge


# clear function
def clear_func():
    set_clear_color(HIGHLIGHT, HIGHLIGHT, HIGHLIGHT)
    clear()


def draw():
    # clear
    clear_func()

    # draw image
    draw_image(img, 0, 0)

    # draw all vertices
    draw_all()

    # highlight path
    highlight_points()
    highlight_dfs()


start_graphics(draw, width=WIDTH, height=HEIGHT, mouse_press=mouse_click, mouse_move=mouse_hover)
