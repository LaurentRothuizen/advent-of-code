import sys
import os

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
sys.path.insert(0, project_root)

from utils.input_parser import read_input
from utils.submit import submit
def create_lists(data):
    first = []
    second = []
    for line in data:
        a,b = line.split()
        first.append(int(a))
        second.append(int(b))
    first.sort()
    second.sort()
    return first, second


def solve_part1(data):
    f,s = create_lists(data)
    tot = 0
    for i in range(len(f)):
        tot += abs(f[i]-s[i])
    return tot

def solve_part2(data):
    f,s = create_lists(data)
    tot = 0
    for j in f:
        tot += s.count(j) * j
    return tot

if __name__ == "__main__":
    year, day = 2024, 1
    
    # Read inputs
    input_data = read_input(year, day, file_name="input.txt")
    test_data = read_input(year, day, file_name="test.txt")
    
    # Test cases (update with known solutions for the test input)
    known_test_solution_part1 = 11  # Replace with the known result for part 1
    known_test_solution_part2 = 31  # Replace with the known result for part 2
    
    # Verify test cases for Part 1
    print(f"Testing Part 1 for Day 1, Year 2024...")
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
    try:
        part1_result = solve_part1(input_data)
        print(f"Part 1 Result: {part1_result}")
    except Exception as e:
        print(f"❌ Error solving Part 1: {e}")

    # Only proceed to Part 2 if Part 1 is implemented and working
    if part1_result is not None and known_test_solution_part2 is not None and known_test_solution_part2 is not None:
        # Verify test cases for Part 2
        print(f"Testing Part 2 for Day 1, Year 2024...")
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
