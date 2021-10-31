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
    assert len(puzzle) == 81
    
    return {key : ( '123456789' if value =='.' and replace else value) for key,value in zip(boxes,puzzle)}


def display_sudoku(p_values:Dict[str,str])  -> None:
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
            pt='-'*(max_len*3) #tern
            print('+'.join([pt,pt,pt]),'\n')
            
def find_peers(box:str,unit_list:List[List[str]]) -> List[str]:
    """This function returns the peers of box.
    Args:
        box (str): A box unit
        unit_list (LList[List[str]]): A list of units
    
    Returns:
        List[str]: A List of peers for the given box.
    """
    
    peers_list=[list for list in unit_list if box in list]
    peers = list(set([item for sub_list in peers_list for item in sub_list if item !=box]))
    return peers
     
def eliminate(grids:Dict[str,str],unit_list:List[List[str]]) -> Dict[str,str]:
    """This function eliminates values from temporary box units(with values 1-9) if 
       that is present in single valued peers of that box.
    Args:
        grids (Dict[str,str]): A dictionary of sudoku box units
        unit_list (List[List[str]]): A list of units
    
    Returns:
        grids (Dict[str,str]): A dictionary of sudoku box units with eliminated values.
    """
    for key,value in grids.items():
        if len(value) > 1:
            peers = find_peers(key,unit_list)
            peers_values = [grids.get(k) for k in peers if len(grids.get(k))==1]
            for v in peers_values:
                value=value.replace(v,"")
            grids[key]=value
    return grids

def only_choice(grids:Dict[str,str],unit_list:List[List[str]]) -> Dict[str,str]:
    """This function replaces eliminated box units with only choice value
       with in the unit.

    Args:
        grids (Dict[str,str]): A dictionary of sudoku box units
        unit_list (List[List[str]]): A list of units

    Returns:
        grids (Dict[str,str]): A dictionary of sudoku box units with replacing only values.
    """
    for unit in unit_list:
        for digit in '123456789':
            d_places = [box for box in unit if digit in grids[box]]
            if len(d_places) == 1:
                grids[d_places[0]] = digit
    return grids
    
def reduce_puzzle(grids:Dict[str,str],unit_list:List[List[str]]) -> Union[Dict[str,str],bool]:
    """This function reduces unsolved box units to single value with repeated elimination and reduction.

    Args:
        grids (Dict[str,str]): A dictionary of sudoku box units
        unit_list (List[List[str]]): A list of units

    Returns:
        grids (Dict[str,str]): A dictionary of sudoku box units with replacing only values.
        solved (bool) : A boolean value to indicate that puzzle is solved or not.
    """
    stalled = False
    solved = False
    while not stalled:
        solved_values_before = len([value for value in grids.values() if len(value)==1])#total units with single value
        grids = eliminate(grids, unit_list)
        grids = only_choice(grids, unit_list)
        solved_values_after = len([value for value in grids.values() if len(value)==1])#total units with single value
        stalled = solved_values_before == solved_values_after
        
    for unit in unit_list:
        unit_values_sum = sum([int(grids.get(k)) for k in unit])
        solved = unit_values_sum == 45
    return grids,solved
  
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
        print(f"unit_lists : \n{unit_list}\n")
    
    puzzle = '..3.2.6..9..3.5..1..18.64....81.29..7.......8..67.82....26.95..8..2.3..9..5.1.3..'
    print("\nUnsolved Sudoku.")
    display_sudoku(grid_values(puzzle,boxes,replace=False)) #display original
    
    print("\nSudoku with replaced dots.")
    grid_units = grid_values(puzzle,boxes)
    display_sudoku(grid_units) #display replaced
    
    print("\nSudoku with eliminated values.")
    eliminated_values=eliminate(grid_units,unit_list)
    display_sudoku(eliminated_values) #display eliminated
    
    print("\nSudoku after replacing with only choices.")
    elimination_with_only_coices_values=only_choice(eliminated_values,unit_list)
    display_sudoku(elimination_with_only_coices_values)
    
    print("\nSudoku after Constraint Propagation.")
    reduced_puzzle_values,solved=reduce_puzzle(eliminated_values,unit_list)
    display_sudoku(reduced_puzzle_values)
    
    print(f'The SUDOKU is {"Solved" if solved else "UnSolved"}.')
    
if __name__ == "__main__":
    
    main()