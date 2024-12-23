# SAT Solver for Sudoku 4x4 and 9x9

## Overview
This project implements three SAT solvers for solving Sudoku puzzles:
1. **DPLL Solver**: Basic SAT solving using the DPLL algorithm.
2. **Jeroslow-Wang (JW) Solver**: Enhances DPLL with a heuristic that prioritizes variables in smaller clauses.
3. **Conflict-Driven Clause Learning (CDCL) Solver**: Adds clause learning and backjumping to improve efficiency.

The project includes:
- A DIMACS generator to encode Sudoku puzzles into CNF format.
- A comparison experiment for the three solvers on 4x4 and 9x9 Sudoku puzzles.

## Project Structure
- sat_solver.py # Contains DPLL, JW, and CDCL solver implementations 
- dimacs_generator.py # Generates DIMACS constraints for 4x4 and 9x9 Sudoku
- experiment.py # Runs the experiment comparing the three solvers 
- README.md # This file


## Requirements
- Python 3.x
- No additional libraries are required.

## Usage

## Experiment

Run the experiment:
python experiment.py

Expected Output:
DPLL on 4x4: 0.05s
JW on 4x4: 0.03s
CDCL on 4x4: 0.02s
DPLL on 9x9: 1.25s
JW on 9x9: 0.85s
CDCL on 9x9: 0.60s

Final Results:
4x4 Sudoku:
  DPLL: 0.05s
  JW: 0.03s
  CDCL: 0.02s
9x9 Sudoku:
  DPLL: 1.25s
  JW: 0.85s
  CDCL: 0.60s


## Experiment Details
4x4 Sudoku: Smaller grid with simpler constraints.
9x9 Sudoku: Standard grid with more variables and constraints.
Metrics: Runtime comparison across solvers for puzzles of different sizes.
Solver Descriptions
DPLL Solver:

Implements the basic Davis–Putnam–Logemann–Loveland algorithm.
Exhaustively searches the solution space using backtracking.
Jeroslow-Wang (JW) Solver:

Adds a heuristic to prioritize variables in smaller clauses, reducing search space.
CDCL Solver:

Conflict-driven learning to avoid revisiting bad decisions.
Backjumping to skip unnecessary parts of the search tree.
## Extending the Project
Add support for other Sudoku variants (e.g., Hypersudoku, 16x16) by modifying dimacs_generator.py.
Implement additional SAT solving heuristics (e.g., VSIDS, random restarts).
Visualize performance metrics like backtracks, conflicts, and learned clauses.

