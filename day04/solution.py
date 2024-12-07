# aoc2024/day04/solution.py
# Solution to Advent of Code 2024 Day 4: Ceres Search

import argparse


# grid == word search
# num_rows == max index for rows
# num_cols == max index for columns


def search_forward(i, j, grid, num_cols) -> int:
    if j + 3 > num_cols:
      return 0
    
    line = grid[i]
    if line[j:j + 4] != "XMAS":
      return 0
    
    return 1


def search_backward(i, j, grid) -> int:
    if j - 3 < 0:
        return 0

    line = grid[i]
    if line[j - 3: j + 1] != "SAMX":
        return 0

    return 1


def search_down(i, j, grid, num_rows) -> int:
    if i + 3 > num_rows:
        return 0

    if (grid[i + 1][j] != "M" or
        grid[i + 2][j] != "A" or
        grid[i + 3][j] != "S"):
        return 0

    return 1


def search_up(i, j, grid) -> int:
    if i - 3 < 0:
        return 0
      
    if (grid[i - 3][j] != "S" or
        grid[i - 2][j] != "A" or
        grid[i - 1][j] != "M"):
        return 0
      
    return 1


def search_diagonal_down_right(i, j, grid, num_rows, num_cols,
                               a="M", b="A", c="S") -> int:
    if i + 3 > num_rows or j + 3 > num_cols:
        return 0
    
    if (grid[i + 1][j + 1] != a or
        grid[i + 2][j + 2] != b or
        grid[i + 3][j + 3] != c):
        return 0
  
    return 1


def search_diagonal_up_right(i, j, grid, num_cols,
                             a="M", b="A", c="S") -> int:
    if i - 3 < 0 or j + 3 > num_cols:
        return 0

    if (grid[i - 1][j + 1] != a or
        grid[i - 2][j + 2] != b or
        grid[i - 3][j + 3] != c):
        return 0

    return 1


def search_diagonal_down_left(i, j, grid, num_rows,
                              a="M", b="A", c="S") -> int:
    if i + 3 > num_rows or j - 3 < 0:
        return 0

    if (grid[i + 1][j - 1] != a or
        grid[i + 2][j - 2] != b or
        grid[i + 3][j - 3] != c):
        return 0

    return 1


def search_diagonal_up_left(i, j, grid, a="M", b="A", c="S") -> int:
    if i - 3 < 0 or j - 3 < 0:
        return 0

    if (grid[i - 1][j - 1] != a or
        grid[i - 2][j - 2] != b or
        grid[i - 3][j - 3] != c):
        return 0

    return 1


def search_cross_mas(i, j, grid, num_rows, num_cols) -> int:
    if (i + 1 > num_rows or i - 1 < 0 or
        j + 1 > num_cols or j - 1 < 0):
        return 0

    # M S       M M
    #  A    or   A 
    # M S       S S
    if (grid[i - 1][j - 1] == "M" and grid[i + 1][j + 1] == "S"):
        if ((grid[i + 1][j - 1] == "M" and grid[i - 1][j + 1] == "S") or
            (grid[i + 1][j - 1] == "S" and grid[i - 1][j + 1] == "M")):
            return 1
          
    # S S       S M
    #  A    or   A 
    # M M       S M
    if (grid[i - 1][j - 1] == "S" and grid[i + 1][j + 1] == "M"):
        if ((grid[i + 1][j - 1] == "M" and grid[i - 1][j + 1] == "S") or
            (grid[i + 1][j - 1] == "S" and grid[i - 1][j + 1] == "M")):
            return 1

    return 0


def part_1(text: list[str]) -> int:
    """Finds all X's. For each X, it searches for XMAS in an omnidirectional
    way.

    Args:
        text (list[str]): The input as a list of its lines.

    Returns:
        int: The number of xmas's found in a word search.
    """
    number_of_xmas = 0
    word_search = [line for line in text]
    MAX_ROW_INDEX = len(word_search) - 1
    MAX_COL_INDEX = len(word_search[0]) - 1 if MAX_ROW_INDEX else 0
    for i, line in enumerate(word_search):
        for j, char in enumerate(line):
            if char == "X":
                number_of_xmas += (search_forward(i, j,
                                                  word_search,
                                                  MAX_COL_INDEX) +
                                   search_backward(i, j,
                                                   word_search) +
                                   search_down(i, j,
                                               word_search,
                                               MAX_ROW_INDEX) +
                                   search_up(i, j,
                                             word_search) +
                                   search_diagonal_down_right(i, j,
                                                              word_search,
                                                              MAX_ROW_INDEX,
                                                              MAX_COL_INDEX) +
                                   search_diagonal_up_right(i, j,
                                                            word_search,
                                                            MAX_COL_INDEX) +
                                   search_diagonal_down_left(i, j,
                                                             word_search,
                                                             MAX_ROW_INDEX) +
                                   search_diagonal_up_left(i, j,
                                                           word_search))
    
    return number_of_xmas


def part_2(text: list[str]) -> int:
    """Finds all A's. For each A, it checks if a crossed is formed by two
    mas's at that A.

    Args:
        text (list[str]): The input as a list of its lines.

    Returns:
        int: The number of crossed mas's that form an X,
             found in a word search.
    """
    number_of_xmas = 0
    word_search = [line for line in text]
    MAX_ROW_INDEX = len(word_search) - 1
    MAX_COL_INDEX = len(word_search[0]) - 1 if MAX_ROW_INDEX else 0
    for i, line in enumerate(word_search):
        for j, char in enumerate(line):
            if char == "A":
                number_of_xmas += search_cross_mas(i, j, word_search,
                                                   MAX_ROW_INDEX,
                                                   MAX_COL_INDEX)
    
    return number_of_xmas
    

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
