def pldu(M):
    n = len(M)
    P = [[1 if i == j else 0 for j in range(n)] for i in range(n)]
    L = [[0 for j in range(n)] for i in range(n)]
    D = [[0 for j in range(n)] for i in range(n)]
    U = [[0 for j in range(n)] for i in range(n)]

    for k in range(n):
        pivot_row = max(range(k, n), key=lambda i: abs(M[i][k]))
        M[k], M[pivot_row] = M[pivot_row], M[k]
        P[k], P[pivot_row] = P[pivot_row], P[k]
        L[k][k] = 1
        for i in range(k + 1, n):
            L[i][k] = M[i][k] / M[k][k]
            U[k][i] = M[k][i] / M[k][k]
        for i in range(k, n):
            U[i][k] = M[i][k]
        D[k][k] = M[k][k]
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                M[i][j] -= L[i][k] * U[k][j]

    return P, L, D, U

M = [[1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]]

P, L, D, U = pldu(M)

print("P matrix:")
for row in P:
    print(row)

print("L matrix:")
for row in L:
    print(row)

print("D matrix:")
for row in D:
    print(row)

print("U matrix:")
for row in U:
    print(row)
