# aoc2024/day01/solution.py
# Solution to Advent of Code 2024 Day 1: Historian Hysteria

import argparse
from collections import Counter

def part_1(text: list[str]) -> int:
    """Parses 'text' into left and right (sorted) lists,
    and calculates total distance between each list value via zip(left, right).

    Args:
        text (list[str]): The input as a list of its lines.

    Returns:
        int: The total distance.
    """
    total_distance = 0
    left_location_ids = []
    right_location_ids = []
    for line in text:
        left_id, right_id = line.split()
        left_location_ids.append(int(left_id))
        right_location_ids.append(int(right_id))
    
    # Sort the two lists to match requirement
    left_location_ids.sort()
    right_location_ids.sort()
    for pair in zip(left_location_ids, right_location_ids):
        total_distance += (abs(pair[1] - pair[0]))
        
    return total_distance


def part_2(text: list[str]) -> int:
    """Parses 'text' into left and right lists,
    and calculates similarity score by adding up each number in the left list
    after multiplying it by the number of times that number appears in the
    right list.

    Args:
        text (list[str]): The input as a list of its lines.

    Returns:
        int: The similarity score.
    """
    similarity_score = 0
    left_location_ids = []
    right_location_ids = []
    for line in text:
        left_id, right_id = line.split()
        left_location_ids.append(int(left_id))
        right_location_ids.append(int(right_id))
        
    right_id_counter = Counter(right_location_ids)
    for id in left_location_ids:
        similarity_score += id * right_id_counter[id]
    
    return similarity_score
    
    

def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--test", action="store_true", help="Enable command line input for testing")
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
        
        
    # Part 1 w/input file
    file_lines = []
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
