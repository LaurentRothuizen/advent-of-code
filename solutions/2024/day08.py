from itertools import combinations
import sys
import os

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
sys.path.insert(0, project_root)


from utils.common_functions import find_all_chars_in_grid_dict
from utils.input_parser import read_input
from utils.submit import submit

def all_pairs_per_key(nodes):
    return list(combinations(nodes, 2))
    
def all_antinodes(pair_list, w, h):
    antinodes = []
    for pair in pair_list:
        d_tuple = tuple(map(lambda i, j: i - j, pair[0], pair[1]))
        loc1 = tuple(map(lambda i, j: i + j, pair[0], d_tuple))
        loc2 = tuple(map(lambda i, j: i - j, pair[1], d_tuple))
        if 0 <= loc1[0] <= h and 0 <= loc1[1] < w: 
            antinodes.append(loc1)
        if 0 <= loc2[0] <= h and 0 <= loc2[1] < w: 
            antinodes.append(loc2)
    return antinodes

def all_antinodes_freq(pair_list, w, h):
    antinodes = []
    maxnumber = max(w,h)
    for pair in pair_list:
        d_tuple = tuple(map(lambda i, j: i - j, pair[0], pair[1]))
        for k in range(-maxnumber,maxnumber):
            loc = tuple(map(lambda i, j: i + k*j, pair[0], d_tuple))
            if 0 <= loc[0] < h and 0 <= loc[1] < w: 
                antinodes.append(loc)
    return antinodes

def solve_part1(data):
    grid = [list(line.strip('\n')) for line in data]
    w, h = len(grid[0]), len(grid)
    print(w,h)
    node_dict = find_all_chars_in_grid_dict(grid, '.')
    antinodes_total = []
    for key in node_dict:
        pair_list = all_pairs_per_key(node_dict[key])
        antinodes_total.extend(all_antinodes(pair_list, w, h))
    return len(set(antinodes_total))

def solve_part2(data):
    grid = [list(line.strip('\n')) for line in data]
    w, h = len(grid[0]), len(grid)
    print(w,h)
    node_dict = find_all_chars_in_grid_dict(grid, '.')
    antinodes_total = []
    for key in node_dict:
        pair_list = all_pairs_per_key(node_dict[key])
        antinodes_total.extend(all_antinodes_freq(pair_list, w, h))
    return len(set(antinodes_total))

if __name__ == "__main__":
    year, day = 2024, 8
    
    # Read inputs
    input_data = read_input(year, day, file_name="input.txt")
    test_data = read_input(year, day, file_name="test.txt")
    
    # Test cases (update with known solutions for the test input)
    known_test_solution_part1 = 14  # Replace with the known result for part 1
    known_test_solution_part2 = 34  # Replace with the known result for part 2
    
    # Verify test cases for Part 1
    print(f"Testing Part 1 for Day 8, Year 2024...")
    # try:
    test_result_part1 = solve_part1(test_data)
    if test_result_part1 == known_test_solution_part1:
        print("✅ Part 1 Test Passed")
    else:
        print(f"❌ Part 1 Test Failed: Expected {known_test_solution_part1}, Got {test_result_part1}")
    # except Exception as e:
    #     print(f"❌ Part 1 Test Error: {e}")
    
    # Solve Part 1
    part1_result = None
    if test_result_part1 == known_test_solution_part1:
        try:
            part1_result = solve_part1(input_data)
            print(f"Part 1 Result: {part1_result}")
        except Exception as e:
            print(f"❌ Error solving Part 1: {e}")

    # Only proceed to Part 2 if Part 1 is implemented and working
    if part1_result is not None and known_test_solution_part2 is not None:
        # Verify test cases for Part 2
        print(f"Testing Part 2 for Day 8, Year 2024...")
        try:
            test_result_part2 = solve_part2(test_data)
            if test_result_part2 == known_test_solution_part2:
                print("✅ Part 2 Test Passed")
            else:
                print(f"❌ Part 2 Test Failed: Expected {known_test_solution_part2}, Got {test_result_part2}")
        except Exception as e:
            print(f"❌ Part 2 Test Error: {e}")
        
        # Solve Part 2
        try:
            part2_result = solve_part2(input_data)
            print(f"Part 2 Result: {part2_result}")
            submit(year, day, part1_result, part2_result)
        except Exception as e:
            print(f"❌ Error solving Part 2: {e}")
