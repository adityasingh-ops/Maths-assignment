def simplex(A_matrix, b_vector, c_vector):
    num_constraints, num = len(A_matrix), len(A_matrix[0])
    table = [[0] * (num + num_constraints + 1) for _ in range(num_constraints + 1)]
    
    for i in range(num_constraints):
        table[i][:num] = A_matrix[i]
        table[i][num + i] = 1
        table[i][-1] = b_vector[i]
    
    table[-1][:num] = c_vector
    
    while any(value > 0 for value in table[-1][:-1]):
        entering_var = max(range(num), key=lambda i: table[-1][i])
        ratios = [table[i][-1] / table[i][entering_var] if table[i][entering_var] > 0 else float('inf') for i in range(num_constraints)]
        exiting_var = ratios.index(min(ratios))
        pivot = table[exiting_var][entering_var]
        
        for j in range(num + num_constraints + 1):
            table[exiting_var][j] /= pivot
        
        for i in range(num_constraints + 1):
            if i != exiting_var:
                factor = table[i][entering_var]
                for j in range(num + num_constraints + 1):
                    table[i][j] -= factor * table[exiting_var][j]
    
    # Extract solution from table matrix
    solution = [0] * num
    for j in range(num):
        non_basic_var = [table[i][j] for i in range(num_constraints) if table[i][j] != 0]
        if len(non_basic_var) == 1:
            basic_var_index = [i for i in range(num_constraints) if table[i][j] != 0][0]
            solution[j] = table[basic_var_index][-1]
    
    return solution

# Test the function
c = [1, 1, 0, 0, 0]
A = [
    [-1, 1, 1, 0, 0],
    [ 1, 0, 0, 1, 0],
    [ 0, 1, 0, 0, 1]
]
b = [2, 4, 4]
solution = simplex(A, b, c)
print("Optimal Solution:", solution)
