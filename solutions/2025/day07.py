import sys
import os

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
sys.path.insert(0, project_root)


from utils.common_functions import find_all_occurence_char_in_grid_list, find_in_grid, print_grid
from utils.input_parser import read_input
from utils.submit import submit

SPLIT = [
    (0,-1), (0,1)
]

DOWN = (1,0)

def add_tuples(t1,t2):
    return tuple(t1[i] + t2[i] for i in range(len(t1)))
    

def update_beams_down(beams):
    return [tuple(add_tuples(beam,DOWN)) for beam in beams]

def update_beams_split(beams, splitters):
    splits_new = 0
    beams_new = []
    for beam in beams:
        if beam in splitters:
            splits_new += 1
            beams_new.append(add_tuples(beam, SPLIT[0]))
            beams_new.append(add_tuples(beam, SPLIT[1]))
        else:
            beams_new.append(beam)
    return list(set(beams_new)), splits_new

def solve_part1(data):
    print_grid(data)
    beams = find_in_grid(data, 'S')
    splits = 0
    splitters = find_all_occurence_char_in_grid_list(data, '^')
    print(splitters)
    generations = 0
    while generations <= len(data):
        beams = update_beams_down(beams)
        beams, splits_new = update_beams_split(beams,splitters)
        splits += splits_new
        generations += 1
    print(splits)
    return splits

def update_particle_down(particle):
    return tuple(add_tuples(particle,DOWN))

def solve_part2(data):
    particle_start = find_in_grid(data, 'S')[0]
    splitters = find_all_occurence_char_in_grid_list(data, '^')
    memo = {}
    def count_paths(gen, particle):
        # Stop condition
        if gen > len(data):
            return 1

        # Memoization
        key = (gen, particle)
        if key in memo:
            return memo[key]

        particle2 = update_particle_down(particle)

        if particle2 in splitters:
            left  = count_paths(gen + 1, add_tuples(particle2, SPLIT[0]))
            right = count_paths(gen + 1, add_tuples(particle2, SPLIT[1]))
            total = left + right
        else:
            total = count_paths(gen + 1, particle2)

        memo[key] = total
        return total
    
    all_paths = count_paths(0,particle_start)
    print(all_paths)
    return all_paths

if __name__ == "__main__":
    year, day = 2025, 7
    
    # Read inputs
    input_data = read_input(year, day, file_name="input.txt")
    test_data = read_input(year, day, file_name="test.txt")
    
    # Test cases (update with known solutions for the test input)
    known_test_solution_part1 = 21  # Replace with the known result for part 1
    known_test_solution_part2 = 40  # Replace with the known result for part 2
    
    # Verify test cases for Part 1
    print(f"Testing Part 1 for Day 7, Year 2025...")
    if known_test_solution_part2 is None:
        test_result_part1 = solve_part1(test_data)
        if test_result_part1 == known_test_solution_part1:
            print("✅ Part 1 Test Passed")
            part1_result = solve_part1(input_data)
            print(f"Part 1 Result: {part1_result}")
        else:
            raise AssertionError(f"❌ Part 1 Test Failed: Expected {known_test_solution_part1}, Got {test_result_part1}")
    else:
        part1_result = 1717
        # part1_result = 231507396180012

    # Only proceed to Part 2 if Part 1 is implemented and working
    if part1_result is not None and known_test_solution_part2 is not None:
        # Verify test cases for Part 2
        print(f"Testing Part 2 for Day 7, Year 2025...")
        test_result_part2 = solve_part2(test_data)
        if test_result_part2 == known_test_solution_part2:
            print("✅ Part 2 Test Passed")
            part2_result = solve_part2(input_data)
            print(f"Part 2 Result: {part2_result}")
            submit(year, day, part1_result, part2_result)
        else:
            raise AssertionError(f"❌ Part 2 Test Failed: Expected {known_test_solution_part2}, Got {test_result_part2}")
