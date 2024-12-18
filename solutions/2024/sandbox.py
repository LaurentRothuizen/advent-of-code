# import os
# import sys
#DAY 6

# project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
# sys.path.insert(0, project_root)
# from utils.input_parser import read_input


# grid = read_input(2024, 6, file_name="input.txt")

# rn, cn = len(grid), len(grid[0])

# def get_element(pos):
#     r, c = int(pos.real), int(pos.imag)
#     if not (0<=r<rn and 0<=c<cn):
#         raise IndexError
#     return grid[r][c]

# def escape_route(grid, pos, direction, obs=None, return_path=False):
#     path, vectors = set(), set()

#     while True:
#         if (vector:=(pos, direction)) in vectors:
#             return -1

#         vectors.add(vector)
#         path.add(pos)

#         try:
#             if get_element(next_pos:=pos+direction) == '#' or next_pos == obs:
#                 direction *= -1j
#             else:
#                 pos = next_pos
#         except IndexError:
#             return path if return_path else len(path)

# start_position = next(r+c*1j for r in range(rn) for c in range(cn) if get_element(r+c*1j) == '^')

# start_direction = -1 + 0j

# print(len(path := escape_route(grid, start_position, start_direction, return_path=True))) # part 1

# print(sum(escape_route(grid, start_position, start_direction, obs) == -1 for obs in path if get_element(obs) == '.' )) # part 2

#!/usr/bin/env python3
# 2024 Day 15: Warehouse Woes

import os

#DAY 15

# def process_input(filename):
#     """Acquire input data"""
#     with open(filename) as file:
#         input = file.read().splitlines()

#     map = {}
#     x_len = len(input[0]) * 2
#     y_len = 0
#     move_ch = ''

#     for y in range(len(input)):
#         line = input[y]
#         if len(line) == 0:
#             continue
#         elif line[0] == '#':
#             x = 0
#             y_len += 1
#             for ch in line:
#                 if ch == '#':
#                     tile = '##'
#                 elif ch == 'O':
#                     tile = '[]'
#                 elif ch == '.':
#                     tile = '..'
#                 elif ch == '@':
#                     robot = (x,y)
#                     tile = '@.'
#                 map[x,y] = tile[0]
#                 x += 1
#                 map[x,y] = tile[1]
#                 x += 1
#         elif line[0] in '<v>^':
#             move_ch += line
    
#     moves = list(move_ch)

#     return map, x_len, y_len, robot, moves


# def move_robot(robot):
#     if draw_the_map: draw_map(robot)
#     for move in moves:
#         robot = move_boxes(robot, move)
#         if draw_the_map: draw_map(robot)
#     return

# def move_boxes(robot, direction):
#     # find all the boxes that would move
#     boxes = find_all_boxes(robot, direction)
#     if len(boxes) == 0:
#         return robot            # can't move
#     clear_boxes(boxes)
#     robot = move_boxes_and_robot(boxes, direction)
#     return robot

# def find_all_boxes(robot, direction):
#     # find all the boxes that would move
#     this_row = {robot:'@'}      # start with just the robot
#     all_boxes = dict(this_row)
#     while True:
#         next_row = {}
#         for (x,y) in this_row:
#             nx, ny = move(x,y,direction)
#             next_ch = map[nx,ny]
#             if next_ch == '#':
#                 return {}        # would hit a wall, can't move
#             elif next_ch == '[':
#                 next_row[nx,ny] = '['   # add it to next row
#                 if direction in '^v':
#                     next_row[nx+1,ny] = ']'
#             elif next_ch == ']':
#                 next_row[nx,ny] = ']'   # add it to next row
#                 if direction in '^v':
#                     next_row[nx-1,ny] = '['
#         # Next row now has all the boxes that would move
#         if len(next_row) == 0:      # if no boxes, ready to move
#             return all_boxes
#         all_boxes.update(next_row)  # add this row to total rows
#         this_row = next_row
#     return all_boxes

# def clear_boxes(boxes):
#     # Change current position of everything we're going to movce to '.'
#     # This includes the robot
#     for (x,y) in boxes:
#         map[x,y] = '.'
#     return

# def move_boxes_and_robot(boxes, direction):
#     # Translate all of the boxes and robot by one space in direction
#     for (x,y), ch in boxes.items():
#         nx, ny = move(x,y,direction)
#         map[nx, ny] = ch
#         if ch == '@':
#             robot = (nx,ny)
#     return robot

# def move(x,y,direction):
#     if direction == '>':
#         x += 1
#     elif direction == '<':
#         x -= 1
#     elif direction == '^':
#         y -= 1
#     else:
#         y += 1
#     return x, y

# def gps_sum():
#     total_sum = 0
#     for (x,y), ch in map.items():
#         if ch == '[':
#             coordinate = y * 100 + x
#             total_sum += coordinate
#     return total_sum

# def draw_map(robot):
#     print()
#     for y in range(y_len):
#         line = ''
#         for x in range(x_len):
#             line += map[x,y]
#         print(line)
#     return

# #-----------------------------------------------------------------------------------------

# filename = os.path.join("inputs", '2024', f"day15", 'input.txt')
# # filename = 'input.txt'
# #filename = 'sample2.txt'
# draw_the_map = False
# #draw_the_map = True

# map, x_len, y_len, robot, moves = process_input(filename)

# move_robot(robot)

# total_sum = gps_sum()

# print()
# print('GPS sum =', total_sum)

import re
import sys
import numpy as np
from heapq import heappop, heappush

with open('inputs/2024/day18/input.txt') as f:
    lines = f.readlines()

coords = [[int(num) for num in re.findall(r'\d+', line)] for line in lines]

gridsize = 71
gridlines = []
for i in range(gridsize):
    line = []
    for j in range(gridsize):
        line.append('.')
    gridlines.append(line)

grid = np.array(gridlines)
start = [0,0]
end = [gridsize-1,gridsize-1]

for coord in coords[:1024]:
    grid[coord[1],coord[0]] = '#'

for coord in coords[1024:]:
    grid[coord[1],coord[0]] = '#'

    q = [(0, start)]
    visited = {}
    min_cost = sys.maxsize

    while q:
        (cost, [y, x]) = heappop(q)
        
        if [y,x] == end:
            min_cost = min(min_cost, cost)
            break

        cost += 1

        if y <= gridsize-2 and grid[y+1, x] == '.' and ((y+1, x) not in visited or visited[(y+1, x)] > cost):
            visited[(y+1, x)] = cost
            heappush(q, (cost, [y+1, x]))
        if y >= 1 and grid[y-1, x] == '.' and ((y-1, x) not in visited or visited[(y-1, x)] > cost):
            visited[(y-1, x)] = cost
            heappush(q, (cost, [y-1, x]))
        if x <= gridsize-2 and grid[y, x+1] == '.' and ((y, x+1) not in visited or visited[(y, x+1)] > cost):
            visited[(y, x+1)] = cost
            heappush(q, (cost, [y, x+1]))
        if x >= 1 and grid[y, x-1] == '.' and ((y, x-1) not in visited or visited[(y, x-1)] > cost):
            visited[(y, x-1)] = cost
            heappush(q, (cost, [y, x-1]))
    
    if min_cost == sys.maxsize:
        print(','.join(map(str,coord)))
        break