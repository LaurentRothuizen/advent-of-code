import sys
import os
import re

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
sys.path.insert(0, project_root)


from utils.input_parser import read_input
from utils.submit import submit

def all_in_range(start, end):
    tot = 0
    if len(start) == len(end) and len(start) % 2 != 0:
        return 0
    for num in range(int(start),int(end)+1):
        x = str(num)
        if x[:len(x)//2] == x[len(x)//2:]:
            tot += num
            print(x)
    return tot

def solve_part1(data):
    ranges = [x.split('-') for x in data[0].split(',')]
    print(ranges)
    total = 0
    for r in ranges:
        total += all_in_range(r[0],r[1])
    return total

def check_repeat_pattern(num, x):
    if bool(re.fullmatch(r"(.+)\1+", x)):
        return num
    return 0

def all_in_range_part2(start, end):
    tot = 0
    for num in range(int(start),int(end)+1):
        tot += check_repeat_pattern(num, str(num))
    return tot

def solve_part2(data):
    ranges = [x.split('-') for x in data[0].split(',')]
    print(ranges)
    total = 0
    for r in ranges:
        total += all_in_range_part2(r[0],r[1])
    return total

if __name__ == "__main__":
    year, day = 2025, 2
    
    # Read inputs
    input_data = read_input(year, day, file_name="input.txt")
    test_data = read_input(year, day, file_name="test.txt")
    
    # Test cases (update with known solutions for the test input)
    known_test_solution_part1 = 1227775554  # Replace with the known result for part 1
    known_test_solution_part2 = 4174379265  # Replace with the known result for part 2
    
    # Verify test cases for Part 1
    print(f"Testing Part 1 for Day 2, Year 2025...")
    if known_test_solution_part2 is None:
        test_result_part1 = solve_part1(test_data)
        if test_result_part1 == known_test_solution_part1:
            print("✅ Part 1 Test Passed")
            part1_result = solve_part1(input_data)
            print(f"Part 1 Result: {part1_result}")
        else:
            raise AssertionError(f"❌ Part 1 Test Failed: Expected {known_test_solution_part1}, Got {test_result_part1}")
    else:
        part1_result = 64215794229
        #part2_result = 85513235135

    # Only proceed to Part 2 if Part 1 is implemented and working
    if part1_result is not None and known_test_solution_part2 is not None:
        # Verify test cases for Part 2
        print(f"Testing Part 2 for Day 2, Year 2025...")
        test_result_part2 = solve_part2(test_data)
        if test_result_part2 == known_test_solution_part2:
            print("✅ Part 2 Test Passed")
            part2_result = solve_part2(input_data)
            print(f"Part 2 Result: {part2_result}")
            submit(year, day, part1_result, part2_result)
        else:
            raise AssertionError(f"❌ Part 2 Test Failed: Expected {known_test_solution_part2}, Got {test_result_part2}")
