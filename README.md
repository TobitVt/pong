## Pong Game

A recreation of the classic Pong arcade game built in Python using the built-in `turtle` graphics library. The game features two-player gameplay, responsive paddle controls, realistic ball bouncing, increasing ball speed, score tracking, and a classic Pong-inspired interface.

This project was developed to strengthen my understanding of object-oriented programming, event-driven programming, collision detection, and game loop implementation in Python.

---

## Features

* Classic two-player Pong gameplay
* Keyboard-controlled paddles
* Ball collision with walls and paddles
* Ball speed increases after each paddle hit
* Automatic score tracking
* Ball resets after each point
* Retro-inspired playing field with center line

---

## Technologies Used

* Python 3
* Turtle Graphics
* Object-Oriented Programming (OOP)

---

## Project Structure

```text
pong/
│
├── main.py
├── paddle.py
├── ball.py
├── scoreboard.py
├── midline.py
└── README.md
```

### File Overview

### `main.py`

* Creates the game window
* Runs the main game loop
* Detects collisions
* Updates scores
* Coordinates all game objects

### `paddle.py`

* Implements the `Paddle` class
* Handles keyboard input
* Restricts paddle movement within the screen

### `ball.py`

* Implements the `Ball` class
* Controls movement and bouncing
* Gradually increases ball speed
* Resets after a point is scored

### `scoreboard.py`

* Tracks each player's score
* Updates the on-screen scoreboard

### `midline.py`

* Draws the center line of the playing field

---

## Controls

| Player       | Keys          |
| ------------ | ------------- |
| Left Paddle  | **W** / **S** |
| Right Paddle | **↑** / **↓** |

---

## How to Run

### Requirements

* Python 3.x

### Installation

Clone the repository:

```bash
git clone https://github.com/your-username/pong.git
```

Navigate to the project folder:

```bash
cd pong
```

Run the game:

```bash
python main.py
```

---

## Concepts Demonstrated

* Object-Oriented Programming (OOP)
* Event-driven programming
* Game loop implementation
* Collision detection
* Keyboard input handling
* Class design and modular programming
* Animation using Turtle Graphics
* Basic game physics

---

## Future Improvements

* Single-player mode with AI opponent
* Difficulty levels
* Sound effects
* Start menu
* Win screen
* Pause functionality
* Match timer
* Configurable controls
* Power-ups

---

## Author

**Tobit Vervat**

---
