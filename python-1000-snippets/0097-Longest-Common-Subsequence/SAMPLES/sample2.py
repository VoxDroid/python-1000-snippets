# sample2.py
# Reconstruct the actual LCS string

def lcs_with_sequence(a, b):
    m,n=len(a),len(b)
    dp=[[0]*(n+1) for _ in range(m+1)]
    for i in range(1,m+1):
        for j in range(1,n+1):
            if a[i-1]==b[j-1]:
                dp[i][j]=dp[i-1][j-1]+1
            else:
                dp[i][j]=max(dp[i-1][j], dp[i][j-1])
    i,j=m,n; seq=[]
    while i>0 and j>0:
        if a[i-1]==b[j-1]:
            seq.append(a[i-1]); i-=1; j-=1
        elif dp[i-1][j] > dp[i][j-1]:
            i-=1
        else:
            j-=1
    return ''.join(reversed(seq))

if __name__ == '__main__':
    print('seq', lcs_with_sequence('ABCDGH','AEDFHR'))
