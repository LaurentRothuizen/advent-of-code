import sys
import os

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
sys.path.insert(0, project_root)


from utils.input_parser import read_input
from utils.submit import submit
def parse_instructions(data):
    """Convert instructions like 'R12' or 'L5' into signed integers."""
    return [int(line[1:]) * (1 if line[0] == 'R' else -1) for line in data]


def solve_part1(data):
    dial = 50
    count = 0
    instructions = parse_instructions(data)

    for inst in instructions:
        dial = (dial + inst) % 100
        if dial == 0:
            count += 1

    return count

def solve_part2(data):
    dial = 50
    total = 0
    for inst in parse_instructions(data):
        start = dial
        end = dial + inst

        # Number of multiples of 100 in the interval (start, end] or (end, start]
        crossed = abs(end // 100 - start // 100)
        total += crossed
        dial = end % 100

    return total

if __name__ == "__main__":
    year, day = 2025, 1
    
    # Read inputs
    input_data = read_input(year, day, file_name="input.txt")
    test_data = read_input(year, day, file_name="test.txt")
    
    # Test cases (update with known solutions for the test input)
    known_test_solution_part1 = 3  # Replace with the known result for part 1
    known_test_solution_part2 = 6  # Replace with the known result for part 2
    #part1_result = 1177
    #part2_result = 6768
    
    # Verify test cases for Part 1
    print(f"Testing Part 1 for Day 1, Year 2025...")
    if known_test_solution_part2 is None:
        test_result_part1 = solve_part1(test_data)
        if test_result_part1 == known_test_solution_part1:
            print("✅ Part 1 Test Passed")
            part1_result = solve_part1(input_data)
            print(f"Part 1 Result: {part1_result}")
        else:
            raise AssertionError(f"❌ Part 1 Test Failed: Expected {known_test_solution_part1}, Got {test_result_part1}")
    else:
        part1_result = 1177

    # Only proceed to Part 2 if Part 1 is implemented and working
    if part1_result is not None and known_test_solution_part2 is not None:
        # Verify test cases for Part 2
        print(f"Testing Part 2 for Day 1, Year 2025...")
        test_result_part2 = solve_part2(test_data)
        if test_result_part2 == known_test_solution_part2:
            print("✅ Part 2 Test Passed")
            part2_result = solve_part2(input_data)
            print(f"Part 2 Result: {part2_result}")
            submit(year, day, part1_result, part2_result)
        else:
            raise AssertionError(f"❌ Part 2 Test Failed: Expected {known_test_solution_part2}, Got {test_result_part2}")
