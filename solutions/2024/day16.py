from enum import Enum
import sys
import os
import math

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
sys.path.insert(0, project_root)


from utils.common_functions import create_border_around_grid, find_all_occurence_char_in_grid_list, find_in_grid, print_grid
from utils.input_parser import read_input
from utils.submit import submit

class Direction(Enum):
    UP = (-1, 0)
    RIGHT = (0, 1)
    DOWN = (1, 0)
    LEFT = (0, -1)

def real_vertex(grid, v):
    (x,y) = v
    return (
       (grid[x+1][y] == '.' and  grid[x][y+1] == '.') or
       (grid[x+1][y] == '.' and  grid[x][y-1] == '.') or
       (grid[x-1][y] == '.' and  grid[x][y+1] == '.') or
       (grid[x-1][y] == '.' and  grid[x][y-1] == '.') 
    )
    
def extra_step(d, step):
    return (step*d[0], step*d[1])

def all_edges_for_v(v,vertices,grid):
    TURN_CONSTANT = 1000
    edges = []
    max_step = len(grid)
    for d in Direction:
        for step in range(1,max_step):
            loc = tuple(a + b for a, b in zip(v, extra_step(d.value, step)))
            if loc in vertices:
                edges.append((v,loc,step + TURN_CONSTANT)) # E = (V1,V2,W)
            if grid[loc[0]][loc[1]] == '#':
                break
    return edges


def get_edges_with_weights(grid,vertices):
    edges = []
    for v in vertices:
        edges.extend(all_edges_for_v(v,vertices,grid))
    return edges

def get_all_vertices(grid):
    all_places = find_all_occurence_char_in_grid_list(grid, '.')
    vertices = [v for v in all_places if real_vertex(grid, v)]
    return vertices
  
def create_graph(grid,start,end,direction):
    vertices = get_all_vertices(grid)
    vertices.append(start)
    vertices.append(end)
    edges_weights = get_edges_with_weights(grid,vertices)
    return (vertices,edges_weights)
     
def find_cheapest_path(graph, current_location, end, path = [], weight = 0): 
        path = path + [current_location] 
        if current_location == end: 
            return path 
        shortest = None
        for node in graph[current_location]: 
            if node not in path: 
                newpath = find_cheapest_path(graph, node, end, path) 
                if newpath: 
                    if not shortest or len(newpath) < len(shortest): 
                        shortest = newpath 
        return shortest 
   
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

def dijkstra_all_paths(graph, start):
    (V, E) = graph
    dist = {}
    predecessors = {}
    Q = []
    
    for v in V:
        dist[v] = math.inf
        predecessors[v] = []  # Use a list to store all predecessors
        Q.append(v)
    dist[start] = 0
    
    while len(Q) > 0:
        u = get_min_dist(Q, dist)
        Q.remove(u)
        for v in neighbors_of_u_in_Q(u, Q, E):
            alt = dist[u] + v[2]
            if alt < dist[v[1]]:
                dist[v[1]] = alt
                predecessors[v[1]] = [u]  # Replace with the new predecessor
            elif alt == dist[v[1]]:
                predecessors[v[1]].append(u)  # Add another predecessor
                
    return dist, predecessors

def get_all_paths(predecessors, start, end, path=[]):
    """
    Recursively find all paths from start to end using the predecessors dictionary.
    """
    if end == start:
        return [path + [start]]
    if not predecessors[end]:
        return []
    
    paths = []
    for pred in predecessors[end]:
        paths.extend(get_all_paths(predecessors, start, pred, path + [end]))
    
    return paths

# 1  S ← empty sequence
# 2  u ← target
# 3  if prev[u] is defined or u = source:          // Proceed if the vertex is reachable
# 4      while u is defined:                       // Construct the shortest path with a stack S
# 5          insert u at the beginning of S        // Push the vertex onto the stack
# 6          u ← prev[u]                           // Traverse from target to source

    
def path_to_end_extra(prev, start, end):
    S = []
    u = [end]
    if len(prev[u[0]]) > 0 or u == start:
        while len(u) > 0:
            S.extend(u)
            u = prev[u]
    return S

def neighbors_of_u_in_Q(u,Q,E):
    nbs = [v for v in E if v[0]==u and v[1] in Q]
    return nbs
 
def get_min_dist(Q,dist):
    lowest_dist_u = math.inf
    lowest_u = None
    for u in Q:
        if dist[u] < lowest_dist_u:
            lowest_dist_u = dist[u]
            lowest_u = u
    return lowest_u

def generate_tuples_between_pairs(points):
    result = []
    
    for i in range(len(points) - 1):
        # Get the current and next tuple
        (x1, y1) = points[i]
        (x2, y2) = points[i + 1]
        
        # Generate the range of x and y values
        x_range = range(min(x1, x2), max(x1, x2) + 1)
        y_range = range(min(y1, y2), max(y1, y2) + 1)
        
        # Add all tuples between the two points
        for x in x_range:
            for y in y_range:
                result.append((x, y))
    
    return result
    
def solve_part1(data):
    grid = create_border_around_grid(data, 0, True)
    print_grid(grid)
    start = find_in_grid(grid,'S')[0]
    end = find_in_grid(grid,'E')[0]
    direction =Direction.RIGHT
    graph = create_graph(grid,start,end,direction)
    dist, prev = dijkstra(graph,start)
    return dist[end]

def solve_part2(data):
    grid = create_border_around_grid(data, 0, True)
    print_grid(grid)
    start = find_in_grid(grid,'S')[0]
    end = find_in_grid(grid,'E')[0]
    direction =Direction.RIGHT
    graph = create_graph(grid,start,end,direction)
    dist, predecessors = dijkstra_all_paths(graph,start)
    paths = get_all_paths(predecessors, start, end, path=[])
    print(paths)
    all_locs = []
    for p in paths:
        all_locs.extend(generate_tuples_between_pairs(p))
    return len(set(all_locs))

if __name__ == "__main__":
    year, day = 2024, 16
    
    # Read inputs
    input_data = read_input(year, day, file_name="input.txt")
    test_data = read_input(year, day, file_name="test.txt")
    
    # Test cases (update with known solutions for the test input)
    known_test_solution_part1 = 7036  # Replace with the known result for part 1
    known_test_solution_part2 = 45  # Replace with the known result for part 2
    
    # Verify test cases for Part 1
    print(f"Testing Part 1 for Day 16, Year 2024...")
    if known_test_solution_part2 is None:
        test_result_part1 = solve_part1(test_data)
        if test_result_part1 == known_test_solution_part1:
            print("✅ Part 1 Test Passed")
            part1_result = solve_part1(input_data)
            print(f"Part 1 Result: {part1_result}")
        else:
            raise AssertionError(f"❌ Part 1 Test Failed: Expected {known_test_solution_part1}, Got {test_result_part1}")
    else:
        part1_result = None

    # Only proceed to Part 2 if Part 1 is implemented and working
    if part1_result is None and known_test_solution_part2 is not None:
        # Verify test cases for Part 2
        print(f"Testing Part 2 for Day 16, Year 2024...")
        test_result_part2 = solve_part2(test_data)
        if test_result_part2 == known_test_solution_part2:
            print("✅ Part 2 Test Passed")
            part2_result = solve_part2(input_data)
            print(f"Part 2 Result: {part2_result}")
            submit(year, day, part1_result, part2_result)
        else:
            raise AssertionError(f"❌ Part 2 Test Failed: Expected {known_test_solution_part2}, Got {test_result_part2}")
