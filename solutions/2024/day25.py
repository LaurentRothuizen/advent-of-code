import sys
import os

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
sys.path.insert(0, project_root)


from utils.input_parser import read_input
from utils.submit import submit

def build_lock(build):
    key = [0]*5
    for l in build[1:]:
        for index, char in enumerate(l):
            if char == '#':
                key[index] += 1
    return key

def parse_input(data):
    locks, keys = [], []
    lock = False if data[0] == '.....\n' else True
    build = []
    for index, line in enumerate(data):
        if line == '\n':
            if lock:
                lock_build = build_lock(build)
                locks.append(lock_build)
            else: 
                key_build = build_lock(list(reversed(build)))
                keys.append(key_build)
            build = []
            if data[index + 1] == '.....\n':
                lock = False
            elif data[index + 1] == '#####\n':
                lock = True
        else:
            build.append(line.strip('\n'))
            
    if lock:
        lock_build = build_lock(build)
        locks.append(lock_build)
    else: 
        key_build = build_lock(list(reversed(build)))
        keys.append(key_build)
    return locks, keys

def solve_part1(data):
    locks, keys = parse_input(data)
    unique = 0
    for lock in locks:
        for key in keys:
            if max([sum(x) for x in zip(lock, key)]) <= 5:
                unique += 1            
    return unique

def solve_part2(data):
    # Solution for Part 2
    pass

if __name__ == "__main__":
    year, day = 2024, 25
    
    # Read inputs
    input_data = read_input(year, day, file_name="input.txt")
    test_data = read_input(year, day, file_name="test.txt")
    
    # Test cases (update with known solutions for the test input)
    known_test_solution_part1 = 3  # Replace with the known result for part 1
    known_test_solution_part2 = None  # Replace with the known result for part 2
    
    # Verify test cases for Part 1
    print(f"Testing Part 1 for Day 25, Year 2024...")
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
        print(f"Testing Part 2 for Day 25, Year 2024...")
        test_result_part2 = solve_part2(test_data)
        if test_result_part2 == known_test_solution_part2:
            print("✅ Part 2 Test Passed")
            part2_result = solve_part2(input_data)
            print(f"Part 2 Result: {part2_result}")
            submit(year, day, part1_result, part2_result)
        else:
            raise AssertionError(f"❌ Part 2 Test Failed: Expected {known_test_solution_part2}, Got {test_result_part2}")
