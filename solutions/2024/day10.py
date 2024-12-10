import sys
import os

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
sys.path.insert(0, project_root)


from utils.common_functions import create_border_around_grid, find_all_occurence_char_in_grid_list, print_grid
from utils.input_parser import read_input
from utils.submit import submit

def get_nbs(z):
    return [(z[0]+1,z[1]),(z[0],z[1]+1),(z[0]-1,z[1]),(z[0],z[1]-1)]

def score_rec(g,z, current_value):
    all_nines = []
    if current_value == 9:
        return [z]
    nbs = get_nbs(z)
    for nb in nbs:
        if g[nb[0]][nb[1]] != '*' and int(g[nb[0]][nb[1]]) == current_value + 1:
            all_nines.extend(score_rec(g,nb,current_value + 1))
    return all_nines

def score(g,zero):
    s= score_rec(g,zero,0)
    print(s)
    return len(set(s))

def construct_score_list(g, zeros):
    score_list = []
    for zero in zeros:
        print(zero)
        score_list.append(score(g,zero))
        
    return score_list

def rating_rec(g,z, current_value, path):
    all_nines = []
    if current_value == 9:
        print(path)
        return [path]
    nbs = get_nbs(z)
    for nb in nbs:
        if g[nb[0]][nb[1]] != '*' and int(g[nb[0]][nb[1]]) == current_value + 1:
            all_nines.extend(rating_rec(g,nb,current_value + 1, path + [nb]))
    return all_nines

def rating(g,zero):
    s=rating_rec(g,zero,0,[zero])
    return len(s)

def construct_rating_list(g, zeros):
    rating_list = []
    for zero in zeros:
        rating_list.append(rating(g,zero))
    return rating_list
    
    
def solve_part1(data):
    grid = create_border_around_grid(data, 1, True)
    # print_grid(grid)
    all_zeros = find_all_occurence_char_in_grid_list(grid,'0')
    print(all_zeros)
    return sum(construct_score_list(grid,all_zeros))

def solve_part2(data):
    grid = create_border_around_grid(data, 1, True)
    # print_grid(grid)
    all_zeros = find_all_occurence_char_in_grid_list(grid,'0')
    print(all_zeros)
    return sum(construct_rating_list(grid,all_zeros))

if __name__ == "__main__":
    year, day = 2024, 10
    
    # Read inputs
    input_data = read_input(year, day, file_name="input.txt")
    test_data = read_input(year, day, file_name="test.txt")
    
    # Test cases (update with known solutions for the test input)
    known_test_solution_part1 = 36  # Replace with the known result for part 1
    known_test_solution_part2 = 81  # Replace with the known result for part 2
    
    # Verify test cases for Part 1
    print(f"Testing Part 1 for Day 10, Year 2024...")
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
        print(f"Testing Part 2 for Day 10, Year 2024...")
        test_result_part2 = solve_part2(test_data)
        if test_result_part2 == known_test_solution_part2:
            print("✅ Part 2 Test Passed")
            part2_result = solve_part2(input_data)
            print(f"Part 2 Result: {part2_result}")
            submit(year, day, part1_result, part2_result)
        else:
            raise AssertionError(f"❌ Part 2 Test Failed: Expected {known_test_solution_part2}, Got {test_result_part2}")
