def solve(coefficients, constants):
    num_equations, num_variables = len(coefficients), len(coefficients[0])
    if num_equations != num_variables:
        return -1
    determinant = calculate_determinant(coefficients)
    if determinant == 0:
        if any(row[-1] != 0 for row in coefficients):
            return -1
        else:
            return -2
    augmented_matrix = []
    for i in range(num_equations):
        augmented_matrix.append(coefficients[i] + [constants[i]])
    for i in range(num_variables):
        max_row = i
        for j in range(i + 1, num_equations):
            if abs(augmented_matrix[j][i]) > abs(augmented_matrix[max_row][i]):
                max_row = j
        augmented_matrix[i], augmented_matrix[max_row] = augmented_matrix[max_row], augmented_matrix[i]
        if augmented_matrix[i][i] == 0:
            return -1
        for j in range(i + 1, num_equations):
            factor = augmented_matrix[j][i] / augmented_matrix[i][i]
            for k in range(i, num_variables + 1):
                augmented_matrix[j][k] -= factor * augmented_matrix[i][k]
    solution = [0] * num_variables
    for i in range(num_variables - 1, -1, -1):
        solution[i] = augmented_matrix[i][num_variables]
        for j in range(i + 1, num_variables):
            solution[i] -= augmented_matrix[i][j] * solution[j]
        solution[i] /= augmented_matrix[i][i]
    return solution

def calculate_determinant(matrix):
    num_rows, num_columns = len(matrix), len(matrix[0])
    num_rows, num_columns = len(matrix), len(matrix[0])
    if num_rows != num_columns:
        return 0
    if num_columns == 1:
        return matrix[0][0]
    determinant = 0
    for j in range(num_columns):
        submatrix = [row[:j] + row[j + 1:] for row in matrix[1:]]
        determinant += ((-1) ** j) * matrix[0][j] * calculate_determinant(submatrix)
    return determinant

coef = [[2, 4], [1, -1]]
const = [3, 1]
print(calculate_determinant(coef))
sol = solve(coef, const)
print("Solution:", sol)

coef_inf = [[2, 1], [4, 2]]
const_inf = [3, 6]
sol_inf = solve(coef_inf, const_inf)
print("Solution with infinite solutions:", sol_inf)

coef_no_sol = [[1, 2], [2, 4]]
const_no_sol = [3, 5]
sol_no_sol = solve(coef_no_sol, const_no_sol)

print("Solution with no solution:", sol_no_sol)
