from enum import Enum
import math

class Direction(Enum):
    UP = (-1, 0)
    RIGHT = (0, 1)
    DOWN = (1, 0)
    LEFT = (0, -1)

def create_border_around_grid(original_grid_input, size=1, split=False):
    # Ensure grid is a list of lists
    original_grid = [list(x.strip('\n')) if split else list(x.strip('\n')) for x in original_grid_input]

    width_original_grid = len(original_grid[0])

    top_border = [['*' for _ in range(width_original_grid + 2 * size)] for _ in range(size)]

    bordered_grid = [
        ['*'] * size + row + ['*'] * size for row in original_grid
    ]

    bottom_border = [['*' for _ in range(width_original_grid + 2 * size)] for _ in range(size)]

    full_grid = top_border + bordered_grid + bottom_border

    return full_grid

def print_grid(g):
    print('\n'.join(' '.join(str(x) for x in row) for row in g))

def get_index(my_list, item):
    try:
        index = my_list.index(item)
        return index
    except ValueError:
        return -1
        
def find_in_grid(grid, char):
    found = []
    for x, row in enumerate(grid):
        for y, cell in enumerate(row):
            if cell == char:
                found.append((x, y))
    return found

def find_all_chars_in_grid_dict(grid, empty_char):
    found = {}
    for x, row in enumerate(grid):
        for y, cell in enumerate(row):
            if cell != empty_char:
                if cell in found:
                    found[cell].append((x,y))
                else:
                    found[cell] = [(x,y)]
    return found

def find_all_occurence_char_in_grid_list(grid, char):
    found = []
    for x, row in enumerate(grid):
        for y, cell in enumerate(row):
            if cell == char:
                found.append((x,y))
    return found

'''
Vertices are (x,y)
Edges are ((x1,y1),(x2,y2), w)
'''
def dijkstra(graph,start):
    (V,E) = graph
    dist = {}
    prev = {}
    Q = []
    for v in V:
        dist[v] = math.inf
        prev[v] = None
        Q.append(v)
    dist[start] = 0
    
    while len(Q) > 0:
        u = get_min_dist(Q,dist)
        Q.remove(u)
        for v in neighbors_of_u_in_Q(u,Q,E): 
            alt = dist[u] + v[2]
            if alt < dist[v[1]]:
                dist[v[1]] = alt
                prev[v[1]] = v[0]
    return dist, prev

def get_min_dist(Q,dist):
    lowest_dist_u = math.inf
    lowest_u = None
    for u in Q:
        if dist[u] < lowest_dist_u:
            lowest_dist_u = dist[u]
            lowest_u = u
    return lowest_u

def neighbors_of_u_in_Q(u,Q,E):
    nbs = [v for v in E if v[0]==u and v[1] in Q]
    return nbs

def neighbors_of_u_in_E(u,E):
    nbs = [v[1] for v in E if v[0]==u]
    return nbs

# Use BFS to check path between s and d
def isReachable(G, s, d):
    # Mark all the vertices as not visited
    (V,E) = G
    visited = {}
    Q = []
    for v in V:
        visited[v] = False
        Q.append(v)

    # Mark the source node as visited and enqueue it
    Q.append(s)
    visited[s] = True

    while len(Q):

        #Dequeue a vertex from queue 
        u = Q.pop(0)
            
        # If this adjacent node is the destination node,
        # then return true
        if u == d:
            return True

        #  Else, continue to do BFS
        for i in neighbors_of_u_in_E(u,E):
            if visited[i] == False:
                Q.append(i)
                visited[i] = True
        # If BFS is complete without visited d
    return False