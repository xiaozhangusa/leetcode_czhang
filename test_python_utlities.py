import multiprocessing as mp
import random
import string

def cube(x):
    return x**3

pool = mp.Pool(processes=4)
results = [pool.apply(cube, args=(x, )) for x in range(1, 7)]
print (results)
