import tkinter as tk
from controllers.Game import Game
from utils.constants import *


class UIBoard(tk.Frame):
    """
    Game board canvas
    Handles cell rendering and left/right click events
    """

    def __init__(self, parent, window):
        super().__init__(parent, bg=COLOR_BG)
        self.window = window

        rows = window.difficulty.rows
        cols = window.difficulty.cols

        self.game = Game(rows, cols, window)
        self._first_click = True

        width = cols * CELL_SIZE
        height = rows * CELL_SIZE
        self.canvas = tk.Canvas(self, width=width, height=height,
                                bg=COLOR_CELL, highlightthickness=0)
        self.canvas.pack()

        self.canvas.bind("<Button-1>", self._on_left_click)
        self.canvas.bind("<Button-3>", self._on_right_click)

        self._draw_board()

    def _draw_board(self):
        """Redraws all cells on the board."""
        self.canvas.delete("all")
        for row in range(self.game.board.rows):
            for col in range(self.game.board.cols):
                self._draw_cell(row, col)

    def _draw_cell(self, row: int, col: int):
        """Draws a single cell based on its current state."""
        cell = self.game.board.get_cell(row, col)
        x1 = col * CELL_SIZE
        y1 = row * CELL_SIZE
        x2 = x1 + CELL_SIZE
        y2 = y1 + CELL_SIZE
        cx = x1 + CELL_SIZE // 2
        cy = y1 + CELL_SIZE // 2

        tag = f"cell_{row}_{col}"
        self.canvas.delete(tag)

        if not cell.is_revealed:
            self.canvas.create_rectangle(x1, y1, x2, y2,
                                         fill=COLOR_CELL, outline=COLOR_BORDER,
                                         width=1, tags=tag)
            if cell.state == CellState.FLAGGED:
                self.canvas.create_text(cx, cy, text="🚩",
                                        font=("Arial", 14), tags=tag)
            elif cell.state == CellState.QUESTIONED:
                self.canvas.create_text(cx, cy, text="❓",
                                        font=("Arial", 14), tags=tag)
        else:
            self.canvas.create_rectangle(x1, y1, x2, y2,
                                         fill=COLOR_CELL_REVEALED,
                                         outline=COLOR_BORDER_REVEALED,
                                         width=1, tags=tag)
            if cell.is_mine:
                self.canvas.create_text(cx, cy, text="💣",
                                        font=("Arial", 14), tags=tag)
            elif cell.value > 0:
                color = NUMBER_COLORS.get(cell.value, "#cdd6f4")
                self.canvas.create_text(cx, cy, text=str(cell.value),
                                        font=("Courier", 13, "bold"),
                                        fill=color, tags=tag)

    def _get_cell_pos(self, event):
        """Returns (row, col) from event coordinates"""
        col = event.x // CELL_SIZE
        row = event.y // CELL_SIZE
        return row, col

    def _on_left_click(self, event):
        """Reveals the clicked cell"""
        row, col = self._get_cell_pos(event)
        if not self.game.board.is_valid(row, col):
            return

        if self._first_click:
            self._first_click = False
            self.window.on_first_click()
            self.game.board.place_mines(row, col, self.window.difficulty.mine_count)

        self.game.reveal(row, col)
        self._draw_board()

    def _on_right_click(self, event):
        """Cycles through: flag, question mark, unknown"""
        row, col = self._get_cell_pos(event)
        if not self.game.board.is_valid(row, col):
            return

        self.game.cycle_flag(row, col)
        self.window.hud.update_mines(self.game.board.mines_left())
        self._draw_cell(row, col)

    def reset(self):
        """Creates a new game on the same board"""
        self._first_click = True
        rows = self.window.difficulty.rows
        cols = self.window.difficulty.cols
        self.game = Game(rows, cols, self.window)
        self._draw_board()