# sample1.py
# Basic vector addition, subtraction, dot product

def vector_add(v1,v2):
    if len(v1)!=len(v2): return None
    return [v1[i]+v2[i] for i in range(len(v1))]
def vector_subtract(v1,v2):
    if len(v1)!=len(v2): return None
    return [v1[i]-v2[i] for i in range(len(v1))]
def dot_product(v1,v2):
    if len(v1)!=len(v2): return None
    return sum(v1[i]*v2[i] for i in range(len(v1)))

if __name__ == '__main__':
    a=[1,2,3]; b=[4,5,6]
    print('add', vector_add(a,b))
    print('sub', vector_subtract(a,b))
    print('dot', dot_product(a,b))
