"""
My version of "Skyscrapers game" winning combination check on GitHub:
https://github.com/bmykhaylivvv/coding_semester_2/tree/main/lab_1/skyscrapers
"""

import collections


def read_input(path: str):
    """
    Read game board file from path.
    Return list of str.

    >>> read_input("check.txt")
    ['***21**', '412453*', '423145*', '*543215', '*35214*', '*41532*', '*2*1***']
    """

    with open(path) as brd:
        board = brd.readlines()

    board = [line.rstrip() for line in board]
    return board


def left_to_right_check(input_line: str, pivot: int):
    """
    Check row-wise visibility from left to right.
    Return True if number of building from the left-most hint is visible looking to the right,
    False otherwise.

    input_line - representing board row.
    pivot - number on the left-most hint of the input_line.

    >>> left_to_right_check("412453*", 4)
    True
    >>> left_to_right_check("452453*", 5)
    False
    """
    counter = 1
    highest = input_line[1]
    for i in range(2, len(input_line[1:-1]) + 1):
        if input_line[i] > highest:
            counter += 1
            highest = input_line[i]

    if counter == pivot:
        return True

    return False


def check_not_finished_board(board: list):
    """
    Check if skyscraper board is not finished, i.e., '?' present on the game board.

    Return True if finished, False otherwise.

    >>> check_not_finished_board(['***21**', '4?????*', '4?????*', '*?????5', '*?????*', '*?????*', '*2*1***'])
    False
    >>> check_not_finished_board(['***21**', '412453*', '423145*', '*543215', '*35214*', '*41532*', '*2*1***'])
    True
    >>> check_not_finished_board(['***21**', '412453*', '423145*', '*5?3215', '*35214*', '*41532*', '*2*1***'])
    False
    """
    for line in range(1, len(board)-1):
        if '?' in board[line][1:-1]:
            return False
    return True


def check_uniqueness_in_rows(board: list):
    """
    Check buildings of unique height in each row.

    Return True if buildings in a row have unique length, False otherwise.

    >>> check_uniqueness_in_rows(['***21**', '412453*', '423145*', '*543215', '*35214*', '*41532*', '*2*1***'])
    True
    >>> check_uniqueness_in_rows(['***21**', '452453*', '423145*', '*543215', '*35214*', '*41532*', '*2*1***'])
    False
    >>> check_uniqueness_in_rows(['***21**', '412453*', '423145*', '*553215', '*35214*', '*41532*', '*2*1***'])
    False
    """
    for line in board[1:-1]:
        dict = collections.Counter(line[1:-1])

        for number in dict.items():
            if number[1] > 1:
                return False
    return True


def check_horizontal_visibility(board: list):
    """
    Check row-wise visibility (left-right and vice versa)

    Return True if all horizontal hints are satisfiable,
     i.e., for line 412453* , hint is 4, and 1245 are the four buildings
      that could be observed from the hint looking to the right.

    >>> check_horizontal_visibility(['***21**', '412453*', '423145*', '*543215', '*35214*', '*41532*', '*2*1***'])
    True
    >>> check_horizontal_visibility(['***21**', '452453*', '423145*', '*543215', '*35214*', '*41532*', '*2*1***'])
    False
    >>> check_horizontal_visibility(['***21**', '452413*', '423145*', '*543215', '*35214*', '*41532*', '*2*1***'])
    False
    """
    def horizontal_visibility(line):
        if line[0] != '*':
            pivot = int(line[0])
            counter = 1
            highest = line[1]
            for i in range(2, len(line[1:-1]) + 1):
                if line[i] > highest:
                    counter += 1
                    highest = line[i]

            if counter == pivot:
                return True
            return False
        pass

    board = board + [line[::-1] for line in board]

    tf = []
    for ln in board:
        res = horizontal_visibility(ln)
        if res is not None:
            tf.append(res)

    return all(tf)


def check_columns(board: list):
    """
    Check column-wise compliance of the board for uniqueness (buildings of unique height) and visibility (top-bottom and vice versa).

    Same as for horizontal cases, but aggregated in one function for vertical case, i.e. columns.

    >>> check_columns(['***21**', '412453*', '423145*', '*543215', '*35214*', '*41532*', '*2*1***'])
    True
    >>> check_columns(['***21**', '412453*', '423145*', '*543215', '*35214*', '*41232*', '*2*1***'])
    False
    >>> check_columns(['***21**', '412553*', '423145*', '*543215', '*35214*', '*41532*', '*2*1***'])
    False
    """
    reversed_board = []
    for line in range(len(board)):
        new_line = ''
        for char in range(len(board[line])):
            new_line += board[char][line]
        reversed_board.append(new_line)

    if check_uniqueness_in_rows(reversed_board) and check_horizontal_visibility(reversed_board):
        return True
    return False


def check_skyscrapers(input_path: str):
    """
    Main function to check the status of skyscraper game board.
    Return True if the board status is compliant with the rules,
    False otherwise.

    >>> check_skyscrapers("check.txt")
    True
    """
    board = read_input(input_path)

    if check_not_finished_board(board) and check_uniqueness_in_rows(board)\
            and check_horizontal_visibility(board) and check_columns(board):
        return True
    return False


if __name__ == "__main__":
    print(check_skyscrapers("check.txt"))
    import doctest
    doctest.testmod()
