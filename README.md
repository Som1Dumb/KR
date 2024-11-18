# SAT Solver for Sudoku and Hypersudoku

## Overview
This project implements a SAT solver using the DPLL algorithm to solve Sudoku and Hypersudoku puzzles. It includes:
- A SAT solver (`sat_solver.py`) that supports DIMACS format.
- A DIMACS generator (`dimacs_generator.py`) to encode Sudoku and Hypersudoku rules.
- An experiment script (`experiment.py`) to compare the complexity of solving Standard Sudoku and Hypersudoku puzzles.

## Project Structure


- sat_solver.py # Implementation of the SAT solver 
- dimacs_generator.py # Generates DIMACS constraints for Sudoku and Hypersudoku 
- experiment.py # Runs the experiment comparing Sudoku and Hypersudoku 
- README.md # This file


## Requirements
- Python 3.x
- No additional libraries are required.

## Usage

### 1. Running the SAT Solver
The SAT solver works with DIMACS-formatted input files. To solve a puzzle:
1. Generate a DIMACS file for the Sudoku or Hypersudoku puzzle using `dimacs_generator.py`.
2. Use `sat_solver.py` to solve the puzzle.

### 2. Running the Experiment
The `experiment.py` script generates Sudoku and Hypersudoku constraints and measures the solver's runtime.

Run the script:
```bash
python experiment.py
```
The experiment script will print the runtime for solving Standard Sudoku and Hypersudoku puzzles:

Running puzzle 1...
Sudoku time: 0.45s, Hypersudoku time: 0.78s
...
Results:
Puzzle 1: Sudoku = 0.45s, Hypersudoku = 0.78s
...

