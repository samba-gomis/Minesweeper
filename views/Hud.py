import tkinter as tk

class Hud(tk.Frame):
    """
    Game status bar: mine counter, timer and reset button
    """

    def __init__(self, parent, window):
        super().__init__(parent, bg="#313244", padx=8, pady=6)
        self.window = window

        # Mine counter
        self.mine_var = tk.StringVar(value="💣 000")
        self.mine_label = tk.Label(self, textvariable=self.mine_var,
                                   bg="#313244", fg="#f38ba8",
                                   font=("Courier", 16, "bold"))
        self.mine_label.pack(side=tk.LEFT, padx=(4, 0))

        # Reset button
        self.reset_btn = tk.Button(self, text="🙂", font=("Arial", 18),
                                   bg="#45475a", fg="#cdd6f4",
                                   activebackground="#585b70",
                                   relief="flat", cursor="hand2",
                                   command=self.window.new_game)
        self.reset_btn.pack(side=tk.LEFT, expand=True)

        # Timer
        self.timer_var = tk.StringVar(value="⏱ 000")
        self.timer_label = tk.Label(self, textvariable=self.timer_var,
                                    bg="#313244", fg="#a6e3a1",
                                    font=("Courier", 16, "bold"))
        self.timer_label.pack(side=tk.RIGHT, padx=(0, 4))

    def update_mines(self, count: int):
        """Updates the remaining mine counter"""
        self.mine_var.set(f"💣 {count:03d}")

    def update_timer(self, seconds: int):
        """Updates the timer display"""
        self.timer_var.set(f"⏱ {min(seconds, 999):03d}")

    def show_result(self, won: bool):
        """Changes the reset button emoji based on the game result"""
        self.reset_btn.config(text="😎" if won else "😵")

    def reset(self):
        """Resets the HUD to its initial state"""
        self.reset_btn.config(text="🙂")
        self.timer_var.set(" 000")
        mine_count = self.window.difficulty.mine_count
        self.mine_var.set(f"💣 {mine_count:03d}")