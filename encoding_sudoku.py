from typing import *
ROWS = 'ABCDEFGHI'
COLS = '123456789'


def cross(row: str, col: str) -> List[str]:
    """This function returns the list formed by 
    all the possible concatenations of a letter r in string row with a letter c in string col.

    Args:
        row (str): String of concatenated Characters
        col (str): String of concatenated Numbers

    Returns:
        List[str]: List of all possible cross concatenations.
    """
    return [r + c for r in row for c in col]


def chunk_string_by_3(string: str, n: int = 3) -> List[str]:
    """This function returns chunks of strings of length 3

    Args:
        string (str): Any String
        n (int): Length of chunk

    Returns:
        List[str]: List of all possible chunks
    """
    return [string[i:i+n] for i in range(0, len(string), n)]


if __name__ == "__main__":
    
    boxes = cross(ROWS, COLS)
    
    row_units = [cross(r,COLS) for r in ROWS]
    col_units = [cross(ROWS,c) for c in COLS]
    square_units = [cross(r,c) for r in chunk_string_by_3(ROWS) for c in chunk_string_by_3(COLS)]
    
    print(f"boxes : \n{boxes}\n")
    print(f"row_units : \n{row_units}\n")
    print(f"col_units : \n{col_units}\n")
    print(f"square_units : \n{square_units}\n")
