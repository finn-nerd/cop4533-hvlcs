def highest_value_lcs(A: str, B: str, v: dict):

    n = len(A)
    m = len(B)

    # M: first row and column are all 0, rest are None
    mem = [
        [0 if r == 0 or c == 0 else None for c in range(n)]
        for r in range(m)
    ]

    for i in range(n):
        for j in range(m):
            
            # Characters match, consider taking (or skipping)
            if A[i] == A[B]:
                mem[i][j] = max(v[i] + mem[i-1, j-1], mem[i-1][j], mem[i][j-1])

            # Characters don't match, continue
            else:
                mem[i][j] = max(mem[i-1][j], mem[i][j-1])

    return mem