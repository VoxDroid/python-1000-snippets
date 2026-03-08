# sample3.py
# Additional operations and NumPy example

import math
import numpy as np

def norm(v):
    return math.sqrt(sum(x*x for x in v))
def cross(v1,v2):
    if len(v1)==3 and len(v2)==3:
        return [v1[1]*v2[2]-v1[2]*v2[1],
                v1[2]*v2[0]-v1[0]*v2[2],
                v1[0]*v2[1]-v1[1]*v2[0]]
    return None

if __name__ == '__main__':
    v=[1,2,3]
    print('norm', norm(v))
    print('cross', cross([1,0,0],[0,1,0]))
    # numpy version
    a=np.array([1,2,3])
    b=np.array([4,5,6])
    print('np dot', np.dot(a,b))
    print('np cross', np.cross(a,b))
