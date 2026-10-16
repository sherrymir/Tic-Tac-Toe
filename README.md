# ❌⭕ Tic-Tac-Toe AI — Python Terminal Game

A terminal-based **Tic-Tac-Toe game built with Python**, where you play as **X** against a computer opponent playing as **O**.

This project uses an object-oriented approach and implements game logic, win detection, move validation, and basic AI decision-making.

The main goal is to **learn by building the AI from scratch**, improving its decision-making logic step by step instead of jumping straight to an advanced algorithm.

## ✨ Features

* 🎮 **Interactive terminal gameplay** — Play directly in your terminal.
* 🟦 **3×3 game board** — Uses readable position labels.
* ✅ **Input validation** — Prevents invalid moves and occupied-square selections.
* 🏆 **Win detection** — Detects horizontal, vertical, and diagonal wins.
* 🧠 **Basic AI** — Prioritizes winning moves and blocking the opponent.
* 🔍 **Experimental Intermediate AI** — Explores hypothetical moves and potential follow-up opportunities.
* 🎲 **Random fallback** — Chooses an available square when the other AI methods don't return a move.
* 🏗️ **Object-oriented design** — Organizes game state and behavior inside a Python class.

## 🧠 AI Approach

### Why I'm Not Using Minimax

Minimax is a well-known algorithm for creating an optimal Tic-Tac-Toe AI. However, **I'm intentionally not using Minimax in this project because I'm practicing and learning how to build AI decision-making logic myself.**

Rather than implementing an advanced algorithm immediately, I'm developing my understanding of how an AI can evaluate moves, recognize threats, and make better decisions.

The idea is to build up my skills gradually, starting with simple rules and moving toward more advanced strategies.

### 1. Basic AI

The `Basic_ai()` method follows two priorities:

1. **Win:** Check whether the computer can win immediately by completing a winning combination.
2. **Block:** If no immediate win is available, check whether the opponent has a winning move and block it.

If neither condition applies, the method returns `None`, allowing the game to try another strategy.

### 2. Intermediate AI

The `Intermediate_ai()` method experiments with hypothetical moves to evaluate potential follow-up opportunities.

The idea is to temporarily consider a move, examine the resulting board, and determine whether that move could lead to a better outcome.

This part of the project is still experimental. Its current logic is not guaranteed to detect every threat or choose the best move.

### 3. Random Fallback

If neither the basic nor intermediate AI selects a move, `computer_move()` chooses a random unoccupied square.

This ensures that the computer can still make a valid move when the other methods don't return a position.

### AI Decision Flow

```text
Computer's Turn
      |
      v
Check for an Immediate Win
      |
      +---- Found? ---- Yes ----> Make Winning Move
      |
      No
      |
      v
Check for an Opponent's Winning Move
      |
      +---- Found? ---- Yes ----> Block Opponent
      |
      No
      |
      v
Try Intermediate AI
      |
      +---- Found? ---- Yes ----> Make Selected Move
      |
      No
      |
      v
Choose a Random Valid Move
```

*Note: This diagram represents the intended decision flow. The intermediate AI is still under development and may not always behave strategically.*

## 🎮 Getting Started

### Requirements

* Python 3.8 or newer
* No third-party packages required

The project uses Python's standard library.

### Installation

Clone the repository:

```bash
git clone https://github.com/sherrymir/tic-tac-toe-ai.git
```

Navigate to the project directory:

```bash
cd tic-tac-toe-ai
```

### Run the Game

Run the game using Python:

```bash
python game.py
```

If your system uses `python3`, run:

```bash
python3 game.py
```

## 🕹️ How to Play

1. You play as **X**.
2. The computer plays as **O**.
3. Enter the name of an available square when prompted.
4. The game validates your move.
5. The computer selects its move according to its AI logic.
6. The game continues until someone wins or the board is full.

### Example

```text
Where do you wanna put X e.g(TopL,MidC,BotR): MidC
```

Enter the position exactly as shown in the prompt.

## 🗺️ Board Position Guide

The game uses the following position labels:

```text
TopL | TopC | TopR
-----+------+-----
MidL | MidC | MidR
-----+------+-----
BotL | BotC | BotR
```

| Position | Location      |
| -------- | ------------- |
| `TopL`   | Top-left      |
| `TopC`   | Top-center    |
| `TopR`   | Top-right     |
| `MidL`   | Middle-left   |
| `MidC`   | Center        |
| `MidR`   | Middle-right  |
| `BotL`   | Bottom-left   |
| `BotC`   | Bottom-center |
| `BotR`   | Bottom-right  |

## 🏆 Winning Conditions

A player wins by placing three identical marks in a row.

There are eight possible winning combinations:

* **Three horizontal rows**
* **Three vertical columns**
* **Two diagonals**

The `Check_Winner()` method checks these combinations using the predefined `win_conditions` list.

If the board becomes full and neither player wins, the game ends in a draw.

## 📂 Project Structure

```text
tic-tac-toe-ai/
└── game.py    # Game board, rules, AI logic, and main game loop
```

## 🛠️ Implementation Details

The project is organized around the `tictactoe` class.

| Method              | Responsibility                                                             |
| ------------------- | -------------------------------------------------------------------------- |
| `__init__()`        | Initializes the board, positions, and winning combinations.                |
| `The_Table()`       | Displays the current game board.                                           |
| `Check_Winner()`    | Checks whether a player has won.                                           |
| `Basic_ai()`        | Finds an immediate winning move or blocks the opponent.                    |
| `Intermediate_ai()` | Experiments with hypothetical moves and potential follow-up opportunities. |
| `computer_move()`   | Selects a random available position.                                       |
| `Main()`            | Runs the game loop and manages player turns.                               |

## 🚧 Future Improvements

This project will continue to evolve as I learn more about Python and AI.

Possible improvements include:

* **Improve the Intermediate AI:** Make threat detection and hypothetical move evaluation more reliable.
* **Develop a Strategic AI:** Experiment with more advanced decision-making without immediately relying on Minimax.
* **Add difficulty levels:** Introduce easy, intermediate, and advanced modes.
* **Track scores:** Record wins, losses, and draws across multiple games.
* **Build a graphical interface:** Explore Tkinter or Pygame.
* **Write automated tests:** Test winning conditions, invalid moves, draws, and AI decisions.
* **Explore Minimax later:** Implement it once I've developed a stronger understanding of game-state evaluation and search algorithms.

## 🎯 Learning Goals

Through this project, I'm practicing:

* Python fundamentals
* Object-oriented programming
* Loops and conditional statements
* Functions and methods
* Dictionaries and lists
* Game-state management
* Algorithmic thinking
* Basic AI decision-making
* Debugging and testing

**The goal isn't to build the strongest Tic-Tac-Toe AI immediately. It's to understand how AI decision-making works by developing the logic myself, testing it, finding weaknesses, and improving it step by step.**

## 📜 License

No license has been specified yet. A license can be added later to clarify how others may use, modify, and distribute the project.
