# 💣 Minesweeper

A classic Minesweeper game built with Python and Tkinter, featuring a sleek dark theme (Catppuccin Mocha) and three difficulty levels.

---

## ✨ Features

- **3 difficulty levels** with randomized mine counts
- **Safe first click** — the first cell clicked is never a mine
- **Flood-fill reveal** — clicking an empty cell cascades to reveal neighbors
- **Flag cycling** — right-click to cycle through flag 🚩, question mark ❓, and unknown states
- **Live HUD** — mine counter and timer update in real time
- **Auto-reveal on loss** — all bombs are shown when the game is lost
- **Dark theme** — Catppuccin Mocha color palette throughout

---

## 🎮 How to Play

| Action | Effect |
|---|---|
| Left click | Reveal a cell |
| Right click | Cycle: flag 🚩 → question ❓ → clear |
| Reset button 🙂 | Start a new game |
| Menu → New Game | Start a new game |
| Menu → Difficulty | Change difficulty |

**You win** when all non-mine cells are revealed.  
**You lose** if you click on a mine.

---

## 📐 Difficulty Levels

| Level | Grid | Mines |
|---|---|---|
| Easy | 9 × 9 | 5 – 8 |
| Intermediate | 16 × 16 | 30 – 55 |
| Expert | 30 × 16 | 70 – 99 |

Mine counts are randomized within the range each time a new game starts.

---

## 🚀 Getting Started

### Requirements

- Python 3.8+
- Tkinter (included with standard Python installations)

### Installation

```bash
git clone https://github.com/your-username/minesweeper.git
cd minesweeper
```

### Run

```bash
python main.py
```

No additional dependencies are required.

---

## 🗂️ Project Structure

```
minesweeper/
│
├── main.py                  # Entry point
│
├── views/
│   ├── Window.py            # Main window, menu, layout orchestration
│   ├── Hud.py               # Status bar (mine counter, timer, reset button)
│   └── UIBoard.py           # Canvas-based game board, click handling
│
├── controllers/
│   ├── Game.py              # Game logic (reveal, flag, victory check)
│   ├── GameBoard.py         # Board state, mine placement, flood-fill
│   ├── GameSquare.py        # Individual cell model
│   └── Timer.py             # Countdown timer using tkinter `after`
│
├── config/
│   └── Difficulty.py        # Grid size and mine count per difficulty
│
└── utils/
    ├── constants.py         # Colors, grid sizes, cell dimensions
    └── helper.py            # Utility functions (time format, bomb count)
```

---

## 🎨 Theme

The UI uses the [Catppuccin Mocha](https://github.com/catppuccin/catppuccin) color palette.

| Element | Color |
|---|---|
| Background | `#1e1e2e` |
| HUD bar | `#313244` |
| Unrevealed cell | `#585b70` |
| Revealed cell | `#313244` |
| Mine counter | `#f38ba8` (red) |
| Timer | `#a6e3a1` (green) |

Number colors follow the classic Minesweeper convention (1 = blue, 2 = green, 3 = red, …)