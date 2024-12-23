import sys
import os

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
sys.path.insert(0, project_root)


from utils.input_parser import read_input
from utils.submit import submit

MODULO = 16777216

def mix(value, secret):
    return value ^ secret

def prune(value):
    return value % MODULO

def secret_number(current_secret):
    new_secret = prune(mix(current_secret * 64, current_secret))
    new_secret = prune(mix(new_secret//32, new_secret))
    new_secret = prune(mix(new_secret * 2048, new_secret))
    return new_secret

def all_steps_simulation(monkey, steps):
    new_number = monkey
    for _ in range(steps):
        new_number = secret_number(new_number)
    return new_number

def calculate_final(inputs,steps=2000):
    result_dict = {}
    for monkey in inputs:
        result_dict[monkey] = all_steps_simulation(monkey, steps)
    return sum(result_dict.values())


def solve_part1(data):
    inputs = [int(d.strip('\n')) for d in data]
    return calculate_final(inputs)

def all_steps_simulation_part2(monkey, steps):
    new_number = monkey
    delta = []
    last_digit_array = []
    last_digit = int(str(new_number)[-1])
    for _ in range(steps):
        new_number = secret_number(new_number)
        new_last_digit = int(str(new_number)[-1])
        delta.append(new_last_digit - last_digit)
        last_digit_array.append(new_last_digit)
        last_digit = new_last_digit
    return (new_number, last_digit_array, delta)

def get_banana(m_tuple, sequence):
    for i in range(len(m_tuple[2]) - len(sequence)):
        if m_tuple[2][i:i+len(sequence)] == sequence:
            # print(m_tuple[1][i+len(sequence)])
            return m_tuple[1][i+len(sequence)]
    return 0

def get_sequences(inputs, result_dict):
    sequence_list = []
    input_sequence_dict = {}
    for i in inputs:
        sequence_dict = {}
        for j in range(len(result_dict[i][2]) - 4):
            seq = tuple(result_dict[i][2][j:j+4])
            # Check if seq is already in sequence_dict
            if seq in sequence_dict:
                continue
            else:
                sequence_dict[seq] = result_dict[i][1][j+4]
            sequence_list.append(seq)
        input_sequence_dict[i] = sequence_dict
    
    # Get unique sequences
    unique_tuples = set(sequence_list)
    unique_lists = [list(sublist) for sublist in unique_tuples]

    return unique_lists, input_sequence_dict


def calculate_final_part2(inputs,steps=2000):
    result_dict = {}
    for monkey in inputs:
        result_dict[monkey] = all_steps_simulation_part2(monkey, steps)
    sequences, input_sequence_dict = get_sequences(inputs, result_dict)  #[-2,1,-1,3]
    total = 0
    sequence_dict = {}
    print('TOTAL SEQ', len(sequences))
    for index, seq in enumerate(sequences):
        print(f"Iteration {index} of {len(sequences)}")
        total = 0
        for m in inputs:
            total += input_sequence_dict[m].get(tuple(seq),0)
            # total += get_banana(result_dict[m], seq)
        sequence_dict[tuple(seq)] = total
    # print(sequence_dict)
    final = sorted(sequence_dict.values(), reverse=True)
    print(final)
    return final[0]

def solve_part2(data):
    #see sandbox
    inputs = [int(d.strip('\n')) for d in data]
    return calculate_final_part2(inputs)

if __name__ == "__main__":
    year, day = 2024, 22
    
    # Read inputs
    input_data = read_input(year, day, file_name="input.txt")
    test_data = read_input(year, day, file_name="test.txt")
    test2_data = read_input(year, day, file_name="test2.txt")
    
    # Test cases (update with known solutions for the test input)
    known_test_solution_part1 = 37327623  # Replace with the known result for part 1
    known_test_solution_part2 = 25  # Replace with the known result for part 2
    
    # Verify test cases for Part 1
    print(f"Testing Part 1 for Day 22, Year 2024...")
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
        print(f"Testing Part 2 for Day 22, Year 2024...")
        test_result_part2 =  solve_part2(test2_data)
        if test_result_part2 == known_test_solution_part2:
            print("✅ Part 2 Test Passed")
            part2_result = solve_part2(input_data)
            print(f"Part 2 Result: {part2_result}")
            submit(year, day, part1_result, part2_result)
        else:
            raise AssertionError(f"❌ Part 2 Test Failed: Expected {known_test_solution_part2}, Got {test_result_part2}")
