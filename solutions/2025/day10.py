import itertools
import sys
import os

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
sys.path.insert(0, project_root)


from utils.input_parser import read_input
from utils.submit import submit

def make_instructions(d):
    instruction_list = [x.strip('(').strip(')').split(',') for x in d]
    return [list(map(int, x)) for x in instruction_list]

def reduceMod2(l):
    return [i % 2 for i in l]

def solve_part1(data):
    machines = [(d.split()[0][1:-1], make_instructions(d.split()[1:-1]),list(map(int,d.split()[-1].strip('\n')[1:-1].split(',')))) for d in data]
    print(machines)
    total = 0
    for m in machines:
        target = [ 1 if char == '#' else 0 for char in m[0]]
        print(target)
        for button_size in range(1, len(m[1])):
            print(button_size)
            all_perms = list(itertools.combinations(range(len(m[1])), button_size))
            for perm in all_perms:
                found = False
                start = [0] * len(m[2])
                for press_button in perm:
                    for y in m[1][press_button]:
                        start[y] += 1
                check = reduceMod2(start)
                if check == target:
                    print(button_size)
                    total += button_size
                    found = True
                    break
            if found:
                break 
    return total  

def solve_part2(data):
    machines = [(d.split()[0][1:-1], make_instructions(d.split()[1:-1]),list(map(int,d.split()[-1].strip('\n')[1:-1].split(',')))) for d in data]
    print(machines)
    total = 0
    for idx, m in enumerate(machines):
        target = m[2]
        print(idx, len(machines))
        for button_size in range(1, len(m[1])*10):
            print(button_size)
            all_perms = list(itertools.combinations_with_replacement(range(len(m[1])), button_size))
            for perm in all_perms:
                found = False
                start = [0] * len(m[2])
                for press_button in perm:
                    for y in m[1][press_button]:
                        start[y] += 1
                check = start
                if check == target:
                    print(idx, button_size)
                    total += button_size
                    found = True
                    break
            if found:
                break 
    return total  

if __name__ == "__main__":
    year, day = 2025, 10
    
    # Read inputs
    input_data = read_input(year, day, file_name="input.txt")
    test_data = read_input(year, day, file_name="test.txt")
    
    # Test cases (update with known solutions for the test input)
    known_test_solution_part1 = 7  # Replace with the known result for part 1
    known_test_solution_part2 = 33  # Replace with the known result for part 2
    
    # Verify test cases for Part 1
    print(f"Testing Part 1 for Day 10, Year 2025...")
    if known_test_solution_part2 is None:
        test_result_part1 = solve_part1(test_data)
        if test_result_part1 == known_test_solution_part1:
            print("✅ Part 1 Test Passed")
            part1_result = solve_part1(input_data)
            print(f"Part 1 Result: {part1_result}")
        else:
            raise AssertionError(f"❌ Part 1 Test Failed: Expected {known_test_solution_part1}, Got {test_result_part1}")
    else:
        part1_result = 469
        #part2_result = 

    # Only proceed to Part 2 if Part 1 is implemented and working
    if part1_result is not None and known_test_solution_part2 is not None:
        # Verify test cases for Part 2
        print(f"Testing Part 2 for Day 10, Year 2025...")
        test_result_part2 = solve_part2(test_data)
        if test_result_part2 == known_test_solution_part2:
            print("✅ Part 2 Test Passed")
            part2_result = solve_part2(input_data)
            print(f"Part 2 Result: {part2_result}")
            submit(year, day, part1_result, part2_result)
        else:
            raise AssertionError(f"❌ Part 2 Test Failed: Expected {known_test_solution_part2}, Got {test_result_part2}")
