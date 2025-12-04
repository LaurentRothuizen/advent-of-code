import sys
import os

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
sys.path.insert(0, project_root)


from utils.common_functions import create_border_around_grid, print_grid
from utils.input_parser import read_input
from utils.submit import submit

NEIGHBORS = [
    (-1,-1), (-1,0), (-1,1),
    (0,-1),          (0,1),
    (1,-1),  (1,0),  (1,1)
]

def check_roll(grid, x, y):
    if grid[x][y] != '@':
        return False
    return sum(
        grid[x + dx][y + dy] == '@'
        for dx, dy in NEIGHBORS
    ) < 4

def solve_part1(data):
    grid = create_border_around_grid(data)
    size = len(grid)
    total = sum(
        check_roll(grid, i, j)
        for i in range(1, size - 1)
        for j in range(1, size - 1)
    )
    return total

def solve_part2(data):
    grid = create_border_around_grid(data)
    size = len(grid)
    candidates = {
        (i, j)
        for i in range(1, size - 1)
        for j in range(1, size - 1)
        if grid[i][j] == '@'
    }

    total = 0
    while candidates:
        removable = [(x, y) for (x, y) in candidates if check_roll(grid, x, y)]
        if not removable:
            break
        total += len(removable)
        for x, y in removable:
            grid[x][y] = '.'

        new_candidates = set()
        for x, y in removable:
            for dx, dy in NEIGHBORS:
                nx, ny = x + dx, y + dy
                if grid[nx][ny] == '@':
                    new_candidates.add((nx, ny))

        candidates = new_candidates

    return total

if __name__ == "__main__":
    year, day = 2025, 4
    
    # Read inputs
    input_data = read_input(year, day, file_name="input.txt")
    test_data = read_input(year, day, file_name="test.txt")
    
    # Test cases (update with known solutions for the test input)
    known_test_solution_part1 = 13  # Replace with the known result for part 1
    known_test_solution_part2 = 43  # Replace with the known result for part 2
    
    # Verify test cases for Part 1
    print(f"Testing Part 1 for Day 4, Year 2025...")
    if known_test_solution_part2 is None:
        test_result_part1 = solve_part1(test_data)
        if test_result_part1 == known_test_solution_part1:
            print("✅ Part 1 Test Passed")
            part1_result = solve_part1(input_data)
            print(f"Part 1 Result: {part1_result}")
        else:
            raise AssertionError(f"❌ Part 1 Test Failed: Expected {known_test_solution_part1}, Got {test_result_part1}")
    else:
        part1_result = 1376
        #part2_result = 8587

    # Only proceed to Part 2 if Part 1 is implemented and working
    if part1_result is not None and known_test_solution_part2 is not None:
        # Verify test cases for Part 2
        print(f"Testing Part 2 for Day 4, Year 2025...")
        test_result_part2 = solve_part2(test_data)
        if test_result_part2 == known_test_solution_part2:
            print("✅ Part 2 Test Passed")
            part2_result = solve_part2(input_data)
            print(f"Part 2 Result: {part2_result}")
            submit(year, day, part1_result, part2_result)
        else:
            raise AssertionError(f"❌ Part 2 Test Failed: Expected {known_test_solution_part2}, Got {test_result_part2}")
