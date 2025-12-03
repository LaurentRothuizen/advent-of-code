import sys
import os

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
sys.path.insert(0, project_root)


from utils.input_parser import read_input
from utils.submit import submit

def best_two_digits(bank: str) -> int:
    """
    Efficient Part 1 solution:
    1. Find the maximum digit in bank[0 : n-1].
    2. Then find the maximum digit in bank[i+1 : n].
    """
    digits = list(bank)

    # Step 1: find max in the first n-1 digits
    first_max = max(digits[:-1])
    i = digits.index(first_max)  # earliest occurrence (best choice)

    # Step 2: find max in the remaining digits bank[i+1:]
    second_max = max(digits[i+1:])

    return int(first_max + second_max)


def solve_part1(data):
    banks = [line.strip() for line in data]
    return sum(best_two_digits(bank) for bank in banks)

def calc_bank_twelve(bank: str) -> int:
    digits = list(map(int, bank))
    n = len(digits)
    k = 12
    result = []

    start = 0

    for remaining in range(k, 0, -1):
        # The right boundary of the search window
        end = n - remaining

        # Find the max digit in digits[start : end+1]
        window = digits[start:end+1]
        max_digit = max(window)

        # Find the FIRST occurrence of that max digit in the window
        idx = window.index(max_digit) + start

        # Append result
        result.append(str(max_digit))

        # Move start just after the chosen digit
        start = idx + 1

    return int("".join(result))


def solve_part2(data):
    return sum(calc_bank_twelve(line.strip()) for line in data)

if __name__ == "__main__":
    year, day = 2025, 3
    
    # Read inputs
    input_data = read_input(year, day, file_name="input.txt")
    test_data = read_input(year, day, file_name="test.txt")
    
    # Test cases (update with known solutions for the test input)
    known_test_solution_part1 = 357  # Replace with the known result for part 1 17107
    known_test_solution_part2 = 3121910778619  # Replace with the known result for part 2 169349762274117
    
    # Verify test cases for Part 1
    print(f"Testing Part 1 for Day 3, Year 2025...")
    if known_test_solution_part2 is None:
        test_result_part1 = solve_part1(test_data)
        if test_result_part1 == known_test_solution_part1:
            print("✅ Part 1 Test Passed")
            part1_result = solve_part1(input_data)
            print(f"Part 1 Result: {part1_result}")
        else:
            raise AssertionError(f"❌ Part 1 Test Failed: Expected {known_test_solution_part1}, Got {test_result_part1}")
    else:
        part1_result = 17107
        #part2_result = 169349762274117

    # Only proceed to Part 2 if Part 1 is implemented and working
    if part1_result is not None and known_test_solution_part2 is not None:
        # Verify test cases for Part 2
        print(f"Testing Part 2 for Day 3, Year 2025...")
        test_result_part2 = solve_part2(test_data)
        if test_result_part2 == known_test_solution_part2:
            print("✅ Part 2 Test Passed")
            part2_result = solve_part2(input_data)
            print(f"Part 2 Result: {part2_result}")
            submit(year, day, part1_result, part2_result)
        else:
            raise AssertionError(f"❌ Part 2 Test Failed: Expected {known_test_solution_part2}, Got {test_result_part2}")
