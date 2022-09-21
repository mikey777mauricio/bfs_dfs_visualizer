# dfs search func
paths = []
def dfs(start, goal):
    stack = []
    first = [start]
    stack.append(first)
    seen = set()
    while stack:
        # get node
        curr = stack.pop()

        currPoint = curr[len(curr) -1]
        seen.add(currPoint)
        for neighbor in currPoint.adj_list:
            if currPoint not in seen:
                temp = curr
                temp.append(neighbor)
                if neighbor == goal:
                    paths.append(temp)

                else:
                    stack.append(temp)
    return paths









