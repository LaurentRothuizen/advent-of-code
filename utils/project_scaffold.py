import os

def create_advent_folders(base_path, start_year, end_year):
    """
    Create folders for Advent of Code inputs.
    For each year and day (1 to 25), create a folder with input.txt and test.txt files.
    
    :param base_path: The base directory where the folders will be created.
    :param start_year: The first year to create folders for (inclusive).
    :param end_year: The last year to create folders for (inclusive).
    """
    for year in range(start_year, end_year + 1):
        year_path = os.path.join(base_path, str(year))
        os.makedirs(year_path, exist_ok=True)  # Create year folder

        for day in range(1, 26):  # Days 1 to 25
            day_folder = f"day{day:02}"
            day_path = os.path.join(year_path, day_folder)
            os.makedirs(day_path, exist_ok=True)  # Create day folder

            # Create input.txt and test.txt files
            input_file = os.path.join(day_path, "input.txt")
            test_file = os.path.join(day_path, "test.txt")

            for file_path in [input_file, test_file]:
                if not os.path.exists(file_path):
                    with open(file_path, 'w') as f:
                        f.write("")  # Create empty file

            print(f"Created folder and files for {year}/{day_folder}")

def create_solution_files(base_path, start_year, end_year):
    """
    Create folders and Python files for Advent of Code solutions.
    For each year and day (1 to 25), create a Python file (e.g., day01.py).
    
    :param base_path: The base directory where the folders will be created.
    :param start_year: The first year to create folders for (inclusive).
    :param end_year: The last year to create folders for (inclusive).
    """
    for year in range(start_year, end_year + 1):
        year_path = os.path.join(base_path, str(year))
        os.makedirs(year_path, exist_ok=True)  # Create year folder

        for day in range(1, 26):  # Days 1 to 25
            day_file = os.path.join(year_path, f"day{day:02}.py")
            if not os.path.exists(day_file):
                with open(day_file, 'w', encoding="utf-8") as f:  # Specify utf-8 encoding
                    # Template code for each day's solution
                    f.write(f"""\
import sys
import os

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
sys.path.insert(0, project_root)


from utils.input_parser import read_input
from utils.submit import submit
def solve_part1(data):
    # Solution for Part 1
    pass

def solve_part2(data):
    # Solution for Part 2
    pass

if __name__ == "__main__":
    year, day = {year}, {day}
    
    # Read inputs
    input_data = read_input(year, day, file_name="input.txt")
    test_data = read_input(year, day, file_name="test.txt")
    
    # Test cases (update with known solutions for the test input)
    known_test_solution_part1 = None  # Replace with the known result for part 1
    known_test_solution_part2 = None  # Replace with the known result for part 2
    
    # Verify test cases for Part 1
    print(f"Testing Part 1 for Day {day}, Year {year}...")
    try:
        test_result_part1 = solve_part1(test_data)
        if test_result_part1 == known_test_solution_part1:
            print("✅ Part 1 Test Passed")
        else:
            print(f"❌ Part 1 Test Failed: Expected {{known_test_solution_part1}}, Got {{test_result_part1}}")
    except Exception as e:
        print(f"❌ Part 1 Test Error: {{e}}")
    
    # Solve Part 1
    part1_result = None
    try:
        part1_result = solve_part1(input_data)
        print(f"Part 1 Result: {{part1_result}}")
    except Exception as e:
        print(f"❌ Error solving Part 1: {{e}}")

    # Only proceed to Part 2 if Part 1 is implemented and working
    if part1_result is None and known_test_solution_part2 is not None:
        # Verify test cases for Part 2
        print(f"Testing Part 2 for Day {day}, Year {year}...")
        try:
            test_result_part2 = solve_part2(test_data)
            if test_result_part2 == known_test_solution_part2:
                print("✅ Part 2 Test Passed")
            else:
                print(f"❌ Part 2 Test Failed: Expected {{known_test_solution_part2}}, Got {{test_result_part2}}")
        except Exception as e:
            print(f"❌ Part 2 Test Error: {{e}}")
        
        # Solve Part 2
        try:
            part2_result = solve_part2(input_data)
            print(f"Part 2 Result: {{part2_result}}")
            submit(year, day, part1_result, part2_result)
        except Exception as e:
            print(f"❌ Error solving Part 2: {{e}}")
""")
                print(f"Created solution file: {year}/day{day:02}.py")


if __name__ == "__main__":
    base_path = "inputs"  # Change this to your desired base directory
    solution_base_path = "solutions"  # Base directory for solution files
    start_year = 2015     # Change to the start year you want
    end_year = 2024       # Change to the end year you want

    # create_advent_folders(base_path, start_year, end_year)

    create_solution_files(solution_base_path, start_year, end_year)
