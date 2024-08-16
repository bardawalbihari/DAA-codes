def matrix_chain_order(p):
    n = len(p) - 1
    # Initialize the m matrix to store the minimum number of multiplications
    m = [[0] * n for _ in range(n)]
    
    # Compute the minimum number of multiplications for chains of increasing length
    for length in range(2, n + 1):  # length is the length of the matrix chain
        for i in range(n - length + 1):
            j = i + length - 1
            m[i][j] = float('inf')  # Start with a large number
            for k in range(i, j):
                # Compute the cost of multiplying the chain from i to j with split at k
                q = m[i][k] + m[k+1][j] + p[i] * p[k+1] * p[j+1]
                if q < m[i][j]:
                    m[i][j] = q

    return m[0][n-1]  # The minimum number of multiplications needed for the full chain

# Matrix dimensions
p = [5, 10, 3, 12, 5, 50, 6]

# Compute and print the minimum number of scalar multiplications needed
min_multiplications = matrix_chain_order(p)
print("Minimum number of scalar multiplications needed:", min_multiplications)
