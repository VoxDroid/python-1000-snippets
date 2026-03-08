# sample3.py
# Space‑optimized LCS length only

def lcs_space(a, b):
    if len(a) < len(b):
        a, b = b, a
    prev = [0] * (len(b)+1)
    for ch in a:
        curr = [0]*(len(b)+1)
        for j,c in enumerate(b,1):
            if ch == c:
                curr[j] = prev[j-1] + 1
            else:
                curr[j] = max(prev[j], curr[j-1])
        prev = curr
    return prev[-1]

if __name__ == '__main__':
    print('space len', lcs_space('AGGTAB','GXTXAYB'))
