import pickle
from numpy import *

R = pickle.load(open("result.dat", "rb"))


EQN = [s.strip() for s in open("eqn.dat", "rt")]

S = array([s for s,eq in pickle.load(open("entropy_log.dat", "rb"))]).argsort()

N = len(EQN)


SS=zeros((N, N))                                                                  

def f(r):
  V, N = unique(r, return_counts=True)
  return (N @ log(N)) / len(r)

Smin=inf                                                                                  
for i in range(N): 
  for j in range(i+1): 
    SS[i,j] = f(R[:,S[i]] + 3**8*R[:,S[j]]) 
    SS[j,i] = SS[i,j] 
    if SS[i,j] < Smin: 
      Smin,n,m = SS[i,j],i,j 
  print(i,n,m,Smin,EQN[S[n]], EQN[S[m]]) 

