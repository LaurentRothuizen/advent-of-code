import sys
import os

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
sys.path.insert(0, project_root)


from utils.input_parser import read_input
from utils.submit import submit

def pasre_data(data):
    patterns = []
    towels = data[0].strip('\n').split(', ')
    for line in data[2:]:
        patterns.append(line.strip('\n'))
    return towels, patterns

def get_possible_towels(length_p, towels):
    return [t for t in towels if len(t) <= length_p]

def recursive_pattern_check(p, towels):
    length_p = len(p)
    if length_p == 0:
        return True
    
    for t in get_possible_towels(length_p, towels):
        if p[:len(t)] == t:
            if recursive_pattern_check(p[len(t):], towels):
                return True
    
    return False
    

def pattern_is_valid(pattern, towels):
    return recursive_pattern_check(pattern,towels)

def all_possible_patterns(towels, patterns):
    total = 0
    for pattern in patterns:
        if pattern_is_valid(pattern, towels):
            total += 1
    return total
    
def solve_part1(data):
    towels, patterns = pasre_data(data)
    return all_possible_patterns(towels, patterns)

# part 2

def recursive_pattern_number(p, towels, dp):
    length_p = len(p)
    if length_p == 0:
        return 1
    if p in dp:
        return dp[p]
    total = 0
    for t in towels:
        if p[:len(t)] == t:
            total += recursive_pattern_number(p[len(t):], towels, dp)
    dp[p] = total
    return total

def number_of_towel_arrangements(pattern,towels):
    dp = {}
    result = recursive_pattern_number(pattern,towels, dp)
    return result

def all_possible_patterns_combinations(towels, patterns):
    possible = []
    for pattern in patterns:
        if pattern_is_valid(pattern, towels):
            possible.append(pattern)
    total = 0
    for index, pat in enumerate(possible):
        print(str(index) + ' uit ' + str(len(possible)))
        total += number_of_towel_arrangements(pat,towels)
    return total

def solve_part2(data):
    towels, patterns = pasre_data(data)
    return all_possible_patterns_combinations(towels, patterns)

if __name__ == "__main__":
    year, day = 2024, 19
    
    # Read inputs
    input_data = read_input(year, day, file_name="input.txt")
    test_data = read_input(year, day, file_name="test.txt")
    
    # Test cases (update with known solutions for the test input)
    known_test_solution_part1 = 6  # Replace with the known result for part 1
    known_test_solution_part2 = 16  # Replace with the known result for part 2
    
    # Verify test cases for Part 1
    print(f"Testing Part 1 for Day 19, Year 2024...")
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
        print(f"Testing Part 2 for Day 19, Year 2024...")
        test_result_part2 = solve_part2(test_data)
        if test_result_part2 == known_test_solution_part2:
            print("✅ Part 2 Test Passed")
            part2_result = solve_part2(input_data)
            print(f"Part 2 Result: {part2_result}")
            submit(year, day, part1_result, part2_result)
        else:
            raise AssertionError(f"❌ Part 2 Test Failed: Expected {known_test_solution_part2}, Got {test_result_part2}")
