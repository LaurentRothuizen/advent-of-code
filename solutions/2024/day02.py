import sys
import os

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
sys.path.insert(0, project_root)


from utils.input_parser import read_input
from utils.submit import submit

def valid(x,y):
    return x < y < x + 4

def safe(b):
    safe = True
    fail = []
    if (b[0] < b[1]):
        for num in range(len(b)-1):
            if not (valid(b[num],b[num+1])):
                fail.append(num)
                safe= False
            if (num == len(b)-1):
                fail.append(num + 1)

    elif (b[0] > b[1]):
        for num in range(len(b)-1):
            if not (valid(b[num+1],b[num])):
                fail.append(num)
                safe= False
            if (num == len(b)-1):
                fail.append(num + 1)

    else:
        fail.append(0)
        safe = False
    return safe, fail

def solve(data):
    a21 = 0
    a22 = 0
    for line in data:
        a = line.split()
        b = list(map(int,a))
        safe1, fail = safe(b)
        if (safe1):
            a21+=1
            a22+=1
        else:
            for i in range(len(b)):
                b_copy = []
                b_copy = b.copy()
                c= b_copy.pop(i)
                safe2, _ = safe(b_copy)
                if (safe2):
                    a22+=1
                    break

    return a21, a22

def solve_part1(data):
    tot, _ = solve(data)
    return tot

def solve_part2(data):
    _, tot = solve(data)
    return tot

if __name__ == "__main__":
    year, day = 2024, 2
    
    # Read inputs
    input_data = read_input(year, day, file_name="input.txt")
    test_data = read_input(year, day, file_name="test.txt")
    
    # Test cases (update with known solutions for the test input)
    known_test_solution_part1 = 2  # Replace with the known result for part 1
    known_test_solution_part2 = 4  # Replace with the known result for part 2
    
    # Verify test cases for Part 1
    print(f"Testing Part 1 for Day 2, Year 2024...")
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
        print(f"Testing Part 2 for Day 2, Year 2024...")
        test_result_part2 = solve_part2(test_data)
        if test_result_part2 == known_test_solution_part2:
            print("✅ Part 2 Test Passed")
            part2_result = solve_part2(input_data)
            print(f"Part 2 Result: {part2_result}")
            submit(year, day, part1_result, part2_result)
        else:
            raise AssertionError(f"❌ Part 2 Test Failed: Expected {known_test_solution_part2}, Got {test_result_part2}")
