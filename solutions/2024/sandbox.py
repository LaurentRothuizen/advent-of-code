import os
import sys


project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
sys.path.insert(0, project_root)
from utils.input_parser import read_input


grid = read_input(2024, 6, file_name="input.txt")

rn, cn = len(grid), len(grid[0])

def get_element(pos):
    r, c = int(pos.real), int(pos.imag)
    if not (0<=r<rn and 0<=c<cn):
        raise IndexError
    return grid[r][c]

def escape_route(grid, pos, direction, obs=None, return_path=False):
    path, vectors = set(), set()

    while True:
        if (vector:=(pos, direction)) in vectors:
            return -1

        vectors.add(vector)
        path.add(pos)

        try:
            if get_element(next_pos:=pos+direction) == '#' or next_pos == obs:
                direction *= -1j
            else:
                pos = next_pos
        except IndexError:
            return path if return_path else len(path)

start_position = next(r+c*1j for r in range(rn) for c in range(cn) if get_element(r+c*1j) == '^')

start_direction = -1 + 0j

print(len(path := escape_route(grid, start_position, start_direction, return_path=True))) # part 1

print(sum(escape_route(grid, start_position, start_direction, obs) == -1 for obs in path if get_element(obs) == '.' )) # part 2