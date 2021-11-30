from typing import *
from utils import cross,chunk_string_by_len

ROWS = 'ABCDEFGHI'
COLS = '123456789'

boxes = cross(ROWS, COLS)
row_units = [cross(r,COLS) for r in ROWS]
col_units = [cross(ROWS,c) for c in COLS]
square_units = [cross(r,c) for r in chunk_string_by_len(ROWS) for c in chunk_string_by_len(COLS)]
unit_list = row_units + col_units + square_units

def get_puzzle(complex:bool = False) -> str:
    """Returns puzzle with high or medium complexity.

    Args:
        complex (bool, optional):An option if harder puzzle is required. Defaults to False.

    Returns:
        str: Returns puzzle string.
    """
    if complex:
        return '4.....8.5.3..........7......2.....6.....8.4......1.......6.3.7.5..2.....1.4......'
    
    return '..3.2.6..9..3.5..1..18.64....81.29..7.......8..67.82....26.95..8..2.3..9..5.1.3..'

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
            
def find_peers(box:str) -> List[str]:
    """This function returns the peers of box.
    Args:
        box (str): A box unit
    
    Returns:
        List[str]: A List of peers for the given box.
    """
    
    peers_list=[list for list in unit_list if box in list]
    peers = list(set([item for sub_list in peers_list for item in sub_list if item !=box]))
    return peers
     
def eliminate(grids:Dict[str,str]) -> Dict[str,str]:
    """This function eliminates values from temporary box units(with values 1-9) if 
       that is present in single valued peers of that box.
    Args:
        grids (Dict[str,str]): A dictionary of sudoku box units
        
    Returns:
        grids (Dict[str,str]): A dictionary of sudoku box units with eliminated values.
    """
    for key,value in grids.items():
        if len(value) > 1:
            peers = find_peers(key)
            peers_values = [grids.get(k) for k in peers if len(grids.get(k))==1]
            for v in peers_values:
                value=value.replace(v,"")
            grids[key]=value
    return grids

def only_choice(grids:Dict[str,str]) -> Dict[str,str]:
    """This function replaces eliminated box units with only choice value
       with in the unit.

    Args:
        grids (Dict[str,str]): A dictionary of sudoku box units

    Returns:
        grids (Dict[str,str]): A dictionary of sudoku box units with replacing only values.
    """
    for unit in unit_list:
        for digit in '123456789':
            d_places = [box for box in unit if digit in grids[box]]
            if len(d_places) == 1:
                grids[d_places[0]] = digit
    return grids
    
def reduce_puzzle(grids:Dict[str,str]) -> Union[Dict[str,str],bool]:
    """This function reduces unsolved box units to single value with repeated elimination and reduction.

    Args:
        grids (Dict[str,str]): A dictionary of sudoku box units

    Returns:
        grids (Dict[str,str]): A dictionary of sudoku box units with replacing only values.
        solved (bool) : A boolean value to indicate that puzzle is solved or not.
    """
    stalled = False
    solved = False
    while not stalled:
        solved_values_before = len([value for value in grids.values() if len(value)==1])#total units with single value
        grids = eliminate(grids)
        grids = only_choice(grids)
        solved_values_after = len([value for value in grids.values() if len(value)==1])#total units with single value
        stalled = solved_values_before == solved_values_after
        if len([box for box in grids.keys() if len(grids[box]) == 0]):
            return False 
    return grids

def search(values:Dict[str,str])->Dict[str,str]:
    "Using depth-first search and propagation, create a search tree and solve the sudoku."
    # First, reduce the puzzle using the previous function
    values = reduce_puzzle(values)
    if values is False:
        return False ## Failed earlier
    if all(len(values[s]) == 1 for s in boxes): 
        return values ## Solved!
    
    # Choose one of the unfilled squares with the fewest possibilities
    # checks min values with in the list of tuples
    n,k =  min((len(v),k) for k,v in values.items() if len(v)>1)
    
    # Now use recursion to solve each one of the resulting sudokus, and if one returns a value (not False), return that answer!
    for value in values[k]:
        new_sudoku=values.copy()
        new_sudoku[k]=value
        attempt = search(new_sudoku,)
        if attempt:
            return attempt
        
def check_if_sudoku_solved(grids:Dict[str,str]) -> bool:
    for unit in unit_list:
        unit_values_sum = sum([int(grids.get(k)) for k in unit])
        solved = unit_values_sum == 45
    return solved

def main(display_units:bool=False):
    """This is the main function to do all the main functionalities.
    Args:
        display_units (bool, optional): A option to display units. Defaults to False.
    """
    
    if display_units:
        print(f"boxes : \n{boxes}\n")
        print(f"row_units : \n{row_units}\n")
        print(f"col_units : \n{col_units}\n")
        print(f"square_units : \n{square_units}\n")
        print(f"unit_lists : \n{unit_list}\n")
        
    # get puzzle
    puzzle = get_puzzle(complex=True)
    print("\nUnsolved Sudoku.")
    display_sudoku(grid_values(puzzle,boxes,replace=False)) #display original
    
    print("\nSudoku with replaced dots by 1-9.")
    grid_units = grid_values(puzzle,boxes)
    display_sudoku(grid_units) #display replaced
    
    print("\nSudoku with eliminated values.")
    eliminated_values=eliminate(grid_units)
    display_sudoku(eliminated_values) #display eliminated
    
    print("\nSudoku after replacing with only choices.")
    elimination_with_only_coices_values=only_choice(eliminated_values)
    display_sudoku(elimination_with_only_coices_values)
    
    print("\nSudoku after Constraint Propagation.")
    reduced_puzzle_values=reduce_puzzle(eliminated_values)
    display_sudoku(reduced_puzzle_values)
    
    solved = check_if_sudoku_solved(reduced_puzzle_values)
    if not solved:
        print("\nThe SUDOKU is UnSolved and needs searching.")
        print("Sudoku after Search.")
        solved_puzzle_with_search=search(eliminated_values)
        display_sudoku(solved_puzzle_with_search)
        solved = check_if_sudoku_solved(solved_puzzle_with_search) 
        
    print(f'The SUDOKU is {"Solved" if solved else "UnSolved"}.')
    
if __name__ == "__main__":
    
    main()