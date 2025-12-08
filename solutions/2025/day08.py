import math
import sys
import os
import networkx as nx

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
sys.path.insert(0, project_root)


from utils.input_parser import read_input
from utils.submit import submit

def euclid_distance(t1,t2):
    return math.sqrt(sum((t1[i] - t2[i])**2 for i in range(len(t1))))

def solve_part1(data):
    boxes = [ tuple(list(map(int, a.strip('\n').split(',')))) for a in data]
    number_of_pairs = 10 if len(data) < 25 else 1000
    dist_dict = []
    for index, box in enumerate(boxes):
        for j in range(index+1, len(boxes)):
            if box != boxes[j]:
                dist_dict.append((euclid_distance(box,boxes[j]), box, boxes[j]))
    sorted_ranges = sorted(dist_dict, key=lambda x: x[0])
    E=[]
    for tuples in sorted_ranges[:number_of_pairs]:
        E.append((tuples[1], tuples[2]))
        E.append((tuples[2], tuples[1]))
    G=nx.Graph()
    G.add_edges_from(E)
    
    print(G)
    group_sizes = []
    for clq in nx.connected_components(G):
        group_sizes.append(len(list(clq)))
    print(math.prod(sorted(group_sizes, reverse=True)[:3]))
    return math.prod(sorted(group_sizes, reverse=True)[:3])

def solve_part2(data):
    boxes = [ tuple(list(map(int, a.strip('\n').split(',')))) for a in data]
    dist_dict = []
    for index, box in enumerate(boxes):
        for j in range(index+1, len(boxes)):
            if box != boxes[j]:
                dist_dict.append((euclid_distance(box,boxes[j]), box, boxes[j]))
    sorted_ranges = sorted(dist_dict, key=lambda x: x[0])
    G=nx.Graph()
    V=[]
    for tuples in sorted_ranges:
        V.append(tuples[1])
        V.append(tuples[2])
    V = list(set(V))
    G.add_nodes_from(V)
    for tuples in sorted_ranges:
        # E.append((tuples[1], tuples[2]))
        # E.append((tuples[2], tuples[1]))
        G.add_edge(tuples[1], tuples[2])
        if nx.is_connected(G):
            print(tuples[1][0] * tuples[2][0])
            return tuples[1][0] * tuples[2][0]

if __name__ == "__main__":
    year, day = 2025, 8
    
    # Read inputs
    input_data = read_input(year, day, file_name="input.txt")
    test_data = read_input(year, day, file_name="test.txt")
    
    # Test cases (update with known solutions for the test input)
    known_test_solution_part1 = 40  # Replace with the known result for part 1
    known_test_solution_part2 = 25272  # Replace with the known result for part 2
    
    # Verify test cases for Part 1
    print(f"Testing Part 1 for Day 8, Year 2025...")
    if known_test_solution_part2 is None:
        test_result_part1 = solve_part1(test_data)
        if test_result_part1 == known_test_solution_part1:
            print("✅ Part 1 Test Passed")
            part1_result = solve_part1(input_data)
            print(f"Part 1 Result: {part1_result}")
        else:
            raise AssertionError(f"❌ Part 1 Test Failed: Expected {known_test_solution_part1}, Got {test_result_part1}")
    else:
        part1_result = 68112
        # part2_result = 44543856

    # Only proceed to Part 2 if Part 1 is implemented and working
    if part1_result is not None and known_test_solution_part2 is not None:
        # Verify test cases for Part 2
        print(f"Testing Part 2 for Day 8, Year 2025...")
        test_result_part2 = solve_part2(test_data)
        if test_result_part2 == known_test_solution_part2:
            print("✅ Part 2 Test Passed")
            part2_result = solve_part2(input_data)
            print(f"Part 2 Result: {part2_result}")
            submit(year, day, part1_result, part2_result)
        else:
            raise AssertionError(f"❌ Part 2 Test Failed: Expected {known_test_solution_part2}, Got {test_result_part2}")
