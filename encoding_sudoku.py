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


def grid_values(puzzle:str,boxes:List[str],replace:bool=True) -> Dict[str,str]:
    """This function maps each puzzle unit to its box unit.
    Args:
        puzzle (str): String of puzzle
        boxes (List[str]): A list of box units
        replace (bool) : An option to relace dots with number 1-9.Defaults to True
    Returns:
        Dict[str,str]: A dictionary of box units with its puzzle value.
    """
    return {key : ( '123456789' if value =='.' and replace else value) for key,value in zip(boxes,puzzle)}


def find_peers(box:str,unit_list:List[List[str]]):
    """This function returns the peers of box.
    Args:
        box (str): A box unit
        unit_list (LList[List[str]]): A list of units
    """
    
    peers_list=[list for list in unit_list if box in list]
    peers = list(set([item for sub_list in peers_list for item in sub_list if item !=box]))
    
    return peers
    
    
def display_grid(p_values:Dict[str,str])  -> None:
    """This function displays the dictonary in proper grid format.
    Args:
        p_values (Dict[str,str]): Dictionary of puzzlle with box number and value.
    """
    assert (len(p_values) == 81),"There must be 81 values in the dictionary."
    
    max_len=len(max(list(p_values.values()),key=len))+2 #max length among all box units
    
    print(f"\n{' SUDOKU '.center(max_len*9,'=')}\n")
    list_puzzle = list(p_values.items())
    
    n=9 #step
    for i in range(0,len(p_values),n):
        row=''
        for index,box in enumerate(list_puzzle[i:i+n]):
            if (index > 1 and index < 9) and index % 3 == 0 :
                row +='|'  #to add a pipe in middle
            row +=box[1].center(max_len)
            
        print(row,'\n')
        if i == 18 or i== 45 :  #to add a decorative line in middle 
            pat='-'*(max_len*3) #pattern
            print('+'.join([pat,pat,pat]),'\n')
            
  
def main(display_units:bool=False):
    """This is the main function to do all the main functionalities.
    Args:
        display_units (bool, optional): A option to display units. Defaults to False.
    """
    boxes = cross(ROWS, COLS)
    
    row_units = [cross(r,COLS) for r in ROWS]
    col_units = [cross(ROWS,c) for c in COLS]
    square_units = [cross(r,c) for r in chunk_string_by_len(ROWS) for c in chunk_string_by_len(COLS)]
    unit_list = row_units + col_units + square_units
    
    if display_units:
        print(f"boxes : \n{boxes}\n")
        print(f"row_units : \n{row_units}\n")
        print(f"col_units : \n{col_units}\n")
        print(f"square_units : \n{square_units}\n")
        print(f"square_units : \n{unit_list}\n")
    
    puzzle = '..3.2.6..9..3.5..1..18.64....81.29..7.......8..67.82....26.95..8..2.3..9..5.1.3..'
    display_grid(grid_values(puzzle,boxes,replace=False)) #display original
    grid_units = grid_values(puzzle,boxes)
    display_grid(grid_units) #display relaced
    display_grid(eliminate(grid_units,unit_list)) #display eliminated
    
if __name__ == "__main__":
    
    main()