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

