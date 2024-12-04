import os

def read_input(year, day, file_name="input.txt"):
    """
    Reads the input file for a given year and day.
    
    :param year: The year of the Advent of Code challenge.
    :param day: The day of the challenge.
    :param file_name: The name of the input file (default is "input.txt").
    :return: The content of the input file as a string.
    """
    file_path = os.path.join("inputs", str(year), f"day{day:02}", file_name)
    with open(file_path, 'r') as f:
        return f.read().strip()