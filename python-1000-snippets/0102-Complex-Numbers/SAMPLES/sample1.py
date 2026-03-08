# sample1.py
# Basic complex arithmetic

def complex_operations(z1,z2):
    return {
        'add': z1+z2,
        'mul': z1*z2,
        'conj1': z1.conjugate(),
        'abs1': abs(z1)
    }

if __name__ == '__main__':
    z1=complex(3,4)
    z2=complex(1,2)
    print(complex_operations(z1,z2))
