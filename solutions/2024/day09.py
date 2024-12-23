from copy import deepcopy
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
        if index % 2 == 0:
            subdisk = [int(index/2) for _ in range(num)]
            disk.extend(subdisk)
        if index % 2 == 1:
            subdisk = ['.' for _ in range(num)]
            disk.extend(subdisk)
    return disk

def compress_disk(disk):
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
    total = 0
    for index, number in enumerate(compressed):
        if number == '.':
            continue
        total += index*number
    return total

def part1_faster(data):
    disk = create_disk(data)
    print(disk)
    print(len(disk))
    total_slots = 0
    for ind,c in enumerate(list(map(int,list(data[0])))):
        if ind % 2 == 0:
            total_slots += int(c)
    print(total_slots)
    queue = disk[total_slots:]
    strippedqueue = [char for char in queue if char != '.']
    pointer = 0
    while len(strippedqueue) > 0:
        if disk[pointer] == '.':
            x=strippedqueue.pop()
            disk[pointer] = x
        pointer += 1
    print(disk[:total_slots])
    return disk[:total_slots]

def shift_disk(data):
    numdata =list(map(int,list(data[0])))
    original_numdata = deepcopy(numdata)
    disk = create_disk(data)
    pointer_free = 1
    for main_pointer in range(len(numdata)-1,0,-2):
        if main_pointer % 1000 == 0:
            print(main_pointer)
        
        continue_free_search = True
        while continue_free_search:
            if (numdata[pointer_free] >= original_numdata[main_pointer]):
                starting = sum(numdata[:pointer_free])
                range_update = original_numdata[main_pointer]
                continue_free_search = False
                numdata[main_pointer-1] += original_numdata[main_pointer]
                numdata[main_pointer] -= original_numdata[main_pointer]
                numdata[pointer_free-1] += original_numdata[main_pointer]
                numdata[pointer_free] -= original_numdata[main_pointer]
                #Update disk
                start_remove = get_index(disk,int(main_pointer/2))
                for i in range(range_update):
                    disk[starting + i] = int(main_pointer/2)
                    disk[start_remove + i] = '.'
                pointer_free = -1
                continue_free_search = False
            pointer_free += 2
            if pointer_free > main_pointer:
                pointer_free = 1
                continue_free_search = False
    print('after', disk)
    return disk

def solve_part1(data):
    compressed = part1_faster(data)
    return checksum(compressed)

def solve_part2(data):
    compressed_2 = shift_disk(data)
    return checksum(compressed_2)

if __name__ == "__main__":
    year, day = 2024, 9
    
    # Read inputs
    input_data = read_input(year, day, file_name="input.txt")
    test_data = read_input(year, day, file_name="test.txt")
    
    # Test cases (update with known solutions for the test input)
    known_test_solution_part1 = 1928  # Replace with the known result for part 1
    known_test_solution_part2 = 2858  # Replace with the known result for part 2
    
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
    if part1_result is None and known_test_solution_part2 is not None:
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
