def create_border_around_grid(original_grid_input, size=1, split=False):
    # Ensure grid is a list of lists
    original_grid = [list(x.strip('\n')) if split else list(x.strip('\n')) for x in original_grid_input]

    width_original_grid = len(original_grid[0])

    top_border = [['*' for _ in range(width_original_grid + 2 * size)] for _ in range(size)]

    bordered_grid = [
        ['*'] * size + row + ['*'] * size for row in original_grid
    ]

    bottom_border = [['*' for _ in range(width_original_grid + 2 * size)] for _ in range(size)]

    full_grid = top_border + bordered_grid + bottom_border

    return full_grid

def print_grid(g):
    print('\n'.join(' '.join(str(x) for x in row) for row in g))

def find_in_grid(grid, char):
    found = []
    for x, row in enumerate(grid):
        for y, cell in enumerate(row):
            if cell == char:
                found.append((x, y))
    return found

def find_all_chars_in_grid_dict(grid, empty_char):
    found = {}
    for x, row in enumerate(grid):
        for y, cell in enumerate(row):
            if cell != empty_char:
                if cell in found:
                    found[cell].append((x,y))
                else:
                    found[cell] = [(x,y)]
    return found


# if __name__ == "__main__":
#     year, day = 2024, 4
    
#     # Read inputs
#     test_data = read_input(year, day, file_name="test.txt")
#     print_grid(test_data)
#     print('--------------------------------------------')
#     print_grid(create_border_around_grid(test_data, size=3, split=True))