def generate_sudoku_clauses(grid_size):
    clauses = []

    def var(i, j, k):
        return grid_size * grid_size * (i - 1) + grid_size * (j - 1) + k

    for i in range(1, grid_size + 1):
        for j in range(1, grid_size + 1):
            clauses.append([var(i, j, k) for k in range(1, grid_size + 1)])
            for k1 in range(1, grid_size + 1):
                for k2 in range(k1 + 1, grid_size + 1):
                    clauses.append([-var(i, j, k1), -var(i, j, k2)])

    for i in range(1, grid_size + 1):
        for k in range(1, grid_size + 1):
            for j1 in range(1, grid_size + 1):
                for j2 in range(j1 + 1, grid_size + 1):
                    clauses.append([-var(i, j1, k), -var(i, j2, k)])

    box_size = int(grid_size ** 0.5)
    for k in range(1, grid_size + 1):
        for box_i in range(0, box_size):
            for box_j in range(0, box_size):
                cells = [
                    var(box_i * box_size + di + 1, box_j * box_size + dj + 1, k)
                    for di in range(box_size) for dj in range(box_size)
                ]
                for i in range(len(cells)):
                    for j in range(i + 1, len(cells)):
                        clauses.append([-cells[i], -cells[j]])
    return clauses


def save_as_cnf(clauses, grid_size, file_path):
    with open(file_path, 'w') as file:
        # Write the preamble for CNF format
        num_variables = grid_size ** 3
        num_clauses = len(clauses)
        file.write(f"p cnf {num_variables} {num_clauses}\n")

        # Write each clause
        for clause in clauses:
            file.write(" ".join(map(str, clause)) + " 0\n")


# Generate clauses for a 9x9 Sudoku puzzle
grid_size = 9
clauses = generate_sudoku_clauses(grid_size)

# Save to a .cnf file
file_path = "sudoku.cnf"
save_as_cnf(clauses, grid_size, file_path)

file_path
