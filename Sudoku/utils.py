from typing import List
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

