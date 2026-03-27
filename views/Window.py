import tkinter as tk
from views.Hud import Hud
from views.UIBoard import UIBoard
from controllers.Timer import Timer
from config.Difficulty import Difficulty


class Window(tk.Tk):
    """
    Main game window for Minesweeper
    Orchestrates all widgets: HUD, game board and timer
    """

    def __init__(self):
        super().__init__()

        self.title("Minesweeper")
        self.resizable(False, False)
        self.configure(bg="#1e1e2e")

        self.difficulty = Difficulty("EXPERT")
        self.timer = Timer(self)

        self._build_menu()
        self._build_ui()

        self.update_idletasks()
        self._center_window()

    def _build_menu(self):
        menubar = tk.Menu(self, bg="#313244", fg="#cdd6f4",
                          activebackground="#45475a", activeforeground="#cdd6f4",
                          relief="flat")

        game_menu = tk.Menu(menubar, tearoff=0, bg="#313244", fg="#cdd6f4",
                            activebackground="#45475a", activeforeground="#cdd6f4")
        game_menu.add_command(label="New Game", command=self.new_game)
        game_menu.add_separator()
        game_menu.add_command(label="Quit", command=self.quit)
        menubar.add_cascade(label="Game", menu=game_menu)

        diff_menu = tk.Menu(menubar, tearoff=0, bg="#313244", fg="#cdd6f4",
                            activebackground="#45475a", activeforeground="#cdd6f4")
        diff_menu.add_command(label="Easy (9x9)",
                      command=lambda: self._change_difficulty("EASY"))
        diff_menu.add_command(label="Intermediate (16x16)",
                      command=lambda: self._change_difficulty("INTERMEDIATE"))
        diff_menu.add_command(label="Expert (30x16)",
                      command=lambda: self._change_difficulty("EXPERT"))
        menubar.add_cascade(label="Difficulty", menu=diff_menu)

        self.config(menu=menubar)

    def _build_ui(self):
        self.main_frame = tk.Frame(self, bg="#1e1e2e", padx=10, pady=10)
        self.main_frame.pack(fill=tk.BOTH, expand=True)

        self.hud = Hud(self.main_frame, self)
        self.hud.pack(fill=tk.X, pady=(0, 8))

        self.board = UIBoard(self.main_frame, self)
        self.board.pack()

    def new_game(self):
        self.timer.reset()
        self.hud.reset()
        self.board.reset()
        self._center_window()

    def _change_difficulty(self, level):
        self.difficulty = Difficulty(level)
        self.board.destroy()
        self.board = UIBoard(self.main_frame, self)
        self.board.pack()
        self.new_game()

    def on_first_click(self):
        """Called by UIBoard on the first click: starts the timer"""
        self.timer.start()

    def on_game_over(self, won: bool):
        """Called by Game when the game ends"""
        self.timer.stop()
        self.hud.show_result(won)
        self.board._game_over = True
        if not won:
            self.board.reveal_all_bombs()

    def _center_window(self):
        w = self.winfo_width()
        h = self.winfo_height()
        x = (self.winfo_screenwidth() - w) // 2
        y = (self.winfo_screenheight() - h) // 2
        self.geometry(f"{w}x{h}+{x}+{y}")