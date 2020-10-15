import time
import random

SIZE = 200000
REPETITION = 10000

def zero():
    lista = []
    for i in range(SIZE):
        lista.append(i)

    zero_time_start = time.time()
    for i in range(REPETITION):
        lista[0]
        # lista.index(0)
    zero_time_end = time.time()

    return zero_time_end - zero_time_start

def n():
    lista2 = []
    for i in range(SIZE):
        lista2.append(i)

    n_time_start = time.time()
    for i in range(REPETITION):
        lista2[100003]
        # lista2.index(100003)
    n_time_end = time.time()

    return n_time_end - n_time_start

def rand():
    lista3 = []
    for i in range(SIZE):
        lista3.append(i)

    rand_time_start = time.time()
    for i in range(REPETITION):
        j = random.randint(0, SIZE-1)
        lista3[random.randint(0, SIZE-1)]
        # lista3.index(random.randint(0, SIZE-1))
    rand_time_end = time.time()

    return rand_time_end - rand_time_start

if __name__ == "__main__":
    zerosum = 0
    nsum = 0
    randsum = 0

    # ! DANGER ! -> watch rep number, it may take forever to finish
    rep = 10
    
    exec_time_start = time.time()
    for i in range(rep):
        zerosum += zero()
        nsum += n()
        randsum += rand()
    exec_time_end = time.time()
    
    print("#########")
    print("Zero: {} seconds".format(zerosum / rep))
    print("N: {} seconds".format(nsum / rep))
    print("Random: {} seconds".format(exec_time_end - exec_time_start))
    print("#########")