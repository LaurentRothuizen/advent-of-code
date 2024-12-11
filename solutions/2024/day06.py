import copy
import sys
import os
import time

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
sys.path.insert(0, project_root)


from utils.common_functions import create_border_around_grid, find_in_grid, print_grid
from utils.input_parser import read_input
from utils.submit import submit

from enum import Enum

class Direction(Enum):
    UP = (-1, 0)
    RIGHT = (0, 1)
    DOWN = (1, 0)
    LEFT = (0, -1)

def next_direction(dir):
        directions = list(Direction)
        current_index = directions.index(dir)
        next_index = (current_index + 1) % len(directions)
        return directions[next_index]

def move(grid, current, direction):
    dx, dy = direction.value
    newx, newy = (current[0] + dx, current[1] + dy)
    if grid[newx][newy] == '#':
        new_direction = next_direction(direction)
        return new_direction, (current[0] + new_direction.value[0], current[1] + new_direction.value[1])
    return direction, (newx, newy)

def navigate_to_end_return_path(start,g):
    visited = []
    dir_loc_tuple_list = []
    inside = True
    direction = Direction.UP
    loc = start
    while inside:
        if g[loc[0]][loc[1]] == '*':
            inside=False
            break
        visited.append(loc)
        dir_loc_tuple_list.append((direction,loc))
        direction, loc = move(g, loc, direction)
        if loop(direction, loc, dir_loc_tuple_list):
            return []
    return set(visited)

def move_obstacle(obstacles, current, direction):
    dx, dy = direction.value
    newxy = (current[0] + dx, current[1] + dy)
    if newxy in obstacles:
        new_direction = next_direction(direction)
        return new_direction, (current[0] + new_direction.value[0], current[1] + new_direction.value[1])
    return direction, newxy

def walk_route(start, obstacles, h):
    visited = []
    dir_loc_tuple_list = []
    direction = Direction.UP
    loc = start
    while True:
        if loc[0] < 0 or loc[0] >= h or loc[1] < 0 or loc[1] >= h:
            break
        visited.append(loc)
        dir_loc_tuple_list.append((direction,loc))
        direction, loc = move_obstacle(obstacles, loc, direction)
        if loop(direction, loc, dir_loc_tuple_list):
            return []
    return set(visited)

def loop(direction, loc, dir_loc_tuple_list):
    for tup in dir_loc_tuple_list:
        if (direction,loc) == tup:
            return True
    return False


def solve_part1(data):
    grid = create_border_around_grid(data, 0 ,True)
    h = len(grid)
    start = find_in_grid(grid, '^')[0]
    obstacles = find_in_grid(grid, '#')
    return len(walk_route(start, obstacles, h))
    # return len(navigate_to_end_return_path(start,grid))


def solve_part2(data):
    boxes = []
    grid = create_border_around_grid(data, 1, True)
    h = len(grid)
    start = find_in_grid(grid, '^')[0]
    obstacles = find_in_grid(grid, '#')
    visited_places = list(walk_route(start, obstacles, h))
    print('ALL places ' + str(len(visited_places)))
    i = 0
    for new_obs in visited_places[1:]:
        i += 1
        print('Obstacle ' + str(i) + ' of ' + str(len(visited_places)))
        obstacles.append(new_obs)
        if len(walk_route(start,obstacles, h)) == 0:
            boxes.append(new_obs)
        obstacles.remove(new_obs)
    return len(boxes)

def print_boxes(grid, boxes):
    for b in boxes:
        print('------------------------------------------' + str(b))
        box_grid = copy.deepcopy(grid)
        box_grid[b[0]][b[1]] = 'O'
        print_grid(box_grid)

if __name__ == "__main__":
    year, day = 2024, 6
    
    # Read inputs
    input_data = read_input(year, day, file_name="input.txt")
    test_data = read_input(year, day, file_name="test.txt")
    
    # Test cases (update with known solutions for the test input)
    known_test_solution_part1 = 41  # Replace with the known result for part 1
    known_test_solution_part2 = 6  # Replace with the known result for part 2
    
    # Verify test cases for Part 1
    print(f"Testing Part 1 for Day 6, Year 2024...")
    try:
        test_result_part1 = solve_part1(test_data)
        if test_result_part1 == known_test_solution_part1:
            print("✅ Part 1 Test Passed")
        else:
            print(f"❌ Part 1 Test Failed: Expected {known_test_solution_part1}, Got {test_result_part1}")
    except Exception as e:
        print(f"❌ Part 1 Test Error: {e}")
    
    # Solve Part 1
    part1_result = None
    if test_result_part1 == known_test_solution_part1:
        try:
            part1_result = solve_part1(input_data)
            print(f"Part 1 Result: {part1_result}")
        except Exception as e:
            print(f"❌ Error solving Part 1: {e}")

    # Only proceed to Part 2 if Part 1 is implemented and working
    if part1_result is None and known_test_solution_part2 is not None:
        # Verify test cases for Part 2
        print(f"Testing Part 2 for Day 6, Year 2024...")
        try:
            test_result_part2 = solve_part2(test_data)
            if test_result_part2 == known_test_solution_part2:
                print("✅ Part 2 Test Passed")
            else:
                print(f"❌ Part 2 Test Failed: Expected {known_test_solution_part2}, Got {test_result_part2}")
        except Exception as e:
            print(f"❌ Part 2 Test Error: {e}")
        
        # Solve Part 2
        # 1429 too low
        try:
            part2_result = solve_part2(input_data)
            print(f"Part 2 Result: {part2_result}")
            submit(year, day, part1_result, part2_result)
        except Exception as e:
            print(f"❌ Error solving Part 2: {e}")
