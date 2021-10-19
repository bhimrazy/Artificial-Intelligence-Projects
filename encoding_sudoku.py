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


def chunk_string_by_len(string: str, n: int = 3) -> List[str]:
    """This function returns chunks of strings of length n

    Args:
        string (str): Any String
        n (int): Length of chunk

    Returns:
        List[str]: List of all possible chunks
    """
    return [string[i:i+n] for i in range(0, len(string), n)]

def grid_values(puzzle:str) -> Dict[str,str]:
    """This function maps each puzzle unit to its box unit.

    Args:
        puzzle (str): String of puzzle

    Returns:
        Dict[str,str]: A dictionary of box units with its puzzle value.
    """
    return {key : value for key,value in zip(cross(ROWS, COLS),puzzle)}

def display_grid(p_values:Dict[str,str])  -> None:
    """This function displays the dictonary in proper grid format.

    Args:
        p_values (Dict[str,str]): Dictionary of puzzlle with box number and value.
    """
    assert (len(p_values) == 81),"There must be 81 values in the dictionary."
    
    print(f"\n{'='*15}SUDOKU{'='*14}\n")
    list_puzzle = list(p_values.items())
    n=9
    for i in range(0,len(p_values),n):
        row=''
        for index,box in enumerate(list_puzzle[i:i+n]):
            if (index > 1 and index < 9) and index % 3 == 0 :
                row +=f' |   '  #to add a pipe in middle
            row +=f'{box[1]}  '
            
        print(row,'\n')
        if i == 18 or i== 45 :  #to add a decorative line in middle 
            print('-'*10 + '+' + '-'*13 + '+' + '-'*10,'\n')
  

if __name__ == "__main__":
    
    boxes = cross(ROWS, COLS)
    
    row_units = [cross(r,COLS) for r in ROWS]
    col_units = [cross(ROWS,c) for c in COLS]
    square_units = [cross(r,c) for r in chunk_string_by_len(ROWS) for c in chunk_string_by_len(COLS)]
    
    print(f"boxes : \n{boxes}\n")
    print(f"row_units : \n{row_units}\n")
    print(f"col_units : \n{col_units}\n")
    print(f"square_units : \n{square_units}\n")
    
    unit_list = row_units + col_units + square_units
    print(f"square_units : \n{unit_list}\n")
    
    puzzle = '..3.2.6..9..3.5..1..18.64....81.29..7.......8..67.82....26.95..8..2.3..9..5.1.3..'
    
    display_grid(grid_values(puzzle))
    
"""
===============SUDOKU==============
.  .  3   |   .  2  .   |   6  .  .   

9  .  .   |   3  .  5   |   .  .  1   

.  .  1   |   8  .  6   |   4  .  .   

----------+-------------+---------- 

.  .  8   |   1  .  2   |   9  .  .   

7  .  .   |   .  .  .   |   .  .  8   

.  .  6   |   7  .  8   |   2  .  .   

----------+-------------+---------- 

.  .  2   |   6  .  9   |   5  .  .   

8  .  .   |   2  .  3   |   .  .  9   

.  .  5   |   .  1  .   |   3  .  .
"""