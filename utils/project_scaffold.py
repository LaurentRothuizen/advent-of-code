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

if __name__ == "__main__":
    base_path = "inputs"  # Change this to your desired base directory
    start_year = 2015     # Change to the start year you want
    end_year = 2024       # Change to the end year you want

    create_advent_folders(base_path, start_year, end_year)
