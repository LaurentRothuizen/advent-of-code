import sys
import os

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
sys.path.insert(0, project_root)


from utils.input_parser import read_input
from utils.submit import submit

import re

def extract_mul_expressions(s):
    # Regular expression pattern
    pattern = r"mul\(\d{1,3},\d{1,3}\)"
    
    # Find all matches
    matches = re.findall(pattern, s)
    return matches

def extract_mul_expressions_with_enable(s):
    # Regular expression pattern
    f = 'do()' + s
    pattern = r"mul\(\d{1,3},\d{1,3}\)"
    enable = r"do\(\)"
    disable = r"don't\(\)"
    stop = False
    substring = ''
    start_index = 0
    print(f)
    dos = [match.start() for match in re.finditer(enable, f)]
    donts = [match.start() for match in re.finditer(disable, f)]
    for do in dos:
        if stop:
            break
        if do < start_index:
            start_index = do
            continue
        for dont in donts:
            if dont > do:
                substring += f[do:dont]
                start_index = dont + 4
                break
        if donts[-1] < do:
            substring += f[do:-1]
            stop = True
    
    # Find all matches
    matches = re.findall(pattern, substring)
    return matches

def reg_solve_2(s):
    pattern=r"mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\)"
    matches=re.findall(pattern,s)
    res=[]
    flag=True
    for m in matches:
        if m =="do()":
            flag=True
        elif m =="don't()":
            flag=False
        else:
            if flag:
                res.append(m)
    return res


def solve_part1(data):
    a31 = 0
    muls = []
    total_string = ''
    for instruction in data:
        muls.extend(extract_mul_expressions(instruction))
        total_string += instruction
    for mul in muls:
        x, y = mul[4:-1].split(',')
        a31 += (int(x) * int(y))
    return a31

def solve_part2(data):
    a32 = 0
    muls2 = []
    total_string = ''
    for instruction in data:
        total_string += instruction
    muls2 = reg_solve_2(total_string)
    for mul in muls2:
        x, y = mul[4:-1].split(',')
        a32 += (int(x) * int(y))
    return a32

if __name__ == "__main__":
    year, day = 2024, 3
    
    # Read inputs
    input_data = read_input(year, day, file_name="input.txt")
    test_data = read_input(year, day, file_name="test.txt")
    
    # Test cases (update with known solutions for the test input)
    known_test_solution_part1 = 161  # Replace with the known result for part 1
    known_test_solution_part2 = 48  # Replace with the known result for part 2
    
    # Verify test cases for Part 1
    print(f"Testing Part 1 for Day 3, Year 2024...")
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
    if part1_result is not None and known_test_solution_part2 is not None:
        # Verify test cases for Part 2
        print(f"Testing Part 2 for Day 3, Year 2024...")
        test_result_part2 = solve_part2(test_data)
        if test_result_part2 == known_test_solution_part2:
            print("✅ Part 2 Test Passed")
            part2_result = solve_part2(input_data)
            print(f"Part 2 Result: {part2_result}")
            submit(year, day, part1_result, part2_result)
        else:
            raise AssertionError(f"❌ Part 2 Test Failed: Expected {known_test_solution_part2}, Got {test_result_part2}")
