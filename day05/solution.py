# aoc2024/day04/solution.py
# Solution to Advent of Code 2024 Day 5: Print Queue

import argparse
from itertools import pairwise


def sort_invalid(update: list[str], page_map: dict[str, list[str]]) -> None:
    """Fixes/sorts the update to match the page ordering rules.

    Args:
        update (list[str]): The update to be fixed/sorted.
        page_map (dict[str, list[str]]): The rules of which the update must
        follow.
    """
    n = len(update)
    
    for i in range(n):
        swapped = False
        
        for j in range(0, n - i - 1):
            # Sometimes a page won't be page_map when the rules
            # are parsed
            if (update[j + 1] not in page_map or
                update[j] not in page_map[update[j + 1]]):
                update[j], update[j + 1] = update[j + 1], update[j]
                swapped = True

        if not swapped:
            break

    return


def part_1(text: list[str]) -> int:
    """Parses text into two lists: page ordering rules and updates.
    Converts the rule list into a mapping of predecessor page to its successors
    Then, for each update, it checks every adjacent pair if there exists a
    mapping in the map. Otherwise, it is an invalid update. Also, for all the
    valid updates, it sums all of the middle pages together and returns it.

    Args:
        text (list[str]): The input as a list of its lines.

    Returns:
        int: The sum of all middle page numbers from correctly-ordered updates.
    """
    answer = 0
    page_map = {}
    updates: list[list[str]] = []
    
    # parsing page relations and updates
    for line in text:
        if "|" in line:
            predecessor, successor = line.split("|")
            page_map.setdefault(predecessor, []).append(successor)
        elif "," in line:
            update_as_list = line.split(",")
            updates.append(update_as_list)

    # update validation
    for update in updates:
        is_valid = True
        
        for pair in pairwise(update):
            first, second = pair[0], pair[1]
            if first not in page_map or second not in page_map[first]:
                is_valid = False
                break
            
        if is_valid:
            answer += int(update[len(update)//2]) # middle index of update
    
    return answer


def part_2(text: list[str]) -> int:
    """Parses text into two lists: page ordering rules and updates. Converts
    the rule list into a mapping of predecessor page to its successors.
    Also creates a mapping of each page to a list of the number of pages before
    and the number of pages after the specifed page. Then, for each update, it
    checks every adjacent pair if there exists a mapping in the map. Otherwise,
    it is an invalid update. For each invalid update that is found, it will add
    its "middle" value to the total sum that will be returned.

    Args:
        text (list[str]): The input as a list of its lines.

    Returns:
        int: The sum of all middle page numbers from all invalid updates.
    """
    answer = 0
    page_map = {}
    updates: list[list[str]] = []
    invalid_updates: list[list[str]] = []
    
    # parsing page relations and updates
    for line in text:
        if "|" in line:
            predecessor, successor = line.split("|")
            page_map.setdefault(predecessor, set()).add(successor)
        elif "," in line:
            update_as_list = line.split(",")
            updates.append(update_as_list)


    # update validation
    for update in updates:
        is_valid = True
        
        for pair in pairwise(update):
            first, second = pair[0], pair[1]
            if first not in page_map or second not in page_map[first]:
                is_valid = False
                break
            
        # find the middle of the invalid update
        if not is_valid:
            invalid_updates.append(update)

    for update in invalid_updates:
        sort_invalid(update, page_map)
        answer += int(update[len(update)//2])
    
    return answer


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--test", action="store_true", help="Enable command line input for testing")
    parser.add_argument("-f", "--file", action="store_true", help="Enable command line input for testing")
    args = parser.parse_args()
    
    # Part 1 and 2 w/test input
    test_lines = []
    if args.test:
        print("Please enter your test input.\nPaste the entire value. Enter '\\q' on a new line to finish.")
        while True:
            line = input()
            if line == "\\q":
                break
            test_lines.append(line)
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
