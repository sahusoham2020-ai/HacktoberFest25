# 🐍 CLI Snake Game

A nostalgic, retro-style **Snake Game** that runs entirely in your terminal!  
Developed in **Python** using only the built-in `curses` library — no external dependencies required.  
Simple, fun, and perfect for both beginners and Python enthusiasts.

---

## 🧩 Table of Contents
- [About the Game](#-about-the-game)
- [Features](#-features)
- [Gameplay Logic](#-gameplay-logic)
- [Requirements](#-requirements)
- [Installation](#-installation)
- [How to Run](#-how-to-run)
- [Controls](#-controls)
- [Example Output](#-example-output)
- [Troubleshooting](#-troubleshooting)
- [Future Enhancements](#-future-enhancements)
- [Author](#-author)
- [License](#-license)

---

## 🕹️ About the Game

This **CLI Snake Game** is a lightweight implementation of the classic arcade game — playable directly in your terminal window.  
The player controls a snake 🟩 that moves around the screen to eat apples 🍎 and grow longer.  
The challenge is to **avoid colliding with walls or yourself** — how long can you survive?

---

## ✨ Features

- 🟩 Smooth and responsive real-time movement  
- 🍎 Random food placement on every spawn  
- 🚫 Collision detection for wall and body  
- 🧠 Smart direction control (prevents instant reversal)  
- 📊 Live score tracking during gameplay  
- ⚡ Adjustable speed by changing the delay  
- 💻 Works cross-platform (Linux, macOS, Windows with compatible terminal)  
- 🔥 Entirely in **one `.py` file** — easy to run or modify  

---

## 🧠 Gameplay Logic

1. The snake starts at a fixed position on the screen.  
2. The player uses **arrow keys** to control movement.  
3. When the snake’s head touches a food item 🍎:
   - The score increases by 1.
   - The snake grows in length.
   - New food appears at a random location.
4. The game ends when:
   - The snake’s head hits the wall.
   - The snake collides with itself.
5. The **final score** is displayed after game over.

---

## ⚙️ Requirements

- Python **3.7+**
- A terminal that supports Unicode and ANSI escape sequences (for 🟩 and 🍎)
  

