import tkinter as tk
from controllers.Game import Game
from utils.constants import *


class UIBoard(tk.Frame):
    """
    Game board canvas
    Handles cell rendering and left/right click events
    """

    def __init__(self, parent, window):
        super().__init__(parent, bg=DEEP_BLUE)
        self.window = window

        rows = window.difficulty.rows
        cols = window.difficulty.cols

        self.game = Game(rows, cols, window)
        self._first_click = True
        self._game_over = False

        self.canvas = tk.Canvas(self, width=cols * WIDTH, height=rows * HEIGHT,
                                bg=BLACK, highlightthickness=0)
        self.canvas.pack()

        self.canvas.bind("<Button-1>", self._on_left_click)
        self.canvas.bind("<Button-3>", self._on_right_click)
    def reveal_all_bombs(self):
        for row in range(self.game.board.rows):
            for col in range(self.game.board.cols):
                cell = self.game.board.get_cell(row, col)
                if cell.is_mine:
                    cell.is_revealed = True
        self._draw_board()

        self._draw_board()

    def _draw_board(self):
        """Redraws all cells on the board"""
        self.canvas.delete("all")
        for row in range(self.game.board.rows):
            for col in range(self.game.board.cols):
                self._draw_cell(row, col)

    def _draw_cell(self, row: int, col: int):
        """Draws a single cell based on its current state"""
        cell = self.game.board.get_cell(row, col)
        x1 = col * WIDTH
        y1 = row * HEIGHT
        x2 = x1 + WIDTH
        y2 = y1 + HEIGHT
        cx = x1 + WIDTH // 2
        cy = y1 + HEIGHT // 2

        tag = f"cell_{row}_{col}"
        self.canvas.delete(tag)

        if not cell.is_revealed:
            self.canvas.create_rectangle(x1, y1, x2, y2,
                                         fill="#585b70", outline=BLACK,
                                         width=1, tags=tag)
            if hasattr(cell, 'is_flag') and cell.is_flag:
                self.canvas.create_text(cx, cy, text="🚩",
                                        font=("Arial", 14), tags=tag)
            elif hasattr(cell, 'is_interrogation') and cell.is_interrogation:
                self.canvas.create_text(cx, cy, text="❓",
                                        font=("Arial", 14), tags=tag)
        else:
            self.canvas.create_rectangle(x1, y1, x2, y2,
                                         fill=BLACK, outline="#45475a",
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
        col = event.x // WIDTH
        row = event.y // HEIGHT
        return row, col

    def _on_left_click(self, event):
        """Reveals the clicked cell"""
        if self._game_over:
            return
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
        if self._game_over:
            return
        row, col = self._get_cell_pos(event)
        if not self.game.board.is_valid(row, col):
            return

        self.game.cycle_flag(row, col)
        self.window.hud.update_mines(self.game.board.mines_left())
        self._draw_cell(row, col)

    def reset(self):
        """Creates a new game on the same board"""
        self._first_click = True
        self._game_over = False
        rows = self.window.difficulty.rows
        cols = self.window.difficulty.cols
        self.game = Game(rows, cols, self.window)
        self._draw_board()