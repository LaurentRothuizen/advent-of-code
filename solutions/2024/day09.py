import sys
import os

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
sys.path.insert(0, project_root)


from utils.common_functions import get_index
from utils.input_parser import read_input
from utils.submit import submit

def create_disk(data):
    disk = []
    numdata =list(map(int,list(data[0])))
    for index, num in enumerate(numdata):
        print(index, num)
        if index % 2 == 0:
            subdisk = [int(index/2) for _ in range(num)]
            disk.extend(subdisk)
        if index % 2 == 1:
            subdisk = ['.' for _ in range(num)]
            disk.extend(subdisk)
    print(disk)
    return disk

def compress_disk(disk):
    # for i in range(len(disk)-1, 0):
    #     if x := disk.find('.') > -1: 
    #         disk[x] = disk[i]
    while True:
        print(disk)
        x = disk.pop()
        if x == '.':
            continue
        if dot := get_index(disk, '.') > -1: 
            disk[dot+1] = x
        else:
            print(x)
            disk.extend(x)
            break
    print(disk)
    return disk

def checksum(compressed):
    return

def solve_part1(data):
    disk = create_disk(data)
    compressed = compress_disk(disk)
    return checksum(compressed)

def solve_part2(data):
    # Solution for Part 2
    pass

if __name__ == "__main__":
    year, day = 2024, 9
    
    # Read inputs
    input_data = read_input(year, day, file_name="input.txt")
    test_data = read_input(year, day, file_name="test.txt")
    
    # Test cases (update with known solutions for the test input)
    known_test_solution_part1 = 1928  # Replace with the known result for part 1
    known_test_solution_part2 = None  # Replace with the known result for part 2
    
    # Verify test cases for Part 1
    print(f"Testing Part 1 for Day 9, Year 2024...")
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
        print(f"Testing Part 2 for Day 9, Year 2024...")
        test_result_part2 = solve_part2(test_data)
        if test_result_part2 == known_test_solution_part2:
            print("✅ Part 2 Test Passed")
            part2_result = solve_part2(input_data)
            print(f"Part 2 Result: {part2_result}")
            submit(year, day, part1_result, part2_result)
        else:
            raise AssertionError(f"❌ Part 2 Test Failed: Expected {known_test_solution_part2}, Got {test_result_part2}")
