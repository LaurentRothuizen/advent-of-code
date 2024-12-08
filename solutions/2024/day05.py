import sys
import os

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
sys.path.insert(0, project_root)


from utils.input_parser import read_input
from utils.submit import submit



def split_data(data):
    instruction = False
    i_list = []
    r_list = []
    for line in data:
        if line == '\n':
            instruction = True
            continue
        if not instruction:
            r_list.append(line.strip('\n').split('|'))
        else:
            i_list.append(line.strip('\n').split(','))
    return r_list, i_list

def calc_score_middle(valid_list):
    tot = 0
    for v in valid_list:
        tot += v[len(v)//2]
    return tot

def get_index(my_list, item):
    try:
        index = my_list.index(item)
        return index
    except ValueError:
        return -1

def invalid_instructions(r_list, i_list):
    valid_dict = {}
    for i in i_list:
        valid_dict[','.join([str(x) for x in i])] = True
    for r in r_list:
        for j in i_list:
            if valid_dict[','.join([str(x) for x in j])]:
                loc = get_index(j,int(r[0]))
                if loc > 0:
                    if get_index(j[0:loc],int(r[1]))>-1:
                        valid_dict[','.join([str(x) for x in j])] = False
    return [ins for ins in i_list if not valid_dict[','.join([str(x) for x in ins])]]

def valid_instructions(r_list, i_list):
    valid_dict = {}
    for i in i_list:
        valid_dict[','.join([str(x) for x in i])] = True
    for r in r_list:
        for j in i_list:
            if valid_dict[','.join([str(x) for x in j])]:
                loc = get_index(j,int(r[0]))
                if loc > 0:
                    if get_index(j[0:loc],int(r[1]))>-1:
                        valid_dict[','.join([str(x) for x in j])] = False
    return [ins for ins in i_list if valid_dict[','.join([str(x) for x in ins])]]

def sorted_invalid(r_list,invalid_list):
    r_list2 = []
    sorted_invalid_list = []
    for rr in r_list:
        r_list2.append([int(s) for s in rr ])
    for il in invalid_list:
        all_rules = []
        for r in r_list2:
            if len(set(r).intersection(set(il))) == 2:
                all_rules.append((r[0],r[1]))
        sorted_invalid_list.append(sort_with_rules(il, all_rules))
    return sorted_invalid_list

from collections import defaultdict, deque

def sort_with_rules(numbers, rules):
    """
    Sort a list of numbers according to a set of precedence rules.

    :param numbers: List of numbers to sort.
    :param rules: List of tuples (a, b) where a must come before b.
    :return: A sorted list of numbers that satisfies the rules.
    """
    # Build a graph and in-degree map
    graph = defaultdict(list)
    in_degree = defaultdict(int)

    # Add rules to the graph
    for a, b in rules:
        graph[a].append(b)
        in_degree[b] += 1
        if a not in in_degree:
            in_degree[a] = 0

    # Topological sort using Kahn's algorithm
    queue = deque([node for node in numbers if in_degree[node] == 0])
    sorted_list = []

    while queue:
        current = queue.popleft()
        sorted_list.append(current)
        for neighbor in graph[current]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    # Verify if all nodes in 'numbers' are in the sorted list
    if len(sorted_list) != len(numbers):
        raise ValueError("The rules contain a cycle or some numbers are missing in the rules.")

    return sorted_list

def solve_part1(data):
    r_list, i_list = split_data(data)
    i_list2 = []
    for i in i_list:
        i_list2.append([ int(x) for x in i ])
    valid_list = valid_instructions(r_list, i_list2)
    return calc_score_middle(valid_list)

def solve_part2(data):
    r_list, i_list = split_data(data)
    i_list2 = []
    for i in i_list:
        i_list2.append([ int(x) for x in i ])
    invalid_list = invalid_instructions(r_list, i_list2)
    invalid_list_sorted = sorted_invalid(r_list,invalid_list)
    return calc_score_middle(invalid_list_sorted)


if __name__ == "__main__":
    year, day = 2024, 5
    
    # Read inputs
    input_data = read_input(year, day, file_name="input.txt")
    test_data = read_input(year, day, file_name="test.txt")
    
    # Test cases (update with known solutions for the test input)
    known_test_solution_part1 = 143  # Replace with the known result for part 1
    known_test_solution_part2 = 123  # Replace with the known result for part 2
    
    # Verify test cases for Part 1
    print(f"Testing Part 1 for Day 5, Year 2024...")
    test_result_part1 = solve_part1(test_data)
    try:
        if test_result_part1 == known_test_solution_part1:
            print("✅ Part 1 Test Passed")
        else:
            print(f"❌ Part 1 Test Failed: Expected {known_test_solution_part1}, Got {test_result_part1}")
    except Exception as e:
        print(f"❌ Part 1 Test Error: {e}")
    
    # Solve Part 1
    part1_result = None
    if test_result_part1 == known_test_solution_part1:
        try:
            part1_result = 4790 #solve_part1(input_data)
            print(f"Part 1 Result: {part1_result}")
        except Exception as e:
            print(f"❌ Error solving Part 1: {e}")

    # Only proceed to Part 2 if Part 1 is implemented and working
    if part1_result is not None and known_test_solution_part2 is not None:
        # Verify test cases for Part 2
        print(f"Testing Part 2 for Day 5, Year 2024...")
        test_result_part2 = solve_part2(test_data)
        if test_result_part2 == known_test_solution_part2:
            print("✅ Part 2 Test Passed")
            part2_result = solve_part2(input_data)
            print(f"Part 2 Result: {part2_result}")
            submit(year, day, part1_result, part2_result)
        else:
            raise AssertionError(f"❌ Part 2 Test Failed: Expected {known_test_solution_part2}, Got {test_result_part2}")
