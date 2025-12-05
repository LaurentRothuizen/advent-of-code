import sys
import os

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
sys.path.insert(0, project_root)


from utils.input_parser import read_input
from utils.submit import submit

def parse_input(data):
    ranges = [(int(b.split('-')[0]),int(b.split('-')[1].strip('\n'))) for b in data if '-' in b]
    ids = [int(id.strip('\n')) for id in data if '-' not in id and id.strip('\n')]
    return ranges, ids

def check_inclusion(id,ranges):
    return 1 if any(id in range(start, end + 1) for start, end in ranges) else 0

def solve_part1(data):
    ranges, ids = parse_input(data)
    total = sum(check_inclusion(id,ranges) for id in ids)
    print(total)
    return total

def solve_part2(data):
    ranges, _ = parse_input(data)
    sorted_ranges = sorted(ranges, key=lambda x: x[0])
    total_ids = 0
    pointer = 0
    for r in sorted_ranges:
        if r[0] > pointer:
            total_ids += abs(r[1]-r[0]) + 1
        elif r[0] <= pointer and r[1] > pointer:
            total_ids += abs(r[1]-pointer)
        pointer = max(r[1], pointer)
    return total_ids

if __name__ == "__main__":
    year, day = 2025, 5
    
    # Read inputs
    input_data = read_input(year, day, file_name="input.txt")
    test_data = read_input(year, day, file_name="test.txt")
    
    # Test cases (update with known solutions for the test input)
    known_test_solution_part1 = 3  # Replace with the known result for part 1
    known_test_solution_part2 = 14  # Replace with the known result for part 2
    #371234949762002
    #353608561649390
    #352509891817881
    
    # Verify test cases for Part 1
    print(f"Testing Part 1 for Day 5, Year 2025...")
    if known_test_solution_part2 is None:
        test_result_part1 = solve_part1(test_data)
        if test_result_part1 == known_test_solution_part1:
            print("✅ Part 1 Test Passed")
            part1_result = solve_part1(input_data)
            print(f"Part 1 Result: {part1_result}")
        else:
            raise AssertionError(f"❌ Part 1 Test Failed: Expected {known_test_solution_part1}, Got {test_result_part1}")
    else:
        part1_result = 674
        #part2_result = 352509891817881 

    # Only proceed to Part 2 if Part 1 is implemented and working
    if part1_result is not None and known_test_solution_part2 is not None:
        # Verify test cases for Part 2
        print(f"Testing Part 2 for Day 5, Year 2025...")
        test_result_part2 = solve_part2(test_data)
        if test_result_part2 == known_test_solution_part2:
            print("✅ Part 2 Test Passed")
            part2_result = solve_part2(input_data)
            print(f"Part 2 Result: {part2_result}")
            submit(year, day, part1_result, part2_result)
        else:
            raise AssertionError(f"❌ Part 2 Test Failed: Expected {known_test_solution_part2}, Got {test_result_part2}")
