from copy import deepcopy
import sys
import os
from time import sleep

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
sys.path.insert(0, project_root)


from utils.common_functions import create_border_around_grid, find_all_chars_in_grid_dict, print_grid
from utils.input_parser import read_input
from utils.submit import submit

def get_nbs(cur):
    x,y = cur
    return [(x+1,y),(x,y+1),(x-1,y),(x,y-1),]
    


def area_score(letter_tuples):
    all_tuples = deepcopy(letter_tuples)
    total_score_letter = 0
    while len(all_tuples) > 0:
        total_score = 0
        first = all_tuples.pop(0)
        queue = [first]
        area = []
        while len(queue) > 0:
            tup_score = 4
            cur = queue.pop()
            area.append(cur)
            nbh = get_nbs(cur)
            for nb in nbh:
                if nb in letter_tuples:
                    tup_score -= 1
                    if nb not in queue and nb not in area:
                        queue.append(nb)
                    if nb in all_tuples: 
                        all_tuples.remove(nb)
            total_score += tup_score
        total_score_letter += total_score * len(area)
    return total_score_letter

def calculate_sides(area):
    north_facing = []
    east_facing = []
    south_facing = []
    west_facing = []
    for (x,y) in area:
        if (x-1,y) not in area:
            north_facing.append((x,y))
        if (x,y+1) not in area:
            east_facing.append((x,y))
        if (x+1,y) not in area:
            south_facing.append((x,y))
        if (x,y-1) not in area:
            west_facing.append((x,y))
    total = 0
    for (x,y) in sorted(north_facing, key=lambda x: x[0]):
        if (x,y+1) not in north_facing:
            total += 1
    for (x,y) in sorted(east_facing, key=lambda x: x[1]):
        if (x+1,y) not in east_facing:
            total += 1
    for (x,y) in sorted(south_facing, key=lambda x: x[0]):
        if (x,y+1) not in south_facing:
            total += 1
    for (x,y) in sorted(west_facing, key=lambda x: x[1]):
        if (x+1,y) not in west_facing:
            total += 1
    return total
    

def area_score_part2(letter_tuples):
    all_tuples = deepcopy(letter_tuples)
    total_score_letter = 0
    while len(all_tuples) > 0:
        first = all_tuples.pop(0)
        queue = [first]
        area = []
        while len(queue) > 0:
            cur = queue.pop()
            area.append(cur)
            nbh = get_nbs(cur)
            for nb in nbh:
                if nb in letter_tuples:
                    if nb not in queue and nb not in area:
                        queue.append(nb)
                    if nb in all_tuples: 
                        all_tuples.remove(nb)
        total_score_letter += (calculate_sides(area) * len(area))
    return total_score_letter

def solve_part1(data):
    grid = create_border_around_grid(data, size=1, split=True)
    all_chars_dict = find_all_chars_in_grid_dict(grid, '*')
    total_score = 0
    for letter in all_chars_dict:
        total_score += area_score(all_chars_dict[letter])
    return total_score

def solve_part2(data):
    grid = create_border_around_grid(data, size=1, split=True)
    all_chars_dict = find_all_chars_in_grid_dict(grid, '*')
    total_score = 0
    for letter in all_chars_dict:
        total_score += area_score_part2(all_chars_dict[letter])
    return total_score

if __name__ == "__main__":
    year, day = 2024, 12
    
    # Read inputs
    input_data = read_input(year, day, file_name="input.txt")
    test_data = read_input(year, day, file_name="test.txt")
    
    # Test cases (update with known solutions for the test input)
    known_test_solution_part1 = 1930  # Replace with the known result for part 1
    known_test_solution_part2 = 1206  # Replace with the known result for part 2
    
    # Verify test cases for Part 1
    print(f"Testing Part 1 for Day 12, Year 2024...")
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
        print(f"Testing Part 2 for Day 12, Year 2024...")
        test_result_part2 = solve_part2(test_data)
        if test_result_part2 == known_test_solution_part2:
            print("✅ Part 2 Test Passed")
            part2_result = solve_part2(input_data)
            print(f"Part 2 Result: {part2_result}")
            submit(year, day, part1_result, part2_result)
        else:
            raise AssertionError(f"❌ Part 2 Test Failed: Expected {known_test_solution_part2}, Got {test_result_part2}")
