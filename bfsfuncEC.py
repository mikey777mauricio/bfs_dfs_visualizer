#  Author: Mikey Mauricio
#  Date: Thursday, June 3rd 2021
#  Purpose: Lab 4

from collections import deque


# breadth-first search function
def bfs(start, goal):
    frontier = deque()  # set frontier as a Queue
    frontier.append(start)  # enqueue start vertex
    list_frontier = []

    backpointer = {start: None}  # set backpointer as a dictionary
    while len(frontier) != 0:  # while the frontier is not empty
        current = frontier.popleft()  # pop first item
        list_frontier.append(current)
        if current == goal:  # if current is goal
            path = []  # initialize path to None
            previous = goal  # set previous to goal
            while previous is not None:  # while previous != None
                path.append(previous)  # append to path
                previous = backpointer[previous]  # set previous to value in backpointer dictionary
            return list_frontier, backpointer, path  # return path

        else:
            for vertex in current.adj_list:  # for vertex in its adjacent list
                if vertex not in backpointer:  # if vertex not in backpointer
                    backpointer[vertex] = current  # set backpointer value to current
                    frontier.append(vertex)  # append to frontier
    return None  # return None if nothing found
