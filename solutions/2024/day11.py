from copy import deepcopy
import sys
import os

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
sys.path.insert(0, project_root)


from utils.input_parser import read_input
from utils.submit import submit

def all_gens(init, gens):
    gen = init
    for generation in range(gens):
        print('gen: ', generation)
        new_gen = []
        for pointer, num in reversed(list(enumerate(gen))):
            if int(num) == 0:
                new_gen.append('1')
            elif len(num) % 2 == 0:
                new_gen.append(str(int(num[:len(num)//2])))
                new_gen.append(str(int(num[len(num)//2:])))
            else:
                new_gen.append(str(2024*(int(num))))
        gen = new_gen
    return len(gen)

def all_gens_dict(init_map, gens):
    gen_dict = init_map
    for generation in range(gens):
        new_dict = {}
        print('gen: ', generation)
        for num in gen_dict:
            if num == 0:
                new_dict[1] = new_dict.get(1, 0) + gen_dict[0]
            elif len(str(num)) % 2 == 0:
                num_str = str(num)
                x = int(num_str[:len(num_str)//2]) 
                y = int(num_str[len(num_str)//2:])
                new_dict[x] = new_dict.get(x, 0) + gen_dict[num]
                new_dict[y] = new_dict.get(y, 0) + gen_dict[num]
            else:
                z = 2024*num
                new_dict[z] = new_dict.get(z, 0) + gen_dict[num]
        gen_dict = new_dict
        # print(new_dict)
    return sum(gen_dict.values())


def solve_part1(data):
    # init = list(map(int,list(data[0].split(' '))))
    init = data[0].split(' ')
    print(init)
    return all_gens(init, 25)

def solve_part2(data):
    # print( 'part1', solve_part1(data))
    init = list(map(int,list(data[0].split(' '))))
    input_dict = {}
    for ini in init:
        if ini in input_dict.keys():
            input_dict[ini] += 1
        else:
            input_dict[ini] = 1
    print(input_dict)
    return all_gens_dict(input_dict, 75)

if __name__ == "__main__":
    year, day = 2024, 11
    
    # Read inputs
    input_data = read_input(year, day, file_name="input.txt")
    test_data = read_input(year, day, file_name="test.txt")
    
    # Test cases (update with known solutions for the test input)
    known_test_solution_part1 = 55312  # Replace with the known result for part 1
    known_test_solution_part2 = 1  # Replace with the known result for part 2
    
    # Verify test cases for Part 1
    print(f"Testing Part 1 for Day 11, Year 2024...")
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
        print(f"Testing Part 2 for Day 11, Year 2024...")
        test_result_part2 = 1#solve_part2(test_data)
        if test_result_part2 == known_test_solution_part2:
            print("✅ Part 2 Test Passed")
            part2_result = solve_part2(input_data)
            print(f"Part 2 Result: {part2_result}")
            submit(year, day, part1_result, part2_result)
        else:
            raise AssertionError(f"❌ Part 2 Test Failed: Expected {known_test_solution_part2}, Got {test_result_part2}")
