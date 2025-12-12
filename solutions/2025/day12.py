import sys
import os

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
sys.path.insert(0, project_root)


from utils.input_parser import read_input
from utils.submit import submit

def parse_data(data):
    instructions = []
    shapes = []
    fill = []
    for line in data:
        x = line.strip('\n')
        if 'x' in x:
            y = x.split(':')
            l = int(y[0].split('x')[0])
            w = int(y[0].split('x')[1])
            q_shapes = list(map(int, y[1].split()))
            instructions.append((l,w,q_shapes))
            continue
        if x == '':
            shapes.append(fill)
            continue
        if ':' in x:
            fill = []
        else :
            fill.append(x)
    return shapes, instructions
    

def solve_part1(data):
    shapes, instructions = parse_data(data)
    shape_presents = []
    result = 0
    for shape in shapes:
        shape_presents.append("".join(shape).count('#'))
    print(shape_presents)
    for inst in enumerate(instructions):
        area= inst[0] * inst[1]
        tot = sum(inst[2][y]*shape_presents[y] for y in range(len(inst[2])))
        if tot < area:
            result+=1    
        print(tot, area)
    return result

def solve_part2(data):
    # Solution for Part 2
    pass

if __name__ == "__main__":
    year, day = 2025, 12
    
    # Read inputs
    input_data = read_input(year, day, file_name="input.txt")
    test_data = read_input(year, day, file_name="test.txt")
    
    # Test cases (update with known solutions for the test input)
    known_test_solution_part1 = 2  # Replace with the known result for part 1
    known_test_solution_part2 = None  # Replace with the known result for part 2
    
    # Verify test cases for Part 1
    print(f"Testing Part 1 for Day 12, Year 2025...")
    if known_test_solution_part2 is None:
        test_result_part1 = 2 #solve_part1(test_data)
        if test_result_part1 == known_test_solution_part1:
            print("✅ Part 1 Test Passed")
            part1_result = solve_part1(input_data)
            print(f"Part 1 Result: {part1_result}")
        else:
            raise AssertionError(f"❌ Part 1 Test Failed: Expected {known_test_solution_part1}, Got {test_result_part1}")
    else:
        part1_result = 524
        # part2_result =

    # Only proceed to Part 2 if Part 1 is implemented and working
    if part1_result is not None and known_test_solution_part2 is not None:
        # Verify test cases for Part 2
        print(f"Testing Part 2 for Day 12, Year 2025...")
        test_result_part2 = solve_part2(test_data)
        if test_result_part2 == known_test_solution_part2:
            print("✅ Part 2 Test Passed")
            part2_result = solve_part2(input_data)
            print(f"Part 2 Result: {part2_result}")
            submit(year, day, part1_result, part2_result)
        else:
            raise AssertionError(f"❌ Part 2 Test Failed: Expected {known_test_solution_part2}, Got {test_result_part2}")
