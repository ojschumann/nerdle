from nerdle import result
from numpy import *


EQN = [s.strip() for s in open("eqn.dat", "rt")]

N = len(EQN)
V = array([3**n for n in range(8)])

R = empty((N,N), dtype=int)

for i,a in enumerate(EQN):
  for j,b in enumerate(EQN):
    R[i,j] = dot(result(a,b), V)

  print(i)


import pickle
pickle.dump(R, open("result.dat", "wb"))







