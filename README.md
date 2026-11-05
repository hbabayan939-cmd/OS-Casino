## Attention

This game is intended as a joke and is not meant to satirize any particular corporation (or operating system). This is NOT A REAL CASINO it's a simple game written in Python. Thanks for reading

# OS Casino

OS Casino is a small desktop slot game built with Python and CustomTkinter for fun. Spin three reels featuring operating system names and see your points change when all three match.

## Requirements

- customtkinter>=5.2.0
- pillow>=13.0.0
- playsound3>=3.0.0

The Python packages are listed in `requirements.txt`.

## Setup

From the project directory, create and activate a virtual environment, then install the dependencies:

```bash
python -m venv .venv
```

Activate it:

```bash
# Linux/macOS
source .venv/bin/activate

# Windows PowerShell
.venv\Scripts\Activate.ps1
```

Install the packages and launch the app:

```bash
python -m pip install -r requirements.txt
python main.py
```

## How to play

Press **SPIN** to roll the three reels. A matching triple awards or subtracts points; mixed reels do not change the score.

| Matching reels | Points |
|----------------|--------|
| Linux ×3       | +500   |
| FreeBSD ×3     | +400   |
| NetBSD ×3      | +250   |
| OpenBSD ×3     | +250   |
| macOS ×3       | −300   |
| Windows ×3     | −500   |

The score starts at zero and carries over between spins while the app is open.

## Tests

Run the game model tests with Python's built-in unittest runner:

```bash
python -m unittest discover -s tests -v
```

## Project layout

```text
core/                 Game configuration and slot game logic
functions/            Result text formatting
tests/                Unit tests for the game logic
main.py               CustomTkinter desktop application
requirements.txt      Python dependencies
```
