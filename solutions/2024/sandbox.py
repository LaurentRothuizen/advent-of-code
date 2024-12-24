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

from collections import deque
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

# import re
# import sys
# import numpy as np
# from heapq import heappop, heappush

# with open('inputs/2024/day18/input.txt') as f:
#     lines = f.readlines()

# coords = [[int(num) for num in re.findall(r'\d+', line)] for line in lines]

# gridsize = 71
# gridlines = []
# for i in range(gridsize):
#     line = []
#     for j in range(gridsize):
#         line.append('.')
#     gridlines.append(line)

# grid = np.array(gridlines)
# start = [0,0]
# end = [gridsize-1,gridsize-1]

# for coord in coords[:1024]:
#     grid[coord[1],coord[0]] = '#'

# for coord in coords[1024:]:
#     grid[coord[1],coord[0]] = '#'

#     q = [(0, start)]
#     visited = {}
#     min_cost = sys.maxsize

#     while q:
#         (cost, [y, x]) = heappop(q)
        
#         if [y,x] == end:
#             min_cost = min(min_cost, cost)
#             break

#         cost += 1

#         if y <= gridsize-2 and grid[y+1, x] == '.' and ((y+1, x) not in visited or visited[(y+1, x)] > cost):
#             visited[(y+1, x)] = cost
#             heappush(q, (cost, [y+1, x]))
#         if y >= 1 and grid[y-1, x] == '.' and ((y-1, x) not in visited or visited[(y-1, x)] > cost):
#             visited[(y-1, x)] = cost
#             heappush(q, (cost, [y-1, x]))
#         if x <= gridsize-2 and grid[y, x+1] == '.' and ((y, x+1) not in visited or visited[(y, x+1)] > cost):
#             visited[(y, x+1)] = cost
#             heappush(q, (cost, [y, x+1]))
#         if x >= 1 and grid[y, x-1] == '.' and ((y, x-1) not in visited or visited[(y, x-1)] > cost):
#             visited[(y, x-1)] = cost
#             heappush(q, (cost, [y, x-1]))
    
#     if min_cost == sys.maxsize:
#         print(','.join(map(str,coord)))
#         break

# day 21
# import copy

# CodeList = []
# with open("inputs/2024/day21/input.txt", "r") as data:
#     for t in data:
#         Line = t.strip()
#         CodeList.append(Line)

# Keys = ["A"]
# for y in range(10):
#     Keys.append(str(y))
# KeypadDict = {}
# ArrowDict = {}
# KeypadLocations = {"7": (0,3), "8": (1,3), "9": (2,3), "4": (0,2), "5": (1,2), "6": (2,2), "1": (0,1), "2": (1,1), "3": (2,1), "0": (1,0), "A": (2,0)}
# ArrowLocations = {"<": (0,0), ">": (2,0), "V": (1,0), "^": (1,1), "A": (2,1)}
# Directions = {"^": (0,1), "V": (0,-1), "<": (-1,0), ">": (1,0)}

# def BFSKey(Start, Finish, Type):
#     if Type == "Key":
#         Dictionary = KeypadLocations
#     else:
#         Dictionary = ArrowLocations
#     StartPoint = Dictionary[Start]
#     EndPoint = Dictionary[Finish]
#     Frontier = deque()
#     Frontier.append((0,StartPoint,""))
#     Score = None
#     ReturnList = []

#     while Frontier:
#         Distance,Location,History = Frontier.popleft()
#         if Score != None and Distance > Score:
#             break
#         if Location == EndPoint:
#             History += "A"
#             Score = Distance
#             ReturnList.append(History)
#             continue
#         if Location not in Dictionary.values():
#             continue

#         X,Y = Location
#         for c in Directions:
#             DX,DY = Directions[c]
#             NX,NY = X+DX,Y+DY
#             NewLoc = (NX,NY)
#             if NewLoc not in Dictionary.values():
#                 continue
#             NewHistory = History + c
#             Frontier.append((Distance+1,NewLoc,NewHistory))
    
#     return tuple(ReturnList)

# for c in Keys:
#     for d in Keys:
#         KeyPair = c+d
#         if c == d:
#             KeypadDict[KeyPair] = ("A",)
#             continue
#         PathTuple = BFSKey(c,d,"Key")
#         KeypadDict[KeyPair] = PathTuple

# for c in ArrowLocations:
#     for d in ArrowLocations:
#         KeyPair = c+d
#         if c == d:
#             ArrowDict[KeyPair] = ("A",)
#             continue
#         PathTuple = BFSKey(c,d,"Arr")
#         ArrowDict[KeyPair] = PathTuple

# for k in KeypadDict:
#     print(k, KeypadDict[k])

# ArrowDict["<A"] = ('>>^A',)
# ArrowDict[">^"] = ('<^A',)
# ArrowDict["VA"] =  ('^>A',)
# ArrowDict["^>"] = ('V>A',)
# ArrowDict["A<"] = ('V<<A',)
# ArrowDict["AV"] =  ('<VA',)
# for a in ArrowDict:
#     ArrowDict[a] = ArrowDict[a][0]

# for a in ArrowDict:
#     print(a, ArrowDict[a])

# print()


# def ButtonPresses(String, Cypher, Last):
#     String = "A" + String
#     ReturnList = [""]
#     LastCount = 0
#     for t in range(len(String)-1):
#         StringPair = String[t:t+2]
#         if Cypher == "Keypad":
#             BranchTuple = KeypadDict[StringPair]
#         else:
#             NewString = ArrowDict[StringPair]
#             #print(StringPair, BranchTuple)
#         if Last:
#             LastCount += len(NewString)
#             ReturnList[0] += NewString
#             continue
#         ReturnLen = len(ReturnList)
#         NewReturnList = []
#         if Cypher == "Keypad":
#             for g in BranchTuple:
#                 for r in ReturnList:
#                     NewString = r + g
#                     NewReturnList.append(NewString)
#             ReturnList = copy.deepcopy(NewReturnList)
#         else:
#             ReturnList[0] += NewString
        
#     if Last:
#         return LastCount, ReturnList  
#     return tuple(ReturnList)


# Part2Dict = {}
# for a in ArrowDict:
#     NewList = []
#     String = ArrowDict[a]
#     if len(String) == 1:
#         Part2Dict[a] = ("AA",)
#         continue
#     for t in range(len(ArrowDict[a])):
#         if t == 0:
#             Substring = "A" + String[0]
#         else:
#             Substring = String[t-1:t+1]
#         NewList.append(Substring)
#         Part2Dict[a] = tuple(NewList)

# print(Part2Dict)
# print()

# Part1Answer = 0
# Part2Answer = 0

# for Code in CodeList:
#     FirstSet = set(ButtonPresses(Code, "Keypad", False))

#     SecondSet = set()
#     for c in FirstSet:
#         NewSet = set(ButtonPresses(c, "Arrows", False))
#         SecondSet = SecondSet | NewSet

#     MinLength = 1000
#     ThirdSet = set()
#     for c in SecondSet:
#         NewLen, String = ButtonPresses(c, "Arrows", True)
#         if NewLen < MinLength:
#             SecondC = c
#             MinLength = NewLen
#             ThirdSet = set()
#             ThirdSet.add(c)
#         elif NewLen == MinLength:
#             ThirdSet.add(c)
    
    
#     FinalLen = 1000**100
#     for f in ThirdSet:
    
#         CodeDict = {}
#         for a in ArrowDict:
#             CodeDict[a] = 0
#         NewString = ButtonPresses(f, "Arrows", False)[0]
#         for t in range(len(NewString)-1):
#             SubString = NewString[t:t+2]
#             CodeDict[SubString] += 1
#         FirstLetter = NewString[0]
#         print(NewString)
#         print(CodeDict)

#         for u in range(23):
#             NewDict = {}
#             for a in ArrowDict:
#                 NewDict[a] = 0
#             FirstString = "A" + FirstLetter
#             CodeDict[FirstString] += 1
#             FirstLetter = Part2Dict[FirstString][0][1]
#             RemoveString = Part2Dict[FirstString][0]
#             for c in CodeDict:
#                 for g in Part2Dict[c]:
#                     NewDict[g] += CodeDict[c]
#             NewDict[RemoveString] -= 1
#             CodeDict = NewDict.copy()

#         NewLen = sum(CodeDict.values())+1
#         print(NewLen)
#         if NewLen < FinalLen:
#             FinalLen = NewLen

#     Integer = int(Code[:-1])

#     print(ButtonPresses(SecondC, "Arrows", False)[0])
#     print(MinLength, Integer, MinLength*Integer)
#     print(FinalLen, Integer, FinalLen*Integer)
#     print()
#     Part1Answer += Integer * MinLength
#     Part2Answer += Integer * FinalLen


# print(f"{Part1Answer = }")
# print(f"{Part2Answer = }")

# day 22

# import numpy as np
# nums = [int(x) for x in open('inputs/2024/day22/input.txt').read().split('\n')]
# m = 16777216
# repeats = 2000
# total = 0
# memos = {}
# for x in nums: 
#     seq = np.zeros(repeats + 1, dtype = int)
#     seq[0] = x % 10
#     for j in range(1, repeats + 1):
#         x = (x ^ (x * 64)) % m
#         x = (x ^ (x // 32)) % m
#         x = (x ^ (x * 2048)) % m
#         seq[j] =  x % 10
#     total += x
#     diffs = np.diff(seq)
#     seen = set()
#     for p in range(4,len(diffs)):
#         h = tuple(diffs[p-3:p+1])
#         if h not in memos and h not in seen:
#             memos[h] = seq[p + 1]
#         elif h not in seen:
#             memos[h] += seq[p + 1]
#         seen.add(h)
# print('Part 1:', total)
# print('Part 2: ', max(memos.values()))

from itertools import combinations
from collections import defaultdict
from functools import reduce

gWires = dict()
get_wire_cache = dict()

def get_wire(wire):

    if wire in get_wire_cache:
        return get_wire_cache[wire]

    if wire in gWires:

        result = gWires[wire]()
        get_wire_cache[wire] = result

        return result

    raise Exception('FUCK')

def do_and(wire_a, wire_b):
    return lambda: get_wire(wire_a) & get_wire(wire_b)

def do_or(wire_a, wire_b):
    return lambda: get_wire(wire_a) | get_wire(wire_b)

def do_xor(wire_a, wire_b):
    return lambda: get_wire(wire_a) ^ get_wire(wire_b)

def add_wire(wire):
    parts = wire.split(':')
    wire_name = parts[0]

    gWires[wire_name] = lambda: int(parts[1].strip())


def get_wire_number(wire):
    total = 0
    for entry in sorted(filter(lambda x: x[0] == wire, gWires.keys()), reverse=True):
        total <<= 1
        total |= gWires[entry]()
    return total

def zero_bit():
    return lambda: 0

def one_bit():
    return lambda: 1

def validate_full_adder(num):

    clear_all_inputs()

    x_wire = f'x{num:02d}'
    y_wire = f'y{num:02d}'
    z_wire = f'z{num:02d}'

    gWires[x_wire] = zero_bit()
    gWires[y_wire] = zero_bit()

    get_wire_cache.clear()
    if get_wire(z_wire) != 0:
        return False

    gWires[x_wire] = one_bit()
    gWires[y_wire] = zero_bit()

    get_wire_cache.clear()
    if get_wire(z_wire) != 1:
        return False

    gWires[x_wire] = zero_bit()
    gWires[y_wire] = one_bit()

    get_wire_cache.clear()
    if get_wire(z_wire) != 1:
        return False

    gWires[x_wire] = one_bit()
    gWires[y_wire] = one_bit()

    get_wire_cache.clear()
    if get_wire(z_wire) != 0:
        return False

    if num > 0:
        prev_x_wire = f'x{num-1:02d}'
        prev_y_wire = f'y{num-1:02d}'

        gWires[prev_x_wire] = one_bit()
        gWires[prev_y_wire] = one_bit()
        gWires[x_wire] = zero_bit()
        gWires[y_wire] = zero_bit()

        get_wire_cache.clear()
        if get_wire(z_wire) != 1:
            return False

        gWires[prev_x_wire] = one_bit()
        gWires[prev_y_wire] = one_bit()
        gWires[x_wire] = one_bit()
        gWires[y_wire] = zero_bit()

        get_wire_cache.clear()
        if get_wire(z_wire) != 0:
            return False

        gWires[prev_x_wire] = one_bit()
        gWires[prev_y_wire] = one_bit()
        gWires[x_wire] = zero_bit()
        gWires[y_wire] = one_bit()

        get_wire_cache.clear()
        if get_wire(z_wire) != 0:
            return False
        
        gWires[prev_x_wire] = one_bit()
        gWires[prev_y_wire] = one_bit()
        gWires[x_wire] = one_bit()
        gWires[y_wire] = one_bit()

        get_wire_cache.clear()
        if get_wire(z_wire) != 1:
            return False


    for entry in get_prev_wires(num):
        if entry not in get_wire_cache:
            return False

    for entry in get_next_wires(num):
        if entry in get_wire_cache:
            return False

    return True


def clear_all_inputs():
    get_wire_cache.clear()
    for key in gWires.keys():
        if key[0] == 'x' or key[0] == 'y':
            gWires[key] = zero_bit()

def get_prev_wires(num):
    while num > 0:
        yield f'x{num:02d}'
        yield f'y{num:02d}'
        num -= 1

def get_next_wires(num):
    while num > 45:
        yield f'x{num:02d}'
        yield f'y{num:02d}'
        num += 1



def exchange_wires(wire_a, wire_b):

    tmp = gWires[wire_a]
    gWires[wire_a] = gWires[wire_b]
    gWires[wire_b] = tmp

def find_full_adder_fix(current_bit, max_bit, valid_wires, current_solution):

    if current_bit >= max_bit:
        return True, current_solution
    
    res = validate_full_adder(current_bit)

    if res:
        return  find_full_adder_fix(current_bit + 1, max_bit, valid_wires - set(get_wire_cache.keys()), current_solution)


    if len(current_solution) >= 4:
        return (False, None)

    for combo in combinations(valid_wires, 2):

        exchange_wires(*combo)
        try:
            if validate_full_adder(current_bit):

                new_valid_wires = valid_wires - {*combo}
                success, pairs = find_full_adder_fix(current_bit + 1, max_bit, new_valid_wires, current_solution + [combo])

                if success is True:
                    return (success, pairs)

        except RecursionError:
            pass

        exchange_wires(*combo)

    return (False, None)

def main():

    data = None
    with open('inputs/2024/day24/input.txt', 'r') as fp:
        data = fp.readlines()
        data = map(lambda x: x.strip(), data)
        data = list(data)

    split_index = data.index('')

    wires = data[:split_index]

    for wire in wires:
        add_wire(wire)

    x_num = get_wire_number('x')
    y_num = get_wire_number('y')

    operations = data[split_index+1:]

    for operation in operations:
        parts = operation.split('->')

        end_wire = parts[1].strip()

        wire_a, op, wire_b = tuple(parts[0].split())

        res_op = None
        if op == 'AND':
            res_op = do_and(wire_a, wire_b)
        elif op == 'OR':
            res_op = do_or(wire_a, wire_b)
        elif op == 'XOR':
            res_op = do_xor(wire_a, wire_b)

        if res_op is None:
            raise Exception('Forgot')

        gWires[end_wire] = res_op

    output_wires = set(filter(lambda x: x[0] != 'x' and x[0] != 'y', gWires.keys()))

    max_z_bit = max(map(lambda y: int(y.strip('z')), filter(lambda x: x[0] == 'z', gWires.keys())))

    success, pairs = find_full_adder_fix(0, max_z_bit, output_wires, [])

    if not success:
        print('Failed')
        return

    entries = reduce(lambda x,y: x+y, pairs)
    print(','.join(sorted(entries)))




if __name__ == '__main__':
    main()