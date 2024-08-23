# Sudoku Solver GUI

## Overview
The Sudoku Solver GUI is a Python-based application designed to solve Sudoku puzzles through a user-friendly graphical interface built using Tkinter. This project provides a seamless experience for both entering Sudoku puzzles and solving them automatically with the click of a button. Whether you're a puzzle enthusiast or someone looking to automate the solving process, this application is built to cater to your needs with an intuitive interface and powerful solving algorithms.

## Features

### Interactive 9x9 Sudoku Grid
The application provides a 9x9 grid where users can input their Sudoku puzzle. Each cell is represented by a text entry field, which allows the user to input numbers ranging from 1 to 9.

### Automated Sudoku Solver
The core functionality of the application is its ability to solve Sudoku puzzles automatically. It uses a backtracking algorithm to ensure that it can solve even the most challenging puzzles.

### Input Validation
The solver algorithm includes a validation mechanism to ensure that numbers are placed according to Sudoku rules—no duplicates in any row, column, or 3x3 sub-grid.

### Instant Feedback
Once the puzzle is solved, the grid updates automatically, highlighting the filled cells with a different background color to indicate the solution. If the puzzle is unsolvable, the user is notified via a pop-up message.

### Grid Clearing Functionality
The application provides a "Clear" button that allows users to reset the entire grid, making it easy to input new puzzles without restarting the application.

### User-Friendly Interface
The application features a clean and simple design with buttons and entry fields that are easy to interact with, making it accessible to users of all ages.

## How It Works

### Grid Creation
Upon launching the application, a 9x9 grid is created using Tkinter’s `Entry` widgets, where each cell represents a Sudoku cell. The cells are styled for better readability and accessibility, ensuring a smooth user experience.

### Sudoku Solving Algorithm
The Sudoku solving algorithm is implemented using a backtracking approach. The algorithm systematically tries every possible number in empty cells, backtracking whenever it encounters a violation of Sudoku rules, until it either finds a solution or determines that the puzzle is unsolvable.

## User Interaction

### Solve Button
When the user has finished entering a puzzle and clicks the "Solve" button, the application reads the current grid state and attempts to solve it. If successful, the solution is displayed on the grid; otherwise, an error message is shown.

### Clear Button
This button resets the grid, allowing the user to clear the current puzzle and start fresh.

## Technical Details
- **Language:** Python
- **GUI Library:** Tkinter
- **Algorithm:** Backtracking

## Getting Started

### Prerequisites
- Python 3.x should be installed on your machine.
- Tkinter library, which comes pre-installed with Python.

### Installation
Clone the repository to your local machine using:

```bash
https://github.com/FocusedPoetry10/Prodigy_Infotech_Software_Development_Tasks.git
```

### Navigate to the project directory:

```bash
cd "PRODIGY_SD_04"
```

### Run the application:

```bash
python Solver.py
```

## Usage

### Input
Click on any cell in the grid and enter a number between 1 and 9.

### Solve
Click the "Solve" button to automatically solve the puzzle.

### Clear
Click the "Clear" button to reset the grid.

## Contributing
Contributions are welcome! Feel free to open issues or submit pull requests to improve the application.

## License
This project is licensed under the MIT License.
