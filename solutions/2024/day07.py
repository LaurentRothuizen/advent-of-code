import itertools
import sys
import os

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
sys.path.insert(0, project_root)


from utils.input_parser import read_input
from utils.submit import submit

def parse_input(data):
    d1 = [line.strip('\n').split(': ') for line in data]
    all = []
    for l in d1:
        lhs = int(l[0])
        rhs = list(map(int, l[1].split()))
        all.append((lhs, rhs))
    return all

def get_configs(operators_number):
    combs = [''.join(comb) for comb in itertools.product(['+', '*'], repeat=operators_number)]
    return combs

def evaluate(lhs,nums,ops):
    for op in ops:
        o = list(op)
        
        # Build the expression dynamically
        expression = str(nums[0])
        for i, op in enumerate(o):
            if op == '|':
                expression += f"{nums[i + 1]}"
            else:
                expression += f" {op} {nums[i + 1]}"
                expression = str(eval(expression))

        if int(expression) == lhs:
            return True
    return False

def possible_eq(eq):
    lhs = eq[0]
    operators_number = len(eq[1]) - 1
    all_configs = get_configs(operators_number)
    return evaluate(lhs, eq[1],all_configs)

def solve_part1(data):
    total_score = 0
    equation_list = parse_input(data)
    for i, eq in enumerate(equation_list):
        print(str(i) + ' of ' + str(len(equation_list)) )
        if possible_eq(eq):
            total_score += eq[0]
    return total_score

def get_max_operator(equation_list):
    return max([len(eq[1]) for eq in equation_list ])

def get_config_map(max_operator):
    config_dict = {}
    for j in range(1,max_operator):
        config_dict[j] = [''.join(comb) for comb in itertools.product(['+', '*', '|'], repeat=j)]
    return config_dict

def possible_eq2(eq, config):
    lhs = eq[0]
    return evaluate(lhs, eq[1], config)

def solve_part2(data):
    total_score = 0
    equation_list = parse_input(data)
    max_operator = get_max_operator(equation_list)
    config_map = get_config_map(max_operator)
    for i, eq in enumerate(equation_list):
        print(str(i) + ' of ' + str(len(equation_list)) )
        if possible_eq2(eq, config_map[len(eq[1]) - 1]):
            total_score += eq[0]
    return total_score

if __name__ == "__main__":
    year, day = 2024, 7
    
    # Read inputs
    input_data = read_input(year, day, file_name="input.txt")
    test_data = read_input(year, day, file_name="test.txt")
    
    # Test cases (update with known solutions for the test input)
    known_test_solution_part1 = 3749  # Replace with the known result for part 1
    known_test_solution_part2 = 11387  # Replace with the known result for part 2
    
    # Verify test cases for Part 1
    print(f"Testing Part 1 for Day 7, Year 2024...")
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
    if test_result_part1 == known_test_solution_part1:
        try:
            part1_result = 1582598718861 # solve_part1(input_data)
            print(f"Part 1 Result: {part1_result}")
        except Exception as e:
            print(f"❌ Error solving Part 1: {e}")

    # Only proceed to Part 2 if Part 1 is implemented and working
    if part1_result is None and known_test_solution_part2 is not None:
        # Verify test cases for Part 2
        print(f"Testing Part 2 for Day 7, Year 2024...")
        # try:
        test_result_part2 = solve_part2(test_data)
        if test_result_part2 == known_test_solution_part2:
            print("✅ Part 2 Test Passed")
        else:
            print(f"❌ Part 2 Test Failed: Expected {known_test_solution_part2}, Got {test_result_part2}")
        # except Exception as e:
        #     print(f"❌ Part 2 Test Error: {e}")
        
        # Solve Part 2
        if test_result_part2 == known_test_solution_part2:
            try:
                part2_result = solve_part2(input_data)
                print(f"Part 2 Result: {part2_result}")
                submit(year, day, part1_result, part2_result)
            except Exception as e:
                print(f"❌ Error solving Part 2: {e}")
