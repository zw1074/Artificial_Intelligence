# Default Value
from random import *
from math import *

def DAG_Generator(N, Maxsize):
    fobj = open('sample text2.txt', 'w')

    # Generate Basic Info
    TargetV = uniform(
        N ** 2 * (1 - 2 / sqrt(N)) / 4, N ** 2 * (1 + 2 / sqrt(N)) / 4)
    Deadline = uniform(
        N ** 2 * (1 - 2 / sqrt(N)) / 4, N ** 2 * (1 + 2 / sqrt(N)) / 4)
    fobj.write(str(N) + ' ' + str(TargetV) + ' ' +
               str(Deadline) + ' ' + str(Maxsize) + '\n')

    # Generate Task Info
    for x in range(0, N):
        fobj.write(
            str(x) + ' ' + str(randint(0, N)) + ' ' + str(randint(0, N)) + '\n')

    # Generate DAG
    P = range(0, N)
    for I in range(0, N):
        J = randint(I, N - 1)
        M = P[I]
        P[I] = P[J]
        P[J] = M
    for I in range(0, N - 1):
        for J in range(I + 1, N):
            if random() > 0.5:
                fobj.write(str(P[I]) + ' ' + str(P[J]) + '\n')
    fobj.close()

DAG_Generator(100, 100)