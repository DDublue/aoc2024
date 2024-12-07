# aoc2024/day02/solution.py
# Solution to Advent of Code 2024 Day 2: Red-Nosed Reports

import argparse
from copy import deepcopy


def part_1(text: list[str]) -> int:
    """Goes through each report in text,
    and checks the levels for increases and decreases by at least 1/at most 3.

    Args:
        text (list[str]): The input as a list of its lines.

    Returns:
        int: The number of safe reports.
    """
    safe_reports = 0
    for report in text:
        is_safe = True
        report_as_list = [int(level) for level in report.split()]
        
        # All up/down check
        if (report_as_list != sorted(report_as_list) and
            report_as_list != sorted(report_as_list, reverse=True)):
            continue

        # Amount change check
        for i, level in enumerate(report_as_list[:-1]):
            difference = report_as_list[i + 1] - level
            if abs(difference) > 3 or difference == 0:
                is_safe = False
                break
            
        if is_safe:
            safe_reports += 1

    return safe_reports


def part_2(text: list[str]) -> int:
    """Goes through each report in text,
    and checks the levels for increases and decreases by at least 1/at most 3.
    However, it allows for one bad level.

    Args:
        text (list[str]): The input as a list of its lines.

    Returns:
        int: The number of safe reports.
    """
    safe_reports = 0
    for report in text:
        report_as_list = [int(level) for level in report.split()]
        
        # Brute force every iteration of report
        for i in range(len(report_as_list)):
            sub_list = deepcopy(report_as_list)
            sub_list.pop(i)
            is_safe = True
            unsafe_count = 0
            
            if (sub_list != sorted(sub_list) and
                sub_list != sorted(sub_list, reverse=True)):
                continue

            for i, level in enumerate(sub_list[:-1]):
                difference = sub_list[i + 1] - level
                if abs(difference) > 3 or difference == 0:
                    is_safe = False
                    unsafe_count += 1
                    break
                
            # only need one safe iteration for a report to be fully safe
            if is_safe and unsafe_count == 0:
                safe_reports += 1
                break
        
    return safe_reports
    

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
