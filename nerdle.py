from numpy import *
from collections import defaultdict

def result(eqn, test):
  result = zeros(8, dtype=int)
  used = zeros(8, dtype=bool)

  for i in range(8):
    if eqn[i] == test[i]:
      result[i] = 2
      used[i] = True
  for i in range(8):
    if eqn[i] != test[i]:
      for j in range(8):
        if eqn[j] == test[i] and not used[j]:
          result[i] = 1
          used[j] = True
          break
  
  return tuple(result)



def entropy1(eq):
  part = defaultdict(int)
  for test in EQN:
    part[result(eq, test)] += 1

  S = 0.0
  for N in part.values():
    S += N*log(N)

  return S / len(EQN)


def entropy2(EQN, test):
  part = defaultdict(int)
  for eq in EQN:
    part[result(eq, test)] += 1

  S = 0.0
  for N in part.values():
    S += (N-1)**2 # N*log(N)

  return S / len(EQN)






