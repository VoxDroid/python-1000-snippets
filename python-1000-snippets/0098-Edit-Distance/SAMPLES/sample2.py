# sample2.py
# Space-optimized edit distance (one row)

def edit_distance_space(a,b):
    m,n=len(a),len(b)
    prev=list(range(n+1))
    for i in range(1,m+1):
        curr=[i]+[0]*n
        for j in range(1,n+1):
            if a[i-1]==b[j-1]: curr[j]=prev[j-1]
            else:
                curr[j]=1+min(prev[j-1], prev[j], curr[j-1])
        prev=curr
    return prev[n]

if __name__ == '__main__':
    print('space', edit_distance_space('book','back'))
