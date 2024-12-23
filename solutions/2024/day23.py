from itertools import combinations
import sys
import os
from networkx.algorithms import clique
import networkx as nx

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
sys.path.insert(0, project_root)


from utils.input_parser import read_input
from utils.submit import submit
def create_graph(data):
    V = []
    E = {}
    for line in data:
        temp = line.strip('\n').split('-')
        V.append(temp[0])
        V.append(temp[1])
        E[temp[0]] = E.get(temp[0], []) + [temp[1]]
        E[temp[1]] = E.get(temp[1], []) + [temp[0]]
    V_u = list(set(V))
    G = (V_u,E)
    return G

def is_clique_with_t(c,E):
    x,y,z = c
    if x[0] != 't' and y[0] != 't' and z[0] != 't':
        return False
    if y in E[x] and z in E[x] and z in E[y]:
        return True
    return False

def get_all_3_cliques_with_t(G):
    (V,E) = G
    combination = list(combinations(V, 3))
    cliques = []
    for c in combination:
        if is_clique_with_t(c,E):
            cliques.append(c)      
    return len(cliques)

def solve_part1(data):
    G = create_graph(data)
    all_3_cliques = get_all_3_cliques_with_t(G)
    return all_3_cliques

def code_clique(max_clique):
    sorted_strings = sorted(max_clique)
    return ','.join(sorted_strings)

def solve_part2(data):
    max_clique = create_graph_for_max_clique(data)
    return code_clique(max_clique)

def create_graph_for_max_clique(data):
    V = []
    E = []
    for line in data:
        temp = line.strip('\n').split('-')
        V.append(temp[0])
        V.append(temp[1])
        E.append((temp[0], temp[1]))
        E.append((temp[1], temp[0]))
    V_u = list(set(V))
    G = nx.Graph()
    G.add_edges_from(E)
    cliques = clique.find_cliques(G)
    max_clique_size = 0
    max_clique = None
    for index, clq in enumerate(cliques):
        print( f'Maximal Clique {index+1} ', clq)
        if len(clq) > max_clique_size:
            max_clique_size = len(clq)
            max_clique = clq
    return max_clique

if __name__ == "__main__":
    year, day = 2024, 23
    
    # Read inputs
    input_data = read_input(year, day, file_name="input.txt")
    test_data = read_input(year, day, file_name="test.txt")
    
    # Test cases (update with known solutions for the test input)
    known_test_solution_part1 = 7  # Replace with the known result for part 1
    known_test_solution_part2 = 'co,de,ka,ta'  # Replace with the known result for part 2
    
    # Verify test cases for Part 1
    print(f"Testing Part 1 for Day 23, Year 2024...")
    if known_test_solution_part2 is None:
        test_result_part1 = solve_part1(test_data)
        if test_result_part1 == known_test_solution_part1:
            print("✅ Part 1 Test Passed")
            part1_result = solve_part1(input_data)
            print(f"Part 1 Result: {part1_result}")
        else:
            raise AssertionError(f"❌ Part 1 Test Failed: Expected {known_test_solution_part1}, Got {test_result_part1}")
    else:
        part1_result = None

    # Only proceed to Part 2 if Part 1 is implemented and working
    if part1_result is None and known_test_solution_part2 is not None:
        # Verify test cases for Part 2
        print(f"Testing Part 2 for Day 23, Year 2024...")
        test_result_part2 = solve_part2(test_data)
        if test_result_part2 == known_test_solution_part2:
            print("✅ Part 2 Test Passed")
            part2_result = solve_part2(input_data)
            print(f"Part 2 Result: {part2_result}")
            submit(year, day, part1_result, part2_result)
        else:
            raise AssertionError(f"❌ Part 2 Test Failed: Expected {known_test_solution_part2}, Got {test_result_part2}")
