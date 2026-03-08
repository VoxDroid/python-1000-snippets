# sample2.py
# use apply_async to collect results

from multiprocessing import Pool

def cube(n):
    return n**3

if __name__ == '__main__':
    with Pool(3) as pool:
        results = [pool.apply_async(cube, (i,)) for i in range(4)]
        print('Cubes:', [r.get() for r in results])
