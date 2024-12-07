# aoc2024/day01/solution.py
# Solution to Advent of Code 2024 Day 1: Historian Hysteria

import argparse
import re


def part_1(text: list[str]) -> int:
    """Finds all substrings in the form of 'mul(X,Y)' where X and Y are 1-3
    digit numbers. Then, it multiplies X and Y of each mul() and sums up all
    the products.

    Args:
        text (list[str]): The input as a list of its lines.

    Returns:
        int: The sum of the products of all X*Y's.
    """
    final_sum = 0
    for instr in text:
        all_muls = re.findall("mul[(]\d{1,3},\d{1,3}[)]", instr)
        
        # dirty split x and y from mul(x,y), then clean extract them
        for mul in all_muls:
            mul_split = mul.split(",")
            x, y = mul_split[0].split("(")[1], mul_split[1][:-1]
            # print(f"x: {x}; y: {y}")
            final_sum += int(x) * int(y)

    return final_sum


def part_2(text: list[str]) -> int:
    """Finds all substrings in the form of 'mul(X,Y)' where X and Y are 1-3
    digit numbers. However, mul's that succeed don't()'s are disabled while
    mul's that succeed do()'s are re-enabled. mul's are initially enabled.
    Then, it multiplies X and Y of each mul() and sums up all the products.

    Args:
        text (list[str]): The input as a list of its lines.

    Returns:
        int:
    """
    enabled = True
    final_sum = 0
    for instr in text:
        # regex finds all instances of do(), don't(), and mul()
        cmd_list = re.findall(
            "(?:do\(\))|(?:don't\(\))|(?:mul\(\d{1,3},\d{1,3}\))",
            instr
        )
        
        # a mul()'s inclusion depends on do()'s and don't()'s
        for command in cmd_list:
            if command == "do()":
                enabled = True
            elif command == "don't()":
                enabled = False
            else:
                if not enabled:
                    continue
                
                mul_split = command.split(",")
                x, y = mul_split[0].split("(")[1], mul_split[1][:-1]
                # print(f"x: {x}; y: {y}")
                final_sum += int(x) * int(y)

    return final_sum
    

def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--test", action="store_true", help="Enable command line input for testing")
    parser.add_argument("-f", "--file", action="store_true", help="Enable command line input for testing")
    args = parser.parse_args()
    
    # Part 1 and 2 w/test input
    test_lines = []
    if args.test:
        print("Please enter your test input.\nPaste the entire value, not on one line. Then return twice to end input.")
        line = input()
        while line:
            test_lines.append(line)
            line = input()
        print(f"Answer for part 1 test: {part_1(test_lines)}")
        print(f"Answer for part 2 test: {part_2(test_lines)}\n")
        
        
    # Part 1 and 2 w/input file
    file_lines = []
    if args.file:
        try:
            with open("input.txt", "r") as f:
                for line in f:
                    file_lines.append(line.rstrip())
            print(f"Answer for part 1 file input: {part_1(file_lines)}")
            print(f"Answer for part 2 file input: {part_2(file_lines)}\n")
        except FileNotFoundError:
            print("'input.txt' does not exist in parent directory.")
            return
    
    return


if __name__ == "__main__":
    main()
