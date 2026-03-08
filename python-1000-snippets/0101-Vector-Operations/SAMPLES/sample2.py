# sample2.py
# Handle mismatched lengths gracefully

def vector_add(v1,v2):
    if len(v1)!=len(v2):
        print('lengths differ')
        return None
    return [v1[i]+v2[i] for i in range(len(v1))]

if __name__ == '__main__':
    print(vector_add([1,2],[3]))
    print(vector_add([], []))
