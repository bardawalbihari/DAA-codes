def lcs(seq1, seq2):
    m, n = len(seq1), len(seq2)
    
    # Create a 2D table to store lengths of LCS
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Fill the dp table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if seq1[i - 1] == seq2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    
    # Retrieve the LCS
    lcs = []
    i, j = m, n
    while i > 0 and j > 0:
        if seq1[i - 1] == seq2[j - 1]:
            lcs.append(seq1[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1
        else:
            j -= 1
    
    lcs.reverse()  # Reverse to get the correct order
    
    return dp[m][n], lcs

# Example usage
names1 = ["Sachin", "Virat", "Dhoni", "Rohit", "Jadeja"]
names2 = ["Virat", "Sachin", "Jadeja", "Dhoni", "Rohit"]

length, subsequence = lcs(names1, names2)

print("Length of LCS:", length)
print("Longest Common Subsequence:", subsequence)
