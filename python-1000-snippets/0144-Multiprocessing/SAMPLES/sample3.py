# sample3.py
# demonstrate shared counter via Manager

from multiprocessing import Pool, Manager

def inc(shared):
    shared.value += 1

if __name__ == '__main__':
    mgr = Manager()
    shared = mgr.Value('i', 0)
    with Pool(2) as pool:
        pool.map(lambda _: inc(shared), range(100))
    print('shared count', shared.value)
