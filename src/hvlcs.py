def highest_value_lcs(A: str, B: str, v: dict):

    n = len(A)
    m = len(B)

    # M: first row and column are all 0 (base case), rest are None
    mem = [
        [0 if r == 0 or c == 0 else None for c in range(n)]
        for r in range(m)
    ]

    # Calculate highest value longest common subsequence
    for i in range(1, n+1):
        for j in range(1, m+1):
            
            # Characters match, consider taking (or skipping)
            if A[i] == B[j]:
                mem[i][j] = max(v[i] + mem[i-1][j-1], mem[i-1][j], mem[i][j-1])

            # Characters don't match, continue
            else:
                mem[i][j] = max(mem[i-1][j], mem[i][j-1])

    # Get highest value found
    max_val = mem[0][0]
    max_i, max_j = 0, 0

    for i in range(len(mem)):
        for j in range(len(mem[0])):
            if mem[i][j] > max_val:
                max_val = mem[i][j]
                max_i, max_j = i, j

    # Backtrack to find actual sequence
    subseq = backtrack(A, mem, v, max_i, max_j, "")

    return max_val, subseq


def backtrack(A, mem, v, i, j, subseq):
    # Base case: 0 length subseq
    if i == 0 or j == 0:
        return subseq
    
    # If we came from the diagonal, this character was taken
    if mem[i][j] == mem[i-1][j-1] + v[A[i]]:
        subseq = A[i] + subseq  # prepend since we're going backwards
        return backtrack(A, mem, v, i-1, j-1, subseq)
    # Move in the direction of the larger neighbor
    elif mem[i-1][j] > mem[i][j-1]:
        return backtrack(A, mem, v, i-1, j, subseq)
    else:
        return backtrack(A, mem, v, i, j-1, subseq)