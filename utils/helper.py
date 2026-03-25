from utils.constants import *


def passing_time(seconds: int) -> str:
    """Formats elapsed seconds into a MM:SS string"""
    seconds = min(seconds, 5999)
    minutes = seconds // 60
    secs    = seconds % 60
    return f"{minutes:02d}:{secs:02d}"


def remaining_bombs(total_bombs: int, flagged_count: int) -> int:
    """Returns the number of bombs still not flagged"""
    return total_bombs - flagged_count


def remaining_squares(board) -> int:
    """Returns the number of unrevealed non-mine squares left"""
    count = 0
    for row in range(board.rows):
        for col in range(board.cols):
            cell = board.get_cell(row, col)
            if not cell.is_revealed and not cell.is_mine:
                count += 1
    return count


HELP_TEXT = (
    "Left click  : reveal a square\n"
    "Right click : flag / question / unknown\n"
    "First click : never a mine\n"
    "Numbers     : adjacent mine count (1-8)\n"
    "Flag all mines to win!"
)