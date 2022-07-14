import pickle
from numpy import *

R = pickle.load(open("result.dat", "rb"))


EQN = [s.strip() for s in open("eqn.dat", "rt")]

N = len(EQN)


S=zeros(N)                                                                  

def f(r):
  V, N = unique(r, return_counts=True)
  return (N @ log(N)) / len(r)

Smin=inf                                                                                  
for i in range(N): 
  S[i] = f(R[:,i]) 
  if S[i] < Smin: 
      Smin,n = S[i],i 
  print(i,n,Smin,EQN[n]) 

