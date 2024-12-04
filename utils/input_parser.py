import os

def read_input(year, day):
    """Reads the input file for a given year and day."""
    file_path = os.path.join('inputs', str(year), f'day{day:02}.txt')
    with open(file_path, 'r') as file:
        return file.read().strip()
