import math
import sys
import os

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
sys.path.insert(0, project_root)


from utils.input_parser import read_input
from utils.submit import submit

def parse_input(data):
    ops = data[-1].split()
    lines = []
    exs = []
    for line in data[:-1]:
        lines.append(list(map(int, line.split())))
    print(lines)
    print(ops)
    for i in range(len(ops)):
        ex = []
        ex.append(ops[i])
        for j in lines:
            ex.append(j[i])
        exs.append(ex)
    return exs

def solve_part1(data):
    exs = parse_input(data)
    print(exs)
    total = 0
    for ex in exs:
        if ex[0] == "*":
            total += math.prod(e for e in ex[1:])
        else :
            total += sum(e for e in ex[1:])
    print(total)
    return total

def parse_input_blocks(data):
    print(data)
    ops = data[-1].split()
    blocks = []
    start_block = 0
    for i in range(len(data[0])):
        if all(data[j][i] == ' ' or data[j][i] == '\n' for j in range(len(data[:-1]))):
            blocks.append([row[start_block:i] for row in data[:-1]])
            start_block = i + 1    
    return list(zip(ops,blocks))

def solve_part2(data):
    exs = parse_input_blocks(data)
    print(exs)
    total=0
    for ex in exs:
        nums = []
        word_length = len(ex[1][0])
        for i in range(word_length):
            nums.append(''.join(ex[1][j][i] for j in range(len(ex[1]))).strip())
        print('nums', nums)
        if ex[0] == "*":
            total += math.prod(e for e in list(map(int,nums)))
        else :
            total += sum(e for e in list(map(int,nums)))
        print(total)
    return total

if __name__ == "__main__":
    year, day = 2025, 6
    
    # Read inputs
    input_data = read_input(year, day, file_name="input.txt")
    test_data = read_input(year, day, file_name="test.txt")
    
    # Test cases (update with known solutions for the test input)
    known_test_solution_part1 = 4277556  # Replace with the known result for part 1
    known_test_solution_part2 = 3263827  # Replace with the known result for part 2
    
    # Verify test cases for Part 1
    print(f"Testing Part 1 for Day 6, Year 2025...")
    if known_test_solution_part2 is None:
        test_result_part1 = solve_part1(test_data)
        if test_result_part1 == known_test_solution_part1:
            print("✅ Part 1 Test Passed")
            part1_result = solve_part1(input_data)
            print(f"Part 1 Result: {part1_result}")
        else:
            raise AssertionError(f"❌ Part 1 Test Failed: Expected {known_test_solution_part1}, Got {test_result_part1}")
    else:
        part1_result = 5316572080628
        #part2_result = 11299263623062

    # Only proceed to Part 2 if Part 1 is implemented and working
    if part1_result is not None and known_test_solution_part2 is not None:
        # Verify test cases for Part 2
        print(f"Testing Part 2 for Day 6, Year 2025...")
        test_result_part2 = solve_part2(test_data)
        if test_result_part2 == known_test_solution_part2:
            print("✅ Part 2 Test Passed")
            part2_result = solve_part2(input_data)
            print(f"Part 2 Result: {part2_result}")
            submit(year, day, part1_result, part2_result)
        else:
            raise AssertionError(f"❌ Part 2 Test Failed: Expected {known_test_solution_part2}, Got {test_result_part2}")
