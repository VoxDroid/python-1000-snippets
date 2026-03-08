# sample3.py
# Backtrack to produce edit operations between strings

def edit_distance_ops(a,b):
    m,n=len(a),len(b)
    dp=[[0]*(n+1) for _ in range(m+1)]
    for i in range(m+1): dp[i][0]=i
    for j in range(n+1): dp[0][j]=j
    for i in range(1,m+1):
        for j in range(1,n+1):
            if a[i-1]==b[j-1]: dp[i][j]=dp[i-1][j-1]
            else:
                dp[i][j]=1+min(dp[i-1][j-1],dp[i-1][j],dp[i][j-1])
    ops=[]
    i,j=m,n
    while i>0 or j>0:
        if i>0 and j>0 and a[i-1]==b[j-1]:
            i-=1; j-=1
        elif i>0 and j>0 and dp[i][j]==dp[i-1][j-1]+1:
            ops.append(f'replace {a[i-1]} with {b[j-1]}'); i-=1; j-=1
        elif i>0 and dp[i][j]==dp[i-1][j]+1:
            ops.append(f'delete {a[i-1]}'); i-=1
        else:
            ops.append(f'insert {b[j-1]}'); j-=1
    return dp[m][n], list(reversed(ops))

if __name__ == '__main__':
    dist, ops = edit_distance_ops('kitten','sitting')
    print('distance', dist)
    print('ops', ops)
