from typing import *
ROWS = '123456789'
COLS = 'ABCDEFGHI'


def cross(row: str, col: str) -> List[str]:
    """This function returns the list formed by 
    all the possible concatenations of a letter r in string row with a letter c in string col.

    Args:
        row (str): String of concatenated Numbers
        col (str): String of concatenated Characters
        
    Returns:
        List(str): List of all possible cross concatenations.
    """
    return [r + c for r in row for c in col]


if __name__=="__main__":
    boxes = cross(ROWS,COLS)
    print(boxes)
