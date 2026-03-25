# Colors
RED       = "#f38ba8"
GREEN     = "#a6e3a1"
DEEP_BLUE = "#1e1e2e"
BLUE      = "#8aadf4"
BLACK     = "#313244"

# Number colors (1 to 8)
NUMBER_COLORS = {
    1: BLUE,
    2: GREEN,
    3: RED,
    4: "#cba6f7",
    5: "#fab387",
    6: "#89dceb",
    7: "#cdd6f4",
    8: "#6c7086",
}

# Play state
PLAY_STATE = {
    "WAITING": "waiting",
    "PLAYING": "playing",
    "WON":     "won",
    "LOST":    "lost",
}

# Square state
SQUARE_STATE = {
    "UNKNOWN":    "unknown",
    "FLAGGED":    "flagged",
    "QUESTIONED": "questioned",
}

# Grid sizes
SMALL_GRID  = (9,  9)
MEDIUM_GRID = (16, 16)
BIG_GRID    = (30, 16)

# Bomb count range (min, max) per difficulty
MIN_BOMB = {
    "EASY":         10,
    "INTERMEDIATE": 30,
    "EXPERT":       70,
}

MAX_BOMB = {
    "EASY":         15,
    "INTERMEDIATE": 55,
    "EXPERT":       99,
}

# Cell size
HEIGHT = 32
WIDTH  = 32