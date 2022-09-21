#  Author: Mikey Mauricio
#  Date: Sunday, May 30, 2021
#  Purpose: Lab 4

from vertex import Vertex


# load graph function
def load_graph(filename):
    vertex_dict = {}  # create vertex dictionary
    with open(filename, 'r') as data_file:  # open as a write file
        for line in data_file:  # iterate through each line
            line = line.strip().split(';')  # split and strip line at semi colon
            xy_list = line[2].split(',')  # separate x and y coordinates
            line_name = line[0].strip()  # strip name
            line = Vertex(line[0], xy_list[0], xy_list[1])  # create vertex object
            vertex_dict[line_name] = line  # add vertex into dictionary
    with open(filename, 'r') as data_file:  # re open reading file
        for line in data_file:  # iterate over each line
            line = line.strip().split(';')  # split line and strip at semi colon
            adj_list = line[1].split(',')  # split adjacent list
            for a in adj_list:  # iterate through each item in adjacent list
                vertex_dict[line[0]].adj_list.append(vertex_dict[a.strip()])  # add vertex objects to adjacent list
    return vertex_dict  # return vertex dictionary


vert_dict = load_graph('dartmouth_graphEC.txt')
