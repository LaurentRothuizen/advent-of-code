import importlib

def run_solution(year, day):
    """Dynamically imports and runs the solution for the given year and day."""
    try:
        module_name = f"solutions.{year}.day{day:02}"
        day_module = importlib.import_module(module_name)

        input_data = day_module.read_input(year, day)
        print(f"Year {year}, Day {day}")
        print("Part 1:", day_module.solve_part1(input_data))
        print("Part 2:", day_module.solve_part2(input_data))
    except ModuleNotFoundError:
        print(f"Solution for Year {year}, Day {day} is not implemented.")
    except AttributeError as e:
        print(f"Error in the solution for Year {year}, Day {day}: {e}")

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 3:
        print("Usage: python main.py <year> <day>")
    else:
        year = int(sys.argv[1])
        day = int(sys.argv[2])
        run_solution(year, day)
