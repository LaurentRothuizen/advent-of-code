from copy import deepcopy
import sys
import os

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
sys.path.insert(0, project_root)


from utils.common_functions import create_border_around_grid, find_all_occurence_char_in_grid_list, find_in_grid, print_grid
from utils.input_parser import read_input
from utils.submit import submit
from enum import Enum

class Direction(Enum):
    UP = (-1, 0)
    RIGHT = (0, 1)
    DOWN = (1, 0)
    LEFT = (0, -1)

def parse_data(data):
    grid_lines = []
    instructions = []
    for line in data:
        grid_lines.append(line.strip('\n')) if line[0] == '#' else instructions.extend(line.strip('\n'))
    grid = create_border_around_grid(grid_lines, 0, True)
    # print_grid(grid)
    # print(instructions)
    return grid, instructions

def parse_data_part2(data):
    grid_lines = []
    instructions = []
    for line in data:
        grid_lines.append(line.strip('\n')) if line[0] == '#' else instructions.extend(line.strip('\n'))
    new_grid = []
    for line in grid_lines:
        new_line = ''
        for char in line:
            if char == '#':
                new_line += '##'
            if char == 'O':
                new_line += '[]'
            if char == '.':
                new_line += '..'
            if char == '@':
                new_line += '@.'
        new_grid.append(new_line)
    grid = create_border_around_grid(new_grid, 0, True)
    print_grid(grid)
    # print(instructions)
    return grid, instructions

def calculate_sum_of_boxes(boxes):
    total = 0
    for box in boxes:
        print(box, box[1] + 100*box[0])
        total += box[1] + 100*box[0]
    return total

def new_loc(inst):
    match inst:
        case '<':
            return Direction.LEFT
        case '^':
            return Direction.UP
        case '>':
            return Direction.RIGHT
        case 'v':
            return Direction.DOWN
    
    
    
def complete_instructions(start,grid,instructions):
    location = start
    for inst in instructions:
        # print_grid(grid)
        # print(inst)
        direction = new_loc(inst).value
        loc = tuple(a + b for a, b in zip(location, direction)) 
        if grid[loc[0]][loc[1]] == '.':
            grid[loc[0]][loc[1]] = '@'
            grid[location[0]][location[1]] = '.'
            location = loc
            continue
        elif grid[loc[0]][loc[1]] == '#':
            continue
        elif grid[loc[0]][loc[1]] == 'O':
            update = False
            new_grid = deepcopy(grid)
            location_next_step = loc
            while True:
                box_loc = tuple(a + b for a, b in zip(loc, direction)) 
                if grid[box_loc[0]][box_loc[1]] == '.':
                    new_grid[box_loc[0]][box_loc[1]] = 'O'
                    new_grid[loc[0]][loc[1]] = 'O'
                    new_grid[location[0]][location[1]] = '.'
                    update=True
                    break
                elif grid[box_loc[0]][box_loc[1]] == '#':
                    update=False
                    break
                elif grid[box_loc[0]][box_loc[1]] == 'O':
                    new_grid[box_loc[0]][box_loc[1]] = 'O'
                    new_grid[loc[0]][loc[1]] = 'O'
                    new_grid[location[0]][location[1]] = '.'
                    loc= box_loc
            if update:
                location=location_next_step
                new_grid[location[0]][location[1]] = '@'
                grid = new_grid
    # print_grid(grid)
    return find_all_occurence_char_in_grid_list(grid, 'O')

def extra_step(d):
    return (2*d[0], 2*d[1])

def complete_instructions_part2(start,grid,instructions):
    location = start
    for inst in instructions:
        # print_grid(grid)
        # print(inst)
        direction = new_loc(inst)
        loc = tuple(a + b for a, b in zip(location, direction.value)) 
        if grid[loc[0]][loc[1]] == '.':
            grid[loc[0]][loc[1]] = '@'
            grid[location[0]][location[1]] = '.'
            location = loc
            continue
        elif grid[loc[0]][loc[1]] == '#':
            continue
        elif grid[loc[0]][loc[1]] == '[' or grid[loc[0]][loc[1]] == ']':
            if direction == Direction.LEFT:
                update = False
                new_grid = deepcopy(grid)
                location_next_step = loc
                while True:
                    box_loc1 = tuple(a + b for a, b in zip(loc, direction.value))  ##Second part box
                    box_loc2 = tuple(a + b for a, b in zip(loc, extra_step(direction.value))) #Next char
                    if grid[box_loc2[0]][box_loc2[1]] == '.':
                        new_grid[box_loc2[0]][box_loc2[1]] = '['
                        new_grid[box_loc1[0]][box_loc1[1]] = ']'
                        # new_grid[loc[0]][loc[1]] = '@'
                        new_grid[location[0]][location[1]] = '.'
                        update=True
                        break
                    elif grid[box_loc2[0]][box_loc2[1]] == '#':
                        update=False
                        break
                    elif grid[box_loc2[0]][box_loc2[1]] == ']':
                        new_grid[box_loc2[0]][box_loc2[1]] = '['
                        new_grid[box_loc1[0]][box_loc1[1]] = ']'
                        new_grid[loc[0]][loc[1]] = 'O'
                        new_grid[location[0]][location[1]] = '.'
                        loc= box_loc1
                if update:
                    location=location_next_step
                    new_grid[location[0]][location[1]] = '@'
                    grid = new_grid
            if direction == Direction.RIGHT:
                update = False
                new_grid = deepcopy(grid)
                location_next_step = loc
                while True:
                    box_loc1 = tuple(a + b for a, b in zip(loc, direction.value))  ##Second part box
                    box_loc2 = tuple(a + b for a, b in zip(loc, extra_step(direction.value))) #Next char
                    if grid[box_loc2[0]][box_loc2[1]] == '.':
                        new_grid[box_loc2[0]][box_loc2[1]] = ']'
                        new_grid[box_loc1[0]][box_loc1[1]] = '['
                        # new_grid[loc[0]][loc[1]] = '@'
                        new_grid[location[0]][location[1]] = '.'
                        update=True
                        break
                    elif grid[box_loc2[0]][box_loc2[1]] == '#':
                        update=False
                        break
                    elif grid[box_loc2[0]][box_loc2[1]] == '[':
                        new_grid[box_loc2[0]][box_loc2[1]] = ']'
                        new_grid[box_loc1[0]][box_loc1[1]] = '['
                        new_grid[loc[0]][loc[1]] = 'O'
                        new_grid[location[0]][location[1]] = '.'
                        loc= box_loc1
                if update:
                    location=location_next_step
                    new_grid[location[0]][location[1]] = '@'
                    grid = new_grid
    # COnt in sandbox
    # print_grid(grid)
    return find_all_occurence_char_in_grid_list(grid, '[')

def solve_part1(data):
    grid, instructions = parse_data(data)
    start = find_in_grid(grid, '@')[0]
    boxes = complete_instructions(start,grid, instructions)
    return calculate_sum_of_boxes(boxes)

def solve_part2(data):
    grid, instructions = parse_data_part2(data)
    start = find_in_grid(grid, '@')[0]
    boxes = complete_instructions_part2(start,grid, instructions)
    return calculate_sum_of_boxes(boxes)

if __name__ == "__main__":
    year, day = 2024, 15
    
    # Read inputs
    input_data = read_input(year, day, file_name="input.txt")
    test_data = read_input(year, day, file_name="test.txt")
    test_data_mini = read_input(year, day, file_name="test2.txt")
    
    # Test cases (update with known solutions for the test input)
    mini_test = 2028
    known_test_solution_part1 = 10092  # Replace with the known result for part 1
    known_test_solution_part2 = 9021  # Replace with the known result for part 2
    
    
    # Verify test cases for Part 1
    print(f"Testing Part 1 for Day 15, Year 2024...")
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
        print(f"Testing Part 2 for Day 15, Year 2024...")
        test_result_part2 = solve_part2(test_data)
        if test_result_part2 == known_test_solution_part2:
            print("✅ Part 2 Test Passed")
            part2_result = solve_part2(input_data)
            print(f"Part 2 Result: {part2_result}")
            submit(year, day, part1_result, part2_result)
        else:
            raise AssertionError(f"❌ Part 2 Test Failed: Expected {known_test_solution_part2}, Got {test_result_part2}")
