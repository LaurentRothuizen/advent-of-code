import sys
import os

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
sys.path.insert(0, project_root)


from utils.input_parser import read_input
from utils.submit import submit
def solve_part1(data):
    count = 0
    dial = 50
    instructions = [int(x.strip('\n')[1:]) if x.strip('\n')[0] == 'R' else -int(x.strip('\n')[1:]) for x in data] 
    for inst in instructions:
        dial = (dial + inst) % 100
        if dial == 0:
            count+=1
    return count

def past_100(dial, inst):
    temp = abs(inst) // 100
    if dial == 0:
        print('0', dial, inst, abs(inst) // 100, temp)
        return temp
    new_dial = dial + inst
    if new_dial < 0 and new_dial + temp * 100 < 0:
        temp += 1
    elif new_dial > 100 and new_dial - temp * 100 > 100: #and (dial + inst) % 100 != 0 and dial + inst - temp * 100 > 100
        temp += 1
    print(dial, inst, abs(inst) // 100, temp)
    return temp

def solve_part2(data):
    count = 0
    dial = 50
    instructions = [int(x.strip('\n')[1:]) if x.strip('\n')[0] == 'R' else -int(x.strip('\n')[1:]) for x in data] 
    for inst in instructions:
        count_temp = past_100(dial, inst)
        dial = (dial + inst) % 100
        if dial == 0:
            count_temp+=1
        print('count_temp', count_temp)
        count += count_temp
    return count

if __name__ == "__main__":
    year, day = 2025, 1
    
    # Read inputs
    input_data = read_input(year, day, file_name="input.txt")
    test_data = read_input(year, day, file_name="test.txt")
    
    # Test cases (update with known solutions for the test input)
    known_test_solution_part1 = 3  # Replace with the known result for part 1
    known_test_solution_part2 = 6  # Replace with the known result for part 2
    # 7207, 6971, 6985, 6768
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
