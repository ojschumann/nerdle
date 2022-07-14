import pickle
from numpy import *

R = pickle.load(open("result.dat", "rb"))


EQN = [s.strip() for s in open("eqn.dat", "rt")]

N = len(EQN)


def findTree(I):
  V,N=unique(R[:, I], return_counts=True)
  for i in range(len(V)):
    if N[i]>2:
      D = R[R[:,I]==V[i],:]
      for n in range(len(EQN)):
        if len(unique(D[:,n])) == N[i]:
          break
      else:
        # no guess, that completely partitions D into single solutions
        return False
  # All non-trivial patitions have been solved
  return True



for n in range(N):
  if findTree(n):
    print(n, EQN[n])
  if n%1000==0:
    print(n)
