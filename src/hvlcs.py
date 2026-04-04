def highest_value_lcs(A: str, B: str, v: dict):

    # Get string lengths (+1 for 0 index base case)
    n = len(A)
    m = len(B)

    # M: first row and column are all 0 (base case), rest are None
    mem = [
        [0 if r == 0 or c == 0 else None for c in range(n + 1)]
        for r in range(m + 1)
    ]

    # Calculate highest value longest common subsequence
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            
            # Characters match, consider taking (or skipping)
            if A[i-1] == B[j-1]: # -1 to match actual strings
                mem[i][j] = max(v[A[i-1]] + mem[i-1][j-1], mem[i-1][j], mem[i][j-1])

            # Characters don't match, continue
            else:
                mem[i][j] = max(mem[i-1][j], mem[i][j-1])

    # Get highest value found
    max_val = mem[n][m]

    # Backtrack to find actual sequence
    subseq = backtrack(A, mem, v, n, m, "")

    for i in range(0, n+1):
        for j in range(0, m+1):
            print(mem[i][j], end=" ")
        print("")

    return max_val, subseq


def backtrack(A, mem, v, i, j, subseq):
    # Base case: 0 length subseq
    if i == 0 or j == 0:
        return subseq
    
    # If we came from the diagonal, this character was taken
    if mem[i][j] == mem[i-1][j-1] + v[A[i-1]]:
        subseq = A[i-1] + subseq  # prepend since we're going backwards
        return backtrack(A, mem, v, i-1, j-1, subseq)
    # Move in the direction of the larger neighbor
    elif mem[i-1][j] > mem[i][j-1]:
        return backtrack(A, mem, v, i-1, j, subseq)
    else:
        return backtrack(A, mem, v, i, j-1, subseq)